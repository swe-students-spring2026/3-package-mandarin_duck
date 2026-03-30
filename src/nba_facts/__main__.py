"""
This file is run when the package is run directly from command 
line, as opposed to importing it into another program.
"""
import argparse
from .facts import getFact, getDecade, getPosition, getTeam, parseJSON

def main():
    data = parseJSON()

    parser = argparse.ArgumentParser(
        description="NBA Facts: Get fun facts about the NBA by team, decade, or position!"
    )
    parser.add_argument(
        "--random", action="store_true", help="Get a random NBA fact."
    )
    parser.add_argument(
        "--team", type=str, help="Get a fact about a specific NBA team (e.g., 'Lakers')."
    )
    parser.add_argument(
        "--decade", type=str, help="Get a fact about a specific NBA decade (e.g., '1990s')."
    )
    parser.add_argument(
        "--position", type=str, help="Get a fact about a specific NBA position (e.g., 'Point Guard')."
    )

    args = parser.parse_args()

    if args.random:
        print(getFact(data))
    elif args.team:
        print(getTeam(args.team, data))
    elif args.decade:
        print(getDecade(args.decade, data))
    elif args.position:
        print(getPosition(args.position, data))
    else:
        print("No valid arguments provided. Use --help for usage information.")


if __name__ == "__main__":
    # run the main function
    main()