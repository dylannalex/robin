import telegram
import telegram.ext
from os_utn.tgm.task import guide
from os_utn.tgm.task import example
from os_utn.tgm import context_buffer as cb


class Callback:
    def query_handler(update: telegram.Update, context: telegram.ext.CallbackContext):
        cqd = update.callback_query.data

        # Start
        if cqd == cb.MainBuffer.PROCESSES_SCHEDULING_CALLBACK:
            guide.ProcessesScheduling.select_processes_scheduling_algorithm(
                update, context
            )

        if cqd == cb.MainBuffer.PAGING_CALLBACK:
            guide.Paging.select_task(update, context)

        # Precesses Scheduling
        if cqd in (
            cb.ProcessesSchedulingBuffer.RR_SA,
            cb.ProcessesSchedulingBuffer.SJF_SA,
            cb.ProcessesSchedulingBuffer.SRTN_SA,
            cb.ProcessesSchedulingBuffer.FCFS_SA,
        ):

            if cqd == cb.ProcessesSchedulingBuffer.RR_SA:
                cb.ProcessesSchedulingBuffer.set_scheduling_algorithm(
                    context, cb.ProcessesSchedulingBuffer.RR_SA
                )

            if cqd == cb.ProcessesSchedulingBuffer.SJF_SA:
                cb.ProcessesSchedulingBuffer.set_scheduling_algorithm(
                    context, cb.ProcessesSchedulingBuffer.SJF_SA
                )

            if cqd == cb.ProcessesSchedulingBuffer.SRTN_SA:
                cb.ProcessesSchedulingBuffer.set_scheduling_algorithm(
                    context, cb.ProcessesSchedulingBuffer.SRTN_SA
                )

            if cqd == cb.ProcessesSchedulingBuffer.FCFS_SA:
                cb.ProcessesSchedulingBuffer.set_scheduling_algorithm(
                    context, cb.ProcessesSchedulingBuffer.FCFS_SA
                )

            cb.MainBuffer.set_expected_input(
                context, cb.ProcessesSchedulingBuffer.PROCESSES_EI
            )
            guide.ProcessesScheduling.load_processes(update, context)

        # Paging
        if cqd == cb.PagingBuffer.TRANSLATE_LOGICAL_TO_REAL:
            cb.MainBuffer.set_expected_input(
                context, cb.PagingBuffer.LOGICAL_ADDRESS_AND_PAGE_SIZE
            )
            guide.Paging.translate_logical_to_real(update, context)

        if cqd == cb.PagingBuffer.REAL_ADDRESS_LENGTH:
            cb.MainBuffer.set_expected_input(
                context, cb.PagingBuffer.FRAME_NUMBER_AND_SIZE
            )
            guide.Paging.real_address_length(update, context)

        if cqd == cb.PagingBuffer.LOGICAL_ADDRESS_LENGTH:
            cb.MainBuffer.set_expected_input(
                context, cb.PagingBuffer.PAGE_NUMBER_AND_SIZE
            )
            guide.Paging.logical_address_length(update, context)

        # Examples
        if cqd.startswith(cb.MainBuffer.CALLBACK_EXAMPLE_INDICATOR):
            cqd = cqd.split("-")[1]
            Callback._example_query_handler(cqd, update, context)

    def _example_query_handler(
        cqd, update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        if cqd == cb.ProcessesSchedulingBuffer.PROCESSES_EI:
            example.ProcessesSchedulingExample.load_processes(update, context)

        elif cqd == cb.ProcessesSchedulingBuffer.RR_TIME_SLICE_AND_MODIFICATION_EI:
            example.ProcessesSchedulingExample.round_robin_time_slice_and_modification(
                update, context
            )

        elif cqd == cb.PagingBuffer.TRANSLATE_LOGICAL_TO_REAL:
            example.PagingExample.translate_logical_to_real(update, context)

        elif cqd == cb.PagingBuffer.GET_REAL_ADDRESS:
            example.PagingExample.get_real_address(update, context)

        elif cqd == cb.PagingBuffer.REAL_ADDRESS_LENGTH:
            example.PagingExample.real_address_length(update, context)

        elif cqd == cb.PagingBuffer.LOGICAL_ADDRESS_LENGTH:
            example.PagingExample.logical_address_length(update, context)
