import datetime
import os
from telegram import Bot

def enviar_mensaje(bot, chat_id):
    ahora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mensaje = f"📅 Aviso programado: Hoy es {ahora}"
    bot.send_message(chat_id=chat_id, text=mensaje)
    print(f"Mensaje enviado correctamente a las {ahora}")

if __name__ == '__main__':
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = int(os.getenv("TELEGRAM_CHAT_ID"))
    dias_aviso = os.getenv("DIAS_AVISO", "1").split(",")  # Ej: '1,15,28' → ['1', '15', '28']

    hoy = datetime.datetime.now().day

    if str(hoy) in dias_aviso:
        print(f"✅ Hoy es {hoy}, enviando aviso...")
        bot = Bot(token=token)
        enviar_mensaje(bot, chat_id)
    else:
        print(f"🔕 Hoy es {hoy}, no está en la lista de días configurados ({dias_aviso}). No se envía nada.")
