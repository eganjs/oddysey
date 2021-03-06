import toml
from pyprojroot import here

from oddysey import __version__


def test_version():
    pyproject = toml.load(here("pyproject.toml"))

    assert __version__ == pyproject["tool"]["poetry"]["version"]
