"""
This file contains classes with commands that, given
the user inputs, computes and shows the results
"""

import os
import telegram
import telegram.ext
from os_utn.tgm import context_buffer as cb
from os_utn.operating_system.processes import process
from os_utn.operating_system.processes import scheduler
from os_utn.operating_system.processes import chart


class ProcessesScheduling:
    def _get_plot_path(user_id: str):
        return os.path.abspath(f"./os_utn/tgm/img/{user_id}.png")

    def _parse_processes(processes_string: str) -> list[process.InteractiveProcess]:
        """
        Parses the given processes string.

        @processes_string: process_name-arrival_time-total_executions|process_name-arrival_time-total_executions...

        Example:
            A-1-5,B-2-6,C-3-8
            >>> [process.Process("A", 1, 5), process.Process("B", 2, 6), process.Process("C", 3, 8)]
        """
        processes_list = [l.split("-") for l in processes_string.split(",")]
        return [
            process.InteractiveProcess(p[0], int(p[1]), int(p[2]))
            for p in processes_list
        ]

    def show_processes_execution(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        processes = ProcessesScheduling._parse_processes(
            cb.ProcessesSchedulingBuffer.get_processes(context)
        )

        chat_id = update.effective_user["id"]

        if (
            cb.ProcessesSchedulingBuffer.get_scheduling_algorithm(context)
            == cb.ProcessesSchedulingBuffer.RR_SA
        ):
            table = scheduler.InteractiveSystem.round_robin(
                processes,
                cb.ProcessesSchedulingBuffer.get_time_slice(context),
                cb.ProcessesSchedulingBuffer.get_with_modification(context),
                [cb.ProcessesSchedulingBuffer.get_modification_change(context)],
            )

        elif (
            cb.ProcessesSchedulingBuffer.get_scheduling_algorithm(context)
            == cb.ProcessesSchedulingBuffer.SJF_SA
        ):
            table = scheduler.BatchSystem.shortest_job_first(processes)

        elif (
            cb.ProcessesSchedulingBuffer.get_scheduling_algorithm(context)
            == cb.ProcessesSchedulingBuffer.SRTN_SA
        ):
            table = scheduler.BatchSystem.shortest_remaining_time_next(processes)

        elif (
            cb.ProcessesSchedulingBuffer.get_scheduling_algorithm(context)
            == cb.ProcessesSchedulingBuffer.FCFS_SA
        ):
            table = scheduler.BatchSystem.first_come_first_served(processes)

        # Get path were the plot will be stored
        chat_id = update.effective_user["id"]
        plot_path = ProcessesScheduling._get_plot_path(chat_id)

        # Generate plot and send it
        chart.chart(table, plot_path)
        context.bot.sendPhoto(
            chat_id=chat_id,
            photo=open(plot_path, "rb"),
        )

        # Remove plot
        os.remove(plot_path)
