"""test3

Revision ID: e0a39fb240a3
Revises: ccb985f3f7a3
Create Date: 2024-05-01 15:50:51.599667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e0a39fb240a3'
down_revision: Union[str, None] = 'ccb985f3f7a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('event', 'date',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('event', 'time',
               existing_type=postgresql.TIME(),
               type_=sa.String(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('event', 'time',
               existing_type=sa.String(),
               type_=postgresql.TIME(),
               existing_nullable=False)
    op.alter_column('event', 'date',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=False)
    # ### end Alembic commands ###
