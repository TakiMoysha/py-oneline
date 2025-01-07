import argparse
import logging

import structlog

parser = argparse.ArgumentParser(prog="taki-python")
parser.add_argument("-l", "--log-level", dest="level", default=10, type=int)
parser.add_argument("-c", "--command", dest="command")
parser.add_argument("entrypoint", nargs="+", help="Executed start point.")
parser.add_argument("args", nargs=argparse.REMAINDER)
args = parser.parse_args()

log_level = logging.getLevelName(args.level)
structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(getattr(logging, log_level)),
)

logger = structlog.get_logger()
logger.debug("Database connection established")
logger.info("Processing data from the API", name="runtime", comment_id=5)
logger.warning("Resource usage is nearing capacity")
logger.error("Failed to save the file. Please check permissions")
logger.critical("System has encountered a critical failure. Shutting down")


def repl():
    """Read-eval-print loop."""


def execute():
    """Execute filename."""
