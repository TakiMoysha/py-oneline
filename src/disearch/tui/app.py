from textual.app import App
from textual.binding import Binding

from disearch.tui.screens import AboutScreen


class TUIApp(App):
    SCREENS = {
        "about": AboutScreen,
    }

    MODES = {
        "about": AboutScreen,
        # "dashboard": DashboardScreen,
        # "settings": SettingsScreen,
        # "help": HelpScreen,
    }

    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit", show=True, priority=True),
        ("d", "switch_mode('dashboard')", "Dashboard"),
        ("s", "switch_mode('settings')", "Settings"),
        ("h", "switch_mode('help')", "Help"),
    ]

    def __init__(self, is_debug: bool, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.mode = "NORMAL"
        self.is_debug = is_debug

    async def action_quit(self) -> None:
        return await super().action_quit()
