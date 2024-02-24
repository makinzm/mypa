"""PyProject class to handle the pyproject.toml file."""
from __future__ import annotations

from platform import python_version
from typing import Self

from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from tomlkit.toml_file import TOMLFile


class PyProject:
    """PyProject class to handle the pyproject.toml file."""
    def __init__(self: Self, path: str = "pyproject.toml"):
        """Initialize the PyProject object."""
        self._path = path
        self._file = TOMLFile(self._path).read()

    def get_myma_dependencies(self: Self) -> list[Requirement]:
        """Return the myma dependencies."""
        requirements = self._file["project"]["dependencies"]
        return [Requirement(r) for r in requirements]

    def check_python_version(self: Self) -> bool:
        """Check if the system python version matches the required version."""
        version_required = self._file["project"].get("requires-python")
        system_version = python_version()
        if version_required and system_version in SpecifierSet(version_required):
            return True

        err_msg = f"Python version {system_version} does not match the required version {version_required}"
        raise ValueError(err_msg)
