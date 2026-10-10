"""Local Stable Diffusion backend.

The pipeline loads the first time you generate with it, not at startup,
so the app opens instantly and OpenAI-only users never need a GPU.
"""

from functools import lru_cache

from registry import MODELS


@lru_cache(maxsize=1)
def _load_pipeline():
    import torch
    from diffusers import StableDiffusionPipeline

    model_id = MODELS["sd-1.5"].model_id
    print(f"Loading {model_id}...")

    if torch.cuda.is_available():
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
        # Keeps SD 1.5 inside 4 GB of VRAM (e.g. RTX 3050)
        pipe.enable_attention_slicing()
        pipe.enable_model_cpu_offload()
        device = "cuda"
    else:
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
        pipe.to("cpu")
        device = "cpu"

    print(f"Model loaded on {device}.")
    return pipe, device


def generate_local(prompt, negative_prompt, width, height, count, steps, guidance, seed):
    import torch

    pipe, device = _load_pipeline()

    generator = None
    if seed is not None and seed >= 0:
        generator = torch.Generator(device="cpu").manual_seed(int(seed))

    result = pipe(
        prompt,
        negative_prompt=negative_prompt or None,
        width=width,
        height=height,
        num_images_per_prompt=int(count),
        num_inference_steps=int(steps),   # 20-35 is the sweet spot
        guidance_scale=float(guidance),   # 5-8: higher follows the prompt more literally
        generator=generator,
    )
    return result.images
