import aiosqlite

DB_NAME = "bot_database.db"

async def create_tables():
    """Создает таблицу в базе данных, если ее нет"""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS poll_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                name TEXT,
                age TEXT,
                subject TEXT,
                color TEXT,
                movie TEXT,
                sport TEXT,
                music TEXT,
                season TEXT
            )
        """)
        await db.commit()

async def save_poll_result(user_id, name, age, subject, color, movie, sport, music, season):
    """Сохраняет данные пользователя в БД"""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            INSERT INTO poll_results (user_id, name, age, subject, color, movie, sport, music, season)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (user_id, name, age, subject, color, movie, sport, music, season))
        await db.commit()

async def get_db_connection():
    """Создает и возвращает соединение с БД"""
    return await aiosqlite.connect(DB_NAME)
