import requests
import os

def send_telegram_notification(name, email, message):
    token = os.environ.get('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID', 'YOUR_CHAT_ID')
    
    text = (
        "🔔 **Yangi aloqa xabari!**\n\n"
        f"👤 **Ism:** {name}\n"
        f"📧 **Email:** {email}\n"
        f"💬 **Xabar:**\n{message}"
    )
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown'
    }
    
    try:
        requests.post(url, json=payload, timeout=5)
    except requests.RequestException:
        pass