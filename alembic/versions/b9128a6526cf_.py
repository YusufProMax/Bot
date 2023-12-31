"""empty message

Revision ID: b9128a6526cf
Revises: 8647e82cf028
Create Date: 2023-12-10 16:10:28.175978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9128a6526cf'
down_revision: Union[str, None] = '8647e82cf028'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('modme_id', sa.BigInteger(), nullable=True))
    op.add_column('users', sa.Column('login', sa.String(), nullable=True))
    op.drop_column('users', 'age')
    op.drop_column('users', 'full_name')
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('age', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.drop_column('users', 'login')
    op.drop_column('users', 'modme_id')
    # ### end Alembic commands ###
