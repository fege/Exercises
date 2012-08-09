'''
Created on 11/apr/2012

@author: fede
To help planning your trip you have to write a function crossing that given 
a country name and n (the desired number of steps) gives you the set of countries 
you can reach crossing n countries starting from the given country. Note that:

in zero steps you can't exit from the starting country;
in one step you get only in the border countries;
the path must always be minimal, e.g., from Italy you can get in Belgium crossing Switzerland 
and Germany or only France the second is the one to choose;
you can't cross a country twice or more or get back, e.g., Italy → Switzerland → Italy 
or Italy → Switzerland → France are wrong.
Since Europe is tightly coupled to Asia in the exercise exclude Kazakhstan, Georgia, 
Azerbaijan, Cyprus and Turkey from Europe, i.e., consider Europe as a group of islands 
separated from Asia in the listed countries (that could be considered as ocean if you like). 
Hint define a generator border, used by crossing, that given the starting country at each step 
provides the set of border countries of the border computed in the previous step.
'''
neighborhood = {
    'albania': ['greece', 'macedonia', 'serbia', 'montenegro'],
    'andorra': ['spain', 'france'],
    'austria': ['liechtenstein', 'switzerland', 'italy',
    'czech republic', 'germany', 'slovakia',
    'hungary', 'slovenia'],
    'belarus': ['russia', 'lithuania', 'latvia', 'poland',
    'ukraine'],
    'belgium': ['luxembourg', 'germany', 'france', 'netherlands'],
    'bosnia and herzegovina': ['montenegro', 'serbia', 'croatia'],
    'bulgaria': ['romania', 'serbia', 'macedonia', 'greece'],
    'croatia': ['bosnia and herzegovina', 'serbia', 'hungary',
    'slovenia'],
    'czech republic': ['slovakia', 'austria', 'germany', 'poland'],
    'denmark': ['germany'],
    'estonia': ['russia', 'latvia'],
    'finland': ['sweden', 'russia', 'norway'],
    'france': ['spain', 'andorra', 'monaco', 'luxembourg',
    'belgium', 'germany', 'switzerland', 'italy'],
    'germany': ['denmark', 'luxembourg', 'belgium', 'france',
    'netherlands', 'poland', 'czech republic',
    'austria', 'switzerland'],
    'greece': ['bulgaria', 'macedonia', 'albania'],
    'hungary': ['romania', 'ukraine', 'slovakia', 'austria',
    'slovenia', 'croatia', 'serbia'],
    'iceland': [],
    'ireland': ['united kingdom'],
    'italy': ['france', 'switzerland', 'austria', 'slovenia',
    'san marino', 'vatican city'],
    'latvia': ['russia', 'estonia', 'lithuania', 'belarus'],
    'liechtenstein': ['austria', 'switzerland'],
    'lithuania': ['russia', 'latvia', 'belarus', 'poland'],
    'luxembourg': ['belgium', 'germany', 'france'],
    'macedonia': ['bulgaria', 'serbia', 'albania', 'greece'],
    'malta': [],
    'moldova': ['ukraine', 'romania'],
    'monaco': ['france'],
    'montenegro': ['albania', 'serbia', 'bosnia and herzegovina'],
    'netherlands': ['germany', 'belgium'],
    'norway': ['sweden', 'finland', 'russia'],
    'poland': ['russia', 'lithuania', 'belarus', 'ukraine',
    'slovakia', 'czech republic', 'germany'],
    'portugal': ['spain'],
    'romania': ['ukraine', 'moldova', 'bulgaria', 'serbia',
    'hungary'],
    'russia': ['norway', 'finland', 'estonia', 'latvia',
    'lithuania', 'belarus', 'ukraine', 'poland'],
    'san marino': ['italy'],
    'serbia': ['bosnia and herzegovina', 'hungary', 'croatia',
    'montenegro', 'albania', 'macedonia', 'bulgaria',
    'romania'],
    'slovakia': ['hungary', 'austria', 'czech republic', 'poland',
    'ukraine'],
    'slovenia': ['italy', 'austria', 'hungary', 'croatia'],
    'spain': ['portugal', 'andorra', 'france'],
    'sweden': ['norway', 'finland'],
    'switzerland': ['germany', 'france', 'liechtenstein', 'austria',
    'italy'],
    'ukraine': ['russia', 'belarus', 'poland', 'moldova',
    'slovakia', 'hungary', 'romania'],
    'united kingdom': ['ireland'],
    'vatican city': ['italy']
}


def border(naz):
    vicini = set([naz])
    yield vicini
    visitati = vicini
    while True:
        nuovo = set()
        for c in vicini:
            nuovo.update(set(neighborhood[c]))
        yield nuovo - visitati
        visitati.update(nuovo)
        vicini=nuovo



def crossing(naz,step):
    vicini = border(naz)
    for i in range(step):
        next(vicini)
    return next(vicini)

if __name__ == '__main__':
    print("*** From Italy in ")
    for steps in range(0,8):
        print("[{0}] = {1}".format(steps, crossing("italy", steps)))
    print("*** From Sweden in [5] steps, you get in", crossing('sweden', 5))
    print("*** From Germany in [2] steps, you get in", crossing('germany', 2))
    print("*** From Iceland in [3] steps, you get in", crossing('iceland', 3))