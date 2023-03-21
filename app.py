import gradio as gr
from whisperui import WhisperModelUI

my_app = gr.Blocks()
iface = WhisperModelUI(my_app)
iface.create_whisper_ui()
iface.launch()
