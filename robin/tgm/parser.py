import telegram
import telegram.ext
from robin.tgm import data
from robin.tgm.response import guide
from robin.tgm.response import result
from robin.tgm import context_buffer as cb

from mysql.connector.connection_cext import CMySQLConnection


def parser(
    update: telegram.Update, context: telegram.ext.CallbackContext, db: CMySQLConnection
):
    if not cb.MainBuffer.has_expected_input(context):
        guide.Guide.invalid_input(update, context)

    expected_input = cb.MainBuffer.get_expected_input(context)
    input_ = str(update.message.text)

    if expected_input == data.ProcessScheduling.EXPECTED_INPUT["processes"]:
        processes = input_.replace(" ", "")
        scheduling_algo = cb.ProcessesSchedulingBuffer.get_scheduling_algorithm(context)
        cb.ProcessesSchedulingBuffer.set_processes(context, processes)

        if scheduling_algo == data.ProcessScheduling.GUIDE["round_robin"]:
            cb.MainBuffer.set_expected_input(
                context,
                data.ProcessScheduling.EXPECTED_INPUT["time_slice_and_modification"],
            )
            guide.ProcessesScheduling.round_robin_time_slice_and_modification(
                update, context
            )

        else:
            result.ProcessesScheduling.show_processes_execution(update, context, db)

    elif expected_input == data.Paging.EXPECTED_INPUT["logical_address_and_page_size"]:
        # Set excepted input
        cb.MainBuffer.set_expected_input(
            context, data.Paging.EXPECTED_INPUT["page_frame"]
        )
        # Compute page number and call get_real_address Paging method
        logical_address, page_size = input_.replace(" ", "").split("-")
        cb.PagingBuffer.set_logical_address(context, logical_address)
        page_size = result.Paging.convert_page_size(page_size)
        cb.PagingBuffer.set_page_size(context, page_size)
        page_number = result.Paging.get_page_number(logical_address, page_size)
        guide.Paging.get_real_address(update, context, page_number)

    elif expected_input == data.Paging.EXPECTED_INPUT["page_frame"]:
        page_frame = int(input_)
        cb.PagingBuffer.set_page_frame(context, page_frame)
        result.Paging.translate_logical_to_real(update, context, db)

    elif (
        expected_input
        == data.ProcessScheduling.EXPECTED_INPUT["time_slice_and_modification"]
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
        result.ProcessesScheduling.show_processes_execution(update, context, db)

    elif expected_input == data.Paging.EXPECTED_INPUT["frame_number_and_size"]:
        input_ = input_.replace(" ", "")
        frame_number, frame_size = input_.split("-")
        cb.PagingBuffer.set_frame_number(context, frame_number)
        cb.PagingBuffer.set_frame_size(context, frame_size)
        result.Paging.real_address_length(update, context, db)

    elif expected_input == data.Paging.EXPECTED_INPUT["page_number_and_size"]:
        input_ = input_.replace(" ", "")
        page_number, page_size = input_.split("-")
        cb.PagingBuffer.set_page_number(context, page_number)
        cb.PagingBuffer.set_page_size(context, page_size)
        result.Paging.logical_address_length(update, context, db)
