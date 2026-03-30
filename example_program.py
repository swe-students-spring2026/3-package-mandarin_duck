"""
Basic example program to show the package functionality.

It demonstrates every function in ``src/nba_facts/facts.py``.
"""

from pathlib import Path
import sys

try:
    from nba_facts.facts import getDecade, getFact, getPosition, getTeam, parseJSON
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
    from nba_facts.facts import getDecade, getFact, getPosition, getTeam, parseJSON


def main():
    """Run a simple end-to-end demo of the package."""
    data = parseJSON()

    sample_team = "Boston Celtics"
    sample_decade = "1990s"
    sample_position = "Point Guard"

    print("NBA Facts package demo")
    print("======================")
    print()

    print("1. Random fact from any team:")
    print(getFact(data))
    print()

    print(f"2. Fact from the {sample_decade}:")
    print(getDecade(data, sample_decade))
    print()

    print(f"3. Fact about a {sample_position}:")
    print(getPosition(data, sample_position))
    print()

    print(f"4. Fact about the {sample_team}:")
    print(getTeam(data, sample_team))


if __name__ == "__main__":
    main()
