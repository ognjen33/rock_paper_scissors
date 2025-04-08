import pytest
from datetime import datetime
from app.models.game import Game, GameResult

def test_game_model_creation():
    game = Game(
        player_id=1,
        computer_id=2,
        result=GameResult.win
    )
    assert game.player_id == 1
    assert game.computer_id == 2
    assert game.result == GameResult.win

def test_game_result_enum():
    assert GameResult.win.value == "win"
    assert GameResult.lose.value == "lose"
    assert GameResult.tie.value == "tie"

