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
