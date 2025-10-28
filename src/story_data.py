START_SCENE = "start"

STORY = {
    "start": {
        "id": "start",
        "title": "Начало пути",
        "text": "Вы просыпаетесь на рассвете у дороги на окраине своей деревни. Перед вами - несколько путей. Куда пойдёте?",
        "choices": [
            {"text": "Пойти в сторону ворот деревни", "target": "village_gate", "effects": {"xp": 1}},
            {"text": "Отправиться в лес - ради приключений", "target": "forest_entrance", "effects": {"luck": 1}},
        ],
        "is_ending": False,
        "ending_name": None,
    },

    "village_gate": {
        "id": "village_gate",
        "title": "Ворота деревни",
        "text": "У ворот людно: купцы, дети, стража. Можно поторговаться, спросить про слухи или пойти в городской рынок.",
        "choices": [
            {"text": "Спуститься на рынок - попытаться продать найденные вещи", "target": "market_square", "effects": {"xp": 5, "karma": 1}},
            {"text": "Взять короткую дорогу через просёлок (риск)", "target": "bandit_road", "effects": {"luck": -1}},
        ],
        "is_ending": False,
        "ending_name": None,
    },

    "forest_entrance": {
        "id": "forest_entrance",
        "title": "У входа в лес",
        "text": "Деревья над головой плотно сплелись. Тропинка делится: одна ведёт глубже, другая - к старой избе.",
        "choices": [
            {"text": "Пойти по глубокой тропе", "target": "deep_path", "effects": {"xp": 2, "health": -1}},
            {"text": "Заглянуть в старую избу", "target": "old_cottage", "effects": {"luck": 1}},
        ],
        "is_ending": False,
        "ending_name": None,
    },

    "deep_path": {
        "id": "deep_path",
        "title": "Глубь леса",
        "text": "Чем дальше, тем темнее. Вдруг тропа обрывается у пещеры, у реки - можно переплыть.",
        "choices": [
            {"text": "Исследовать пещеру", "target": "cave_entrance", "effects": {"xp": 4, "health": -3}},
            {"text": "Спуститься к реке", "target": "river_bank", "effects": {"luck": 1}},
        ],
        "is_ending": False,
        "ending_name": None,
    },

    "old_cottage": {
        "id": "old_cottage",
        "title": "Старая изба",
        "text": "В избе живёт мудрец. Он предлагает выбор: учение или помощь в обмен на услугу.",
        "choices": [
            {"text": "Принять учение - получить знания", "target": "ruined_temple", "effects": {"xp": 10, "karma": 1}},
            {"text": "Отказаться и вернуться в деревню", "target": "market_square", "effects": {"xp": 1}},
        ],
        "is_ending": False,
        "ending_name": None,
    },

    "ruined_temple": {
        "id": "ruined_temple",
        "title": "Разрушенный храм",
        "text": "Вы достигли древнего храма. Обряд пробуждает в вас новые способности и понимание. Это - просветление.",
        "choices": [],
        "is_ending": True,
        "ending_name": "Просветление",
    },

    "cave_entrance": {
        "id": "cave_entrance",
        "title": "Вход в пещеру",
        "text": "Пещера полна странных звуков. Глубже вы находите подземное озеро - и темное свечение.",
        "choices": [
            {"text": "Погрузиться в свечение - рискованно", "target": "underground_lake", "effects": {"health": -10, "karma": 0, "xp": 15}},
            {"text": "Вернуться назад к тропе", "target": "deep_path", "effects": {"xp": 1}},
        ],
        "is_ending": False,
        "ending_name": None,
    },

    "underground_lake": {
        "id": "underground_lake",
        "title": "Подземное озеро",
        "text": "Вы жертвуете частью себя ради силы. Это оставляет отпечаток - вы получили силу, но потеряли многое.",
        "choices": [],
        "is_ending": True,
        "ending_name": "Жертва ради силы",
    },

    "bandit_road": {
        "id": "bandit_road",
        "title": "Разбитая дорога",
        "text": "Дорога узкая, вокруг - следы недавней драки. Отсюда виден лагерь бандитов.",
        "choices": [
            {"text": "Подойти тихо и разведать лагерь", "target": "bandit_camp", "effects": {"luck": -1, "xp": 3}},
            {"text": "Помочь раненому путнику и пойти с ним к лодке", "target": "fisher_boat", "effects": {"karma": 1, "xp": 2, "health": -1}},
        ],
        "is_ending": False,
        "ending_name": None,
    },

    "bandit_camp": {
        "id": "bandit_camp",
        "title": "Лагерь бандитов",
        "text": "Вас поймали в плен - долгое испытание. Вы теряете свободу и часть имущества.",
        "choices": [],
        "is_ending": True,
        "ending_name": "Пленение",
    },

    "river_bank": {
        "id": "river_bank",
        "title": "Берег реки",
        "text": "Берег полон лодок. Моряк предлагает переправить вас на соседний остров в обмен на помощь.",
        "choices": [
            {"text": "Согласиться - помочь переправить лодку", "target": "fisher_boat", "effects": {"xp": 3, "karma": 1}},
            {"text": "Игнорировать и идти вдоль берега", "target": "graveyard", "effects": {"health": -2}},
        ],
        "is_ending": False,
        "ending_name": None,
    },

    "fisher_boat": {
        "id": "fisher_boat",
        "title": "Лодка рыбака",
        "text": "На лодке вы плывёте к маленькому острову с древним святилищем.",
        "choices": [
            {"text": "Осмотреть святилище на острове", "target": "island_shrine", "effects": {"xp": 8, "luck": 1}},
            {"text": "Вернуться в деревню и устроиться на рынке", "target": "market_square", "effects": {"xp": 2}},
        ],
        "is_ending": False,
        "ending_name": None,
    },

    "island_shrine": {
        "id": "island_shrine",
        "title": "Святилище на острове",
        "text": "Вы находите сокровище и древние знания. Богатство и слава - ваш выбор.",
        "choices": [],
        "is_ending": True,
        "ending_name": "Сокровище и слава",
    },

    "market_square": {
        "id": "market_square",
        "title": "Рынок деревни",
        "text": "Вы вернулись домой, поделились историями и остатками добычи - простой, но тёплый финал.",
        "choices": [],
        "is_ending": True,
        "ending_name": "Возвращение домой",
    },

    "graveyard": {
        "id": "graveyard",
        "title": "Кладбище",
        "text": "Раны оказались слишком тяжёлыми. На этом ваша дорога заканчивается - тихая могила под дубом.",
        "choices": [],
        "is_ending": True,
        "ending_name": "Печальный конец: смерть",
    },
}


# перечислить все концовки
def list_endings():
    return [(sid, s["ending_name"]) for sid, s in STORY.items() if s.get("is_ending")]


__all__ = ["START_SCENE", "STORY", "list_endings"]
