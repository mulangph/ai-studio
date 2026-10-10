import gradio as gr
from dotenv import load_dotenv

from model import generate_local
from openai_models import GenerationError, generate_openai
from prompt_engine import DEFAULT_NEGATIVE, STYLES, enhance_prompt
from registry import DEFAULT_MODEL, MODELS, choices, size_for
from theme import HEADER_HTML

load_dotenv()

HISTORY_LIMIT = 48


def create(model_key, prompt, style, aspect, quality, count,
           negative, steps, guidance, seed, api_key, history,
           progress=gr.Progress()):
    if not prompt or not prompt.strip():
        raise gr.Error("Describe the image you want first.")

    model = MODELS[model_key]
    count = min(int(count), model.max_images)
    width, height = size_for(model, aspect)
    enhanced = enhance_prompt(prompt, style, model.provider)

    progress(0.1, desc=f"Generating with {model.label}")
    try:
        if model.provider == "local":
            images = generate_local(enhanced, negative, width, height, count, steps, guidance, seed)
        else:
            images = generate_openai(model, enhanced, width, height, count, quality, api_key)
    except GenerationError as err:
        raise gr.Error(str(err))
    except Exception as err:  # e.g. CUDA out of memory
        raise gr.Error(f"{model.label} failed: {err}")

    caption = f"{model.label}: {prompt.strip()[:80]}"
    history = ([(img, caption) for img in images] + (history or []))[:HISTORY_LIMIT]
    return images, enhanced, history, history


def on_model_change(model_key):
    model = MODELS[model_key]
    is_local = model.provider == "local"
    return (
        gr.update(value=model.blurb),
        gr.update(visible=not is_local),                 # quality
        gr.update(visible=is_local),                     # local-only settings
        gr.update(visible=not is_local),                 # api key
        gr.update(maximum=model.max_images),
    )


def build_ui():
    with gr.Blocks(title="AI Creative Studio", fill_width=True) as demo:
        history = gr.State([])

        gr.HTML(HEADER_HTML)

        with gr.Row(equal_height=False):
            # ---------- Controls ----------
            with gr.Column(scale=4, min_width=340, elem_id="panel"):
                model_key = gr.Dropdown(
                    label="Model", choices=choices(), value=DEFAULT_MODEL, interactive=True,
                )
                model_blurb = gr.Markdown(MODELS[DEFAULT_MODEL].blurb, elem_id="model-blurb")

                prompt = gr.Textbox(
                    label="Prompt", lines=5, max_lines=12, elem_id="prompt",
                    placeholder="A lone astronaut walking through a field of glowing flowers at dusk",
                )

                style = gr.Radio(
                    label="Style", choices=list(STYLES), value="Cinematic", elem_classes="chips",
                )
                aspect = gr.Radio(
                    label="Aspect ratio", choices=["Square", "Landscape", "Portrait"],
                    value="Square", elem_classes="chips",
                )
                quality = gr.Radio(
                    label="Quality", choices=["Low", "Medium", "High", "Auto"],
                    value="Medium", elem_classes="chips",
                    info="Higher quality takes longer and costs more.",
                )
                count = gr.Slider(label="Images", minimum=1, maximum=4, step=1, value=1)

                with gr.Accordion("Settings", open=False):
                    api_key = gr.Textbox(
                        label="OpenAI API key", type="password",
                        placeholder="Uses OPENAI_API_KEY from .env when empty",
                    )
                    with gr.Group(visible=False) as local_settings:
                        negative = gr.Textbox(label="Negative prompt", value=DEFAULT_NEGATIVE, lines=2)
                        steps = gr.Slider(label="Steps", minimum=10, maximum=50, step=1, value=25,
                                          info="20 to 35 is the sweet spot.")
                        guidance = gr.Slider(label="Prompt strength", minimum=1, maximum=15, step=0.5,
                                             value=7.5, info="Higher follows your words more literally.")
                        seed = gr.Number(label="Seed", value=-1, precision=0,
                                         info="-1 picks a random seed each time.")

                generate = gr.Button("Generate", variant="primary", elem_id="generate")

            # ---------- Canvas ----------
            with gr.Column(scale=8, elem_id="canvas"):
                with gr.Tabs():
                    with gr.Tab("Result"):
                        gallery = gr.Gallery(
                            show_label=False, columns=2, height=620, object_fit="contain",
                            elem_id="gallery", preview=True,
                        )
                        enhanced = gr.Textbox(
                            label="Prompt sent to the model", lines=2, interactive=False,
                            buttons=["copy"],
                        )
                    with gr.Tab("History"):
                        history_gallery = gr.Gallery(
                            show_label=False, columns=4, height=700, object_fit="cover",
                            elem_id="history",
                        )

        model_key.change(
            on_model_change, inputs=model_key,
            outputs=[model_blurb, quality, local_settings, api_key, count],
        )

        inputs = [model_key, prompt, style, aspect, quality, count,
                  negative, steps, guidance, seed, api_key, history]
        outputs = [gallery, enhanced, history, history_gallery]
        generate.click(create, inputs, outputs)

    return demo
