import argparse
import logging

from structlog import get_logger

parser = argparse.ArgumentParser(prog="taki-python")
parser.add_argument("-l", "--level", dest="log_level", default=10, type=int)
parser.add_argument("-c", "--command", dest="command")
parser.add_argument("entrypoint", nargs="+", help="Executed start point.")
parser.add_argument("args", nargs=argparse.REMAINDER)
args = parser.parse_args()

log_level = logging.getLevelName(args.log_level)
logging.basicConfig(filename="tmp/taki-python.log", level=log_level)

logger = get_logger()
logger.debug("debug")
logger.info("info")


def repl():
    """Read-eval-print loop."""


def execute():
    """Execute filename."""
