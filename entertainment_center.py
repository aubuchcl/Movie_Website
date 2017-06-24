import media
import fresh_tomatoes

toy_story = media.Movie(
    "Toy Story",
    "A Story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "http://www.youtube.com/watch?v=-9ceBgWV8io")


die_in_the_west = media.Movie(
    "A Million Ways to Die in the West",
    "A story about how many ways there are to die in the west",
    "https://upload.wikimedia.org/wikipedia/en/2/22/A_Million_Ways_to_Die_in_the_West_poster.jpg",
    "https://www.youtube.com/watch?v=KniKvVxaM1o")

school_of_rock = media.Movie(
    "School of Rock",
    "Using rock music to learn",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie(
    "Ratatouille",
    "A rat is a chef in Paris",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://vimeo.com/40123311")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Going back in time to meet authors",
    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=FAfR8omt-CY")

# a list that stores all the movie objects so
# they can be called by fresh tomatoes
movies = [toy_story, avatar, die_in_the_west,
          school_of_rock, ratatouille, midnight_in_paris]

fresh_tomatoes.open_movies_page(movies)
