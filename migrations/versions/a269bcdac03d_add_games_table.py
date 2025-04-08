"""Add games table

Revision ID: a269bcdac03d
Revises: 5f9d854bef0b
Create Date: 2025-04-07 23:24:09.464168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import enum


# revision identifiers, used by Alembic.
revision: str = 'a269bcdac03d'
down_revision: Union[str, None] = '5f9d854bef0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Define Enum type used in the table even if it is redundant due
# do best practice being having separate enums from models.
class GameResultEnum(enum.Enum):
    win = "win"
    lose = "lose"
    tie = "tie"


def upgrade() -> None:
    # Create Enum type
    game_result_enum = sa.Enum(GameResultEnum, name="gameresultenum")
    game_result_enum.create(op.get_bind())

    # Create games table
    op.create_table(
        "games",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("player_id", sa.Integer(), sa.ForeignKey("choices.id"), nullable=False),
        sa.Column("computer_id", sa.Integer(), sa.ForeignKey("choices.id"), nullable=False),
        sa.Column("result", sa.Enum(GameResultEnum, name="gameresultenum"), nullable=False),
        sa.Column("created_date", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False)
    )
    op.create_index("ix_games_id", "games", ["id"])


def downgrade() -> None:
    op.drop_index("ix_games_id", table_name="games")
    op.drop_table("games")

    # Drop enum type
    game_result_enum = sa.Enum(GameResultEnum, name="gameresultenum")
    game_result_enum.drop(op.get_bind())
   # ### end Alembic commands ###

