from typer.testing import CliRunner

from level_calculator import __app_name__, __version__, cli

runner = CliRunner()

def test_version():
    result = runner.invoke(cli, ['--version'])

    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.output

def test_calculate_level_zero_experience():
    result = runner.invoke(cli, ['level', '0'])
    assert result.exit_code == 0
    assert f":sparkles: You are now level 1! :sparkles\n" in result.output

def test_calculate_level():
    result = runner.invoke(cli, ['level', '25'])

    assert result.exit_code == 0
    assert f":sparkles: You are now level 2! :sparkles\n" in result.output