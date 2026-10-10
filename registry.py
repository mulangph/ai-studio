"""Every image model the studio can use, in one place.

To add a model, add an entry to MODELS. `provider` decides which backend runs it:
  - "local"     Stable Diffusion on your own GPU (see model.py)
  - "images"    OpenAI Images API  (client.images.generate)
  - "responses" OpenAI Responses API with the image_generation tool (for chat models like GPT-4o)
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ImageModel:
    label: str          # shown in the dropdown
    model_id: str       # sent to the API / diffusers
    provider: str       # "local" | "images" | "responses"
    blurb: str          # one-line description under the dropdown
    max_images: int = 4


MODELS: dict[str, ImageModel] = {
    "gpt-image-2.5-sunburst": ImageModel(
        "GPT Image 2.5 Sunburst", "gpt-image-2.5-sunburst", "images",
        "OpenAI's newest model, tuned for top quality and precise detail.",
    ),
    "gpt-image-2.5-flare": ImageModel(
        "GPT Image 2.5 Flare", "gpt-image-2.5-flare", "images",
        "GPT Image 2.5 tuned for speed. Great for fast iteration.",
    ),
    "gpt-image-2": ImageModel(
        "GPT Image 2", "gpt-image-2", "images",
        "Excellent text rendering and photorealism.",
    ),
    "gpt-image-1.5": ImageModel(
        "GPT Image 1.5", "gpt-image-1.5", "images",
        "Previous generation. Reliable and widely available.",
    ),
    "gpt-image-1-mini": ImageModel(
        "GPT Image 1 Mini", "gpt-image-1-mini", "images",
        "Cheapest OpenAI option for drafts.",
    ),
    "gpt-4o": ImageModel(
        "GPT-4o", "gpt-4o", "responses",
        "GPT-4o drawing through its built-in image tool. Strong at following long prompts.",
    ),
    "sd-1.5": ImageModel(
        "Stable Diffusion 1.5 (local)", "runwayml/stable-diffusion-v1-5", "local",
        "Runs free on your own GPU. No API key needed.",
    ),
}

DEFAULT_MODEL = "gpt-image-2"

# Aspect ratio -> (width, height) for each backend family
SIZES = {
    "local": {"Square": (512, 512), "Landscape": (768, 512), "Portrait": (512, 768)},
    "openai": {"Square": (1024, 1024), "Landscape": (1536, 1024), "Portrait": (1024, 1536)},
}


def size_for(model: ImageModel, aspect: str) -> tuple[int, int]:
    family = "local" if model.provider == "local" else "openai"
    return SIZES[family][aspect]


def choices() -> list[tuple[str, str]]:
    return [(m.label, key) for key, m in MODELS.items()]
