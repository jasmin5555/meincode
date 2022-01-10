print(" Programmbeginn ")

neues_Auto = int(input( " wie viele PS hat das Auto? "))

if neues_Auto < 100:
    print( " Lassen sie es stehen")
else:
    print(" dieses Auto hat genügend PS" )
    
    farbe = input(" Welche Farbe hat das Auto?")
    
    if farbe == "rot" :
        print(" Dieses Auto hat die richtige Farbe es passt zu ihnen")
    else :
        print(" Es ist nicht für sie geeignet ")

print(" Danke für ihren Besuch")