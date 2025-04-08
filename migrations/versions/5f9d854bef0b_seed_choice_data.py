from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text
import json

# revision identifiers, used by Alembic
revision = '5f9d854bef0b'
down_revision = '15deccbb9102'
branch_labels = None
depends_on = None

# Enum values to seed
choices_to_seed = ["rock", "paper", "scissors", "lizzard", "spock"]

# Mapping from values to winners
wins = {
    "rock": ["scissors", "lizzard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizzard"],
    "lizzard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

def upgrade():
    connection = op.get_bind()

    for value in choices_to_seed:
        # Insert only if it doesn't already exist
        connection.execute(text(f"""
            INSERT INTO choices (name, wins)
            SELECT :value, :wins
            WHERE NOT EXISTS (
                SELECT 1 FROM choices WHERE name = :value
            )
        """), {"value": value, "wins": json.dumps(wins[value])})


def downgrade():
    connection = op.get_bind()

    for value in choices_to_seed:
        connection.execute(text("""
            DELETE FROM choices WHERE choice = :value
        """), {"value": value})
