import sys

from .cli import cli_app


def repl():
    """Read-eval-print loop."""
    cli_app()


def parse_command(command: str): ...


def parse_entrypoint(entrypoint: str): ...


def execute(input: str | None = None):
    """Execute filename."""
    cli_app()


def main() -> sys.exit:
    app = cli_app()

    if app.ns.command:
        bytecode = parse_command(app.ns.command)
        execute(bytecode)
    elif app.ns.entrypoint:
        bytecode = parse_entrypoint(app.ns.entrypoint)
        execute(bytecode)
    else:
        repl()

    sys.exit(0)
