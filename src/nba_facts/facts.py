"""
This module provides a function to retrieve a NBA fact or statistic from the 25-26 season.
Structured and inspired following examplepackagefb1258:
https://github.com/nyu-software-engineering/python-package-example/blob/main/src/examplepackagefb1258/wisdom.py 
"""

import random

def get():
    """
    Returns a NBA fact or statistic from the 25-26 season.
    """

    facts = """
    
    """

    lines = facts.split("\n")
    lines = [line for line in lines if line.strip() != ""]  # remove empty lines
    random_fact = random.choice(lines)
    return random_fact