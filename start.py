from flask import Flask
from threading import Thread
from telethon.sync import TelegramClient, events

app = Flask(__name__)

@app.route('/')
def index():
    return '🤖 Bot is running'

def run_flask():
    app.run(host='0.0.0.0', port=10000)

Thread(target=run_flask).start()

api_id = 21843289
api_hash = '3c634c61bf31d05bb7259ad714c25aed'
client = TelegramClient('session', api_id, api_hash)
client.connect()

@client.on(events.NewMessage(pattern='/start'))
async def handler(event):
    await event.reply('✅ البوت يعمل تلقائيًا على Render (مجاني)!')

print("✅ Bot is running...")
client.run_until_disconnected()