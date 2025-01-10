from rich.text import Text
from textual.app import ComposeResult, RenderResult
from textual.screen import Screen
from textual.widgets import Static

from disearch.__about__ import VERSION

# mods:
# - existed file
# - buffer input


class AboutMessage(Static):
    def render(self) -> RenderResult:
        msg = f"DiSearch v{VERSION}"
        text = Text.from_markup(msg)
        return text


class AboutScreen(Screen):
    BINDING = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield AboutMessage()


## ======================= BUFFER =========================
class Buffer(Screen):
    pass


## ======================= DISPLAY =========================
class Display(Screen):
    pass


## ======================= OUTPUT =========================
class Output(Screen):
    pass


from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Placeholder


class DashboardScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Dashboard Screen")
        yield Footer()


class SettingsScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Settings Screen")
        yield Footer()


class HelpScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Help Screen")
        yield Footer()


class ModesApp(App):
    def on_mount(self) -> None:
        self.switch_mode("dashboard")
