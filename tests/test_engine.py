import os
import tempfile

from engine import GameEngine
import story_data


def test_engine_apply_choices_and_save_results():
    eng = GameEngine(player_name="TestPlayer")
    sc1 = eng.load_scene("start")
    eng.apply_choice(sc1, 0)
    assert eng.current_scene_id == "village_gate"

    sc2 = eng.load_scene("village_gate")
    eng.apply_choice(sc2, 0)
    assert eng.current_scene_id == "market_square"

    sc3 = eng.load_scene("market_square")
    assert sc3.is_ending
    fd, path = tempfile.mkstemp(prefix="results_", suffix=".txt")
    os.close(fd)
    try:
        saved = eng.save_results(path)
        assert os.path.exists(saved)
        with open(saved, "r", encoding="utf-8") as f:
            text = f.read()
        assert "Player: TestPlayer" in text
        assert "Ending:" in text
    finally:
        os.remove(path)
