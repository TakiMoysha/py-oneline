from typing import TYPE_CHECKING

import rich
from rich.text import Text
from textual.app import App, ComposeResult, RenderResult
from textual.binding import Binding
from textual.widgets import Static
from textual.screen import Screen

from disearch.__about__ import VERSION

if TYPE_CHECKING:
    from disearch.tui import DiSearcher

# mods:
# - existed file
# - buffer input


class AboutMessage(Static):
    @property
    def app(self) -> "DiSearcher":
        app = super().app

        if not isinstance(app, DiSearcher):
            raise Exception("jfpiqhgaodg")

        return app

    def render(self) -> RenderResult:
        msg = f"DiSearch v{VERSION}"
        text = Text.from_markup(msg)
        return text


class AboutScreen(Screen):
    BINDING = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield AboutMessage()


class DiSearcher(App):
    SCREENS = {
        "about": AboutScreen,
    }

    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit", show=True, priority=True),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = "NORMAL"

    async def action_quit(self) -> None:
        return await super().action_quit()
