import nox

source_directory = "app/"


@nox.session(python=["3.8"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "xml", "-i")
    session.run("coverage", "report")


@nox.session(reuse_venv=True)
def lint(session):
    session.run("flakehell", "lint", source_directory)
    session.run("black", "--check", source_directory)


@nox.session(reuse_venv=True)
def check_typing(session):
    session.run("mypy", source_directory)


@nox.session(reuse_venv=True)
def check_dependencies(session):
    session.run(
        "poetry",
        "export",
        "--format=requirements.txt",
        "--output=.reports/requirements.txt",
    )
    session.run("safety", "check", "--full-report", "-r", ".reports/requirements.txt")
