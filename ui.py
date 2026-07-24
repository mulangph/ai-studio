import gradio as gr

from model import generate_image
from prompt_engine import enhance_prompt


def create(prompt, style):

    enhanced = enhance_prompt(
        prompt,
        style
    )

    image = generate_image(
        enhanced
    )

    return image, enhanced


#Build the UI using gradio
def build_ui():

    with gr.Blocks() as demo:

        gr.Markdown(
        """
        # 🎨 AI Creative Studio

        Text-to-image generation
        using Stable Diffusion
        """
        )


        prompt = gr.Textbox(
            label="Describe your image"
        )


        style = gr.Dropdown(
            label="Your style",
            choices=[
                "Cinematic",
                "Anime",
                "Cyberpunk",
                "Fantasy",
                "3D"
            ],
            value="Cinematic"
        )


        button = gr.Button(
            "Generate"
        )


        image = gr.Image()

        enhanced = gr.Textbox(
            label="Enhanced Prompt"
        )


        button.click(
            create,
            inputs=[
                prompt,
                style
            ],
            outputs=[
                image,
                enhanced
            ]
        )


    return demo