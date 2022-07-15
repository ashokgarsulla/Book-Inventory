import requests
from . import settings



result = requests.get(
		'https://maps.googleapis.com/maps/api/directions/json?',
		 params={
		 'q': "python",
		 "key": settings.GOOGLE_API_KEY
		 })