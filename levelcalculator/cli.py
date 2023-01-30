from typing import Optional

import typer

from levelcalculator import __app_name__, __version__

app = typer.Typer()

""" Callback function for the `version` command.

:param value:
"""
def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} {__version__}")
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

@app.callback()