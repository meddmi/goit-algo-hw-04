"""Small helpers for colored terminal output without dependencies."""

import sys


class Color:
    """ANSI color codes for terminal output."""

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"


def colorized_print(message: str, color: str) -> None:
    """Print a message in color if the output is a terminal."""
    if sys.stdout.isatty():
        print(f"{color}{message}{Color.RESET}")
    else:
        print(message)


def print_error(message: str) -> None:
    """Print an error message in red."""
    colorized_print(message, Color.RED)


def print_warning(message: str) -> None:
    """Print a warning message in yellow."""
    colorized_print(message, Color.YELLOW)


def print_info(message: str) -> None:
    """Print an info message in cyan."""
    colorized_print(message, Color.CYAN)
