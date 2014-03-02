import nuodb

connection = pynuodb.connect("test", "localhost", "dba", "goalie", options={'schema':'hockey'})
cursor = connection.cursor()

while 1:
	search_movie = raw_input('Would you like to search by movie (m) or actor (a)?: ')
	if (search_movie == "quit"): break

	if (search_movie == "m" or search_movie == "M"):
		data_input = raw_input('What movie would you like to search the actor/actress database by?: ')
		if (search_movie == "quit"): break

		cursor.execute("SELECT NAME FROM ACTOR WHERE MOVIE=data_input")
	elif (search_movie == "a" or search_movie == "A"):
		data_input = raw_input('Which actor would you like to search the movie database by?: ')
		if (search_movie == "quit"): break

		cursor.execute("SELECT MOVIE FROM ACTOR WHERE NAME=data_input")
	else
		print("Unrecognizable character, type 'quit' to exit if that's what you want to do")