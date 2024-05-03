"""resp int

Revision ID: 143f68688711
Revises: 9990b88a80ae
Create Date: 2024-05-01 16:55:22.874173

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '143f68688711'
down_revision: Union[str, None] = '9990b88a80ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('maxPeople', sa.Integer(), nullable=False),
    sa.Column('place', sa.String(), nullable=False),
    sa.Column('responsible_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['responsible_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('application')
    op.drop_table('event')
    # ### end Alembic commands ###
