import telegram
import telegram.ext
from os_utn.tgm import settings
from os_utn.tgm.response import guide
from os_utn.tgm import parser
from os_utn.database import database
from os_utn.tgm.callback import handler


if settings.MODE == "test":
    # Local access
    def run(updater):
        updater.start_polling()
        print("[STATUS] bot loaded")
        updater.idle()  # End bot with ctrl + C

elif settings.MODE == "deploy":
    # Heroku access
    def run(updater):
        updater.start_webhook(
            listen="0.0.0.0",
            port=settings.PORT,
            url_path=settings.TOKEN,
            webhook_url=f"https://{settings.HEROKU_APP_NAME}.herokuapp.com/{settings.TOKEN}",
        )


def main() -> None:
    bot = telegram.Bot(token=settings.TOKEN)
    updater = telegram.ext.Updater(bot.token, use_context=True)
    dp = updater.dispatcher
    db = database.connect()

    # Commands
    dp.add_handler(
        telegram.ext.CommandHandler(
            "start", lambda update, context: guide.Guide.start(update, context, db)
        )
    )
    dp.add_handler(
        telegram.ext.MessageHandler(
            telegram.ext.Filters.text,
            lambda update, context: parser.parser(update, context, db),
        )
    )
    dp.add_handler(telegram.ext.CallbackQueryHandler(handler.query_handler))
    run(updater)


if __name__ == "__main__":
    main()
