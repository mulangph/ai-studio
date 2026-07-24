import gradio as gr
from ui import build_ui


demo = build_ui()


if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        inbrowser=True
    )