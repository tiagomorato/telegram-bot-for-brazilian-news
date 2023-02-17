from bs4 import BeautifulSoup
import logging
import telebot
import requests


# Outputs debug messages to the console
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

API_KEY = '<YOUR-TELEGRAM-BOT-API-KEY>'
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['g1'])
def greet(message):
    url = "https://g1.globo.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    global elements_g1
    elements_g1 = soup.find_all("a", class_="feed-post-link gui-color-primary gui-color-hover")

    # Save indexed messages
    messages = [f"{index}. {element.text}" for index, element in enumerate(elements_g1, 1)]

    # Send message
    bot.reply_to(message, "Please choose the news you want to look at closer:\n" + "\n\n".join(messages))


@bot.message_handler(func=lambda message: message.text.isdigit())
def redirect_handler(message):
    index = int(message.text)

    try:
        selected_element = elements_g1[index - 1]
    except IndexError:
        bot.reply_to(message, "You chose an invalid number.")
    else:
        bot.reply_to(message, f"You have selected: {selected_element.text}.\n"
                                          f"Redirecting you to: {selected_element['href']}")

bot.infinity_polling(timeout=10, long_polling_timeout=5)