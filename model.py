import torch
from diffusers import StableDiffusionPipeline


MODEL_ID = "runwayml/stable-diffusion-v1-5"


print("Loading model...")


pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16
)


# Important for RTX 3050 4GB
pipe.enable_attention_slicing()
pipe.enable_model_cpu_offload()


print("Model loaded!")


def generate_image(prompt):

    result = pipe(
        prompt,
        height=512,
        width=512,
        num_inference_steps=25,
        guidance_scale=7.5
    )

    return result.images[0]