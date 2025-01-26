import requests
import random
import string
import time

TELEGRAM_TOKEN = "7911469039:AAFbpPSKTvgGT9cdzyB-wkwNsmFToxT5-Lw"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"  # Замініть на ID чату або каналу, куди надсилатимуться повідомлення
BASE_URL = "https://gachi.gay/"

def random_string(length=5):
    """Генерує випадкову строку з великих та малих літер."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def check_for_image(url):
    """Перевіряє, чи є відповідь від сайту зображенням."""
    try:
        response = requests.get(url, stream=True, timeout=5)
        content_type = response.headers.get('Content-Type', '')
        return 'image' in content_type  # Перевіряємо, чи це зображення
    except requests.RequestException:
        return False

def send_to_telegram(url):
    """Надсилає повідомлення в Telegram."""
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": f"Знайдено зображення: {url}"
    }
    try:
        response = requests.post(telegram_url, json=payload)
        if response.status_code == 200:
            print(f"Повідомлення надіслано: {url}")
        else:
            print(f"Помилка при надсиланні повідомлення: {response.text}")
    except Exception as e:
        print(f"Не вдалося надіслати повідомлення: {e}")

while True:
    random_part = random_string()
    url = f"{BASE_URL}{random_part}"
    print(f"Перевіряю: {url}")
    
    if check_for_image(url):
        print(f"Знайдено зображення за адресою: {url}")
        send_to_telegram(url)  # Надсилаємо посилання в Telegram
    else:
        print("Зображення не знайдено. Продовжую...")
    
    # Затримка в 1 секунду
    time.sleep(1)