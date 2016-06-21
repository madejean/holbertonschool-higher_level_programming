import mysql.connector

db = mysql.connector.connect(
	host = "173.246.108.142",
	port = '3306',
	user = "student",
	password = "aLQQLXGQp2rJ4Wy5",
	database = "Project_169",
	charset = 'utf8',
	use_unicode= False,
)

cursor = db.cursor()
sql_shows = "SELECT TVShow.name, TVShow.id FROM TVShow ORDER BY TVShow.name"
sql_seasons = "SELECT Season.id, Season.number FROM Season WHERE Season.tvshow_id = "

cursor.execute(sql_shows)
results = cursor.fetchall()

for row in results:
	print row[0] + ":"
	cursor.execute(sql_seasons + str(row[1]))
	seasons = cursor.fetchall()
	for s in seasons:
		print "\tSeason " + str(s[1]) + ":"
		sql_episodes = "SELECT Episode.name, Episode.number FROM Episode WHERE Episode.season_id = " + str(s[0]) + " ORDER BY Episode.number"
		cursor.execute(sql_episodes)
		episodes = cursor.fetchall()
		for ep in episodes:
			print "\t\t" + str(ep[1]) + ": " + str(ep[0])
