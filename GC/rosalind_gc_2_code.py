with open("fastat.txt") as tiedosto:
    tiedot = {}
    nimi = ""
    for rivi in tiedosto:
        if rivi[0] == ">":
            nimi = rivi[1:].strip()
            tiedot[nimi] = ""
        else:
            tiedot[nimi] += rivi.strip()

    suurin = ""
    suurinprosentti = 0
    for nimi in tiedot.keys():
        geet = tiedot[nimi].count("G")
        ceet = tiedot[nimi].count("C")
        prosentti = (geet+ceet)/len(tiedot[nimi])
        if prosentti >suurinprosentti:
            suurin = nimi
            suurinprosentti = prosentti
    
    print (suurin)
    print(suurinprosentti*100)