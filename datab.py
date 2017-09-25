import sqlite3

db_setup = sqlite3.connect("players.db")
db_setup.row_factory = sqlite3.Row

conn = db_setup
cur = conn.cursor()

if __name__ == "__main__":
    cur.execute("""
    CREATE TABLE IF NOT EXISTS stats (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PLAYER TEXT,
        STATS TEXT,
        USAGE TEXT,
        AGG TEXT,
        FOUR_FACTOR TEXT,
        ADVANCED_STATS TEXT,
        SHOTS TEXT,
        BOX_SCORE TEXT,
        DRAFT_KINGS TEXT,
        MISC TEXT,
        PLAYER_NAME TEXT,
        PLAYER_ID INTEGER,
        BIRTH_DATE INTEGER,
        TEAM_ID INTEGER,
        DRAFTKINGS_ID INTEGER,
        POSITION INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS teams (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TEAMS TEXT
    )
    """)

    conn.commit()
