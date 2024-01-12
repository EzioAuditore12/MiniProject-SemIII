import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import boto3

var1 = tk.Tk()
var1.geometry("450x400")
var1.title("InkAlchemy")
l1 = tk.Label(var1, text="Upload an image", width=30, font=('times', 18, 'bold'))
l1.pack()

# Initialize the Textract client
aws_mag_con = boto3.session.Session(profile_name='MiniProjectIIIDEMO')
client = aws_mag_con.client(service_name='textract', region_name='ap-south-1')

def upload_file():
    global img  # Store a reference to the image to prevent it from being garbage-collected
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)

    # Resize the image to fit the dialogue
    img_resize = img.resize((400, 200))
    img_tk = ImageTk.PhotoImage(img_resize)

    imgbytes = get_image_byte(filename)
    
    # Display the image on a button
    img_button = tk.Button(var1, image=img_tk)
    img_button.image = img_tk  # Store a reference to the image in the button
    img_button.pack()

    # Use the correct client when calling detect_document_text
    response = client.detect_document_text(Document={'Bytes': imgbytes})
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            print(item['Text'])

def get_image_byte(filename):
    with open(filename, 'rb') as imgfile:
        return imgfile.read()

b1 = tk.Button(var1, text='Upload file to see its content in text', width=30, command=upload_file)
b1.pack()

var1.mainloop()
