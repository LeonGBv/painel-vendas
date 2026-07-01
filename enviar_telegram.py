import requests
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def enviar_mensagem(texto):

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    requests.post(url, data={
        'chat_id': CHAT_ID,
        'text': texto
    })