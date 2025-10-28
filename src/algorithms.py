# - рекурсивный обход для перечисления концовок
# - BFS для поиска кратчайшего пути
# - DFS для поиска всех путей

from typing import Dict, List, Set, Optional
from collections import deque


def enumerate_endings_recursive(story: Dict[str, Dict], node_id: str, visited: Optional[Set[str]] = None) -> Set[str]:
    if visited is None:
        visited = set()
    endings = set()
    if node_id in visited:
        return endings
    visited.add(node_id)

    node = story.get(node_id)
    if node is None:
        return endings

    if node.get("is_ending"):
        endings.add(node_id)
        return endings

    for choice in node.get("choices", []):
        target = choice.get("target")
        if not target:
            continue
        endings.update(enumerate_endings_recursive(story, target, visited))

    return endings


def bfs_shortest_path(story: Dict[str, Dict], start: str, goal: str) -> Optional[List[str]]:
    if start == goal:
        return [start]

    queue = deque([[start]])
    seen = {start}

    while queue:
        path = queue.popleft()
        node_id = path[-1]
        node = story.get(node_id)
        if node is None:
            continue
        for choice in node.get("choices", []):
            target = choice.get("target")
            if not target or target in seen:
                continue
            new_path = path + [target]
            if target == goal:
                return new_path
            queue.append(new_path)
            seen.add(target)
    return None


def dfs_all_paths(story: Dict[str, Dict], start: str, goal: str, limit: int = 1000) -> List[List[str]]:
    paths = []

    def _dfs(current: str, path: List[str], visited: Set[str]):
        if len(paths) >= limit:
            return
        if current == goal:
            paths.append(list(path))
            return
        node = story.get(current)
        if node is None:
            return
        for choice in node.get("choices", []):
            target = choice.get("target")
            if not target or target in visited:
                continue
            visited.add(target)
            path.append(target)
            _dfs(target, path, visited)
            path.pop()
            visited.remove(target)

    _dfs(start, [start], {start})
    return paths


def all_endings_reachable_from_start(story: Dict[str, Dict], start: str) -> bool:
    actual_endings = {sid for sid, s in story.items() if s.get("is_ending")}
    reachable = enumerate_endings_recursive(story, start, visited=set())
    return actual_endings.issubset(reachable)