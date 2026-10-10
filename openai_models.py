"""OpenAI image backends: the Images API (GPT Image models) and the
Responses API image tool (chat models such as GPT-4o)."""

import base64
import io
import os

from PIL import Image

from registry import ImageModel


class GenerationError(Exception):
    """Raised with a message that is safe to show in the UI."""


def _client(api_key: str | None):
    from openai import OpenAI

    key = (api_key or "").strip() or os.getenv("OPENAI_API_KEY")
    if not key:
        raise GenerationError(
            "Add your OpenAI API key: put OPENAI_API_KEY in a .env file, "
            "or paste it under Settings."
        )
    return OpenAI(api_key=key)


def _decode(b64: str) -> Image.Image:
    return Image.open(io.BytesIO(base64.b64decode(b64))).convert("RGB")


def _friendly(err: Exception, model: ImageModel) -> GenerationError:
    import openai

    if isinstance(err, openai.AuthenticationError):
        return GenerationError("OpenAI rejected the API key. Check it and try again.")
    if isinstance(err, (openai.NotFoundError, openai.PermissionDeniedError)):
        return GenerationError(
            f"Your OpenAI account can't use {model.label} yet. Some models need "
            "organization verification or early access. Pick another model."
        )
    if isinstance(err, openai.RateLimitError):
        return GenerationError("OpenAI rate limit or quota reached. Wait a moment or check billing.")
    if isinstance(err, openai.BadRequestError):
        return GenerationError(f"OpenAI refused the request: {getattr(err, 'message', err)}")
    return GenerationError(f"OpenAI error: {err}")


def generate_openai(model: ImageModel, prompt, width, height, count, quality, api_key):
    import openai

    client = _client(api_key)
    size = f"{width}x{height}"
    quality = quality.lower()

    try:
        if model.provider == "images":
            result = client.images.generate(
                model=model.model_id,
                prompt=prompt,
                size=size,
                quality=quality,
                n=int(count),
            )
            return [_decode(d.b64_json) for d in result.data]

        # Responses API: one image per call, so loop for multiple images
        images = []
        for _ in range(int(count)):
            response = client.responses.create(
                model=model.model_id,
                input=prompt,
                tools=[{"type": "image_generation", "size": size, "quality": quality}],
                tool_choice={"type": "image_generation"},
            )
            images += [
                _decode(item.result)
                for item in response.output
                if item.type == "image_generation_call" and item.result
            ]
        if not images:
            raise GenerationError(f"{model.label} answered without an image. Try rewording the prompt.")
        return images

    except openai.OpenAIError as err:
        raise _friendly(err, model) from err
