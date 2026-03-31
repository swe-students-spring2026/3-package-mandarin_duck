import pytest
from nba_facts.facts import parseJSON, getFact, getDecade, getPosition, getTeam


@pytest.fixture
def data():
    """
    Load the NBA facts dataset for use in tests.
    """
