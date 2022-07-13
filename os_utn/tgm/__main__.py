import telegram
import telegram.ext
from os_utn.tgm import settings
from os_utn.tgm.task import guide
from os_utn.tgm.task import parser
from os_utn.tgm.callback import Callback


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

    # Commands
    dp.add_handler(telegram.ext.CommandHandler("start", guide.Guide.start))
    dp.add_handler(
        telegram.ext.MessageHandler(telegram.ext.Filters.text, parser.parser)
    )
    dp.add_handler(telegram.ext.CallbackQueryHandler(Callback.query_handler))
    run(updater)


if __name__ == "__main__":
    main()
