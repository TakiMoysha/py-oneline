import random
import time

from rich import print
from rich.layout import Layout
from rich.live import Live
from rich.table import Table

from disearch.tui import DiSearcher


def generate_table() -> Table:
    table = Table()
    table.add_column("ID")
    table.add_column("Value")
    table.add_column("Status")

    for row in range(random.randint(2, 6)):
        value = random.random() * 100
        table.add_row(f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS")

    return table


def screen_render() -> Layout:
    layout = Layout()

    return layout


def cli_app():
    with Live(screen_render(), refresh_per_second=4) as live:
        pass


# def cli_app():
#     instance = DiSearcher()
#
#     instance.run()
