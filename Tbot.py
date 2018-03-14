import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import re
import time
token = ''


def start(bot, update):
    custom_keyboard = [[ 'Даты проведения экзаменов'], ['Информация о приёмной комиссии'], ['Алгоритм поступления'], ['Статистика проходных баллов']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(update.message.chat_id, text="Привет, здесь можно найти информацию о поступлении в МТУСИ", reply_markup=reply_markup)

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Чем могу помочь*')    
    
def answer(bot, update):
    
    if update.message.text=="Даты проведения экзаменов":
        bot.sendMessage(update.message.chat_id, text="https://abitur.mtuci.ru/#!ekz")
    elif update.message.text=="Информация о приёмной комиссии":
        bot.sendMessage(update.message.chat_id, text="Адрес приёмной комиссии: Москва, ул. Авиамоторная, дом 8 Тел:(495)673-36-25 E-mail: pk@mtuci.ru ")
        bot.sendMessage(update.message.chat_id, text="Часы работы приёмной комиссии с 10:00 до 17:00(кроме субботы и воскресенья, без перерыва на обед)")
        bot.sendPhoto(update.message.chat_id, photo="https://pp.userapi.com/c637120/v637120512/609cb/fQhOG2twL5Q.jpg")
    elif update.message.text=="Алгоритм поступления":
        bot.sendPhoto(update.message.chat_id, photo='https://pp.userapi.com/c836720/v836720820/53f0a/iCVxdOl1Gi8.jpg')
    elif update.message.text=="Статистика проходных баллов":
        bot.sendMessage(update.message.chat_id, text="https://abitur.mtuci.ru/new_abitur/documents/itogi/itogi_2015.pdf")
    else:
        update.message.text=="Что-то ещё?"


    
def main():

    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    #dp.add_handler (CallbackQueryHandler(button))
    dp.add_handler(MessageHandler([Filters.text], answer))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
