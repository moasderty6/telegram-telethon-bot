from telethon.sync import TelegramClient, events

api_id = 21843289
api_hash = '3c634c61bf31d05bb7259ad714c25aed'

# هذا يفترض أن ملف session.session موجود في نفس المجلد
client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(pattern='/start'))
async def handler(event):
    await event.reply('🤖 البوت يعمل تلقائيًا على Render!')

client.start()
print("✅ Bot is running...")
client.run_until_disconnected()
