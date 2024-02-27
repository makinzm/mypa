"""Initialize cli for myma."""
from typing import Self

import fire

from myma.pyproject import PyProject

pyproject = PyProject()

class MyMa:
    """MyMa class."""
    def lock(self: Self) -> str:
        dependences = pyproject.get_myma_dependencies()
        python_version = pyproject.get_python_version()
        return (
            f"//---Python version---\n\t: {python_version}\n"
            f"//---Dependencies---\n\t: {dependences}"
        )

def cli() -> None:
    """Run myma."""
    fire.Fire(MyMa)
