from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.
def index(request):
	try:
		conn = psycopg2.connect(dbname="djangotraining", host='localhost', user="djangouser", password="secret")

		curr = conn.cursor()

		curr.execute("""CREATE TABLE IF NOT EXISTS ex00_movies (
			title varchar(64) NOT NULL,
			episode_nb integer PRIMARY KEY NOT NULL,
			opening_crawl text,
			director varchar(32) NOT NULL,
			producer varchar(128) NOT NULL,
			release_date date NOT NULL,
			UNIQUE(title)
		)
		""")

		conn.commit()
		conn.close()
	except Exception as e:
		return HTTPResponse(e)
	return HttpResponse("OK")