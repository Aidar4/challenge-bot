import os

import telebot
import time
import schedule
from datetime import date, timedelta, datetime

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

START_DATE = date(2025, 2, 1)

def calculate_challenge_data():
    today = date.today()
    day_number = (((today - START_DATE).days + 1)/2)+ 0.5
    burpees_count = 20 + (day_number*2 - 2)
    return day_number, burpees_count

def create_message():
    day_number, burpees_count = calculate_challenge_data()
    message = f"Сегодня {day_number}-й день челленджа. Задание - сделать {burpees_count} шт. берпи. " \
              f"Можно разделить на любое количество не менее 10-ти раз за 1 подход. " \
              f"Выкладываем видео в этот чат. Желаем удачного дня!"
    return message

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, create_message())

def send_daily_message():
    bot.send_message(message, create_message())

def schedule_messages():
    while True:
        now = datetime.now().time()
        target_time = datetime.combine(date.today(), datetime.min.time()).replace(hour=9)
        if now > datetime.min.time().replace(hour=9):
            target_time += timedelta(days=1)
        time_diff = (target_time - datetime.combine(date.today(), now)).total_seconds()
        time.sleep(time_diff)

        send_daily_message()

        time.sleep(2 * 24 * 60 * 60)


if __name__ == '__main__':
    import threading
    threading.Thread(target=schedule_messages, daemon=True).start()
    bot.infinity_polling()

