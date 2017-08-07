""" this class defines a Movie type to hold an individual Movie """


class Movie():

    """    Movie constructor with args:
            movie_title = title string,
            movie_storyline = storyline string,
            movie_poster = poster url, and
            movie_trailer = trailer url
    """
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_poster,
                 movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
