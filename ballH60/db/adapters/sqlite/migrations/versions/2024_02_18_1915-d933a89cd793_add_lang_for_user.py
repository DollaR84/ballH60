"""add lang for user

Revision ID: d933a89cd793
Revises: 00c031af7333
Create Date: 2024-02-18 19:15:00.948703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd933a89cd793'
down_revision: Union[str, None] = '00c031af7333'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('lang', sa.String(length=2), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_column('lang')
    # ### end Alembic commands ###
