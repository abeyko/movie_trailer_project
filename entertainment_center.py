import fresh_tomatoes
import media

labyrinth = media.Movie("Labyrinth",
                        "http://1.bp.blogspot.com/-CmzNSTLR72c/T-HHz7oaCjI/AAAAAAAAHLc/hdyVgDmIVks/s1600/Labyrinth+(1986)+Teaser.jpg",
                        "https://www.youtube.com/watch?v=XRcOZZDvMv4")

moulin_rouge = media.Movie("Moulin Rouge",
                     "http://www.dafont.com/forum/attach/orig/2/4/243446.jpg",
                     "https://www.youtube.com/watch?v=2PpgPxjzbkA")

amelie = media.Movie("Amelie",
                     "http://cdn.miramax.com/media/assets/Amelie1.png",
                     "https://www.youtube.com/watch?v=B-uxeZaM-VM")

love_me_if_you_dare = media.Movie("Love Me If You Dare",
                     "http://i.hungrygowhere.com/cms/73/db/b3/d0/156064/2a1f7cae70_345x518_61e3129169.jpg",
                     "https://www.youtube.com/watch?v=CX23hgYDTwg")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")

rat_race = media.Movie("Rat Race",
                     "https://upload.wikimedia.org/wikipedia/en/9/99/Rat_Race_poster.jpg",
                     "https://www.youtube.com/watch?v=INhtX73tSxY")

movies = [labyrinth, moulin_rouge, amelie, love_me_if_you_dare, midnight_in_paris, rat_race]

fresh_tomatoes.open_movies_page(movies)
