<div align="center">
  <img src="https://finalspaceapi.com/img/logo.png" width="120" />

# final_space.py
> Web-API for [Final Space API](https://finalspaceapi.com) a REST API based on the animated TV show *Final Space*. Access data on characters, episodes, locations, and quotes.
</div>

## Quick Start
```python
from final_space import FinalSpace

fs = FinalSpace()

# Get all characters
print(fs.get_all_characters())

# Get a specific episode
print(fs.get_episode(1))

# Get all quotes
print(fs.get_all_quotes())
```

---

## Characters

| Method | Description |
|--------|-------------|
| `get_all_characters()` | Get all characters |
| `get_character(character_id)` | Get a character by ID |

---

## Episodes

| Method | Description |
|--------|-------------|
| `get_all_episodes()` | Get all episodes |
| `get_episode(episode_id)` | Get an episode by ID |

---

## Locations

| Method | Description |
|--------|-------------|
| `get_all_locations()` | Get all locations |
| `get_location(location_id)` | Get a location by ID |

---

## Quotes

| Method | Description |
|--------|-------------|
| `get_all_quotes()` | Get all quotes |

---

## Misc

| Method | Description |
|--------|-------------|
| `get_endpoints()` | List all available API endpoints |
