from typing import Dict, List
import datetime
import os

from player import Player
from scene import Scene
from utils import get_choice_input, save_results
from story_data import STORY, START_SCENE
from algorithms import enumerate_endings_recursive, bfs_shortest_path, all_endings_reachable_from_start


class GameEngine:
    def __init__(self, player_name: str = "Игрок"):
        self.player = Player(player_name)
        self.story: Dict[str, Dict] = STORY
        self.current_scene_id: str = START_SCENE
        self.visited: set = set()
        self.history: List[Dict] = []
        self.start_time = datetime.datetime.now()

    def load_scene(self, scene_id: str) -> Scene:
        data = self.story.get(scene_id)
        if data is None:
            raise KeyError(f"Scene {scene_id} not found in story")
        return Scene(data)

    def show_scene(self, scene: Scene):
        print(f"\n=== {scene.title} ===\n")
        print(scene.text + "\n")
        choices = scene.get_choices_text()
        if not choices:
            return
        for i, c in enumerate(choices, start=1):
            print(f"  {i}) {c}")

    def apply_choice(self, scene: Scene, choice_index: int):
        target = scene.choice_target(choice_index)
        effects = scene.choice_effects(choice_index)
        choice_text = scene.get_choices_text()[choice_index]

        self.player.apply_effects(effects)

        self.history.append({"scene": scene.id, "choice_text": choice_text})
        if target:
            self.visited.add(target)
            self.current_scene_id = target

    def determine_ending(self, scene: Scene) -> str:
        if not self.player.is_alive():
            return "Смерть (здоровье 0)"
        if scene.is_ending:
            return scene.ending_name or "Неизвестная концовка"
        endings = enumerate_endings_recursive(self.story, scene.id, visited=set())
        if endings:
            eid = next(iter(endings))
            return self.story[eid].get("ending_name", eid)
        return "Безымянная концовка"

    def final_score(self) -> int:
        return self.player.health + 2 * self.player.xp + 3 * self.player.karma + self.player.luck

    def save_results(self, path: str = None) -> str:
        if path is None:
            base = os.path.dirname(__file__)
            path = os.path.join(base, "results.txt")
        ending_name = self.determine_ending(self.load_scene(self.current_scene_id))
        player_summary = self.player.summary()
        player_summary["score"] = self.final_score()
        save_results(path, player_summary, self.history, ending_name, self.start_time)
        return path

    def run(self):
        all_ok = all_endings_reachable_from_start(self.story, START_SCENE)
        if not all_ok:
            print("Внимание: не все концовки достижимы из стартовой сцены (проверьте сюжет).\n")

        while True:
            scene = self.load_scene(self.current_scene_id)
            self.visited.add(scene.id)
            self.show_scene(scene)

            if scene.is_terminal() or not self.player.is_alive():
                ending = self.determine_ending(scene)
                print(f"\n--- Концовка: {ending} ---\n")
                print("Итоговое состояние игрока:")
                for k, v in self.player.summary().items():
                    print(f"  {k}: {v}")
                saved_path = self.save_results()
                print(f"Результаты сохранены в: {saved_path}")
                return saved_path

            num_choices = len(scene.choices)
            idx = get_choice_input(num_choices)
            self.apply_choice(scene, idx)

            if not self.player.is_alive():
                scene = self.load_scene(self.current_scene_id)
                print("\nВы не смогли продолжить дальше - ваше здоровье упало до нуля.")
