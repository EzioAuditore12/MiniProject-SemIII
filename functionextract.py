import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import boto3

# Initialize the Textract client
aws_mag_con = boto3.session.Session(profile_name='MiniProjectIIIDEMO')
client = aws_mag_con.client(service_name='textract', region_name='ap-south-1')

def upload_file(root):
    global img, img_tk  # Add img_tk to the global variables
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    if filename:  # Check if a file was selected
        img = Image.open(filename)

        # Resize the image to fit the dialogue
        img_resize = img.resize((400, 200))
        img_tk = ImageTk.PhotoImage(img_resize)

        # Display the image on a button
        img_button = tk.Button(root, image=img_tk)
        img_button.image = img_tk  # Store a reference to the image in the button
        img_button.pack()

        with open(filename, 'rb') as imgfile:
            imgbytes = imgfile.read()

        # Use the correct client when calling detect_document_text
        response = client.detect_document_text(Document={'Bytes': imgbytes})
        for item in response['Blocks']:
            if item['BlockType'] == 'LINE':
                print(item['Text'])

def get_image_byte(filename):
    with open(filename, 'rb') as imgfile:
        return imgfile.read()
