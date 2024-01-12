import tkinter as tk
import sys
import os
from tempfile import gettempdir
from contextlib import closing

# Create the main window
root = tk.Tk()
root.geometry("400x240")
root.title("InkAlchemy")

# Create the headline
headline = tk.Label(root, text="InkAlchemy", font=("Helvetica", 16))
headline.pack()

# Dynamically import functions from each file
def import_functions(module_name):
    module = __import__(module_name)
    return getattr(module, 'upload_file'), getattr(module, 'translate_to_hindi'), getattr(module, 'getText2'), getattr(module, 'getText3')

# Define the command for each button
def call_function(imported_functions):
    imported_functions()

btn_extract = tk.Button(root, height=1, width=10, text="Extract handwritten text", command=lambda: call_function(import_functions('functionextract')))
btn_extract.pack()

btn_translator = tk.Button(root, height=1, width=10, text="Translator", command=lambda: call_function(import_functions('functiontranslator')))
btn_translator.pack()

btn_senitmenanalysis = tk.Button(root, height=1, width=10, text="Sentiment analysis of text", command=lambda: call_function(import_functions('senitmenanalysis')))
btn_senitmenanalysis.pack()

btn_texttospeech = tk.Button(root, height=1, width=10, text="Text to speech", command=lambda: call_function(import_functions('texttospeech')))
btn_texttospeech.pack()

# Start the tkinter event loop
root.mainloop()
