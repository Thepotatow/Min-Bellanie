#characters
init python:
    def define_character(name, color):
        return Character(name, color=color)

    sv = define_character(None, "#000000")  # or any color you like
    c = define_character("Cass", "#642929")
    a = define_character("Alvin", "#0d37a0")
    t = define_character("Tyler", "#0da037")
    b = define_character("Bella", "#da19ec")
    s = define_character("Starr", "#b429ff")
    bb = define_character("Bear Blaine", "#1e6b2a")
    bs = define_character("Burt Salem", "#ff0b0b")
    k = define_character("Kendall Salem", "#d46767")
    pj = define_character("P. Johnsson", "#967eff")


#affections
default affection_burt = 0
default affection_bella = 0
default affection_bear = 0

default phone_bella = 0

#bulleons

default subtle_letter = True

default alvin_good = True

default tyler_lie = True

default camera_hacked = True

default ending_10 = False

default ending_9 = False


image bg courtyard = "images/courtyard.jpg"
image bg hallway = "images/hallway.jpg"
image bg classroom = "images/classroom.jpg"
image bg ice_rink = "images/ice_rink.jpg"
image bg busstop = "images/busstop.jpg"
image bg crawlspace = "images/crawlspace.jpg"
image bg garage = "images/garage.jpg"
image bg party = "images/party.jpg"
image bg road = "images/road.jpg"
image bg vent = "images/vent.jpg"


image bg cass_bedroom = "images/cass_bedroom.jpg"
image bg cass_livingroom = "images/cass_bigroom.jpg"
image bg cass_entrance = "images/cass_entranceway.jpg"


image bella happy = "images/bella happy.png"
image bella neutral = "images/bella neutral.png"
image bella thinking = "images/bella thinking.png"
image bella serius = "images/bella serius.png"
image bella scarred = "images/bella scarred.png"
image bella tied upp = "images/bella tied_upp.png"

image alvin happy = "images/alvin happy.png"
image alvin neutral = "images/alvin neutral.png"

image tyler happy = "images/tyler happy.png"
image tyler neutral = "images/tyler neutral.png"
image tyler angry = "images/tyler angry.png"
image tyler furius = "images/tyler furius.png"
image tyler thinking = "images/tyler thinking.png"

#cutscenes


#camera view
image my_video = Movie(play="movie/cutscene-test-2.webm", loop=False)
image my_video = Movie(play="movie/cutscene-test.webm", loop=False)


# $ renpy.pause(renpy.movie_cutscene("movie/cutscene-test.webm"))

