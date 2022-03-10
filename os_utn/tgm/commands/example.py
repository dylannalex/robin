import os
import time
import telegram
import telegram.ext
from os_utn.tgm.commands import text
from os_utn.tgm import context_buffer


class ExampleButton(telegram.InlineKeyboardButton):
    def __init__(self, callback_function: str):
        super().__init__(
            text=text.NEED_AN_EXAMPLE_BUTTON,
            callback_data=context_buffer.MainBuffer.CALLBACK_EXAMPLE_INDICATOR
            + callback_function,
        )


class ProcessesSchedulingExample:
    PROCESSES_TABLE_IMG_PATH = os.path.abspath(
        "./os_utn/tgm/img/processes-table-example.png"
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

    def round_robin_time_slice_and_modification(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        chat_id = update.effective_user["id"]
        for message in text.RR_TIME_SLICE_AND_MODIFICATION_EXAMPLE:
            context.bot.sendMessage(
                parse_mode="MarkdownV2",
                text=message,
                chat_id=chat_id,
            )
            time.sleep(3)
