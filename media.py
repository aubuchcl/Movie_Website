import webbrowser

class Movie():
	# initialize the class movie
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):

		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	# this method allows you to access the movie objects trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

