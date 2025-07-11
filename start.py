from flask import Flask
from threading import Thread
from telethon.sync import TelegramClient, events
import yt_dlp
import asyncio
import os

# إعداد Flask للسيرفر
app = Flask(__name__)

@app.route('/')
def index():
    return '🤖 Bot is running'

def run_flask():
    app.run(host='0.0.0.0', port=10000)

Thread(target=run_flask).start()

# بيانات Telethon
api_id = 21843289
api_hash = '3c634c61bf31d05bb7259ad714c25aed'
client = TelegramClient('session', api_id, api_hash)

# الرد على /start
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.reply('✅ البوت جاهز! أرسل رابط أي فيديو وسأقوم بتنزيله لك.')

# الرد على أي رابط فيديو
@client.on(events.NewMessage)
async def download_handler(event):
    url = event.raw_text.strip()

    if not url.startswith("http"):
        return  # تجاهل أي رسالة ليست رابط

    # أرسل رسالة انتظار
    waiting_msg = await event.reply("📥 جاري تنزيل الفيديو... يرجى الانتظار...")

    try:
        # إعداد yt-dlp
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/%(id)s.%(ext)s',
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info)

        # إرسال الفيديو
        await client.send_file(event.chat_id, video_path, caption="✅ تم التنزيل بنجاح.")

        # حذف الفيديو بعد الإرسال
        os.remove(video_path)

        # حذف رسالة "جاري التنزيل"
        await waiting_msg.delete()

    except Exception as e:
        await waiting_msg.edit(f"❌ حدث خطأ أثناء التنزيل:\n{str(e)}")

print("✅ Bot is running...")
client.start()
client.run_until_disconnected()
