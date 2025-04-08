from sqlalchemy.orm import Session
from app.models.game import Game
from app.schemas.game import GameResult




def get_last_10_games(db: Session):
    return db.query(Game).order_by(Game.created_date.desc()).limit(10).all()

def create_game(db: Session, game: GameResult):
    db_game = Game(result=game.result, player_id=game.player, computer_id=game.computer)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def get_game_statistics(db: Session):
    print("INSIDE A REPO")
    stats = {
        'total_games': db.query(Game).count(),
        'wins': db.query(Game).filter(Game.result == "win").count(),
        'losses': db.query(Game).filter(Game.result == "lose").count(),
        'draws': db.query(Game).filter(Game.result == "tie").count()
    }
    print(stats, "STATS")
    stats['win_rate'] = (stats['wins'] / stats['total_games'] * 100) if stats['total_games'] > 0 else 0
    print("WIN RATE")
    return stats

