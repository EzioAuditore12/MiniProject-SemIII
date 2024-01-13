import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import sys
import os
from tempfile import gettempdir
from contextlib import closing

# Dynamically import the entire module
def import_module(module_name):
    return __import__(module_name)

# Create the main window
root = ThemedTk(theme="radiance")  # You can try other themes like 'arc', 'equilux', etc.
root.geometry("700x550")  # Increase the size of the main window
root.title("InkAlchemy")
root.configure(bg='AliceBlue') 

# Create a style to use for widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 24, "bold"), background="#3498db", foreground="black")  # Increase the font size of the "InkAlchemy" text

# Create the headline
headline = ttk.Label(root, text="   InkAlchemy  ", style="TLabel")
headline.pack(pady=30)  # Increase the padding below the "InkAlchemy" text

# Define a custom style for buttons
style.configure("TButton", font=("Helvetica", 12), background="#2ecc71", foreground="black", padding=5)

# Define the command for each button
def call_function(imported_module):
    # Call specific functions from the module as needed
    imported_module.upload_file(root)
    # Add other function calls as needed


btn_extract = ttk.Button(root, text="Extract handwritten text", style="TButton", command=lambda: call_function(import_module('functionextract')))
btn_extract.pack(pady=5)
btn_translator = ttk.Button(root, text="Translator", style="TButton", command=lambda: call_function(import_module('functiontranslator')))
btn_translator.pack(pady=5)

btn_senitmenanalysis = ttk.Button(root, text="Sentiment analysis of text", style="TButton", command=lambda: call_function(import_module('senitmenanalysis')))
btn_senitmenanalysis.pack(pady=5)

btn_texttospeech = ttk.Button(root, text="Text to speech", style="TButton", command=lambda: call_function(import_module('texttospeech')))
btn_texttospeech.pack(pady=5)

# Start the tkinter event loop
root.mainloop()
