import pytest
from algorithms import enumerate_endings_recursive, bfs_shortest_path
import story_data


def test_enumerate_endings_from_start():
    endings = enumerate_endings_recursive(story_data.STORY, story_data.START_SCENE, visited=set())
    # Убедимся, что как минимум пять уникальных концовок найдены
    assert isinstance(endings, set)
    assert len(endings) >= 5
    # Проверим, что конкретные id концовок присутствуют
    expected = {"ruined_temple", "underground_lake", "bandit_camp", "island_shrine", "market_square", "graveyard"}
    assert expected.intersection(endings)


def test_bfs_shortest_path_to_market():
    path = bfs_shortest_path(story_data.STORY, story_data.START_SCENE, "market_square")
    assert path is not None
    assert path[0] == story_data.START_SCENE
    assert path[-1] == "market_square"
