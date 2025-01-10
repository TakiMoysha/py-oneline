import random
from time import sleep
from typing import Any

from rich.traceback import install
from rich.console import Console, ConsoleOptions, RenderResult
from rich.layout import Layout
from rich.live import Live
from rich.table import Table


console = Console()
install()


def generate_table() -> Table:
    table = Table()
    table.add_column("ID")
    table.add_column("Value")
    table.add_column("Status")

    for row in range(random.randint(2, 6)):  # noqa: S311
        value = random.random() * 100  # noqa: S311
        table.add_row(f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS")

    return table


def build_root_layout() -> Layout:
    _layout = Layout(name="root")
    _layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=4),
    )
    _layout["main"].split_row(
        Layout(name="size"),
        Layout(name="body", ratio=2, minimum_size=60),
    )
    _layout["size"].split(
        Layout(name="box1"),
        Layout(name="box2"),
    )

    return _layout


class BaseScreen:
    def __init__(self) -> None:
        pass

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        raise NotImplementedError("Subclasses must implement this method")


class AboutScreen(BaseScreen):
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        yield generate_table()


class WorkspaceScreen(BaseScreen):
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        layout = Layout(name="workspace")
        layout.split_column(
            Layout(name="buffer", size=3),
            Layout(name="preview", ratio=1),
        )
        yield layout


class App:
    SCREENS = {"about": AboutScreen, "workspace": WorkspaceScreen}

    def __init__(self) -> None:
        self._properties = []

    def __len__(self) -> int:
        return len(self._properties)

    def append(self, prop: Any) -> None:
        self._properties.append(prop)

    def pop(self) -> Any:
        return self._properties.pop()

    def clear(self) -> None:
        self._properties = []

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        properties = Table(expand=True)
        properties.add_column("Property")
        properties.add_column("Value")
        for prop in self._properties:
            properties.add_row(prop[0], prop[1])

        yield properties


def run_app(is_debug: bool) -> int:
    status_code = 0
    app = App()

    for i in range(10):
        app.append((f"Property {i}", f"Value {i}"))

    try:
        with Live(app, refresh_per_second=1) as live:
            input()
            console.push_render_hook(live)
            live.stop()
            pass
    except KeyboardInterrupt:
        pass

    return status_code
