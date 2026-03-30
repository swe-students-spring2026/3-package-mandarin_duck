"""
This module provides a function to retrieve a NBA fact or statistic from the 25-26 season.
Structured and inspired following examplepackagefb1258:
https://github.com/nyu-software-engineering/python-package-example/blob/main/src/examplepackagefb1258/wisdom.py 
"""

"""
This module provides a function to retrieve a NBA fact or statistic from the 25-26 season.
Structured and inspired following examplepackagefb1258:
https://github.com/nyu-software-engineering/python-package-example/blob/main/src/examplepackagefb1258/wisdom.py 
"""

import random
import json

def parseJSON():
    """
    Parses the data.json file
    """
    with open("data.json") as f:
        raw_data = json.load(f)

    facts = {}
    for fact in raw_data:
        if fact["team"] not in facts:
            facts[fact["team"]] = []
        facts[fact["team"]].append(fact)
    return facts

def getFact(data):
    """
    Returns a random fact about the NBA
    """
    return

def getDecade(decade):
    """
    Returns a random fact about the NBA for the specified decade
    """
    return

def getPosition(position):
    """
    Returns a random fact about the NBA for the specified position
    """
    return

def getTeam(team):
    """
    Returns a random fact about the NBA for the specified team
    """
    return
parseJSON()