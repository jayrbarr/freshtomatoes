import media
import fresh_tomatoes

# Tommy Boy Movie - title, storyline, poster, trailer
tommy_boy = media.Movie(
    "Tommy Boy",
    "A college dropout has to save his father's company.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/f8/Tommy_Boy.jpg/220px-Tommy_Boy.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6nQ4K2bvVxY&t=13s")

# The Incredibles Movie - title, storyline, poster, trailer
the_incredibles = media.Movie(
    "The Incredibles",
    "Superhero family comes out of retirement.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/The_Incredibles.jpg/220px-The_Incredibles.jpg",  # NOQA
    "https://www.youtube.com/watch?v=eZbzbC9285I")

# Happy Gilmore Movie - title, storyline, poster, trailer
happy_gilmore = media.Movie(
    "Happy Gilmore",
    "Washout hockey player becomes golf sensation.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Happygilmoreposter.jpg/220px-Happygilmoreposter.jpg",  # NOQA
    "https://www.youtube.com/watch?v=y1emDAYCfVQ")

# Indiana Jones Movie - title, storyline, poster, trailer
indiana_jones = media.Movie(
    "Raiders of the Lost Ark",
    "Archaeology professor recovers Ark of the Covenant.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Raiders_of_the_Lost_Ark.jpg/220px-Raiders_of_the_Lost_Ark.jpg",  # NOQA
    "https://www.youtube.com/watch?v=XkkzKHCx154")

# Pirates of the Caribbean Movie - title, storyline, poster, trailer
pirates_caribbean = media.Movie(
    "Pirates of the Caribbean",
    "Cursed undead pirates wreak havoc until another pirate intervenes.",
    "https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",  # NOQA
    "https://www.youtube.com/watch?v=naQr0uTrH_s")

# Matrix Movie - title, storyline, poster, trailer
matrix = media.Movie(
    "The Matrix",
    "We are all really just batteries.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=vKQi3bBA1y8")

# Monty Python and the Holy Grail Movie - title, storyline, poster, trailer
monty_python = media.Movie(
    "Monty Python & The Holy Grail",
    "Go away, or I shall taunt you a second time-a.",
    "https://s3.amazonaws.com/images.hamlethub.com/hhresized/original/6926/201707/monty-python-movie-cover-1500745395.jpg",  # NOQA
    "https://www.youtube.com/watch?v=LG1PlkURjxE")

# list of Movies used to generate media file
movies = [
    tommy_boy,
    the_incredibles,
    happy_gilmore,
    indiana_jones,
    pirates_caribbean,
    matrix,
    monty_python]

# generate webpage and open in browser via fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
