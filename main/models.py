import sqlalchemy
from sqlalchemy import DateTime
from main.database_set import metadata


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("modme_id", sqlalchemy.BigInteger, nullable=True),
    sqlalchemy.Column("login", sqlalchemy.String),
    sqlalchemy.Column('first_name', sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger)
)


space_shop = sqlalchemy.Table(
    "space_shop",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("product_name", sqlalchemy.String),
    sqlalchemy.Column("product_price", sqlalchemy.BigInteger),
    sqlalchemy.Column('product_photo', sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True),
    sqlalchemy.Column('contact', sqlalchemy.String),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger)
)