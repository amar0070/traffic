import Queue as Q
import random

global street
street = Q.Queue()


def make_street():
    global street
    street = Q.Queue()


# Load up a street. Each car is a keyword indicating the direction it's going.
def populate_street(street, car_count):
    # global street
    for num in range(0, car_count):
        street.put(random.choice([':straight', ':straight', ':left', ':right']))


directions = {':north': {':straight' ':south' ':right' ':west' ':left' ':east'},
              ':south': {':straight' ':north' ':right' ':east' ':left' ':west'},
              ':east': {':straight' ':west' ':right' ':north' ':left' ':south'},
              ':west': {':straight' ':east' ':right' ':south' ':left' ':north'}}


def allowed (lights, coming_from, direction) :
    #TODO: write
    return


def four_way_intersection():
    global street
    r = {':streets': {':north': {make_street(), populate_street(street, 10)},
                      ':south': {make_street(), populate_street(street, 10)},
                      ':east': {make_street(), populate_street(street, 10)},
                      ':west': {make_street(), populate_street(street, 10)}},
         ':lights': {':north': {':green'}}, ':south': {':red'}, ':east': {':red'}, ':west': {':red'}}

    return r


# [this would need to be changed]Create a thread that adds new cars to the streets.
def traffic_generator(streets):
    t = {streets}
    for s in t:
        populate_street(s, 1)


def move_car(coming_from, direction):
    print 'Car Coming from' + coming_from + 'went' + direction


def step(intersection):
    # TODO: write
    return

def main(steps):
    steps = int(float(steps))
    intersection = four_way_intersection()
    generator = traffic_generator(intersection.get(':streets'))
    # .start check this line with Dan
    for num in range(0, steps):
        step(intersection)
