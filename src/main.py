import argparse
import os

from engine import GameEngine


def parse_args():
    parser = argparse.ArgumentParser(description="Интерактивная текстовая игра - GameProjectHSE")
    parser.add_argument("--name", "-n", type=str, default="Игрок", help="Имя персонажа")
    parser.add_argument("--results", "-r", type=str, default=None, help="Путь для сохранения results.txt")
    return parser.parse_args()


def main():
    args = parse_args()
    engine = GameEngine(player_name=args.name)
    if args.results:
        saved = engine.run()
        if args.results and os.path.exists(saved):
            try:
                os.replace(saved, args.results)
                print(f"Файл результатов перемещён в: {args.results}")
            except Exception:
                print(f"Не удалось переместить файл результатов в {args.results}. Файл сохранён здесь: {saved}")
    else:
        engine.run()


if __name__ == "__main__":
    main()
