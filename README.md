# AI Creative Studio

Generate images from text with OpenAI's GPT Image models, GPT-4o, or Stable Diffusion running on your own GPU, in a dark Higgsfield-style Gradio interface.

## Features

- Pick a model per generation: GPT Image 2.5 Sunburst, GPT Image 2.5 Flare, GPT Image 2, GPT Image 1.5, GPT Image 1 Mini, GPT-4o, or local Stable Diffusion 1.5
- Eight style presets, written as tags for Stable Diffusion and as plain sentences for OpenAI models
- Square, landscape and portrait sizes, mapped to each model's native resolutions
- Up to 4 images per run, plus a session history tab
- Quality setting for OpenAI models; negative prompt, steps, prompt strength and seed for Stable Diffusion
- Stable Diffusion loads only when you first use it, so the app opens instantly

## Setup

```bash
uv sync
cp .env.example .env      # then paste your OpenAI key into .env
uv run main.py
```

The app opens at http://127.0.0.1:7860. You can also paste a key under Settings instead of using `.env`.

## Customising

- Models: add or edit entries in `registry.py`
- Colours and fonts: edit `COLORS` in `theme.py`
- Styles: edit `STYLES` in `prompt_engine.py`

## Project layout

| File | Purpose |
| --- | --- |
| `main.py` | Launches the app with the theme |
| `ui.py` | Layout and event wiring |
| `theme.py` | Colours, Gradio theme and CSS |
| `registry.py` | List of available models and sizes |
| `openai_models.py` | OpenAI Images API and Responses API backends |
| `model.py` | Local Stable Diffusion backend |
| `prompt_engine.py` | Style presets and prompt building |
