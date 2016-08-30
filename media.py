import webbrowser


class Movie():

    """ This class provides a way to store movie related information

    Args:
        movie_title (str): Movie title.
        poster_image (str): Poster image url.
        trailer_youtube (str): Youtube trailer url.

    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
