from typer.testing import CliRunner

from levelcalculator import __app_name__, __version__, cli

runner = CliRunner()

def test_version():
    result = runner.invoke(cli, ['--version'])

    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.output

def test_calculate_level():
    result = runner.invoke(cli, )