'''
Created on 11/mag/2012

@author: fede
'''
nations= ['albania','andorra','austria','belarus','belgium','bosnia and herzegovina',
          'bulgaria','croatia','czech republic','denmark','estonia',  
          'finland','france','germany','greece','hungary',
          'iceland','ireland','italy','latvia','liechtenstein','lithuania','luxembourg',
          'macedonia','malta','moldova','monaco','montenegro','netherlands', 
          'norway','poland','portugal','romania','russia',  
          'san marino','serbia','slovakia','slovenia','spain','sweden', 'switzerland',
          'ukraine','united kingdom','vatican city'] 


def path(start, countries=nations):
    remaining = list(countries)
    del remaining[remaining.index(start)]
    possibles = [x for x in remaining if x[0] == start[-1]]
    maxchain = []
    for c in possibles:
        l = path(c, remaining)
        if len(l) > len(maxchain):
            maxchain = l
    return [start] + maxchain


if __name__ == "__main__":
    print("the longest chain starting from {0} is {1}".
    format('italy', path('italy')))
    print("the longest chain starting from {0} is {1}".
    format('spain', path('spain')))
    print("the longest chain starting from {0} is {1}".
    format('switzerland', path('switzerland')))
    print("the longest chain starting from {0} is {1}".
    format('luxembourg', path('luxembourg')))  
    print("the longest chain starting from {0} is {1}".
    format('belarus', path('belarus')))
    print("the longest chain starting from {0} is {1}".
    format('belgium', path('belgium')))
    print("the longest chain starting from {0} is {1}".
    format('portugal', path('portugal')))