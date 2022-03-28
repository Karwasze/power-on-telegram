import telebot
import os
import subprocess


MAC_ADDRESS = os.getenv('MAC_ADDRESS', "not_specified")
if MAC_ADDRESS == "not_specified":
    print("Please provide environment variable MAC_ADDRESS as described in the README.md")
    exit(1)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', "not_specified")
if TELEGRAM_TOKEN == "not_specified":
    print("Please provide environment variable TELEGRAM_TOKEN as described in the README.md")
    exit(1)

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def turn_on(message):
    subprocess.call(['sudo', 'etherwake', '-i', 'eth0', MAC_ADDRESS])
    bot.reply_to(message, "Computer turned on!")


bot.infinity_polling()
