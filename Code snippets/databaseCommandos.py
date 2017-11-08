def insert():
    import sqlite3
    conn = sqlite3.connect("Database.db")
    c = conn.cursor()

    """Voegt de nieuwe tweet en de status toe"""
    c.execute('INSERT INTO tweets(tweet, status ) VALUES("Dit is een tweet", "toBeProcessed")')
    conn.commit()
    conn.close()

def read():
    import sqlite3

    conn = sqlite3.connect("Database.db")
    c = conn.cursor()
    for row in c.execute(
            'SELECT tweet, tweetID FROM tweets WHERE status = "toBeProcessed"'):
        print(row)
    conn.commit()
    conn.close()

def reject():
    import sqlite3
    conn = sqlite3.connect("Database.db")
    c = conn.cursor()
    c.execute(
        'UPDATE tweets SET status = "REJECT" WHERE tweetId = ?', (4,))
    conn.commit()
    conn.close()

def delete():
    import sqlite3
    conn = sqlite3.connect("Database.db")
    c = conn.cursor()
    c.execute(
        'DELETE FROM tweets WHERE tweetId = ?', (4,))
    conn.commit()
    conn.close()
