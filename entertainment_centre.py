import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        r"E:\python\movie_website\toy_story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     r"E:\python\movie_website\avatar.jpg",
                     "http//www.youtube.com/watch?v=-9ceBgWV8io")

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
