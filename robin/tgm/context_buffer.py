"""
The bot needs to store user inputs in order to return the
correct command.

These inputs are stored in context.user_data dictionary.

This file contain static classes and functions to manage
context.user_data effectively.
"""

import telegram.ext
from datetime import datetime

"""
Tasks buffers
"""


class MainBuffer:
    def set_expected_input(context: telegram.ext.CallbackContext, expected_input: str):
        context.user_data["expected_input"] = expected_input

    def get_expected_input(context: telegram.ext.CallbackContext) -> str:
        return context.user_data["expected_input"]

    def has_expected_input(context: telegram.ext.CallbackContext):
        try:
            MainBuffer.get_expected_input(context)
            return True
        except KeyError:
            return False


class ProcessesSchedulingBuffer:
    def set_scheduling_algorithm(
        context: telegram.ext.CallbackContext, scheduling_algorithm: str
    ):
        """
        @scheduling_algorithm: "round_robin", "sjf", "srtn" or "fcfs"
        """
        context.user_data["scheduling_algorithm"] = scheduling_algorithm

    def get_scheduling_algorithm(context: telegram.ext.CallbackContext) -> str:
        return context.user_data["scheduling_algorithm"]

    def set_processes(context: telegram.ext.CallbackContext, processes: str):
        context.user_data["processes"] = processes

    def get_processes(context: telegram.ext.CallbackContext) -> str:
        return context.user_data["processes"]

    def set_time_slice(context: telegram.ext.CallbackContext, time_slice: str):
        context.user_data["time_slice"] = time_slice

    def get_time_slice(context: telegram.ext.CallbackContext) -> str:
        return context.user_data["time_slice"]

    def set_with_modification(
        context: telegram.ext.CallbackContext, with_modification: str
    ):
        context.user_data["with_modification"] = with_modification

    def get_with_modification(context: telegram.ext.CallbackContext) -> str:
        return context.user_data["with_modification"]

    def set_modification_change(
        context: telegram.ext.CallbackContext, modification_change: str
    ):
        context.user_data["modification_change"] = modification_change

    def get_modification_change(context: telegram.ext.CallbackContext) -> str:
        return context.user_data["modification_change"]


class PagingBuffer:
    def set_logical_address(
        context: telegram.ext.CallbackContext, logical_address: str
    ):
        context.user_data["paging_logical_address"] = logical_address

    def set_page_size(context: telegram.ext.CallbackContext, page_size: str):
        context.user_data["paging_page_size"] = page_size

    def get_page_size(context: telegram.ext.CallbackContext):
        return context.user_data["paging_page_size"]

    def set_page_frame(context: telegram.ext.CallbackContext, page_frame: str):
        context.user_data["paging_page_frame"] = page_frame

    def get_logical_to_real_parameters(context: telegram.ext.CallbackContext):
        return (
            context.user_data["paging_logical_address"],
            context.user_data["paging_page_size"],
            context.user_data["paging_page_frame"],
        )

    def set_frame_size(context: telegram.ext.CallbackContext, frame_size: int):
        context.user_data["paging_frame_size"] = frame_size

    def get_frame_size(context: telegram.ext.CallbackContext):
        return context.user_data["paging_frame_size"]

    def set_frame_number(context: telegram.ext.CallbackContext, frame_number: int):
        context.user_data["paging_frame_number"] = frame_number

    def get_frame_number(context: telegram.ext.CallbackContext):
        return context.user_data["paging_frame_number"]

    def set_page_number(context: telegram.ext.CallbackContext, page_number: int):
        context.user_data["paging_page_number"] = page_number

    def get_page_number(context: telegram.ext.CallbackContext):
        return context.user_data["paging_page_number"]


"""
Database buffer
"""


class DatabaseBuffer:
    def set_task_start_time(context: telegram.ext.CallbackContext):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        context.user_data["task_start_time"] = now

    def get_task_start_time(context: telegram.ext.CallbackContext):
        return context.user_data["task_start_time"]
