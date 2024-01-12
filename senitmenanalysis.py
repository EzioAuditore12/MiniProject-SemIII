import tkinter as tk
import boto3

root = tk.Tk()
root.geometry("400x240")
root.title("InkAlchemy SentimenAnalyzer")

textExample = tk.Text(root, height=10)
textExample.pack()

def getText2():
    aws_mag_con = boto3.session.Session(profile_name="MiniProjectIIIDEMO")
    client = aws_mag_con.client(service_name='comprehend', region_name="ap-south-1")
    result = textExample.get("1.0", "end-1c")
    print(result)
    response = client.detect_sentiment(Text=result, LanguageCode='en')

    # Determine the prominent sentiment
    prominent_sentiment = max(response['SentimentScore'], key=response['SentimentScore'].get)

    print(f"The prominent sentiment is: {prominent_sentiment}")
    print(f"Sentiment Score is: {response['SentimentScore'][prominent_sentiment]}")
    print("Major text is:")
    if 'KeyPhrases' in response:
        for ph in response['KeyPhrases']:
            print(ph['Text'])
    else:
        print("No KeyPhrases found in the response.")


btnRead = tk.Button(root, height=1, width=10, text="Read", command=getText2)
btnRead.pack()

root.mainloop()






