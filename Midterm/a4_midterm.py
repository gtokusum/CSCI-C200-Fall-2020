import math
def ASCII_square(n):
    baseSquare = ''
    k = n
    while k > 0:
        baseSquare = baseSquare + ('*' * n) + '\n'
        k += -1
    return baseSquare


def ASCII_triangle(n):
    basetriangle = ''
    k = 1
    pace = n
    while k <= n:
        space = (pace/2) - 0.5
        basetriangle = basetriangle + (' ' * int(space)) + ('*' * k) + '\n'
        pace -= 2
        k += 2
    return basetriangle



def my_range(start,stop,step):
    ap = start
    sol = [ap]
    if start < stop:
        while sol[-1] < stop - step:
            ap += step
            sol.append(ap)
    else:
        sol = []
    return sol

Act, Au,Ag,Pd,Pt ="Act", "gold", "silver", "paladium", "platinum"
spot_price = {Au:1918.40, Ag:24.23,\
              Pt:912.45, Pd: 2353.35}
portfolio = {"Act": 100000, Au:0, Ag:0, Pt:0, Pd:0}
            
def purchase(portfolio, metal, amt):
    metalPrice = spot_price[metal] * amt
    portfolio["Act"] = portfolio["Act"] - metalPrice
    portfolio[metal] = portfolio[metal] + amt
    
def worth(portfolio):
    liquid = 0
    portAmt = portfolio["Act"]
    goldPrice = portfolio[Au] * spot_price[Au]
    silverPrice = portfolio[Ag] * spot_price[Ag]
    paladiumPirce = portfolio[Pt] * spot_price[Pt]
    platinumPrice = portfolio[Pd] * spot_price[Pd]
    liquid = portAmt + goldPrice + silverPrice + paladiumPirce + platinumPrice
    return liquid

def how_much(portfolio, metal):
    amtOfMetal = portfolio["Act"] // spot_price[metal]
    return amtOfMetal


def find_num_min(xlst):
    minAmt = 0
    if len(xlst) > 0:
        for i in xlst:
            minValue = min(xlst)
            if i == minValue:
                minAmt += 1
        return (minValue, minAmt)
    else:
        return ()
        
    

