import streamlit as st
import math

st.title("Rx Calc.")
st.header("Beta version 1.0 by JRT DVM TFP")

patientname = st.text_input("Patient Name: ")
species = st.text_input("Species: ").lower().strip()
weight = st.number_input("Patient Weight: ")

def main ():
    drug = st.text_input("Please input drug code: ").strip().lower()
    if drug == "coamox":
        coamox()
    
    elif drug == "pred":
        pred()
    

    elif drug == "doxy":
        doxy()
        

    elif drug == "doxyko" or drug == "doxy100":
        doxyko()
        

    elif drug == "clinda":
        clinda()
        

    elif  drug == "clinda150":
        clinda150()
        

    elif drug == "marbo25":
        marbo25()
        

    elif drug == "marbo50":
        marbo50()

    elif drug == "maropitant26":
        maropitant26()
        

    elif drug == "maropitant60":
        maropitant60()
        

    elif drug == "itra":
        itra()
        

    elif drug == "gs":
        gs100()
        

    elif drug == "end" or drug == "exit":
        st.write ("Good bye!")

    elif drug == "pimo":
        pimo()
        

    elif drug == "prednisolone":
        prednisolone()
        

    elif drug == "retromad":
        retromad()
        

    elif drug == "cefurox" or drug == "cefuroxime":
        cefurox()
        

    elif drug == "fortekor" or drug == "benazepryl":
        benazepryl()
        

    else:
        st.write ("Refer to Drug Codex")




def round_half_up(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier + 0.5) / multiplier

def benazepryl():
    benazepryldsg = st.number_input("Please choose Benazpryl (Fortekor) dpsage: 0.25 - 0.5mg/kg: ")
    benazeprylcons = 5
    benazeprylgive = int(round_half_up((weight * benazepryldsg / benazeprylcons)*4)) / 4
    st.write (f"Benazepryl HCl (Fortekor): \nGive {benazeprylgive} tab/s once to twice a day as maintenance.")

def cefurox():
    cefuroxdsg = st.number_input("Please choose Cefuroxime axetil dosage: 10 - 20mg/kg: ")
    cefuroxcons = 50
    cefuroxgive = (weight * cefuroxdsg / cefuroxcons)
    st.write (f"Cefuroxime axetil 250mg/5ml: \nGive {cefuroxgive:.2f} ml twice a day for 14 days.")


#GUI taking patient info
#coamoxiclav stuff
def pimo():
    pimodsg = st.number_input("Please choose Pimobendan dosage: 0.25 - 0.3mg/kg: ")
    pimogive_1 = (weight * pimodsg)
    if pimogive_1 < (2.3):
        pimocons = 1.25
        pimogive_2 = int(round_half_up((pimogive_1 / pimocons)*4)) / 4
        st.write (f"Pimobendan 1.25mg: \nGive {pimogive_2} tab twice a day for 14 days.")

    elif pimogive_1 == (2.3) and pimogive_1 < (5):
        pimocons = 2.5
        pimogive_2 = int(round_half_up((pimogive_1 / pimocons)*4)) / 4
        st.write (f"Pimobendan 2.5mg: \nGive {pimogive_2} tab twice a day for 14 days.")

    elif pimogive_1 == (5) and pimogive_1 < (10):
        pimocons = 5
        pimogive_2 = int(round_half_up((pimogive_1 / pimocons)*4)) / 4
        st.write (f"Pimobendan 5mg: \nGive {pimogive_2} tab twice a day for 14 days.")

    elif pimogive_1 >= (10):
        pimocons = 10
        pimogive_2 = int(round_half_up((pimogive_1 / pimocons)*4)) / 4
        st.write (f"Pimobendan 10mg: \nGive {pimogive_2} tab twice a day for 14 days.")


def retromad():
    if species == "feline" or species == "cat":
        retromad_dz = st.text_input("Enter Disease: \nFeLV \nFIV \nFPV \nFCV \nFIP \nFHV\n\n").strip().lower()
        if retromad_dz == "felv" or retromad_dz == "fiv" :
            retromaddsg = 0.3
            retromadgive = (retromaddsg * weight)
            st.write (f"RetroMad1: Inject {(retromadgive / 2):.2f} ml SQ every 8 hours for 90 days. \n\nOr give {retromadgive:.2f} ml orally every 8 hours for 90 days.")

        elif retromad_dz == "fip" or retromad_dz == "fpv" or retromad_dz == "fcov" or retromad_dz == "corona" or retromad_dz == "parvo"  :
            retromaddsg = 0.5
            retromadgive = (retromaddsg * weight)
            if retromad_dz == "fip" or retromad_dz == "fcov" or retromad_dz == "corona" :
                st.write (f"RetroMad1: Inject {retromadgive:.2f} ml SQ every 8 hours for 40 days.")

            elif retromad_dz == "fpv" or retromad_dz == "parvo" :
                st.write (f"RetroMad1: Inject {retromadgive:.2f} ml SQ every 8 hours for 10 days.")

        elif retromad_dz == "fhv" or retromad_dz == "herpes" or retromad_dz == "fcv" :
            retromaddsg = 0.5
            retromadgive = (retromaddsg * weight)
            st.write (f"RetroMad1: Inject {(retromadgive / 2):.2f} ml SQ every 8 hours for 10 - 20 days. \n\nOr give {retromadgive:.2f} ml orally every 8 hours for 10 -20 days.")

    elif species == "canine" or species == "dog":
        retromad_dz = st.text_input("Enter Disease: \nCDV \nCPV \n\n").strip().lower()
        if retromad_dz == "cdv" or retromad_dz == "distemper" :
            retromaddsg = 0.5
            retromadgive = (retromaddsg * weight)
            st.write (f"RetroMad1: Inject {(retromadgive / 2):.2f} ml SQ every 8 hours for 15 days. \n\nOr give {retromadgive:.2f} ml orally every 8 hours for 15 days.")

        elif retromad_dz == "cpv" or retromad_dz == "parvo" :
            retromaddsg = 0.5
            retromadgive = (retromaddsg * weight)
            st.write (f"RetroMad1: Inject {retromadgive:.2f} ml SQ every 8 hours for 10 days.")




