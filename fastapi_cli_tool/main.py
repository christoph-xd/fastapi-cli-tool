from typing import Optional

import typer
from questionary.form import form
from fastapi_cli_tool.options import License, PackageManager, PythonVersion
from fastapi_cli_tool.helpers import question_list, question_input

app = typer.Typer(
    add_completion=False, help="Managing FastAPI applications!", name="FastAPI CLI Tool"
)


@app.command(help="Creates a new FastAPI project from the template.")
def startproject(
    name: str = typer.Option(""),
    license: Optional[License] = typer.Option(None, "--license", case_sensitive=False),
    python_version: PythonVersion = typer.Option(PythonVersion.THREE_DOT_EIG),
    packaging_manager: PackageManager = typer.Option(PackageManager.PIP),
):
    response = form(
        name=question_input(),
        python_version=question_list(PythonVersion),
        license=question_list(License),
        packaging_manager=question_list(PackageManager),
    ).ask()

    print(response)


@app.command(help="Create a new FastAPI App from the Tempalte.")
def startapp(name: str):
    pass
