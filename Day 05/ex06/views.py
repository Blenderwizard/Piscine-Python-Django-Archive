from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.
def index(request):
	try:
		conn = psycopg2.connect(dbname="djangotraining", host='localhost', user="djangouser", password="secret")

		curr = conn.cursor()

		curr.execute("""
		CREATE TABLE IF NOT EXISTS ex06_movies (
			title varchar(64) NOT NULL,
			episode_nb integer PRIMARY KEY NOT NULL,
			opening_crawl text,
			director varchar(32) NOT NULL,
			producer varchar(128) NOT NULL,
			release_date date NOT NULL,
			created timestamp DEFAULT NOW(),
			updated timestamp DEFAULT NOW(),
			UNIQUE(title)
		);

		CREATE OR REPLACE FUNCTION update_changetimestamp_column()
		RETURNS TRIGGER AS $$
		BEGIN
		NEW.updated = now();
		NEW.created = OLD.created;
		RETURN NEW;
		END;
		$$ language 'plpgsql';
		CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
		ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
		update_changetimestamp_column();
		""")

		conn.commit()
		conn.close()
	except Exception as e:
		return HttpResponse(e)
	return HttpResponse("OK")

def populate(request):
	insert_text = """INSERT INTO ex06_movies (title, episode_nb, opening_crawl, director, producer, release_date) VALUES (%s,%s,%s,%s,%s,%s)"""
	inputs = [
		("The Phantom Menace", 1, None, "George Lucas", "Rick McCallum", '1999-05-19'),
		("Attack of the Clones", 2, None, "George Lucas", "Rick McCallum", '2002-05-16'),
		("Revenge of the Sith", 3, None, "George Lucas", "Rick McCallum", '2005-05-19'),
		("A New Hope", 4, None, "George Lucas", "Gary Kurtz, Rick McCallum", '1977-05-25'),
		("The Empire Strikes Back", 5, None, "Irvin Kershner", "Gary Kurtz, Rick McCallum", '1980-05-17'),
		("Return of the Jedi", 6, None, "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", '1983-05-25'),
		("The Force Awakens", 7, None, "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", '2015-12-11')
	]
	
	response = []
	try:
		conn = psycopg2.connect(dbname="djangotraining", user="djangouser", password="secret")
		curr = conn.cursor()
		for ins in inputs:
			try:
				curr.execute(insert_text, ins)
				response.append("OK")
			except Exception as e:
				response.append(str(e))
		conn.commit()
		conn.close()
	except Exception as e:
		return HttpResponse(e)

	return HttpResponse("1: {}<br />2: {}<br />3: {}<br />4: {}<br />5: {}<br />6: {}<br />7: {}<br />".format(
		response[0],
		response[1],
		response[2],
		response[3],
		response[4],
		response[5],
		response[6]
	))

def display(request):
	fetch_text = """select * from ex06_movies"""
	conn = ''
	try:
		conn = psycopg2.connect(dbname="djangotraining", host='localhost', user="djangouser", password="secret")
	except Exception as e:
		return HttpResponse("No data available")

	curr = conn.cursor()
	data = []
	try:
		curr.execute(fetch_text)
		data = curr.fetchall()
	except Exception as e:
		return HttpResponse("No data available")
	conn.close()

	if len(data) == 0:
		return HttpResponse("No data available")

	return render(request, 'ex06/view.html', {
		"data": data
	})

def update(request):
	fetch_text = """select * from ex06_movies"""
	conn = ''
	try:
		conn = psycopg2.connect(dbname="djangotraining", host='localhost', user="djangouser", password="secret")
	except Exception as e:
		return HttpResponse("No data available")

	curr = conn.cursor()
	if request.method == 'POST':
		try:
			curr.execute("UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s", (request.POST['content'], request.POST['selection'] ))
			conn.commit()
		except Exception as e:
			return HttpResponse("No data available")
	
	data = []
	try:
		curr.execute(fetch_text)
		data = curr.fetchall()
	except Exception as e:
		return HttpResponse("No data available")
	conn.close()

	if len(data) == 0:
		return HttpResponse("No data available")

	return render(request, 'ex06/update.html', {
		"data": data
	})