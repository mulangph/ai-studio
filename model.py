import torch
from diffusers import StableDiffusionPipeline


MODEL_ID = "runwayml/stable-diffusion-v1-5"


print("Loading model...")


pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16
)


# Important for RTX 3050 4GB
# For memory optimization
pipe.enable_attention_slicing()
pipe.enable_model_cpu_offload()


print("Model loaded!")

#Main function to generate image
def generate_image(prompt):

    result = pipe(
        prompt,
        height=512,
        width=512,
        num_inference_steps=25, #Quality slider, sweet spot between 20-35, low=blur, higher=longer time to generate
        guidance_scale=7.5  #Creativity vs Strictiness Toggle sweet spot 5.0 - 8.0, low value =AI choice, High=AI follows hard every single word
    )

    return result.images[0]