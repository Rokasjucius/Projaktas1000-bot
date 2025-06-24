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
    return '', 200
