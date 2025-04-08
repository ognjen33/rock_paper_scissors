"""Initial migration

Revision ID: 15deccbb9102
Revises: 
Create Date: 2025-04-06 22:05:20.041093

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.models.choices import JSONEncodedList



# revision identifiers, used by Alembic.
revision: str = '15deccbb9102'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('choices',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Enum('rock', 'paper', 'scissors', 'lizzard', 'spock', name='choiceenum'), nullable=False),
    sa.Column('wins', JSONEncodedList(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_choices_id'), 'choices', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_choices_id'), table_name='choices')
    op.drop_table('choices')
    # ### end Alembic commands ###
