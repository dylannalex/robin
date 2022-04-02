import telegram
import telegram.ext
from os_utn.tgm.commands import guide
from os_utn.tgm.commands import result
from os_utn.tgm import context_buffer as cb


def parser(update: telegram.Update, context: telegram.ext.CallbackContext):
    if not cb.MainBuffer.has_expected_input(context):
        guide.Guide.invalid_input(update, context)

    expected_input = cb.MainBuffer.get_expected_input(context)
    input_ = str(update.message.text)

    if expected_input == cb.ProcessesSchedulingBuffer.PROCESSES_EI:
        processes = input_.replace(" ", "")
        cb.ProcessesSchedulingBuffer.set_processes(context, processes)

        if (
            cb.ProcessesSchedulingBuffer.get_scheduling_algorithm(context)
            == cb.ProcessesSchedulingBuffer.RR_SA
        ):
            cb.MainBuffer.set_expected_input(
                context, cb.ProcessesSchedulingBuffer.RR_TIME_SLICE_AND_MODIFICATION_EI
            )
            guide.ProcessesScheduling.round_robin_time_slice_and_modification(
                update, context
            )

        else:
            result.ProcessesScheduling.show_processes_execution(update, context)

    elif expected_input == cb.PagingBuffer.LOGICAL_ADDRESS_AND_PAGE_SIZE:
        # Set excepted input
        cb.MainBuffer.set_expected_input(context, cb.PagingBuffer.PAGE_FRAME)
        # Compute page number and call get_real_address Paging method
        logical_address, page_size = input_.replace(" ", "").split("-")
        cb.PagingBuffer.set_logical_address(context, logical_address)
        page_size = result.Paging.convert_page_size(page_size)
        cb.PagingBuffer.set_page_size(context, page_size)
        page_number = result.Paging.get_page_number(logical_address, page_size)
        guide.Paging.get_real_address(update, context, page_number)

    elif expected_input == cb.PagingBuffer.PAGE_FRAME:
        page_frame = int(input_)
        cb.PagingBuffer.set_page_frame(context, page_frame)
        result.Paging.translate_logical_to_real(update, context)
    elif (
        expected_input == cb.ProcessesSchedulingBuffer.RR_TIME_SLICE_AND_MODIFICATION_EI
    ):
        input_ = input_.replace(" ", "")
        time_slice, with_modification, modification_change = input_.split("-")
        cb.ProcessesSchedulingBuffer.set_time_slice(context, int(time_slice))
        cb.ProcessesSchedulingBuffer.set_with_modification(
            context, int(with_modification)
        )
        cb.ProcessesSchedulingBuffer.set_modification_change(
            context, int(modification_change)
        )
        result.ProcessesScheduling.show_processes_execution(update, context)

    elif expected_input == cb.PagingBuffer.FRAME_NUMBER_AND_SIZE:
        input_ = input_.replace(" ", "")
        frame_number, frame_size = input_.split("-")
        cb.PagingBuffer.set_frame_number(context, frame_number)
        cb.PagingBuffer.set_frame_size(context, frame_size)
        result.Paging.real_address_length(update, context)
