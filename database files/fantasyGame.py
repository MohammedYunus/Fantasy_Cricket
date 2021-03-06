import sqlite3
cricMat=sqlite3.connect('FantasyGame.db')
cursmat=cricMat.cursor()

    ##Creating table for match##

cursmat.execute('''CREATE TABLE match(
Player    TEXT (20) NOT NULL,
Scored    INTEGER,
Faced     INTEGER,
Fours     INTEGER,
Sixes     INTEGER,
Bowled    INTEGER,
Maiden    INTEGER,
Given     INTEGER,
Wkts      INTEGER,
Catches   INTEGER,
Stumping  INTEGER,
RO        INTEGER);''')

cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Kohli', 102, 98, 8, 2, 0, 0, 0, 0, 0, 0, 1);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Yuvraj', 12, 20, 1, 0, 48, 0, 36, 1, 0, 0, 0);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Rahane', 49, 75, 3, 0, 0, 0, 0, 0, 1, 0, 0);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Dhawan', 32, 35, 4, 0, 0, 0, 0, 0, 0, 0, 0);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Dhoni', 56, 45, 3, 1, 0, 0, 0, 0, 3, 2, 0);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Axar', 8, 4, 2, 0, 48, 2, 35, 1, 0, 0, 0);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Pandya', 42, 36, 3, 3, 30, 0, 25, 0, 1, 0, 0);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Jadeja', 18, 10, 1, 1, 60, 3, 50, 2, 1, 0, 1);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Kedar', 65, 60, 7, 0, 24, 0, 24, 0, 0, 0, 0);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Ashwin', 23, 42, 3, 0, 60, 2, 45, 6, 0, 0, 0);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Umesh', 0, 0, 0, 0, 54, 0, 50, 4, 1, 0, 0);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Bumrah', 0, 0, 0, 0, 60, 2, 49, 1, 0, 0, 0);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Bhuwaneshwar', 15, 12, 2, 0, 60, 1, 46, 2, 0, 0, 0);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Rohit', 46, 65, 5, 1, 0, 0, 0, 0, 1, 0, 0);")
cursmat.execute("INSERT INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO) VALUES ('Kartick', 29, 42, 3, 0, 0, 0, 0, 0, 2, 0, 1);")
cricMat.commit()

##Creating table for stats##

cursmat.execute('''CREATE TABLE stats(
Player   TEXT (20) PRIMARY KEY,
Matches  INTEGER,
Runs     INTEGER,
'100'    INTEGER,
'50'     INTEGER,
Value    INTEGER,
Ctg      TEXT (10) NOT NULL);''')

cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Kohli', 189, 8257, 28, 43, 120, 'BAT');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Yuvraj', 86, 3589, 10, 21, 100, 'BAT');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Rahane', 158, 5435, 11, 31, 100, 'BAT');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Dhawan', 25, 565, 2, 1, 85, 'AR');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Dhoni', 78, 2573, 3, 19, 75, 'BAT');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Axar', 67, 208, 0, 0, 100, 'BWL');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Pandya', 70, 77, 0, 0, 75, 'BWL');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Jadeja', 16, 1, 0, 0, 85, 'BWL');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Kedar', 111, 675, 0, 1, 90, 'BWL');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Ashwin', 136, 1914, 0, 10, 100, 'AR');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Umesh', 296, 9496, 10, 64, 110, 'WK');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Bumrah', 73, 1365, 0, 8, 60, 'WK');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Bhuwaneshwar', 17, 289, 0, 2, 75, 'AR');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Rohit', 304, 8701, 14, 52, 85, 'BAT');")
cursmat.execute("INSERT INTO stats (Player, Matches, Runs, '100', '50', Value, Ctg) VALUES ('Kartick', 11, 111, 0, 0, 75, 'AR');")
cricMat.commit()

##creating table for teams##
cursmat.execute('''CREATE TABLE teams(
Name    TEXT NOT NULL,
Players TEXT NOT NULL,
Value   INTEGER);
''')
cricMat.commit()
cricMat.close()
