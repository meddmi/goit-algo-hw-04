"""This module contains functions to draw a Koch snowflake using the turtle graphics library."""

import turtle

from colorized_logger import print_error as log_error, Color


def koch_curve(pen: turtle.Turtle, recursion_level: int, length: float) -> None:
    """Draw one side of a Koch snowflake."""
    if recursion_level == 0:
        pen.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(pen, recursion_level - 1, length / 3)
            pen.left(angle)


def draw_koch_snowflake(recursion_level: int, length: float = 300) -> None:
    """Draw a Koch snowflake of a given recursion level."""
    window = turtle.Screen()
    window.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.goto(-length / 2, 0)
    pen.pendown()

    for _ in range(3):
        koch_curve(pen, recursion_level, length)
        pen.right(120)

    window.mainloop()


def main() -> None:
    """Prompt the user for the recursion level of the Koch snowflake and draw it."""
    try:
        input_prompt = (
            f"{Color.CYAN}Enter recursion level for the Koch snowflake (0-5): {Color.RESET}"
        )
        koch_order = int(input(input_prompt))

        if koch_order < 0 or koch_order > 5:
            log_error("Recursion level must be an integer between 0 and 5.")
            return

        draw_koch_snowflake(koch_order)

    except ValueError:
        log_error("Please enter a valid integer for the recursion level of the Koch snowflake.")
    except turtle.Terminator:
        log_error("Drawing was stopped because the turtle window was closed.")


if __name__ == "__main__":
    main()
