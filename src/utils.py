from typing import List, Dict
import datetime
import os


def get_choice_input(num_choices: int) -> int:
    if num_choices <= 0:
        raise ValueError("num_choices must be > 0")
    while True:
        try:
            raw = input(f"Выберите вариант (1-{num_choices}): ")
            choice = int(raw.strip())
            if 1 <= choice <= num_choices:
                return choice - 1
            print(f"Пожалуйста, введите число от 1 до {num_choices}.")
        except ValueError:
            print("Некорректный ввод. Введите число.")


def format_history(history: List[Dict]) -> str:
    lines = []
    for i, item in enumerate(history, start=1):
        scene = item.get("scene")
        choice_text = item.get("choice_text", "(нет)")
        lines.append(f"  {i}) {scene} -> {choice_text}")
    return "\n".join(lines)


def save_results(path: str, player_summary: Dict, history: List[Dict], ending_name: str, start_time: datetime.datetime):
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"Player: {player_summary.get('name', 'Игрок')}\n")
        f.write(f"Start: {start_time.isoformat(sep=' ', timespec='seconds')}\n\n")
        f.write("History:\n")
        f.write(format_history(history) + "\n\n")
        f.write("Final state:\n")
        f.write(f"  health: {player_summary.get('health')}\n")
        f.write(f"  xp: {player_summary.get('xp')}\n")
        f.write(f"  karma: {player_summary.get('karma')}\n")
        f.write(f"  luck: {player_summary.get('luck')}\n\n")
        f.write(f"Ending: {ending_name}\n")

    return path