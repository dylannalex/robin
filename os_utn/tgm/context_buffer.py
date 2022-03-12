"""
The bot needs to store user inputs in order to return the
correct command.

These inputs are stored in context.user_data dictionary.

This file contain static classes and functions to manage
context.user_data effectively.
"""

import telegram.ext


class MainBuffer:
    # Callbacks
    CALLBACK_EXAMPLE_INDICATOR = "example-"
    PROCESSES_SCHEDULING_CALLBACK = "processes_scheduling_callback"

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
    # Scheduling algorithm
    RR_SA = "round_robin"
    SJF_SA = "sjf"
    SRTN_SA = "srtn"
    FCFS_SA = "fcfs"

    # Expected inputs:
    PROCESSES_EI = "processes"
    RR_TIME_SLICE_AND_MODIFICATION_EI = "round_robin_time_slice_and_modification"

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
