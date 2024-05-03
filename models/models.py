from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean, Date, Time

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("telephone", String, nullable=False),
)

event = Table(
    "event",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("description", String, nullable=False),
    Column("date", String, nullable=False),
    Column("time", String, nullable=False),
    Column("address", String, nullable=False),
    Column("maxPeople", Integer, nullable=False),
    Column("place", String, nullable=False),
    Column("responsible_id", Integer, ForeignKey(user.c.id)),
)

application = Table(
    "application",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("event_id", Integer, ForeignKey(event.c.id)),
    Column("user_id", Integer, ForeignKey(user.c.id)),
)

