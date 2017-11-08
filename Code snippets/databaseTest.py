import sqlite3

conn = sqlite3.connect("Database.db")
c = conn.cursor()
for row in c.execute(
        'SELECT tweet, tweetID FROM tweets WHERE status = "toBeProcessed"'):
    print(row)
conn.commit()
conn.close()


conn = sqlite3.connect("Database.db")
c = conn.cursor()
c.execute(
       'UPDATE tweet SET status = "REJECT" WHERE tweetId = ?', (tweetID_cache,))
conn.commit()
conn.close()


conn = sqlite3.connect("Database.db")
c = conn.cursor()
c.execute(
       'DELETE FROM table WHERE tweetId = ?', (tweetID_cache,))
conn.commit()
conn.close()