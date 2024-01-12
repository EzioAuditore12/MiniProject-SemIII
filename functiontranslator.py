import tkinter as tk
import boto3

root = tk.Tk()
root.geometry("400x240")
root.title("InkAlchemy Translator")

textExample = tk.Text(root, height=10)
textExample.pack()

def get_text(target_language_code):
    aws_mag_con = boto3.session.Session(profile_name='MiniProjectIIIDEMO')
    client = aws_mag_con.client(service_name='translate', region_name='ap-south-1')
    result = textExample.get("1.0", "end")
    print(result)
    response = client.translate_text(Text=result, SourceLanguageCode='en', TargetLanguageCode=target_language_code)
    translated_text = response.get('TranslatedText')
    print('Translated Text:', translated_text.encode('utf-8').decode('utf-8'))  # decode here
    print("Source Language Code: " + response.get('SourceLanguageCode'))
    print("Target Language Code: " + response.get('TargetLanguageCode'))

# Function to translate to Hindi
def translate_to_hindi():
    get_text('hi')

# Function to translate to Spanish
def translate_to_spanish():
    get_text('es')

# Function to translate to French
def translate_to_french():
    get_text('fr')

btnRead = tk.Button(root, height=1, width=10, text="Hindi", command=translate_to_hindi)
btnRead.pack()

# Buttons for additional languages
btnSpanish = tk.Button(root, height=1, width=10, text="Spanish", command=translate_to_spanish)
btnSpanish.pack()

btnFrench = tk.Button(root, height=1, width=10, text="French", command=translate_to_french)
btnFrench.pack()

root.mainloop()
