# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT
# ---------

# MODUULIT
# --------

from avtools import sound # Äänimerkit ja äänitiedostot
from avtools import video # Videomoduuli
import identityCheck2

# ASETUKSET
# ---------
kameraIndeksi: int = 0 # Ensimmäinen kamera on aina 0

# Pääohjelman ikuinen silmukka
while True:
    userGivenSsn = input("Syötä asiakkaan henkilötunnus: ")
    userGivenSsn = userGivenSsn.upper() # Varmistetaan, että tarkiste on isolla
    
    # TODO: varaudu tilanteeseen, jossa hetu:n tarkiste on annettu pienillä kirjaimilla

    # TODO: Rakenna funktio, jolla kysytään nimet ja muutetaan yhdysnimet isoille alkukirjaimille -> reg exp

    ssnToCheck = identityCheck2.NationalSSN(userGivenSsn)
    if ssnToCheck.isValidSsn() == True:
        try:
            ssnToCheck.getDateOfBirth()
            ssnToCheck.getGender()
            age = ssnToCheck.calculateAge()
            userGivenLastname = input("Syötä asiakkaan sukunimi: ")
            userGivenLastname = userGivenLastname.capitalize()
            userGivenFirstname = input("Syötä asiakkaan etunimi: ")
            userGivenFirstname = userGivenFirstname.capitalize()
            print("Asiakas:", userGivenLastname, userGivenFirstname)
            print("Syntymäaika:", ssnToCheck.dateOfBirth)
            print("Ikä:", age)
            print("Sukupuoli:", ssnToCheck.gender)
        except Exception as e:
            print("Syöttämässäsi sosiaaliturvatunnuksessa oli virhe", e)

    # kysytään halutaanko poistua ohjelmasta
    wantAbort = input("Haluatko päättää ohjelman k/E: ")
    if wantAbort.upper() == "K":
        break # Poistutaan ikuisesta silmukasta