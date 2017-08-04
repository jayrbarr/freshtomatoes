import media
import fresh_tomatoes

tommy_boy = media.Movie("Tommy Boy",
                        "A college dropout has to save his father's company.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/f/f8/Tommy_Boy.jpg/220px-Tommy_Boy.jpg",
                        "https://www.youtube.com/watch?v=6nQ4K2bvVxY&t=13s")

the_incredibles = media.Movie("The Incredibles", "Superhero family comes out of retirement.", "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/The_Incredibles.jpg/220px-The_Incredibles.jpg",
                     "https://www.youtube.com/watch?v=eZbzbC9285I")

happy_gilmore = media.Movie("Happy Gilmore", "Washout hockey player becomes golf sensation.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Happygilmoreposter.jpg/220px-Happygilmoreposter.jpg",
                             "https://www.youtube.com/watch?v=y1emDAYCfVQ")

indiana_jones = media.Movie("Raiders of the Lost Ark", "Archaeology professor recovers Ark of the Covenant.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Raiders_of_the_Lost_Ark.jpg/220px-Raiders_of_the_Lost_Ark.jpg",
                          "https://www.youtube.com/watch?v=XkkzKHCx154")

pirates_caribbean = media.Movie("Pirates of the Caribbean", "Cursed undead pirates wreak havoc until another pirate intervenes.",
                                "https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",
                                "https://www.youtube.com/watch?v=naQr0uTrH_s")

matrix = media.Movie("The Matrix", "We are all really just batteries.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
                           "https://www.youtube.com/watch?v=vKQi3bBA1y8")

movies = [tommy_boy, the_incredibles, happy_gilmore, indiana_jones, pirates_caribbean, matrix]
fresh_tomatoes.open_movies_page(movies)

                          
