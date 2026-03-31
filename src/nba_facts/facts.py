"""
This module provides a function to retrieve a NBA fact or statistic from the 25-26 season.
Structured and inspired following examplepackagefb1258:
https://github.com/nyu-software-engineering/python-package-example/blob/main/src/examplepackagefb1258/wisdom.py 

"""

import random
import json
import os

def parseJSON():
    """
    Parses the data.json file
    """

    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to data.json
    data_path = os.path.join(current_dir, "data.json")

    with open(data_path) as f:
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
    random_team = random.choice(list(data.keys()))
    fact = random.choice(data[random_team])["fact"]
    return fact

def getDecade(data, decade):
    """
    Returns a random fact about the NBA for the specified decade
    """
    decade = decade.strip()
    if decade and decade[-1].isdigit():
        decade += "s" # in case the user forgot to add 's' to the end 
    
    decade_facts = [fact for team in data.values() for fact in team if fact["decade"]== decade]
    fact = random.choice(decade_facts)["fact"]
    return fact

def getPosition(data, position):
    """
    Returns a random fact about the NBA for the specified position
    """
    position_facts = [fact for team in data.values() for fact in team if fact["position"]== position]
    fact = random.choice(position_facts)["fact"]
    return fact

def getTeam(data, team):
    """
    Returns a random fact about the NBA for the specified team
    """
    team_facts = [fact for facts in data.values() for fact in facts if fact["team"] == team]
    fact = random.choice(team_facts)["fact"]
    return fact
