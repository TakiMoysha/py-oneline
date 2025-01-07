import argparse
import logging

import structlog


class App:
    ns: argparse.Namespace
    logger: structlog.BoundLogger

    def __init__(self, ns: argparse.Namespace) -> None:
        self.ns = ns
        self.logger = structlog.get_logger()

    def __del__(self) -> None:
        self.logger.info("End of app!", ns=self.ns)


def cli_app() -> App:
    parser = argparse.ArgumentParser(prog="taki-python")
    parser.add_argument("-l", "--log-level", dest="level", default=10, type=int)

    parser.add_argument("entrypoint", nargs="?", type=argparse.FileType("r"), help="Executed start point.")
    parser.add_argument("-c", "--command", dest="command", help="Executed command.")

    parser.add_argument("args", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    log_level = logging.getLevelName(args.level)
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(getattr(logging, log_level)),
    )

    return App(args)
