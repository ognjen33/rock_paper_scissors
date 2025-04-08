from sqlalchemy.orm import Session
from app.schemas.game import GamePlay, GameResult
from app.repositories import choice as choice_repo
from app.repositories import game as game_repo

def get_last_10_games(db: Session):
    game_results = game_repo.get_last_10_games(db)
    game_results_out = [GameResult(result=game.result, player=game.player_id, computer=game.computer_id) for game in game_results]
    return game_results_out

def play_game_vs_computer(db: Session, game_play: GamePlay, computer_choice_id: int):
    # get computer choice value
    computer = choice_repo.get_choice(db, computer_choice_id)

    # get player choice value
    player = choice_repo.get_choice(db, game_play.player)

    # determine winner
    result = determine_winner(computer, player)
    
    game_result = GameResult(result=result, player=player.id, computer=computer_choice_id)

    game_repo.create_game(db, game_result)
    return game_result

def determine_winner(computer, player):
    # player beats computer
    if computer.name in player.wins:
        return "win"
    # player and computer played the same hand
    elif computer.name == player.name:
        return "tie"
    # computer beats player
    else:
        return "lose"

def get_game_statistics(db: Session):
    return game_repo.get_game_statistics(db)

