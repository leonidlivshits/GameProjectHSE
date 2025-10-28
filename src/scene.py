from typing import Dict, List, Optional


class Scene:
    def __init__(self, data: Dict):
        self.id: str = data.get("id")
        self.title: str = data.get("title", "")
        self.text: str = data.get("text", "")
        self.choices: List[Dict] = data.get("choices", [])
        self.is_ending: bool = bool(data.get("is_ending", False))
        self.ending_name: Optional[str] = data.get("ending_name")

    def is_terminal(self) -> bool:
        return self.is_ending or len(self.choices) == 0

    def get_choices_text(self) -> List[str]:
        return [c.get("text", "") for c in self.choices]

    def choice_target(self, index: int) -> Optional[str]:
        if index < 0 or index >= len(self.choices):
            return None
        return self.choices[index].get("target")

    def choice_effects(self, index: int) -> Dict[str, int]:
        if index < 0 or index >= len(self.choices):
            return {}
        return self.choices[index].get("effects", {})

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "text": self.text,
            "choices": self.choices,
            "is_ending": self.is_ending,
            "ending_name": self.ending_name,
        }

    def __repr__(self) -> str:
        return f"Scene(id={self.id!r}, title={self.title!r}, choices={len(self.choices)})"