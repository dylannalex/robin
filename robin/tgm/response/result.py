"""
This file contains classes with tasks that, given
the user inputs, computes and shows the results
"""

import os
import telegram
import telegram.ext
from datetime import datetime

from robin.database import database
from robin.database import settings as db_settings

from robin.tgm import context_buffer as cb
from robin.tgm.response import text
from robin.tgm import data
from robin.tgm.callback import callback

from robin.operating_system.processes import process
from robin.operating_system.processes import scheduler
from robin.operating_system.processes import chart
from robin.operating_system.tools import units_converter
from robin.operating_system.memory import paging
from robin import settings as repo_settings

from mysql.connector.connection_cext import CMySQLConnection


def send_result_messages(
    update: telegram.Update,
    context: telegram.ext.CallbackContext,
    db: CMySQLConnection,
    task_id: int,
    result_message: str,
):
    # Send result message
    if result_message:
        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=result_message,
            chat_id=update.effective_user["id"],
        )

    select_task_button = telegram.InlineKeyboardButton(
        text=text.BACK_TO_SELECT_TASK_BUTTON,
        callback_data=callback.Callback.get_callback(
            callback.CallbackType.GUIDE,
            callback.CallbackTask.SELECT_TASK,
            data.TaskSelector.GUIDE["tasks"],
        ),
    )

    support_me_button = telegram.InlineKeyboardButton(
        text=text.SUPPORT_ME_BUTTON, url=repo_settings.GITHUB_REPO_LINK
    )

    report_a_bug_button = telegram.InlineKeyboardButton(
        text=text.REPORT_A_BUG_BUTTON, url=repo_settings.GITHUB_REPO_ISSUES
    )

    context.bot.sendMessage(
        parse_mode="MarkdownV2",
        text=text.SUPPORT_ME_MESSAGE,
        chat_id=update.effective_user["id"],
        reply_markup=telegram.InlineKeyboardMarkup(
            [
                [support_me_button],
                [report_a_bug_button],
                [select_task_button],
            ]
        ),
    )

    # Save task log
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    database.add_task_log(
        db,
        cb.DatabaseBuffer.get_task_start_time(context),
        now,
        update.effective_user["id"],
        task_id,
    )


class ProcessesScheduling:
    def _get_plot_path(user_id: str):
        return os.path.abspath(f"./robin/tgm/img/{user_id}.png")

    def show_processes_execution(
        update: telegram.Update,
        context: telegram.ext.CallbackContext,
        db: CMySQLConnection,
    ):
        processes = process.ProcessList.parse_processes_string(
            cb.ProcessesSchedulingBuffer.get_processes(context)
        )
        scheduling_algo = cb.ProcessesSchedulingBuffer.get_scheduling_algorithm(context)
        chat_id = update.effective_user["id"]

        if scheduling_algo == data.ProcessScheduling.GUIDE["round_robin"]:
            scheduling_algo = "Round Robin"
            table = scheduler.InteractiveSystem.round_robin(
                processes,
                cb.ProcessesSchedulingBuffer.get_time_slice(context),
                cb.ProcessesSchedulingBuffer.get_with_modification(context),
                [cb.ProcessesSchedulingBuffer.get_modification_change(context)],
            )
            task_id = db_settings.ROUND_ROBIN_TASK_ID

        elif scheduling_algo == data.ProcessScheduling.GUIDE["shortest_job_first"]:
            scheduling_algo = "Shortest Job First"
            table = scheduler.BatchSystem.shortest_job_first(processes)
            task_id = db_settings.SJF_TASK_ID

        elif (
            scheduling_algo
            == data.ProcessScheduling.GUIDE["shortest_remaining_time_next"]
        ):
            scheduling_algo = "Shortest Remaining Time Next"
            table = scheduler.BatchSystem.shortest_remaining_time_next(processes)
            task_id = db_settings.SRTN_TASK_ID

        elif scheduling_algo == data.ProcessScheduling.GUIDE["first_come_first_served"]:
            scheduling_algo = "First Come First Served"
            table = scheduler.BatchSystem.first_come_first_served(processes)
            task_id = db_settings.FCFS_TASK_ID

        # Get path were the plot will be stored
        chat_id = update.effective_user["id"]
        plot_path = ProcessesScheduling._get_plot_path(chat_id)

        # Generate plot and send it
        chart.chart(table, plot_path)
        context.bot.sendPhoto(
            chat_id=chat_id,
            photo=open(plot_path, "rb"),
        )

        send_result_messages(
            update,
            context,
            db,
            task_id,
            text.PROCESSES_SCHEDULING_RESULT(
                scheduling_algo, table.get_execution_string()
            ),
        )

        # Remove plot
        os.remove(plot_path)


class Paging:
    def get_page_number(logical_address: str, page_size: int):
        return paging.get_page_number(logical_address, page_size)

    def convert_page_size(page_size: str):
        return units_converter.convert_size_unit_to_bytes(
            *units_converter.decompose_number(page_size)
        )

    def translate_logical_to_real(
        update: telegram.Update,
        context: telegram.ext.CallbackContext,
        db: CMySQLConnection,
    ):
        (
            logical_address,
            page_size,
            page_frame,
        ) = cb.PagingBuffer.get_logical_to_real_parameters(context)

        real_address = paging.get_real_address(logical_address, page_size, page_frame)

        send_result_messages(
            update,
            context,
            db,
            db_settings.TRANSLATE_LOGICAL_TO_REAL_TASK_ID,
            text.TRANSLATE_LOGICAL_TO_REAL_RESULT(real_address),
        )

    def real_address_length(
        update: telegram.Update,
        context: telegram.ext.CallbackContext,
        db: CMySQLConnection,
    ):
        frame_number = cb.PagingBuffer.get_frame_number(context)
        frame_size = cb.PagingBuffer.get_frame_size(context)

        real_address_length = paging.get_physical_address_length(
            int(frame_number), int(frame_size)
        )

        send_result_messages(
            update,
            context,
            db,
            db_settings.REAL_ADDRESS_LENGTH_TASK_ID,
            text.REAL_ADDRESS_LENGTH_RESULT(real_address_length),
        )

    def logical_address_length(
        update: telegram.Update,
        context: telegram.ext.CallbackContext,
        db: CMySQLConnection,
    ):
        page_number = cb.PagingBuffer.get_page_number(context)
        page_size = cb.PagingBuffer.get_page_size(context)

        logical_address_length_ = paging.get_physical_address_length(
            int(page_number), int(page_size)
        )

        send_result_messages(
            update,
            context,
            db,
            db_settings.LOGICAL_ADDRESS_LENGTH_TASK_ID,
            text.LOGICAL_ADDRESS_LENGTH_RESULT(logical_address_length_),
        )