def gs100():
    gsdsg = 6
    gscons = 20
    gsgive = (weight * gsdsg / gscons)
    st.write (f"GS: inject {gsgive:.2f} ml SQ once a day for 84 days.")


def cotricat():
    cotridsg = 2
    cotricons = 20
    cotrigive  = (weight * cotridsg / cotricons)
    st.write (f"Cotri: {cotrigive}")


def itra():
    itradsg = st.number_input("Please choose Itraconazole dosage: 5 -10mg/kg: ")
    itracons = 100
    itragive = int(round_half_up((weight * itradsg / itracons)*4)) / 4
    st.write (f"Itraconazole 100mg: \nGive {itragive} tab/s once to twice a day for 14 days.")


def coamox():
    coamoxdsg = st.number_input("Please choose Co-amoxiclav dosage: 15 - 20mg/kg: ")
    coamoxcons = 62.5
    coamoxgive = (weight * coamoxdsg / coamoxcons)
    st.write (f"Co-amoxiclav 312.5mg/5ml: \nGive {coamoxgive:.2f} ml twice a day for 14 days.")





#pred stuff
def pred():
    preddsg = st.number_input("Please choose Prednisone dosage: 0.5 - 1 mg/kg: ")
    predcons = 2
    predgive = (weight * preddsg / predcons)
    st.write (f"Prednisone 10mg/5ml: \nGive {predgive:.2f} ml twice a day for 5 days. \nThen give {((predgive) / 2):.2f} ml for another 5 days")

def prednisolone():
    prednisolonedsg = st.number_input("Please choose Prednisone dosage: 0.5 - 1 mg/kg: ")
    prednisolonecons = 3
    prednisolonegive = (weight * prednisolonedsg / prednisolonecons)
    st.write (f"Prednisolone 15mg/5ml: \nGive {prednisolonegive:.2f} ml twice a day for 5 days. \nThen give {((prednisolonegive) / 2):.2f} ml for another 5 days")

#doxy stuff
def doxy():
    doxydsg = 5
    doxycons =  20
    doxygive = (weight * doxydsg / doxycons)
    st.write (f"Doxcycline 100mg/5ml: \nGive {doxygive:.2f} ml twice a day for 14 days. \nOR give {((doxygive) * 2):.2f} ml once a day for 14 days. \nSPACE 4 - 6 hours between iron supplements.")

def doxyko():
    doxykodsg = 5
    doxykocons =  100
    doxykogive = int(round_half_up((weight * doxykodsg / doxykocons)*4)) / 4
    st.write (f"Doxcycline 100mg/5ml: \nGive {doxykogive} ml twice a day for 14 days. \nOR give {((doxykogive) * 2)} ml once a day for 14 days. \nSPACE 4 - 6 hours between iron supplements.")


#clinda stuff
def clinda():
    clindadsg = st.number_input("Please choose Clindamycin dosage: 10 - 15 mg/kg: ")
    clindacons = 55
    clindagive = (weight * clindadsg / clindacons)
    st.write (f"Clindamycin 55mg/ml: \nGive {clindagive:.2f} ml once to twice a day for 14 days.")

def clinda150():
    clinda150dsg = st.number_input("Please choose Clindamycin dosage: 10 - 15 mg/kg: ")
    clinda150cons = 150
    clinda150give = int(round_half_up((weight * clinda150dsg / clinda150cons)*4)) / 4
    st.write (f"Clindamycin 150mg: \nGive {clinda150give} tab/s 2 -3x a day for 7 - 14 days.")

#marbo stuff
def marbo25():
    marbo25dsg = st.number_input("Please choose Marbofloxacin dosage: 2.75 - 5.5 mg/kg: ")
    marbo25cons = 25
    marbo25give = int(round_half_up((weight * marbo25dsg / marbo25cons)*4)) / 4
    st.write (f"Marbofloxcacin 25mg: \nGive {marbo25give} tab/s once a day for 7 - 14 days.")

def marbo50():
    marbo50dsg = st.number_input("Please choose Marbofloxacin dosage: 2.75 - 5.5 mg/kg: ")
    marbo50cons = 50
    marbo50give = int(round_half_up((weight * marbo50dsg / marbo50cons)*4)) / 4
    st.write (f"Marbofloxcacin 50mg: \nGive {marbo50give} tab/s twice a day for 14 days.")

#maropitant stuff
def maropitant26():
    maropitant26dsg = 2
    maropitant26cons = 26
    maropitant26give = int(round_half_up((weight * maropitant26dsg / maropitant26cons)*4)) / 4
    st.write (f"Maropitant 26mg: \nGive {maropitant26give} tab/s once a day for 14 days.")

def maropitant60():
    maropitant60dsg = 2
    maropitant60cons = 60
    maropitant60give = int(round_half_up((weight * maropitant60dsg / maropitant60cons)*4)) / 4
    st.write (f"Maropitant 60mg: \nGive {maropitant60give} tab/s once a day for 14 days.")






main()




