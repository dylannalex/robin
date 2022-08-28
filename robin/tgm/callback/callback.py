class CallbackType:
    EXAMPLE = "EXAMPLE"
    GUIDE = "GUIDE"


class CallbackTask:
    SELECT_TASK = "SELECT_TASK"
    PROCESSES_SCHEDULING = "PROCESSES_SCHEDULING"
    PAGING = "PAGING"


class Callback:
    def get_callback(
        type: CallbackType,
        task: CallbackTask,
        data_: str,
    ) -> str:
        return f"{task}:{type}:{data_}"

    def parse_callback(
        cqd: str,
    ) -> tuple[CallbackType, CallbackTask, str]:
        task, type, data_ = cqd.split(":")
        return task, type, data_
