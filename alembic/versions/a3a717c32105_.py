"""empty message

Revision ID: a3a717c32105
Revises: 7e88b7739093
Create Date: 2023-12-15 15:23:51.228447

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3a717c32105'
down_revision: Union[str, None] = '7e88b7739093'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('space_shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(), nullable=True),
    sa.Column('product_price', sa.BigInteger(), nullable=True),
    sa.Column('product_photo', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('contact', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('space_shop')
    # ### end Alembic commands ###
