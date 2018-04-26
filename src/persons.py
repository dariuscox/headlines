import csv
import unicodedata
from random import shuffle

person_csv = "../events/personOfYear.csv"


def get_events(events_csv):
    events = {}
    with open(events_csv) as csvfile:
        person_reader = csv.reader(csvfile)
        csvfile.readline()
        for row in person_reader:
            row[2] = unicodedata.normalize("NFKD", row[2])
            if "(" in row[2]:
                s = row[2][row[2].find("(")+1:row[2].find(")")]
                events[s] = row
            else:
                events[row[2]] = row
    return events


def shuffle_events(events):
    names = list(events.keys())
    shuffle(names)
    return names


def one_plyaer():
    print("Welcome to headlines!")
    hand = []
    events = get_events(person_csv)
    deck = shuffle_events(events)
    hand.append(deck.pop(0))
    print("Your current hand is:", hand)


one_plyaer()

