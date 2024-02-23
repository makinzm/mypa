"""Initialize cli for myma."""
from typing import Self

import fire


class MyMa:
    """MyMa class."""
    def hello(self: Self) -> str:
        """Hello world."""
        return "Hello, world!"

    def add(self: Self, a: int, b: int) -> int:
        """Add two numbers."""
        return a + b

def cli() -> None:
    """Run myma."""
    fire.Fire(MyMa)
