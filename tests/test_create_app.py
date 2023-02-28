from pathlib import Path

from typer.testing import CliRunner

from fastapi_cli_tool.main import app

runner = CliRunner()

CREATED_SUCCESSFULLY = "FastAPI app created successfully! 🎉\n"
ALREADY_EXISTS = "App potato already exists. ❌\n"


def test_startapp_success(tmp_path: Path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["startapp", "potato"])
        assert result.output == CREATED_SUCCESSFULLY
        assert result.exit_code == 0
        
def test_startapp_exists(tmp_path: Path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["startapp", "potato"])
        assert result.output == CREATED_SUCCESSFULLY
        assert result.exit_code == 0
        
        result = runner.invoke(app, ["startapp", "potato"])
        assert result.output == ALREADY_EXISTS
        assert result.exit_code == 0
        