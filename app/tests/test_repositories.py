import pytest
from app.repositories.game import create_game, get_last_10_games, get_game_statistics
from app.models.game import GameResult
from app.schemas.game import GameResult as GameResultSchema

def test_create_game(db_session, sample_choices):
    game_result = GameResultSchema(
        result=GameResult.win,
        player=1,  # rock
        computer=2  # paper
    )
    
    game = create_game(db_session, game_result)
    assert game.result == GameResult.win
    assert game.player_id == 1
    assert game.computer_id == 2

def test_get_last_10_games(db_session, sample_choices):
    # Create 15 games
    for i in range(15):
        game_result = GameResultSchema(
            result=GameResult.win,
            player=1,
            computer=2
        )
        create_game(db_session, game_result)
    
    games = get_last_10_games(db_session)
    assert len(games) == 10

def test_get_game_statistics(db_session, sample_choices):
    # Create games with different results
    results = [
        GameResult.win,
        GameResult.win,
        GameResult.lose,
        GameResult.tie
    ]
    
    for result in results:
        game_result = GameResultSchema(
            result=result,
            player=1,
            computer=2
        )
        create_game(db_session, game_result)
    
    stats = get_game_statistics(db_session)
    
    assert stats['total_games'] == 4
    assert stats['wins'] == 2
    assert stats['losses'] == 1
    assert stats['draws'] == 1
    assert stats['win_rate'] == 50.0

@pytest.mark.parametrize("games,expected_win_rate", [
    ([], 0),  # Test empty database
    ([(GameResult.win, 1, 2)], 100.0),  # Test 100% win rate
    ([(GameResult.lose, 1, 2)], 0.0),  # Test 0% win rate
    ([(GameResult.tie, 1, 2)], 0.0),  # Test only ties
])
def test_get_game_statistics_edge_cases(db_session, sample_choices, games, expected_win_rate):
    for result, player_id, computer_id in games:
        game_result = GameResultSchema(
            result=result,
            player=player_id,
            computer=computer_id
        )
        create_game(db_session, game_result)
    
    stats = get_game_statistics(db_session)
    assert stats['win_rate'] == expected_win_rate
