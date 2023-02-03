#!/usr/bin/env python3
from decouple import config
import telegram
from telegram.ext import CommandHandler, ContextTypes, Updater, ApplicationBuilder

TOKEN = config('TELEGRAM_API_KEY')

print('### [ BOT is running ] ###')
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name} and welcome')

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}, you can get in touch @th333boo')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
    Current commands available:

    /start Welcome Message
    /contact @th333boo
    """)

# dispatcher.add_handler(CommandHandler("start", start))
# dispatcher.add_handler(CommandHandler("contact", contact))
# dispatcher.add_handler(CommandHandler("help", help))
# updater.run_polling()
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("help", help))
app.run_polling()

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# async def start_command(update,context):
#     await update.message.reply_text(f'start {update.effective_user.first_name}')


# app = ApplicationBuilder().token().build()
# app.add_handler(CommandHandler("hello", hello))
# app.run_polling()