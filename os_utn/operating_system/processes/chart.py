from numpy import arange
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from os_utn.operating_system.processes import scheduler


def chart(table: scheduler.ExecutionsTable, path_to_save_plot: str) -> None:
    plt.figure(figsize=(1.2 * len(table.executions), 1.2 * len(table.processes)))
    dx = 0.45
    for interval in table.executions_intervals:
        x0 = interval["initial_time"] + dx
        x1 = interval["final_time"] - dx
        process = [interval["process"], interval["process"]]
        plt.plot([x0, x1], process, color="green", linestyle="solid", linewidth=20)

    x_ticks = list(range(len(table.executions)))

    plt.xticks(ticks=arange(0.5, len(table.executions) + 0.5, 1), labels=x_ticks)

    minor_locator = AutoMinorLocator(2)
    plt.gca(which="both")
    plt.gca().xaxis.set_minor_locator(minor_locator)
    plt.grid(which="minor")
    plt.savefig(path_to_save_plot)
