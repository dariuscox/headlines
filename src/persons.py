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

def give_card(deck,events):
    card = deck.pop(0)
    card_year = events[card][0]
    return card,card_year

def view_card(deck):
    return deck[0]

def check_card(card, hand, events, pos):
    """
    uses index to chose do the ordering, 0 is first, len is last, otherwise index of the card
    :param card:
    :param hand:
    :param events:
    :param pos:
    :return:
    """
    correct =  False
    if pos == 0:
        if hand[0][1]>= events[card][0]:
            correct = True
    elif pos == len(hand):
        if hand[len(hand)-1][1] <= events[card][0]:
            correct = True
    else:
        if hand[pos][1]>= events[card][0] and hand[pos-1][1] <= events[card][0]:
            correct = True
    print(correct)
    return correct


def one_player():
    print("Welcome to headlines!")
    hand = []
    events = get_events(person_csv)
    deck = shuffle_events(events)
    hand.append(give_card(deck, events))
    print("Your current hand is:", hand)
    while len(hand) <= 9:
        current_card = view_card(deck)
        print("The next card is: ", current_card)
        pos = input('Where does %s fit in your hand?\n' % current_card)
        pos = int(pos)
        if check_card(current_card,hand, events, pos):
            if pos == len(hand):
                hand.append(give_card(deck, events))
            else:
                hand.insert(int(pos), give_card(deck, events))
        else:
            deck.pop(0)
        print("Your current hand is:", hand)





one_player()

