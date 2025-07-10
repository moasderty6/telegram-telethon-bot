# telegram-selenium-clicker

مشروع بوت تلغرام يستخدم Selenium لمحاكاة الضغط على الأزرار بشكل تلقائي.

## الملفات

- `bot_clicker.py`: سكربت البوت الرئيسي باستخدام Selenium.
- `Dockerfile`: ملف تعريف الحاوية لتشغيل البوت داخل Docker.
- `README.md`: هذا الملف.

## كيفية الاستخدام

1. استنساخ الريبو:
   ```bash
   git clone https://github.com/YourUsername/telegram-selenium-clicker.git
   cd telegram-selenium-clicker
   ```

2. بناء وتشغيل الحاوية:
   ```bash
   docker build -t telegram-selenium-clicker .
   docker run -d telegram-selenium-clicker
   ```

## الربط مع Render.com

بعد رفع المشروع إلى GitHub، اربطه بخدمة Render لإنشاء Web Service ونشر البوت تلقائيًا.

---

إذا احتجت أي مساعدة، تواصل معي!
