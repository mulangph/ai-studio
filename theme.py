"""Higgsfield-inspired look: deep black canvas, graphite panels, electric lime accent.
Change the hex values in COLORS to re-skin the whole app."""

import gradio as gr

COLORS = {
    "bg": "#050505",        # page
    "panel": "#121212",     # control panel
    "raised": "#1C1C1C",    # inputs, chips
    "line": "#2A2A2A",      # borders
    "text": "#F4F4F2",
    "muted": "#8C8C88",
    "lime": "#D1FE17",      # Higgsfield accent
    "lime_hover": "#E2FF5C",
    "ink": "#0A0A0A",       # text on lime
}

c = COLORS

theme = gr.themes.Base(
    primary_hue=gr.themes.colors.lime,
    neutral_hue=gr.themes.colors.neutral,
    font=[gr.themes.GoogleFont("Inter Tight"), "ui-sans-serif", "system-ui", "sans-serif"],
    radius_size=gr.themes.sizes.radius_lg,
).set(
    body_background_fill=c["bg"],
    body_background_fill_dark=c["bg"],
    body_text_color=c["text"],
    body_text_color_dark=c["text"],
    body_text_color_subdued=c["muted"],
    body_text_color_subdued_dark=c["muted"],
    background_fill_primary=c["panel"],
    background_fill_primary_dark=c["panel"],
    background_fill_secondary=c["raised"],
    background_fill_secondary_dark=c["raised"],
    block_background_fill=c["panel"],
    block_background_fill_dark=c["panel"],
    block_border_color=c["line"],
    block_border_color_dark=c["line"],
    block_label_text_color=c["muted"],
    block_label_text_color_dark=c["muted"],
    block_title_text_color=c["text"],
    block_title_text_color_dark=c["text"],
    border_color_primary=c["line"],
    border_color_primary_dark=c["line"],
    input_background_fill=c["raised"],
    input_background_fill_dark=c["raised"],
    input_border_color=c["line"],
    input_border_color_dark=c["line"],
    input_border_color_focus=c["lime"],
    input_border_color_focus_dark=c["lime"],
    color_accent=c["lime"],
    color_accent_soft=c["raised"],
    color_accent_soft_dark=c["raised"],
    checkbox_background_color_selected=c["lime"],
    checkbox_background_color_selected_dark=c["lime"],
    slider_color=c["lime"],
    slider_color_dark=c["lime"],
    button_primary_background_fill=c["lime"],
    button_primary_background_fill_dark=c["lime"],
    button_primary_background_fill_hover=c["lime_hover"],
    button_primary_background_fill_hover_dark=c["lime_hover"],
    button_primary_text_color=c["ink"],
    button_primary_text_color_dark=c["ink"],
    button_primary_border_color=c["lime"],
    button_primary_border_color_dark=c["lime"],
    button_secondary_background_fill=c["raised"],
    button_secondary_background_fill_dark=c["raised"],
    button_secondary_text_color=c["text"],
    button_secondary_text_color_dark=c["text"],
    link_text_color=c["lime"],
    link_text_color_dark=c["lime"],
    loader_color=c["lime"],
    loader_color_dark=c["lime"],
)

CSS = f"""
:root {{ color-scheme: dark; }}
.gradio-container {{ max-width: 1480px !important; margin: 0 auto !important; padding: 0 20px 32px !important; }}
footer {{ display: none !important; }}

/* Top bar */
#topbar {{ display:flex; align-items:center; justify-content:space-between; padding:18px 4px 22px; }}
#topbar .brand {{ display:flex; align-items:center; gap:12px; font-size:20px; font-weight:700; letter-spacing:-0.02em; color:{c['text']}; }}
#topbar .mark {{ width:30px; height:30px; border-radius:9px; background:{c['lime']}; display:grid; place-items:center; }}
#topbar .tag {{ font-size:13px; color:{c['muted']}; }}

/* Left control panel */
#panel {{ background:{c['panel']}; border:1px solid {c['line']}; border-radius:20px; padding:18px !important; gap:14px !important; }}
#panel .block, #panel .form {{ border:none !important; background:transparent !important; box-shadow:none !important; }}
#model-blurb {{ padding:0 10px !important; overflow:visible !important; margin-top:-6px; }}
#model-blurb p {{ color:{c['muted']}; font-size:13px; line-height:1.4; margin:0; }}

/* Sliders */
input[type=range] {{ accent-color:{c['lime']}; }}

/* Prompt box */
#prompt textarea {{ font-size:15px !important; line-height:1.5 !important; min-height:120px; }}

/* Chip-style radios */
.chips .wrap {{ gap:8px !important; }}
.chips label {{ background:{c['raised']} !important; border:1px solid {c['line']} !important;
  border-radius:999px !important; padding:7px 14px !important; transition:border-color .15s, background .15s; }}
.chips label:hover {{ border-color:{c['muted']} !important; }}
.chips label.selected, .chips label:has(input:checked) {{ background:{c['lime']} !important; border-color:{c['lime']} !important; }}
.chips label.selected span, .chips label:has(input:checked) span {{ color:{c['ink']} !important; font-weight:600; }}
.chips input[type=radio] {{ display:none !important; }}

/* Generate button */
#generate {{ height:56px; font-size:16px !important; font-weight:700 !important; border-radius:14px !important;
  letter-spacing:-0.01em; box-shadow:0 0 0 0 {c['lime']}55; transition:box-shadow .2s, transform .05s; }}
#generate:hover {{ box-shadow:0 0 28px 0 {c['lime']}40; }}
#generate:active {{ transform:translateY(1px); }}

/* Canvas */
#canvas {{ background:{c['panel']}; border:1px solid {c['line']}; border-radius:20px; padding:10px !important; }}
#canvas .block {{ border:none !important; background:transparent !important; }}
#gallery {{ background:{c['bg']} !important; border-radius:14px !important; }}
#history {{ background:{c['bg']} !important; border-radius:14px !important; }}
.tab-nav button.selected, [role=tab][aria-selected=true] {{ color:{c['lime']} !important; border-color:{c['lime']} !important; }}

/* Keyboard focus */
button:focus-visible, input:focus-visible, textarea:focus-visible, label:focus-within {{ outline:2px solid {c['lime']} !important; outline-offset:2px; }}

@media (prefers-reduced-motion: reduce) {{ * {{ transition:none !important; }} }}
@media (max-width: 900px) {{ #topbar .tag {{ display:none; }} }}
"""

LOGO_SVG = (
    f'<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
    f'<path d="M3 13 8 3l5 10M5.2 9h5.6" stroke="{c["ink"]}" stroke-width="2.2" '
    f'stroke-linecap="round" stroke-linejoin="round"/></svg>'
)

HEADER_HTML = f"""
<div id="topbar">
  <div class="brand"><span class="mark">{LOGO_SVG}</span>AI Creative Studio</div>
  <div class="tag">Text to image with OpenAI and Stable Diffusion</div>
</div>
"""
