import pytest
from nba_facts.facts import parseJSON, getFact, getDecade, getPosition, getTeam


@pytest.fixture
def data():
    """
    Load the NBA facts dataset for use in tests.
    """
    return parseJSON()


class TestParseJSON:
    def test_parseJSON_returns_dict(self, data):
        """
        Verify parseJSON() returns a dictionary
        """
        assert isinstance(
            data, dict
        ), f"Expected parseJSON() to return dict, got {type(data)}"

    def test_parseJSON_is_not_empty(self, data):
        """
        Verify parseJSON() returns non empty data
        """
        assert len(data) > 0, "Expected parseJSON() to return non-empty dictionary"

    def test_parseJSON_keys_are_strings(self, data):
        """
        Verify all keys are team names stored as strings
        """
        assert all(
            isinstance(team, str) for team in data.keys()
        ), "Expected all dictionary keys to be strings"

    def test_parseJSON_values_are_lists(self, data):
        assert all(
            isinstance(team_facts, list) for team_facts in data.values()
        ), "Expected each dictionary value to be a list"

    def test_parseJSON_contains_known_team(self, data):
        assert (
            "Boston Celtics" in data
        ), "Expected parsed data to contain 'Boston Celtics'"

    def test_parseJSON_fact_entries_have_expected_keys(self, data):
        first_fact = data["Boston Celtics"][0]
        assert "team" in first_fact, "Expected each fact entry to include 'team'"
        assert "decade" in first_fact, "Expected each fact entry to include 'decade'"
        assert "fact" in first_fact, "Expected each fact entry to include 'fact'"
        assert (
            "position" in first_fact
        ), "Expected each fact entry to include 'position'"


class TestGetFact:
    def test_getFact_returns_string(self, data):
        actual = getFact(data)
        assert isinstance(
            actual, str
        ), f"Expected getFact() to return string, got {type(actual)}"

    def test_getFact_returns_non_empty_string(self, data):
        actual = getFact(data)
        assert len(actual.strip()) > 0, "Expected getFact() to return non-empty string"

    def test_getFact_returns_fact_from_dataset(self, data):
        all_facts = [
            fact["fact"] for team_facts in data.values() for fact in team_facts
        ]
        actual = getFact(data)
        assert (
            actual in all_facts
        ), "Expected getFact() to return a fact from the dataset"


class TestGetDecade:
    def test_getDecade_returns_string_for_valid_decade(self, data):
        actual = getDecade(data, "1990s")
        assert isinstance(
            actual, str
        ), f"Expected getDecade() to return string, got {type(actual)}"

    def test_getDecade_returns_non_empty_string(self, data):
        actual = getDecade(data, "1990s")
        assert (
            len(actual.strip()) > 0
        ), "Expected getDeacde() to return non-empty string"

    def test_getDecade_returns_fact_from_requested_decade(self, data):
        valid_facts = [
            fact["fact"]
            for team_facts in data.values()
            for fact in team_facts
            if fact["decade"] == "1990s"
        ]
        actual = getDecade(data, "1990s")
        assert (
            actual in valid_facts
        ), "Expected getDecade to return a fact from the 1990s"

    def test_getDecade_accepts_decade_without_s(self, data):
        actual = getDecade(data, "1990")
        assert isinstance(actual, str), "Expected getDecade() to accept '1990' as input"
        assert (
            len(actual.strip()) > 0
        ), "Expected getDecade() to return non-empty string for '1990'"

    def test_getDecade_invalid_decade_raises_indexerror(self, data):
        with pytest.raises(IndexError):
            getDecade(data, "3000s")


class TestGetPosition:
    def test_getPosition_returns_string_for_valid_position(self, data):
        actual = getPosition(data, "Point Guard")
        assert isinstance(
            actual, str
        ), f"Expected getPosition() to return string, got {type(actual)}"

    def test_getPosition_returns_non_empty_string(self, data):
        actual = getPosition(data, "Point Guard")
        assert (
            len(actual.strip()) > 0
        ), "Expected getPosition() to return non-empty string"

    def test_getPosition_returns_fact_from_requested_position(self, data):
        valid_facts = [
            fact["fact"]
            for team_facts in data.values()
            for fact in team_facts
            if fact["position"] == "Point Guard"
        ]
        actual = getPosition(data, "Point Guard")
        assert (
            actual in valid_facts
        ), "Expected getPosition() to return a fact for Point Guard"

    def test_getPosition_invalid_position_raises_indexerror(self, data):
        with pytest.raises(IndexError):
            getPosition(data, "Waterboy")
