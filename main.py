from theme import CSS, theme
from ui import build_ui

demo = build_ui()


if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        inbrowser=True,
        theme=theme,   # Gradio 6 takes theme/css in launch(), not Blocks()
        css=CSS,
    )
