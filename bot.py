
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
updater = Updater(token='637395215:AAHVL1tdFrKGQP6eoGbREzw6Lf4XBmaoxu8') # API Telagram BotFather
dispatcher = updater.dispatcher
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, я только учусь, но я хочу пообщаться с тобой')
def textMessage(bot, update):
    request = apiai.ApiAI('1b2e2a4d678248bbb7a0fa6fc9058b48').text_request() #  API Dialogflow 
    request.lang = 'ru' 
    request.session_id = 'BatlabAIBot' # for learn bot
    request.query = update.message.text 
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Моя королева Анна не научила еще этому')#хих

        #!!!!!!!
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
updater.start_polling(clean=True)
updater.idle()
