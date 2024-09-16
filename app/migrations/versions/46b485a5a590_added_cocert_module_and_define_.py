"""Added Cocert module and define relationships

Revision ID: 46b485a5a590
Revises: 058715820878
Create Date: 2024-09-15 18:54:55.832640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46b485a5a590'
down_revision: Union[str, None] = '058715820878'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('concerts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('band_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['band_id'], ['bands.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('concerts')
    # ### end Alembic commands ###
