"""Add birthdate field to User model

Revision ID: 948195db1671
Revises: 0f98f0cac75a
Create Date: 2023-09-02 07:34:14.150211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '948195db1671'
down_revision: Union[str, None] = '0f98f0cac75a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('birthdate', sa.Date(), nullable=True))
    op.create_index(op.f('ix_user_birthdate'), 'user', ['birthdate'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_birthdate'), table_name='user')
    op.drop_column('user', 'birthdate')
    # ### end Alembic commands ###
