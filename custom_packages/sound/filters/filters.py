# relative import
from ..effects import echo

def filter_a():
    print("Invoked filter a and calling echo function...")
    echo.echo_a()
