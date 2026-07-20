from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = 8956469977:AAEbtu3PDx6sKBmyogz7nZTD4xm1LH-M_yE

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 Bienvenue sur ProScore FIFA Bot\n\n"
        "⚽ Score Exact\n"
        "🎮 FIFA\n"
        "📊 Pronostics\n"
        "📞 Contact Admin"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot démarré...")
    app.run_polling()

if __name__ == "__main__":
    main()
