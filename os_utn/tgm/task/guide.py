"""
This file aims to guide the user through the bot
tasks.
"""

import telegram
import telegram.ext
from os_utn.tgm.task import text
from os_utn.tgm import context_buffer as cb
from os_utn.tgm.task import example
from os_utn.database import database

from mysql.connector.connection_cext import CMySQLConnection


class Guide:
    def start(
        update: telegram.Update,
        context: telegram.ext.CallbackContext,
        db: CMySQLConnection,
    ):
        # Add user to database if it is the first time he/she uses the bot
        if not database.is_tgm_user_added(db, update.effective_user["id"]):
            database.add_tgm_user(
                db,
                update.effective_user["username"],
                update.effective_user["first_name"],
                update.effective_user["id"],
            )

        # Set current time
        cb.DatabaseBuffer.set_task_start_time(context)

        # Show available tasks
        processes_scheduling_button = telegram.InlineKeyboardButton(
            text=text.PROCESSES_SCHEDULING_GUIDE_BUTTON,
            callback_data=cb.MainBuffer.PROCESSES_SCHEDULING_CALLBACK,
        )

        paging_button = telegram.InlineKeyboardButton(
            text=text.PAGING_BUTTON,
            callback_data=cb.MainBuffer.PAGING_CALLBACK,
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

    def invalid_input(update: telegram.Update, context: telegram.ext.CallbackContext):
        processes_scheduling_button = telegram.InlineKeyboardButton(
            text=text.PROCESSES_SCHEDULING_GUIDE_BUTTON,
            callback_data=cb.MainBuffer.PROCESSES_SCHEDULING_CALLBACK,
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.START_GUIDE,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup([[processes_scheduling_button]]),
        )


class ProcessesScheduling:
    def select_processes_scheduling_algorithm(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        round_robin_button = telegram.InlineKeyboardButton(
            text=text.ROUND_ROBBIN_BUTTON,
            callback_data=cb.ProcessesSchedulingBuffer.RR_SA,
        )
        sjf_button = telegram.InlineKeyboardButton(
            text=text.SJF_BUTTON,
            callback_data=cb.ProcessesSchedulingBuffer.SJF_SA,
        )

        srtn_button = telegram.InlineKeyboardButton(
            text=text.SRTN_BUTTON,
            callback_data=cb.ProcessesSchedulingBuffer.SRTN_SA,
        )

        fcfs_button = telegram.InlineKeyboardButton(
            text=text.FCFS_BUTTON,
            callback_data=cb.ProcessesSchedulingBuffer.FCFS_SA,
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
            cb.ProcessesSchedulingBuffer.PROCESSES_EI
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
        example_button = example.ExampleButton(
            cb.ProcessesSchedulingBuffer.RR_TIME_SLICE_AND_MODIFICATION_EI
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.RR_TIME_SLICE_AND_MODIFICATION,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup([[example_button]]),
        )


class Paging:
    def select_task(update: telegram.Update, context: telegram.ext.CallbackContext):
        translate_logical_to_real_button = telegram.InlineKeyboardButton(
            text=text.TRANSLATE_LOGICAL_TO_REAL_BUTTON,
            callback_data=cb.PagingBuffer.TRANSLATE_LOGICAL_TO_REAL,
        )
        real_address_length_button = telegram.InlineKeyboardButton(
            text=text.REAL_ADDRESS_LENGTH_BUTTON,
            callback_data=cb.PagingBuffer.REAL_ADDRESS_LENGTH,
        )

        logical_address_length_button = telegram.InlineKeyboardButton(
            text=text.LOGICAL_ADDRESS_LENGTH_BUTTON,
            callback_data=cb.PagingBuffer.LOGICAL_ADDRESS_LENGTH,
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
            cb.PagingBuffer.TRANSLATE_LOGICAL_TO_REAL
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
        example_button = example.ExampleButton(cb.PagingBuffer.GET_REAL_ADDRESS)

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
        example_button = example.ExampleButton(cb.PagingBuffer.REAL_ADDRESS_LENGTH)

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
        example_button = example.ExampleButton(cb.PagingBuffer.LOGICAL_ADDRESS_LENGTH)

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.LOGICAL_ADDRESS_LENGTH,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup([[example_button]]),
        )
