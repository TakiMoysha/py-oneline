import argparse

from disearch.tui.app import TUIApp
from disearch.tui.raw_app import run_app


def cli_app():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", dest="debug", action="store_true", default=False)
    parser.add_argument("--textual", dest="textual", action="store_true", default=False)

    args = parser.parse_args()

    if args.textual:
        TUIApp(is_debug=args.debug).run()
    else:
        run_app(args.debug)
