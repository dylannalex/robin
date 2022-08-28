from matplotlib import pyplot as plt
from robin.operating_system.processes import scheduler


PROCESS_RUNNING_COLOR = "#8E65FF"
ROW_COLS_COLOR = "#BFBFBF"


def chart(table: scheduler.ExecutionsTable, path_to_save_plot: str) -> None:
    last_time = table.executions[-1]["time"]
    columns = list(range(last_time + 1))
    rows = sorted([p.name for p in table.processes])
    colors = [["w" for _ in columns] for _ in rows]
    cell_text = [["" for _ in columns] for _ in rows]

    # Change cell color
    for interval in table.executions_intervals:
        x0 = interval["initial_time"]
        x1 = interval["final_time"]
        process = interval["process"]
        process_index = rows.index(process)
        for i in range(x0, x1 + 1):
            colors[process_index][i] = PROCESS_RUNNING_COLOR

    # Add an "X" when a process arrives
    for process in table.processes:
        process_index = rows.index(process.name)
        cell_text[process_index][process.arrival_time] = "X"

    fig, ax = plt.subplots()
    ax.axis("tight")
    ax.axis("off")
    plt.table(
        cellText=cell_text,
        cellColours=colors,
        rowLabels=rows,
        rowColours=[ROW_COLS_COLOR for _ in range(len(rows))],
        colLabels=columns,
        colColours=[ROW_COLS_COLOR for _ in range(len(columns))],
        loc="center",
    )

    plt.savefig(path_to_save_plot)
