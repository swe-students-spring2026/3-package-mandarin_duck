[![CI](https://github.com/swe-students-spring2026/3-package-mandarin_duck/actions/workflows/ci.yml/badge.svg)](https://github.com/swe-students-spring2026/3-package-mandarin_duck/actions/workflows/ci.yml)

# nba_facts - Python Package Exercise
#### PyPI Website Link (TODO)

Our team made a Python package that provides NBA facts based on user inputs like team, player, decade, or position, with functions designed to return random or category-specific insights about basketball history and players.


### How to import into your own code

After installing the package, import functions from `nba_facts.facts`.

```python
from nba_facts.facts import getFact, parseJSON

data = parseJSON()
print(getFact(data))
```

### Documentation

All examples below use the functions defined in `src/nba_facts/facts.py`.

Link to example program: [example_program.py](./example_program.py)

#### `parseJSON()`
Loads `data.json` and returns the NBA facts grouped by team in a dictionary.

```python
from nba_facts.facts import parseJSON

data = parseJSON()
print(type(data))
print(len(data))
```

#### `getFact(data)`
Returns one random NBA fact from the dataset.

```python
from nba_facts.facts import getFact, parseJSON

data = parseJSON()
print(getFact(data))
```

#### `getDecade(data, decade)`
Returns one random NBA fact for the decade you pass in. This function accepts values like `"1990s"` (with basic robustness with typos)

```python
from nba_facts.facts import getDecade, parseJSON

data = parseJSON()
print(getDecade(data, "1990s"))
print(getDecade(data, "1990"))
```

#### `getPosition(data, position)`
Returns one random NBA fact for a specific basketball position.

```python
from nba_facts.facts import getPosition, parseJSON

data = parseJSON()
print(getPosition(data, "Point Guard"))
```

#### `getTeam(data, team)`
Returns one random NBA fact for a specific NBA team.

```python
from nba_facts.facts import getTeam, parseJSON

data = parseJSON()
print(getTeam(data, "Boston Celtics"))
```


### How to configure and run the project




### How to contribute




### Founders
- [Adam Soliman](https://github.com/adamsolimancs/)
- 
- 
- 
- 
