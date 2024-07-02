import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def fight(number,player):
    if number == 0 and player == "sk":
        print("CY")
        return
    elif number == 0 and player == "cy":
        print("SK")
        return
    
    if number-3 >= 0 :
        if player == "sk":
            fight(number-3,"cy")
        else :
            fight(number-3,"sk")
    if player == "sk":
        fight(number-1,"cy")
    else :
        fight(number-1,"sk")
n = int(input())
fight(n,"sk")
