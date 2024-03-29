import telegram
import telegram.ext
from robin.tgm import settings
from robin.tgm.response import guide
from robin.tgm import parser
from robin.database import database
from robin.tgm.callback import handler


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

    # Task Selector
    dp.add_handler(telegram.ext.CommandHandler("start", guide.Guide.select_task))
    # Parser
    dp.add_handler(
        telegram.ext.MessageHandler(
            telegram.ext.Filters.text,
            lambda update, context: parser.parser(update, context, db),
        )
    )
    # Query handler
    dp.add_handler(
        telegram.ext.CallbackQueryHandler(
            lambda update, context: handler.query_handler(update, context, db)
        )
    )

    run(updater)


if __name__ == "__main__":
    main()
