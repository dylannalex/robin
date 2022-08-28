import os
import telegram
import telegram.ext
from robin.tgm.response import text
from robin.tgm.callback import callback


class ExampleButton(telegram.InlineKeyboardButton):
    def __init__(self, callback_task: callback.CallbackTask, data_: str):
        super().__init__(
            text=text.NEED_AN_EXAMPLE_BUTTON,
            callback_data=callback.Callback.get_callback(
                callback.CallbackType.EXAMPLE, callback_task, data_
            ),
        )


class ProcessesSchedulingExample:
    PROCESSES_TABLE_IMG_PATH = os.path.abspath(
        "./robin/tgm/img/processes-table-example.png"
    )

    def load_processes(update: telegram.Update, context: telegram.ext.CallbackContext):
        chat_id = update.effective_user["id"]
        context.bot.sendPhoto(
            chat_id=chat_id,
            photo=open(ProcessesSchedulingExample.PROCESSES_TABLE_IMG_PATH, "rb"),
        )
        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.LOAD_PROCESSES_EXAMPLE,
            chat_id=chat_id,
        )

    def round_robin_without_modification_change(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        chat_id = update.effective_user["id"]
        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.ROUND_ROBIN_WITHOUT_MODIFICATION_CHANGE_EXAMPLE,
            chat_id=chat_id,
        )

    def round_robin_with_modification_change(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        chat_id = update.effective_user["id"]
        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.ROUND_ROBIN_WITH_MODIFICATION_CHANGE_EXAMPLE,
            chat_id=chat_id,
        )


class PagingExample:
    PAGING_TABLE_IMG_PATH = os.path.abspath("./robin/tgm/img/paging-table-example.png")

    def translate_logical_to_real(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        chat_id = update.effective_user["id"]
        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.TRANSLATE_LOGICAL_TO_REAL_EXAMPLE,
            chat_id=chat_id,
        )

    def get_real_address(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        chat_id = update.effective_user["id"]
        for i, message in enumerate(text.GET_REAL_ADDRESS_EXAMPLE):
            context.bot.sendMessage(
                parse_mode="MarkdownV2",
                text=message,
                chat_id=chat_id,
                disable_web_page_preview=True,
            )
            if i == 0:
                context.bot.sendPhoto(
                    chat_id=chat_id,
                    photo=open(PagingExample.PAGING_TABLE_IMG_PATH, "rb"),
                )

    def real_address_length(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        chat_id = update.effective_user["id"]
        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.REAL_ADDRESS_LENGTH_EXAMPLE,
            chat_id=chat_id,
        )

    def logical_address_length(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        chat_id = update.effective_user["id"]
        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.LOGICAL_ADDRESS_LENGTH_EXAMPLE,
            chat_id=chat_id,
        )
