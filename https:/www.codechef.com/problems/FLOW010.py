# cook your dish here
#B or b	BattleShip
#C or c	Cruiser
#D or d	Destroyer
#F or f	Frigate
t=int(input())
for tc in range(t):
    char=input()
    if char=="B" or char=="b":
        print("BattleShip")
    elif char=="C" or char=="c":
        print("Cruiser")
    elif char=="D" or char=="d":
        print("Destroyer")
    elif char=="F" or char=="f":
        print("Frigate")
    else:
        pass
    
