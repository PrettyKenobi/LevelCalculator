from typing import Optional

import typer
from rich import print
from rich.markup import escape
from rich.panel import Panel

from level_calculator import __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool) -> None:
    """Callback function for the `version` command. Prints `Level Calculator`
    followed by the version as defined in levelcalculator/__init__.py.

    :type value: boolean
    """
    if value:
        print(f"{escape(__app_name__)} {escape(__version__)}")
        raise typer.Exit()

@app.callback()
def version(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return


# def _calculate_level(experience: int) -> None:
# """Callback function for calculate_level command.

# :param experience: The total amount of experience the character has.
# :type experience: int
# """
# calculator = level_calculator.LevelCalculator(1, experience)
# new_level = calculator.calculate_level()
# print(f":sparkles: The current level is now {escape(new_level)}! :sparkels:")

    


@app.command()
def level(experience: int = typer.Argument(
..., 
help="The character's total experience points")) -> None:
    calc = level_calculator.LevelCalculator(1, experience)
    new_level = calc.calculate_new_level()
    print(f":sparkles: You are now level {escape(new_level)}! :sparkels:")
    raise typer.Exit()