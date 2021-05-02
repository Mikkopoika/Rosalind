with open("fastat.txt") as tiedosto:
    tiedot = {}
    nimi = ""
    for rivi in tiedosto:
        if rivi[0] == ">":
            nimi = rivi[1:].strip()
            tiedot[nimi] = ""
        else:
            tiedot[nimi] += rivi.strip()

    
    konsensus = {}
    konsensus["A"] = [0 for i in range(len(tiedot[nimi]))]
    konsensus["C"] = [0 for i in range(len(tiedot[nimi]))]
    konsensus["G"] = [0 for i in range(len(tiedot[nimi]))]
    konsensus["T"] = [0 for i in range(len(tiedot[nimi]))]
    
    for i in range(0, len(tiedot[nimi])):
        for avain in tiedot.keys():
            if tiedot[avain][i] == "A":
                konsensus["A"][i] += 1
            if tiedot[avain][i] == "T":
                konsensus["T"][i] += 1
            if tiedot[avain][i] == "C":
                konsensus["C"][i] += 1
            if tiedot[avain][i] == "G":
                konsensus["G"][i] += 1
    


    konsensusstring = ""

    for i in range(0, len(tiedot[nimi])):
        suurin = konsensus["A"][i]
        suurinemas = "A"
        for avain in konsensus.keys():
            if konsensus[avain][i] > suurin:
                suurin = konsensus[avain][i] 
                suurinemas = avain
        konsensusstring += suurinemas

    print(konsensusstring)

    print("A: ", end="")
    for i in range(0, len(konsensus["A"])):
        print(konsensus["A"][i], end=" ")
    print()
    print("C: ", end="")
    for i in range(0, len(konsensus["C"])):
        print(konsensus["C"][i], end=" ")
    print()
    print("G: ", end="")
    for i in range(0, len(konsensus["G"])):
        print(konsensus["G"][i], end=" ")
    print()
    print("T: ", end="")
    for i in range(0, len(konsensus["T"])):
        print(konsensus["T"][i], end=" ")
    print()

