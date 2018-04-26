import csv
import unicodedata

person_csv = "../events/personOfYear.csv"


def get_events(events_csv):
    events = {}
    with open(person_csv) as csvfile:
        person_reader = csv.reader(csvfile)
        csvfile.readline()
        for row in person_reader:
            row[2] = unicodedata.normalize("NFKD", row[2])
            if "(" in row[2]:
                s = row[2][row[2].find("(")+1:row[2].find(")")]
                events[s] = row
            else:
                events[row[2]] = row

    print(events.keys())
    return


get_events(person_csv)