"""empty message

Revision ID: 9ba666f864c8
Revises: b9128a6526cf
Create Date: 2023-12-11 15:09:31.809365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ba666f864c8'
down_revision: Union[str, None] = 'b9128a6526cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(), nullable=True))
    op.alter_column('users', 'login',
               existing_type=sa.VARCHAR(),
               type_=sa.BigInteger(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'login',
               existing_type=sa.BigInteger(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###
