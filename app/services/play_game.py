from sqlalchemy.orm import Session
from app.schemas.game import GamePlay, GameResult
from app.repositories import choice as choice_repo

def play_game_vs_computer(db: Session, game_play: GamePlay, computer_choice_id: int):
    # get computer choice value
    computer = choice_repo.get_choice(db, computer_choice_id)

    # get player choice value
    player = choice_repo.get_choice(db, game_play.player)

    # determine winner
    result = determine_winner(computer, player)
    
    return GameResult(result=result, player=player.id, computer=computer_choice_id)
    
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

