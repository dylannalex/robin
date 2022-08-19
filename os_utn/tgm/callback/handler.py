import telegram
import telegram.ext
from os_utn.tgm.response import guide
from os_utn.tgm.response import example
from os_utn.tgm import data
from os_utn.tgm import context_buffer as cb
from os_utn.tgm.callback import callback


from abc import ABC
from abc import abstractmethod


class _CallbackHandler(ABC):
    def __init__(self, update: telegram.Update, context: telegram.ext.CallbackContext):
        self.update = update
        self.context = context

    @abstractmethod
    def handle_guide_callback(self) -> None:
        """Handles a guide callback"""

    @abstractmethod
    def handle_example_callback(self) -> None:
        """Handles an example callback"""


class _TaskSelector(_CallbackHandler):
    def __init__(self, update: telegram.Update, context: telegram.ext.CallbackContext):
        super().__init__(update, context)

    def handle_guide_callback(self, data_: str) -> None:
        if data_ == data.TaskSelector.TASK["process_scheduling"]:
            guide.ProcessesScheduling.select_processes_scheduling_algorithm(
                self.update, self.context
            )
        if data_ == data.TaskSelector.TASK["paging"]:
            guide.Paging.select_task(self.update, self.context)

    def handle_example_callback(self) -> None:
        pass


class _ProcessSchedulingCallbackHandler(_CallbackHandler):
    def __init__(self, update: telegram.Update, context: telegram.ext.CallbackContext):
        super().__init__(update, context)

    def handle_guide_callback(self, data_: str) -> None:
        if data_ not in (
            data.ProcessScheduling.GUIDE["round_robin"],
            data.ProcessScheduling.GUIDE["shortest_job_first"],
            data.ProcessScheduling.GUIDE["shortest_remaining_time_next"],
            data.ProcessScheduling.GUIDE["first_come_first_served"],
        ):
            raise ValueError("Invalid 'data_' for ProcessScheduling.")

        cb.ProcessesSchedulingBuffer.set_scheduling_algorithm(
            self.context,
            data_,
        )
        cb.MainBuffer.set_expected_input(
            self.context,
            data.ProcessScheduling.EXPECTED_INPUT["processes"],
        )
        guide.ProcessesScheduling.load_processes(self.update, self.context)

    def handle_example_callback(self, data_: str) -> None:
        if data_ == data.ProcessScheduling.EXAMPLE["load_processes"]:
            example.ProcessesSchedulingExample.load_processes(self.update, self.context)

        if (
            data_
            == data.ProcessScheduling.EXAMPLE["round_robin_time_slice_and_modification"]
        ):
            example.ProcessesSchedulingExample.round_robin_time_slice_and_modification(
                self.update, self.context
            )


class _PagingCallbackHandler(_CallbackHandler):
    def __init__(self, update: telegram.Update, context: telegram.ext.CallbackContext):
        super().__init__(update, context)

    def handle_guide_callback(self, data_: str):
        if data_ == data.Paging.GUIDE["translate_logical_to_real"]:
            cb.MainBuffer.set_expected_input(
                self.context,
                data.Paging.EXPECTED_INPUT["logical_address_and_page_size"],
            )
            guide.Paging.translate_logical_to_real(self.update, self.context)

        if data_ == data.Paging.GUIDE["real_address_length"]:
            cb.MainBuffer.set_expected_input(
                self.context,
                data.Paging.EXPECTED_INPUT["frame_number_and_size"],
            )
            guide.Paging.real_address_length(self.update, self.context)

        if data_ == data.Paging.GUIDE["logical_address_length"]:
            cb.MainBuffer.set_expected_input(
                self.context,
                data.Paging.EXPECTED_INPUT["page_number_and_size"],
            )
            guide.Paging.logical_address_length(self.update, self.context)

    def handle_example_callback(self, data_: str) -> None:
        if data_ == data.Paging.EXAMPLE["translate_logical_to_real"]:
            example.PagingExample.translate_logical_to_real(self.update, self.context)

        if data_ == data.Paging.EXAMPLE["get_real_address"]:
            example.PagingExample.get_real_address(self.update, self.context)

        if data_ == data.Paging.EXAMPLE["real_address_length"]:
            example.PagingExample.real_address_length(self.update, self.context)

        if data_ == data.Paging.EXAMPLE["logical_address_length"]:
            example.PagingExample.logical_address_length(self.update, self.context)


def query_handler(
    update: telegram.Update,
    context: telegram.ext.CallbackContext,
) -> None:
    cqd = update.callback_query.data
    task, type, data_ = callback.Callback.parse_callback(cqd)

    # Create callback_handler
    callback_handler: _CallbackHandler

    if task == callback.CallbackTask.SELECT_TASK:
        callback_handler = _TaskSelector(update, context)

    elif task == callback.CallbackTask.PROCESSES_SCHEDULING:
        callback_handler = _ProcessSchedulingCallbackHandler(update, context)

    elif task == callback.CallbackTask.PAGING:
        callback_handler = _PagingCallbackHandler(update, context)

    # Handle callback
    if type == callback.CallbackType.GUIDE:
        callback_handler.handle_guide_callback(data_)

    elif type == callback.CallbackType.EXAMPLE:
        callback_handler.handle_example_callback(data_)
