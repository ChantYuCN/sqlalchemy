from sqlalchemy.sql import select
s = select([users])
result = conn.execute(s)
