import sqlite3
import random

con = sqlite3.connect('dice_data.db')
cur = con.cursor()

try:
    cur.execute("""CREATE TABLE
        Dice(one INTEGER, two INTEGER, three INTEGER, four INTEGER, five INTEGER, six INTEGER)
    """)
    for i in range(10000):
        dice = []
        for i in range(6):
            dice.append(random.randint(1, 6))
        cur.execute("INSERT INTO Dice VALUES(?, ?, ?, ?, ?, ?)",
        (dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]))
        con.commit()
except:
    print("Already exists!")

cur.execute("""SELECT * FROM Dice WHERE
    one = 1 AND two = 2 AND three = 3 AND four = 4 AND five = 5 AND six = 6
""")
i = 0
for row in cur.fetchall():
    i += 1
    print("Found", i)

cur.execute("SELECT * FROM Dice")
for row in cur.fetchall():
    print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, ")
    