import sys
from antigravity import geohash


def geohash_display() -> None:
	if len(sys.argv) != 4:
		print("Error: Invalid number of arguments!")
		print("geohashing.py [Your Latitude] [Your Longitude] [Date of Dow Opening]")
		return
	latitude = 0
	longitude = 0
	dowopening = b''
	try:
		latitude = float(sys.argv[1])
	except:
		print("Error: Invalid Input for latitude!")
		print("geohashing.py [Your Latitude] [Your Longitude] [Date of Dow Opening]")
		return
	try:
		longitude = float(sys.argv[2])
	except:
		print("Error: Invalid Input for longitude!")
		print("geohashing.py [Your Latitude] [Your Longitude] [Date of Dow Opening]")
		return
	try:
		dowopening = bytes(sys.argv[3], 'ascii')
	except:
		print("Error: Invalid Input for latitude!")
		print("geohashing.py [Your Latitude] [Your Longitude] [Date of Dow Opening]")
	geohash(latitude, longitude, dowopening)

if __name__ == '__main__':
	geohash_display()