from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7729105161:AAEqZCJSQpZBEybUS3ftd1r18YFPirV7RfA"

@app.route('/')
def home():
    return 'Bot is alive!'

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text == '/start':
            send_message(chat_id, "Sveikas! Aš veikiu 🚀")

    return '', 200

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
