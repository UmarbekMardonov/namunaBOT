import asyncio

import asyncpg

from utils.db_api.postgresql import Database


async def test():
    db = Database()
    await db.create()

    print("Users jadvalini yaratamiz")
    #await db.drop_users()
    await db.create_table_users()
    print("Yaratildi")

    await db.add_user("aaa", "xxx", 789456)
    print("Qoshildi")
    users = await db.select_all_users()
    print(f"Barcha {users}")
    user = await db.select_user(id=1)
    print(user)


asyncio.run(test())
