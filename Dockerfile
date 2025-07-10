FROM python:3.11-slim

# تثبيت متطلبات النظام
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    && rm -rf /var/lib/apt/lists/*

# نسخ ملفات المشروع
WORKDIR /app
COPY . /app

# تثبيت مكتبات بايثون المطلوبة
RUN pip install selenium

# تعيين متغير بيئة لموقع كروم
ENV CHROME_BIN=/usr/bin/chromium

CMD ["python", "bot_clicker.py"]
