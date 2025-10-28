# Загрузчик/валидатор сюжета из внешнего JSON-файла.

import json
from typing import Dict, Any, Tuple
import os

from algorithms import enumerate_endings_recursive


def load_story_from_json(path: str) -> Dict[str, Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Формат файла: верхний уровень должен быть объект (dict) со сценами).")
    return data


def save_story_to_json(story: Dict[str, Dict[str, Any]], path: str) -> str:
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(story, f, ensure_ascii=False, indent=2)
    return path


def validate_scene(scene: Dict[str, Any]) -> Tuple[bool, str]:
    if not isinstance(scene, dict):
        return False, "Scene is not a dict"
    if "id" not in scene or not isinstance(scene["id"], str):
        return False, "Missing or invalid 'id'"
    if "title" not in scene or not isinstance(scene["title"], str):
        return False, "Missing or invalid 'title'"
    if "text" not in scene or not isinstance(scene["text"], str):
        return False, "Missing or invalid 'text'"
    if "choices" not in scene or not isinstance(scene["choices"], list):
        return False, "Missing or invalid 'choices' (must be list)"
    if "is_ending" not in scene or not isinstance(scene["is_ending"], bool):
        return False, "Missing or invalid 'is_ending' (must be bool)"
    for i, c in enumerate(scene["choices"]):
        if not isinstance(c, dict):
            return False, f"Choice #{i} is not a dict"
        if "text" not in c or not isinstance(c["text"], str):
            return False, f"Choice #{i} missing 'text'"
        if "target" not in c or not isinstance(c["target"], str):
            return False, f"Choice #{i} missing or invalid 'target'"
        if "effects" in c and not isinstance(c["effects"], dict):
            return False, f"Choice #{i} 'effects' must be dict if present"
    return True, "OK"


def validate_story(story: Dict[str, Dict[str, Any]]) -> Tuple[bool, str]:
    if not isinstance(story, dict):
        return False, "Story must be a dict"
    errors = []
    endings_count = 0
    for sid, scene in story.items():
        ok, msg = validate_scene(scene)
        if not ok:
            errors.append(f"Scene {sid}: {msg}")
        if scene.get("is_ending"):
            endings_count += 1
    if endings_count < 1:
        errors.append("No endings found in story (need at least one)")
    if errors:
        return False, "; ".join(errors)
    return True, "OK"


def check_endings_reachable(story: Dict[str, Dict], start_id: str) -> bool:
    actual_endings = {sid for sid, s in story.items() if s.get("is_ending")}
    reachable = enumerate_endings_recursive(story, start_id, visited=set())
    return actual_endings.issubset(reachable)