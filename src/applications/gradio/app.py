# [Embedding gradio within a fastapi app · Issue #1608 · gradio-app/gradio](https://github.com/gradio-app/gradio/issues/1608#issuecomment-1247038215)
import gradio as gr

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    btn = gr.Button("Greet")
    btn.click(
        fn=lambda name: "Hello, " + name + "!",
        inputs=name,
        outputs=output,
        api_name="greet",
    )


app = gr.routes.App.create_app(demo)
