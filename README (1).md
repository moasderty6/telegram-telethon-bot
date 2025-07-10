# Telegram Bot with Telethon (Render-ready)

بوت تلغرام يعمل باستخدام Telethon ويتم نشره تلقائيًا على Render.

## الملفات:
- `telethon_bot.py`: سكربت البوت باستخدام Telethon
- `Dockerfile`: لتشغيل البوت داخل حاوية Docker
- `session.session`: ملف الجلسة (يُولّد من جهازك)

## خطوات النشر على Render:
1. ارفع المشروع إلى GitHub
2. ادخل إلى https://render.com وأنشئ خدمة جديدة "Web Service"
3. اختر الريبو، واضبط الإعدادات:
   - Environment: Docker
   - Start Command: فارغة (موجود داخل Dockerfile)
4. اضف ملف `session.session` مع باقي الملفات قبل النشر

## ملاحظات:
- البوت يعمل تلقائيًا ويرد على رسالة `/start`
- تأكد من توليد session محليًا ورفعه مع الملفات
