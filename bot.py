import os
import time
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

questions = [
    "📚 Grade 12 Biology\nWhich organelle produces most cellular ATP?\nA) Nucleus\nB) Mitochondrion\nC) Ribosome\nD) Golgi apparatus",
    "📚 Grade 12 Physics\nWhat is the SI unit of force?\nA) Joule\nB) Watt\nC) Newton\nD) Pascal",
    "📚 Grade 12 Mathematics\nWhat is the derivative of x²?\nA) x\nB) 2x\nC) x³\nD) 2",
]

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(
        url,
        json={"chat_id": CHAT_ID, "text": text},
        timeout=20,
    )
    response.raise_for_status()

while True:
    for question in questions:
        send_message("📝 Grade 12 Test\n\n" + question)
        time.sleep(300)
