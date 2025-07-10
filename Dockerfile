FROM python:3.11-slim

# تثبيت المتطلبات
RUN apt-get update && apt-get install -y chromium-driver chromium && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# تثبيت المكتبات
RUN pip install selenium telethon flask

# إضافة Flask وهمي فقط لفتح منفذ
EXPOSE 10000

# سكربت Flask + البوت
CMD ["python", "start.py"]
