from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5737467887:AAGJNk6eYzh_nyQ4wqqD96ei3CHxmJyUsGA",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "HI there I am champion")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
