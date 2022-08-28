"""
This file aims to guide the user through the bot
tasks.
"""

import telegram
import telegram.ext
from os_utn.tgm.response import text
from os_utn.tgm.callback import callback
from os_utn.tgm import data
from os_utn.tgm.response import example


class Guide:
    def select_task(
        update: telegram.Update,
        context: telegram.ext.CallbackContext,
    ):
        # Show available tasks
        processes_scheduling_button = telegram.InlineKeyboardButton(
            text=text.PROCESSES_SCHEDULING_GUIDE_BUTTON,
            callback_data=callback.Callback.get_callback(
                callback.CallbackType.GUIDE,
                callback.CallbackTask.SELECT_TASK,
                data.TaskSelector.GUIDE["process_scheduling"],
            ),
        )

        paging_button = telegram.InlineKeyboardButton(
            text=text.PAGING_BUTTON,
            callback_data=callback.Callback.get_callback(
                callback.CallbackType.GUIDE,
                callback.CallbackTask.SELECT_TASK,
                data.TaskSelector.GUIDE["paging"],
            ),
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.START_GUIDE,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup(
                [[processes_scheduling_button, paging_button]]
            ),
        )


class ProcessesScheduling:
    def select_processes_scheduling_algorithm(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        round_robin_button = telegram.InlineKeyboardButton(
            text=text.ROUND_ROBBIN_BUTTON,
            callback_data=callback.Callback.get_callback(
                callback.CallbackType.GUIDE,
                callback.CallbackTask.PROCESSES_SCHEDULING,
                data.ProcessScheduling.GUIDE["round_robin"],
            ),
        )
        sjf_button = telegram.InlineKeyboardButton(
            text=text.SJF_BUTTON,
            callback_data=callback.Callback.get_callback(
                callback.CallbackType.GUIDE,
                callback.CallbackTask.PROCESSES_SCHEDULING,
                data.ProcessScheduling.GUIDE["shortest_job_first"],
            ),
        )

        srtn_button = telegram.InlineKeyboardButton(
            text=text.SRTN_BUTTON,
            callback_data=callback.Callback.get_callback(
                callback.CallbackType.GUIDE,
                callback.CallbackTask.PROCESSES_SCHEDULING,
                data.ProcessScheduling.GUIDE["shortest_remaining_time_next"],
            ),
        )

        fcfs_button = telegram.InlineKeyboardButton(
            text=text.FCFS_BUTTON,
            callback_data=callback.Callback.get_callback(
                callback.CallbackType.GUIDE,
                callback.CallbackTask.PROCESSES_SCHEDULING,
                data.ProcessScheduling.GUIDE["first_come_first_served"],
            ),
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.SELECT_PROCESSES_SCHEDULING_ALGORITHM,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup(
                [[round_robin_button, sjf_button], [srtn_button, fcfs_button]]
            ),
        )

    def load_processes(update: telegram.Update, context: telegram.ext.CallbackContext):
        example_button = example.ExampleButton(
            callback.CallbackTask.PROCESSES_SCHEDULING,
            data.ProcessScheduling.EXAMPLE["load_processes"],
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.LOAD_PROCESSES,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup([[example_button]]),
        )

    def round_robin_time_slice_and_modification(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        example_without_modification_change_button = telegram.InlineKeyboardButton(
            text=text.RR_WITHOUT_MODIFICATION_CHANGE_EXAMPLE_BUTTON,
            callback_data=callback.Callback.get_callback(
                callback.CallbackType.EXAMPLE,
                callback.CallbackTask.PROCESSES_SCHEDULING,
                data.ProcessScheduling.EXAMPLE["rr_without_modification_change"],
            ),
        )
        example_with_modification_change_button = telegram.InlineKeyboardButton(
            text=text.RR_WITH_MODIFICATION_CHANGE_EXAMPLE_BUTTON,
            callback_data=callback.Callback.get_callback(
                callback.CallbackType.EXAMPLE,
                callback.CallbackTask.PROCESSES_SCHEDULING,
                data.ProcessScheduling.EXAMPLE["rr_with_modification_change"],
            ),
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.RR_TIME_SLICE_AND_MODIFICATION,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup(
                [
                    [example_without_modification_change_button],
                    [example_with_modification_change_button],
                ]
            ),
        )


class Paging:
    def select_task(update: telegram.Update, context: telegram.ext.CallbackContext):
        translate_logical_to_real_button = telegram.InlineKeyboardButton(
            text=text.TRANSLATE_LOGICAL_TO_REAL_BUTTON,
            callback_data=callback.Callback.get_callback(
                callback.CallbackType.GUIDE,
                callback.CallbackTask.PAGING,
                data.Paging.GUIDE["translate_logical_to_real"],
            ),
        )
        real_address_length_button = telegram.InlineKeyboardButton(
            text=text.REAL_ADDRESS_LENGTH_BUTTON,
            callback_data=callback.Callback.get_callback(
                callback.CallbackType.GUIDE,
                callback.CallbackTask.PAGING,
                data.Paging.GUIDE["real_address_length"],
            ),
        )

        logical_address_length_button = telegram.InlineKeyboardButton(
            text=text.LOGICAL_ADDRESS_LENGTH_BUTTON,
            callback_data=callback.Callback.get_callback(
                callback.CallbackType.GUIDE,
                callback.CallbackTask.PAGING,
                data.Paging.GUIDE["logical_address_length"],
            ),
        )
        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.PAGING_SELECT_TASK,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup(
                [
                    [
                        translate_logical_to_real_button,
                        real_address_length_button,
                        logical_address_length_button,
                    ],
                ]
            ),
        )

    def translate_logical_to_real(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        example_button = example.ExampleButton(
            callback.CallbackTask.PAGING,
            data.Paging.EXAMPLE["translate_logical_to_real"],
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.TRANSLATE_LOGICAL_TO_REAL,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup([[example_button]]),
        )

    def get_real_address(
        update: telegram.Update, context: telegram.ext.CallbackContext, page_number: int
    ):
        example_button = example.ExampleButton(
            callback.CallbackTask.PAGING,
            data.Paging.EXAMPLE["get_real_address"],
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.GET_REAL_ADDRESS(page_number),
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup([[example_button]]),
        )

    def real_address_length(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        example_button = example.ExampleButton(
            callback.CallbackTask.PAGING,
            data.Paging.EXAMPLE["real_address_length"],
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.REAL_ADDRESS_LENGTH,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup([[example_button]]),
        )

    def logical_address_length(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        example_button = example.ExampleButton(
            callback.CallbackTask.PAGING,
            data.Paging.EXAMPLE["logical_address_length"],
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.LOGICAL_ADDRESS_LENGTH,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup([[example_button]]),
        )
