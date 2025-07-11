import streamlit as st
import math
from fpdf import FPDF
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime

absolute_path = os.path.abspath("tfplogo.png")



smtp_server = "smtp-mail.outlook.com"
smtp_port = 587
sender_email = "tfpcalcrx@outlook.com"
sender_password = "Iltfp123"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = "thefurrprojectquezoncity@gmail.com"
msg['Subject'] = "Subject of the Email"


st.title("Vet Calc.")
st.header("Alpha version 1.0 by JRT DVM of The Furr Project QC")

patientname = st.text_input("Patient Name: ")

species = st.text_input("Species: ").lower().strip()
weight = st.number_input("Patient Weight: ")
# Call generate_pdf with species and weight
if species == "cat" or species == "feline" or species == "fel":
    BSA = ((weight * 1000)**(2/3)) * 10 * 0.0001
elif species == "dog" or species == "canine" or species == "can":
    BSA = ((weight * 1000)**(2/3)) * 10.1 * 0.0001



def main ():
    if 'results' not in st.session_state:
        st.session_state.results = []

    drug = st.text_input("Please input drug code: ").strip().lower()

    
    if drug == "coamox":
        result = coamox()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    
    
    elif drug == "pred":
        result = pred()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    

    elif drug == "doxy":
        result = doxy()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)


    elif drug == "doxyko" or drug == "doxy100" or drug == "doxy tab":
        result = doxyko()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
        

    elif drug == "clinda":
        result = clinda()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
        

    elif drug == "marbo":
        result = marbo()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
        

    elif drug == "maropitant" or drug == "maropitant citrate":
        result = maropitant()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
        

    elif drug == "itra":
        result = itra()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
        

    elif drug == "gs":
        result = gs()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
        

    elif drug == "end" or drug == "exit":
        st.write ("Good bye!")

    elif drug == "pimo":
        result = pimo()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
        

    elif drug == "prednisolone":
        result = prednisolone()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
        

    elif drug == "retromad":
        result = retromad()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
        

    elif drug == "cefurox" or drug == "cefuroxime" or drug == "cefu":
        result = cefurox()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
        

    elif drug in ["fortekor", "benazepryl" , "aceptor"]:
        result = benazepryl()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
        
    elif drug == "ursodiol" or drug == "urso" or drug == "ursodeoxycholic acid":
        result = urso()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "furo" or drug == "furosemide":
        result = furo()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "spironolactone" or drug == "spiro":
        result = spiro()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "cotri" or drug == "cotrimoxazole":
        result = cotri()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "enro":
        result = enro()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "cri":
        result = cri()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "bsa":
        result = bsa()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "cotrimet":
        result = cotrimet()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "vincristine" or drug == "vinc":
        result = vincristine()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "fluid rate" or drug == "fluid":
        result = fluid()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "previcox":
        result = previcox()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "gaba" or drug == "gabapentin":
        result = gaba()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    
    elif drug == "entero" or drug == "enteroprotek":
        result = entero()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "hepatiale" or drug == "hepatiale forte":
        result = hepatiale()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    
    elif drug == "renal combi" or drug == "renalcombi":
        result = renalcombi()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "renal n":
        result = renaln()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "renal p":
        result = renalp()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "melox" or drug == "meloxicam":
        result = melox()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "aluminum hydroxide" or drug == "alumag" or drug == "medalem":
        result = alumag()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "cardiovet":
        result = cardiovet()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "same" or drug == "s-adenosylmethionine" or drug =="adenosylmethionine":
        result = same()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "leve" or drug == "levetiracetam":
        result = leve()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "cyclo" or drug == "cyclosporine":
        result = cyclo()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)


    elif drug == "campi":
        result = confineampi()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    
    elif drug == "cmarbo":
        result = confinemarbo()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "dexa":
        result = confinedexa()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "ctramadol":
        result = confinetramadol()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "dupha":
        result = dupha()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)


    elif drug == "tolfine":
        result = ctolfine()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    
    elif drug == "orni":
        result = orni()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "fercob":
        result = fercob()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "epo":
        result = epo()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    
    elif drug == "cepo":
        result = cepo()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "filgrastim" or drug == "neupogen" or drug == "filgras":
        result = filgrastim()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "cfilgrastim" or drug == "cneupogen" or drug == "cfilgras":
        result = cfilgrastim()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "cerenia":
        result = cerenia()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "hemacare" or drug == "hemacarefe" or drug == "hemacare-fe":
        result = hemacare()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "hemoglo-aide plus" or drug == "hemoglo":
        result = hemoglo()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "broncure":
        result = hemoglo()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "bromhexine" or drug =="bromhex" or drug =="bromivet":
        result = bromhex()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "sangobion":
        result = sangobion()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "thrombeat" or drug == "thrombbeat":
        result = thrombeat()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "thrombeat" or drug == "thrombbeat":
        result = thrombeat()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    
    elif drug == "soluneb" or drug == "nebulizer":
        result = soluneb()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "dermclens":
        result = dermclens()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "mupirocin" or drug == "mupiro":
        result = mupiro()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "zole" or drug == "zoletil":
        result = zole()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "cmetro":
        result = cmetro()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    
    elif drug == "cleve":
        result = cleve()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "profopol" or drug == "profo" or drug == "propofol" or drug == "propo":
        result = profo()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "actea":
        result = actea()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "atro" or drug == "atropine":
        result = atro()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)    

    elif drug == "oxytocin" or drug == "oxy":
        result = oxytocin()
        if st.button("Save to Rx"):
            st.session_state.results.append(result) 

    elif drug == "cbromhex" or drug == "cbromhexine":
        result = cbromhex()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)    

    elif drug == "calcium" or drug == "calcium borogluconate" or drug == "dcm":
        result = dcm()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)    

    elif drug == "acepro" or drug == "acepromazine":
        result = acepro()
        if st.button("Save to Rx"):
            st.session_state.results.append(result) 

    elif drug == "comep" or drug == "comperazole" or drug == "omeprazole iv":
        result = comep()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)    

    elif drug == "jointrelief":
        result = jointrelief()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)     

    elif drug == "himpyrin":
        result = himpyrin()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)  

    elif drug == "digyton":
        result = digyton()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "otiderm":
        result = otiderm()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "otikoo" or drug == "otiko":
        result = otiko()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)     

    elif drug == "auriko":
        result = auriko()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)     

    elif drug == "otiplus":
        result = otiplus()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)     

    elif drug == "cl-ear cleanser" or drug == "ear cleanser" or drug == "cl ear cleanser" or drug == "cl cleanser" or drug == "cl" or drug == "cl ear" or drug == "cl-ear":
        result = clcleanser()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)     
   
    elif drug == "eye vita" or drug == "eye vitamin" or drug == "eye vitamin drops":
        result = eyevita()
        if st.button("Save to Rx"):
            st.session_state.results.append(result) 


    elif drug == "l-sametine" or drug == "l sametine" or drug == "lsametine":
        result = lsametine()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)   


    elif drug == "immuheal":
        result = immuheal()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)  
    
    elif drug == "finesteride" or drug == "finasteride":
        result = finasteride()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)  

    elif drug == "levo" or drug == "levothyroxine":
        result = levothyroxine()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)  
            
        
    elif drug == "coforta" or drug == "ib" or drug == "immune booster":
        result = coforta()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)  

    elif drug == "tobra" or drug == "tobramycin":
        result = tobra()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)  
    
    elif drug == "sodago" or drug == "tobrasodago":
        result = tobrasodago()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "cyclophosphamide" :
        result = cyclophosphamide()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "coatshine" :
        result = coatshine()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "activim" :
        result = activim()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
            
    elif drug == "cetirizine" :
        result = cet()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "lutein" or drug == "eye care" :
        result = lutein()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "metro" or drug == "metronidazole" :
        result = metro()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    
    elif drug == "doxo" or drug == "doxorubicin":
        result = doxo()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "lactulose":
        result = lactulose()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "bt" or drug == "blood transfusion" or drug == "blood trans":
        result = bt()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "hypromellose" or drug == "hypro":
        result = hypromellose()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "confis ultra" or drug == "confis":
        result = confis()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "potassium citrate":
        result = pc()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "lidocaine" or drug == "lidocaine cri" or drug == "lido"  or drug == "lido cri":
        result = lidocaine()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    
    elif drug == "galibor":
        result = galibor()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "tramadol":
        result = tramadol()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "mannitol":
        result = mannitol()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "pancreasolve":
        result = pancreasolve()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "calphos":
        result = calphos()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug in ["darbe" , "darbepoetin"]:
        result = darbe()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug in ["propocri" , "propo cri" , "propofol cri" , "profo cri" , "profopol cri"]:
        result = propocri()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug in ["carprofen" , "carpro" , "carodyl"]:
        result = carprofen()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "lisybin"  or  drug == "silybin":
        result = lisybin()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug == "orapet":
        result = orapet()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug in ["cepha" , "cefa" , "cephalexin" , "cefalexin"]:
        result = cepha()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    
    elif drug in ["clopridogel", "cloprido"]:
        result = clopridogel()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)

    elif drug in ["atenolol"]:
        result = atenolol()
        if st.button("Save to Rx"):
            st.session_state.results.append(result)
    
    else:
        st.write ("Refer to Drug Codex")

    st.write("Saved Medicines:")
    remove_index = None
    for i, item in enumerate(st.session_state.results):
        col1, col2 = st.columns([8, 1])
        with col1:
            st.write(f"{i+1}. {item}")
        with col2:
            if st.button("Remove", key=f"remove_{i}"):
                remove_index = i
    if remove_index is not None:
        st.session_state.results.pop(remove_index)

    
    if st.button("Generate Rx"):
        generate_pdf(st.session_state.results)
        with open(f"{patientname} Rx.pdf", "rb") as file:
            st.download_button("Download Prescription", file, file_name=f"{patientname} Rx.pdf")
            
    if st.button("Send Rx for printing"):
        filename = (f"{patientname} Rx.pdf")
        attachment = open(filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        msg.attach(part)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, "recipient_email@example.com", msg.as_string())
            


#int(round_half_up((weight * dsg / cons)*4)) / 4
def atenolol():
    if species in ["fel" , "feline" , "cat", "c"]:
        atenolol_dsg = st.selectbox(
                "Please choose dosage: ",
                ("6.25mg (common initial)" , "12.5mg"),
                index=None,
                placeholder="Select dosage...",
            )
        if atenolol_dsg == "6.25mg (common initial)":
            dsg = "1/4"
        else:
            dsg = "1/2"
        atenolol_freq = st.selectbox(
                "Please choose frequency: ",
                ("BID (preferred)" , "SID (for geriatric or those with mild HCM"),
                index=None,
                placeholder="Select frequency...",
            )
        if atenolol_freq == "BID (preferred)":
            freq = "twice a day"
        else:
            freq = "once a day"
        atenolol_print = (f"Atenolol 25mg: \nGive {dsg} tab {freq} as maintenance or as instructed: \nGive on an empty stomach. \n ")
    else:
        atenolol_print = ("Code for canine not yet included. Hehe. But 0.2 - 1mg/kg. Most likely for compounding.")
    st.write (atenolol_print)
    return atenolol_print


def clopridogel():
    if species in ["fel" , "feline" , "cat", "c"]:
        clopridoprint = ("Clopridogel 75mg: \nGive 1/4 tablet once a day as maintenance or as instructed: \n ")
    else:
        clopridodsg = st.number_input("Please choose Clopridogel dosage: 1 - 2 mg/kg")
        loadingdose = int(round_half_up((weight * clopridodsg / 75)*4)) / 4
        loadingdoseprint = (f"A loading dose of {loadingdose} tab (75mg) is recommended depending on the severity of the disease.")
        st.write (loadingdoseprint)
        give = int(round_half_up((weight * clopridodsg / 75)*4)) / 4
        if give == 0.25:
            tab = ("1/4")

        elif give == 0.5:
            tab = ("1/2")

        elif give == 0.75:
            tab = ("3/4")
    
        elif give == 1:
            tab = ("1")

        elif give == 1.25:
            tab = ("1 and 1/4")

        elif give == 1.5:
            tab = ("1 and 1/2")

        elif give == 1.75:
            tab = ("1 and 3/4")
    
        elif give == 2:
            tab = ("2")

        elif give == 2.25:
            tab = ("2 and 1/4")
    
        elif give == 2.5:
            tab = ("2 and 1/2")

        elif give == 2.75:
            tab = ("2 and 3/4")

        elif give == 3:
            tab = ("3")
        clopridoprint = (f"Clopridogel 75mg: \nGive {tab} once a day as maintenance or as intructed: \n ")
    st.write (clopridoprint)
    return clopridoprint
        
        

def cepha():
    cephadsg = st.number_input("Please choose Cephalexin dosage: 22 - 25mg/kg")
    cephagive = (weight * cephadsg / 50)
    cephaprint = (f"Cefalexin 250mg/5ml: \nGive {cephagive:.1f} twice a day for 14 days. \n ")
    st.write (cephaprint)
    return cephaprint

def orapet():
    oraprint = ("Orapet: \nPut 7 drops in a spoon or a syringe, then administer directly on the tongue. DO NOT give food and water for 30 minutes. \nShake well before use. \n ")
    st.write (oraprint)
    return oraprint

def lisybin():
    give = int(round_half_up((weight * 18 / 90)*4)) / 4
    if give == 0.25:
        tab = ("1/4")

    elif give == 0.5:
        tab = ("1/2")

    elif give == 0.75:
        tab = ("3/4")
    
    elif give == 1:
        tab = ("1")

    elif give == 1.25:
        tab = ("1 and 1/4")

    elif give == 1.5:
        tab = ("1 and 1/2")

    elif give == 1.75:
        tab = ("1 and 3/4")
    
    elif give == 2:
        tab = ("2")

    elif give == 2.25:
        tab = ("2 and 1/4")
    
    elif give == 2.5:
        tab = ("2 and 1/2")

    elif give == 2.75:
        tab = ("2 and 3/4")

    elif give == 3:
        tab = ("3")
    print = (f"SAMe and Silybin A+B (Lisybin): \nGive {tab} tab/s once a day for 14 days.  May be used as a supplement. \nGive on an empty stomach.\n ")
    st.write (print)
    return print

def carprofen():
    if species in ["canine", "dog" , "can"]:
        carprofen_dsg = st.selectbox(
                "Please choose dosage: ",
                ("2.2 mg/kg (BID)" , "4.4mg/kg (SID"),
                index=None,
                placeholder="Select dosage...",
            )
        if carprofen_dsg == "2.2 mg/kg (BID)":
            dsg = 2.2
            interval = "twice a day"
        else:
            dsg = 4.4
            interval = "once a day"
    else:
        dsg = 0.5
        interval = "once a day"
    carprofen_cons = st.selectbox(
            "Please choose concentration: ",
            ("25" , "100"),
            index=None,
            placeholder="Select concentration interval..",
        )
    if carprofen_cons == "25":
        cons = 25
    elif carprofen_cons == "100":
        cons = 100
    give = int(round_half_up((weight * dsg / cons)*4)) / 4
    if give == 0.25:
        tab = ("1/4")

    elif give == 0.5:
        tab = ("1/2")

    elif give == 0.75:
        tab = ("3/4")

    elif give == 1:
        tab = ("1")
    
    elif give == 2:
        tab = ("2")

    elif give == 1.25:
        tab = ("1 and 1/4")

    elif give == 1.5:
        tab = ("1 and 1/2")

    elif give == 1.75:
        tab = ("1 and 3/4")
    
    elif give == 2.25:
        tab = ("2 and 1/4")
    
    elif give == 2.5:
        tab = ("2 and 1/2")

    elif give == 2.75:
        tab = ("2 and 3/4")

    elif give == 3:
        tab = ("3")
    carprofenprint = (f"Carprofen (Carodyl) {carprofen_cons}mg: \nGive {tab} tab/s {interval} for 7 - 14 days.\n ")
    st.write (carprofenprint)
    return carprofenprint


def propocri():
    propo_first_give_range_1 = (weight * 1 / 10)
    propo_first_give_range_2 = (weight * 6 / 10)
    propo_cri_dsg = st.number_input("Please choose Profopol 10mg/ml CRI dosage: 0.1 - 0.6mg/kg/min")
    propo_cri = (weight * propo_cri_dsg / 10 * 60)
    propo_duration = st.number_input("Please choose duration of CRI : 6 - 12 hours. Up to 48 hours in dogs. \n\nFor cats, the CRI dose and duration should be short as possible.")
    propo_full_dose = (propo_cri * propo_duration)
    propo_duration = int(propo_duration)
    propo_instructions = (f"Propofol 10mg/ml for SEIZURES! \n\nGive {propo_first_give_range_1:.1f}ml up to {propo_first_give_range_2:.1f}ml SLOW IV TO EFFECT! \n\nPrepare {propo_full_dose:.2f}ml for CRI. \n\nSyringe pump/Infusion pump rate: {propo_cri:.1f}ml/hr.  Duration:{propo_duration} hours. \n\nDO NOT mix directly with fluid bottle.")
    st.write (propo_instructions)
    return propo_instructions
    
         

def darbe(): 
    if species in ["canine" , "can" , "dog"]:
        darbe_dosage = st.number_input("Please choose Darbepoetin dosage: 0.45 – 1.5 mcg/kg ")
        darbe_cons_chnge = st.text_input("Default concentration is 100mcg/ml (40mcg/0.4ml) \n\nChange concentration? (Yes or No)").lower()
        darbe_interval = st.selectbox(
            "Please choose dose interval. Recommendation: q7d until low end of target PCV range is reached. \nWhen target PCV is reached, dosing interval is extended as tolerated (eg, to every 2–3 wk)",
            ("every 7 days" , "every 2 weeks" , "every 3 weeks"),
            index=None,
            placeholder="Select dose interval..",
        )
        if darbe_cons_chnge == "yes":
            darbe_cons = st.number_input("Please provide available concentration: ___mcg/ml")
            darbegive = (darbe_dosage * weight / darbe_cons)
            darbe_cons = int(darbe_cons)
            darbeprint = (f"Darbepoetin alfa {darbe_cons}mcg/ml: \nInject {darbegive:.2f}ml SQ {darbe_interval}. \n ")
            st.write(darbeprint)
            return darbeprint
        else:
            darbegive = (darbe_dosage * weight / 100)
            darbeprint = (f"Darbepoetin alfa 40mcg/0.4ml (100mcg/ml): \nInject {darbegive:.2f}ml SQ {darbe_interval}. \n ")
            st.write(darbeprint)
            return darbeprint
    elif species in ["feline" , "fel" , "cat"]:
        darbe_dosage = st.number_input("Please choose Darbepoetin dosage: 0.7 – 1.8 mcg/kg ")
        darbe_cons_chnge = st.text_input("Default concentration is 100mcg/ml (40mcg/0.4ml) \n\nChange concentration? (Yes or No)").lower()
        darbe_interval = st.selectbox(
            "Please choose dose interval. Recommendation: q7d until low end of target PCV range is reached. \nWhen target PCV is reached, dosing interval is extended as tolerated (eg, to every 2–3 wk)",
            ("every 7 days" , "every 2 weeks" , "every 3 weeks"),
            index=None,
            placeholder="Select dose interval..",
        )
        if darbe_cons_chnge in ["yes" , "y"]:
            darbe_cons = st.number_input("Please provide available concentration: ___mcg/ml")
            darbegive = (darbe_dosage * weight / darbe_cons)
            darbe_cons = int(darbe_cons)
            darbeprint = (f"Darbepoetin alfa {darbe_cons}mcg/ml: \nInject {darbegive:.2f}ml SQ {darbe_interval}. \n ")
            st.write(darbeprint)
            return darbeprint
        else:
            darbegive = (darbe_dosage * weight / 100)
            darbeprint = (f"Darbepoetin alfa 40mcg/0.4ml: \nInject {darbegive:.2f}ml SQ {darbe_interval}. \n ")
            st.write(darbeprint)
            return darbeprint
            
    
def calphos():
    if weight < 9:
        give = ("Calphos D3: \n give 1/2 tab once a day for 14 days.\n ")
    else:
        give = ("Calphos D3: \n give 1 tab once a day for 14 days.\n ")
    st.write(give)
    return give
        
                    

def pancreasolve():
    if species in ["canine" , "dog" , "can"]:
        dsg = st.text_input("Please choose Pancreasolve dosage: 2 - 3 tablets before every meal")
    else:
        dsg = st.text_input("Please choose Pancreasolve dosage: 1/2 - 1 tablet before every meal")
    give = (f"Pancreasolve: \nGive {dsg} tablet/s 15 - 20 minutes before meals. Tablets can be given whole or crushed.\n ")
    st.write(give)
    return give

def mannitol():
    dsg = st.number_input("Please choose Mannitol dosage: 500  - 1500 mg/kg")
    cons = 200
    give = round(dsg * weight / cons)
    infusion_duration = st.number_input("Please choose duration of infusion: 10 - 30 minutes")
    infusion_duration = int(infusion_duration)
    if infusion_duration == 10:
        x = 6
    elif infusion_duration == 20:
        x = 3
    elif infusion_duration == 30:
        x = 2
    mannitol_fluid_rate = (give * x)
    mannitol_print = (f"Mannitol 20% (200mg/ml): Infuse {give} ml over {infusion_duration} minutes. \nINFUSION RATE: {mannitol_fluid_rate} ml/hr")
    st.write(mannitol_print)
    return mannitol_print

def tramadol():
    trama_dosage = st.number_input("Please choose Tramadol dosage: 4 - 10 mg/kg")
    trama_cons = 50
    give = weight * trama_dosage / trama_cons
    if give < 0.8:
        st.write ("Please choose a different drug or adjust the dosage if possible.")
    else:    
        give = round(give)
        interval = st.number_input("Please choose desired dosage interval: every 8 - 12 hours (General pain management) \n\nThe recommended interval for cancer-related pain is every 6 hours.")
        interval = int(interval)
        trama_print = (f"Tramadol 50mg \nGive {give} cap/s every {interval} hours for 7 - 14 days.\n ")
        st.write(trama_print)
        return trama_print
    

def lidocaine():
    if species == "dog" or species == "canine" or species == "can" or species == "c":
        firstgive = (weight / 20)
        fluidrate = st.number_input("Please indicate patient's current fluid rate: ")
        lido_dosage = st.number_input("Please choose Lidocaine CRI dosage: 1.2 - 3 mg/kg/hr")
        change_carrier = st.text_input("Change fluid carrier/bottle? (Yes or No) \n\nDefault fluid carrier is 1000ml.").lower()
        if change_carrier in ["yes" , "y"]:
            carrier = st.number_input("Please provide volume (ml): ")
            crigive = (lido_dosage * weight / fluidrate * carrier / 20)
            print = (f"Lidocaine 20mg/ml CRI: Give {firstgive:.2f} ml IV ONCE. \nRemove {crigive:.2f} ml from fluid bottle then add {crigive:.2f} ml of Lidocaine. \nFluid Rate: {fluidrate} ml/hr")
            st.write (print)  
            return print
        else:
            crigive = (lido_dosage * weight / fluidrate * 1000 / 20)
            print = (f"Lidocaine 20mg/ml CRI: Give {firstgive:.2f} ml IV ONCE. \nRemove {crigive:.2f} ml from fluid bottle (1000ml) then add {crigive:.2f} ml of Lidocaine. \nFluid Rate: {fluidrate} ml/hr")
            st.write (print)
            return print
    else:
        fluidrate = st.number_input("Please indicate patient's current fluid rate: ")
        crigive = (0.1 * weight / fluidrate * 1000 / 20)
        print = (f"Lidocaine 20mg/ml CRI: \nRemove {crigive:.2f} ml from fluid bottle then add {crigive:.2f} ml of Lidocaine. \nFluid Rate: {fluidrate} ml/hr \nUse with caution in cats (Lidocaine toxicity)")
        st.write (print)
        return print

    
def pc():
    dsg = st.number_input(f"Please choose Potassium citrate dosage: 25 - 50 mg/kg \n\nFor Urine alkalinization. \n ")
    checker = dsg * weight
    if checker >= 250:
        give =  int(round_half_up((weight * dsg / 1080)*4)) / 4
        if give == 0.25:
            tab = ("1/4")
    
        elif give == 0.5:
            tab = ("1/2")
    
        elif give == 0.75:
            tab = ("3/4")
    
        elif give == 1.25:
            tab = ("1 and 1/4")
        
        elif give == 1:
            tab = ("1")
    
        elif give == 1.5:
            tab = ("1 and 1/2")
    
        elif give == 1.75:
            tab = ("1 and 3/4")
    
        elif give == 2.25:
            tab = ("2 and 1/4")
        
        elif give == 2:
            tab = ("2")
    
        elif give == 2.5:
            tab = ("2 and 1/2")
    
        elif give == 2.75:
            tab = ("2 and 3/4")
        print = (f"Potassium citrate 1080mg: \nGive {tab} tab/s once a day for 30 days.\n ")
        
    else:
        compound = round(weight * dsg * 5) / 5
        compound = int(compound)
        tab_number = int(math.ceil(compound * 15 / 1080))
        print = (f"Potassium citrate 1080mg #{tab_number}: \nPlease compound into papertabs each with {compound}mg. Thank you!\nSig. Give 1 papertab (powder only) once a day for 15 days.")
    st.write (print)
    return print

def confis():
    if weight <= 5:
        print = (f"Confis ultra: \nGive 1/2 tab/s once a day as maintenance/supplement.\n ")
        st.write (print)
        return print
        
    elif weight <=10:
        x = 1
    elif weight <=20:
        x = 2
    elif weight <=35:
        x = 3
    print = (f"Confis ultra: \nGive {x} tab/s once a day as maintenance/supplement.\n ")
    st.write (print)
    return print
    

def bt():
    patient_pcv = st.number_input("Please indicate patient PCV or HCT:")
    target_pcv = st.number_input("Please indicate target PCV or HCT:")
    give = ((target_pcv - patient_pcv) / 40) * (weight * 90) 
    print = (f"BT: Patient needs {give} ml of blood. \n ")
    st.write (print)
    return print
    
def hypromellose():
    print = ("Hypromellose: \nApply 2 drops on affected eye/s 2 - 3 times a day for 14 days. May be continued as needed. \n ")
    st.write (print)
    return print

def lactulose():
    dsg = st.number_input("Please choose Lactulose dosage: 0.25 - \0.5 ml/kg")
    give = (dsg * weight)
    print = (f"Lactulose 3.35g/5ml: \nGive {give:.1f} ml orally every 3 - 4 hours. \n ")
    st.write (print)
    return print

def comep():
    dsg = st.number_input("Please choose Omeprazole dosage: 0.5 - 1 mg/kg")
    give = (dsg * weight / 40)
    print = (f"Omeprazole: {dsg:.2f} ml IV SID")
    st.write (print)
    return print

def lutein():
    if weight <= 15:
        print = ("Lutein Eye Care: \nMix 1 packet with food once a day as supplement. \n ")
    elif weight <= 35:
        print = ("Lutein Eye Care: \nMix 2 packets with food once a day as supplement. \n ")
    elif weight > 35:
        print = ("Lutein Eye Care: \nMix 3 packets with food once a day as supplement. \n ")
    st.write (print)
    return print

def cet():
    dsg = st.number_input("Please choose Cetirizine dosage: 1 - 2 mg/kg")
    cons = 1
    give = (weight * dsg / cons )
    print = (f"Cetirizine 5mg/5ml: \nGive {give:.1f} ml orally once a day as maintenance. \n ")
    st.write (print)
    return print

def activim():
    if weight <= 5:
        x = 1
    elif weight <=10:
        x = 2
    elif weight >10:
        x = 3
    print = (f"Activim: \nGive {x} inch/es approx. once a day as supplement.\n ")
    st.write (print)
    return print
    

def coatshine():
    if species == "dog" or species == "canine" or species == "can" or species == "c":
        give = (weight / 5)
    else:
        give = (weight / 3)
    print = (f"Coatshine: \nGive {give:.1f} ml once a day as supplement. \n ")
    st.write (print)
    return print
    

def cyclophosphamide():
    dsg = st.number_input("Please choose Cyclophosphamide dosage: 10 - 15 mg/m2")
    cons = 20
    give = (BSA * dsg / cons )
    print = (f"Cyclophosphamide 20mg/ml: \nGive {give:.2f} ml orally once a day as maintenance. \n ")
    st.write (print)
    return print

def tobra():
    print = ("Tobramycin Eye Drops: \nApply 2 drops on both/affected eyes twice a day for 14 days.\n ")
    st.write (print)
    return (print)

def tobrasodago():
    print = ("Tobramycin Eye Drops + Sodago (Stem Cells): \nApply 2 drops on both/affected eyes twice a day for 14 days.\n ")
    st.write (print)
    return (print)
    

def coforta():
    give = (weight / 10)
    print = (f"Coforta: {give:.2f}ml IV SID")
    st. write (print)
    return print
    
def levothyroxine():
    dsg = st.number_input("Please choose levothyroxine dosage: 0.01 - 0.02 mg/kg \nRecommended starting dosage: 0.02mg/kg")
    give =  int(round_half_up((weight * dsg / 0.6)*4)) / 4
    if give == 0.25:
        tab = ("1/4")

    elif give == 0.5:
        tab = ("1/2")

    elif give == 0.75:
        tab = ("3/4")

    elif give == 1.25:
        tab = ("1 and 1/4")
    
    elif give == 1:
        tab = ("1")

    elif give == 1.5:
        tab = ("1 and 1/2")

    elif give == 1.75:
        tab = ("1 and 3/4")

    elif give == 2.25:
        tab = ("2 and 1/4")
    
    elif give == 2:
        tab = ("2")

    elif give == 2.5:
        tab = ("2 and 1/2")

    elif give == 2.75:
        tab = ("2 and 3/4")
    print = (f"Levothyroxine 0.6mg: \nGive {tab} tab/s twice a day for 30 days.\n ")
    st.write (print)
    return print


def finasteride():
    dsg = st.number_input("Please choose finesteride dosage: 0.1 - 0.5 mg/kg")
    give =  int(round_half_up((weight * dsg / 5)*4)) / 4
    if give == 0.25:
        tab = ("1/4")

    elif give == 0.5:
        tab = ("1/2")

    elif give == 0.75:
        tab = ("3/4")

    elif give == 1.25:
        tab = ("1 and 1/4")

    elif give == 1:
        tab = ("1")

    elif give == 1.5:
        tab = ("1 and 1/2")

    elif give == 1.75:
        tab = ("1 and 3/4")

    elif give == 2:
        tab = ("2")

    elif give == 2.25:
        tab = ("2 and 1/4")

    elif give == 2.5:
        tab = ("2 and 1/2")

    elif give == 2.75:
        tab = ("2 and 3/4")
    print = (f"Finasteride 5mg: \nGive {tab} tab/s once a day for 30 days.\n ")
    st.write (print)
    return print

def immuheal():
    if weight <=  8:
        give = ("Immuheal: \nGive 2 ml twice a day as supplement.\n ")
        st.write (give)
    elif weight > 8:
        give = ("Immuheal: \nGive 3 ml twice a day as supplement.\n ")
        st.write (give)
    return give
   
        

def lsametine():
        give = (weight / 5)
        print = (f"L-Sametine: \nGive {give:.1f} ml twice a day as supplement.\n ")
        st.write (print)
        return print

def eyevita():
    if weight <= 3:
        print = ("Eye Vitamin Oral Drops: \Give 1/2 dropper (0.5ml) ORALLY twice a day for 7 - 14 days. \nMay be used aas maintenance.\n ")
    elif weight > 3:
        print = ("Eye Vitamin Oral Drops: \Give 1 dropper (1ml) ORALLY twice a day for 7 - 14 days. \nMay be used aas maintenance.\n ")
    st.write (print)
    return print

def clcleanser():
    print = ("CL-Ear Cleanser: \nApply liberally on affected ear/s twice a day for 7 - 14 days. Use 2 - 3x a week as maintenance. \nBest used before antibiotic ear drops. \n ")
    st.write (print)
    return print

def otiplus():
    print = ("OtiPLUS: \nApply 4 drops on affected ear/s twice a day for 7 - 14 days. Best if ears are cleaned prior.\n ")
    st.write (print)
    return print


def auriko():
    print = ("Auriko: \nApply 4 drops on affected ear/s twice a day for 7 - 14 days. Best if ears are cleaned prior.\n ")
    st.write (print)
    return print

def otiko():
    print = ("OtikOO: \nApply 4 drops on affected ear/s twice a day for 7 - 14 days. Best if ears are cleaned prior.\n ")
    st.write (print)
    return print

def otiderm():
    print = ("Otiderm: \nApply 4 drops on affected ear/s twice a day for 7 - 14 days. Best if ears are cleaned prior.\n ")
    st.write (print)
    return print

def himpyrin():
    if weight <= 8 or species == "cat" or species == "feline" or species == "fel":
        print = ("Himpyrin: \nGive 2ml twice a day for 7 - 14 days.\n ")
    elif weight > 8:
        print = ("Himpyrin: \nGive 3ml twice a day for 7 - 14 days.\n ")
    st.write (print)
    return print

def digyton():
    if species == "dog" or species == "canine" or species == "can" or species == "c":
        if weight <= 8:
            print = ("Digyton: \nGive 5ml twice a day for 7 - 14 days.\n ")
        elif weight > 8:
            print = ("Digyton: \nGive 10ml twice a day for 7 - 14 days.\n ")
    elif species == "cat" or species == "feline" or species == "fel":
            print = ("Digyton: \nGive 2.5ml twice a day for 7 - 14 days.\n ")
    st.write (print)
    return print


def jointrelief():
    if weight <= 5:
        give = ("Joint Relief: \nGive 1 tab once a day for 1 month, then give 1/2 tab once a day as maintenance.\n ")
        st.write (give)

    elif weight <= 10:
        give = ("Joint Relief: \nGive 2 tabs once a day for 1 month, then give 1 tab once a day as maintenance.\n ")
        st.write (give)

    elif weight < 40:
        give = ("Joint Relief: \nGive 4 tabs once a day for 1 month, then give 2 tabs once a day as maintenance.\n ")
        st.write (give)

    elif weight >= 40:
        give = ("Joint Relief: \nGive 8 tabs once a day for 1 month, then give 4 tabs once a day as maintenance.\n ")
        st.write (give)
    
    return give


def acepro():
    dsg = st.number_input("Acepromazine dosage: \n\n0.01 - 0.05 mg/kg (anesthetic protocol) \n\n"
           "0.5 - 2.2 mg/kg (sedation)")
    give = (weight * dsg / 5)
    print = (f"Acepromazine maleate 10mg/ml: {give:.2f}ml IV PRN")
    st.write (print)
    return print

def dcm():
    dsg = st.number_input("Calcium dosage: 5 - 15 mg/kg IV")
    give = (weight * dsg / 180)
    print = (f"DCM: {give:.2f}ml VERY SLOW IV PRN")
    st.write(print)
    return print

def cbromhex():
    give = (weight * 3 / 10)
    print (f"Bromhexine 10 IU: {give:.2f}ml IM BID")
    st.write(print)
    return print

def oxytocin():
    if species == "dog" or species == "canine" or species == "can" or species == "c":
        dsg = st.number_input("Oxy dosage: 0.5 - 2 IU / dose")
        give = (dsg / 10)
        print = (f"Oxytocin 10IU: {give:.2f}ml IM/SQ PRN")
    if species == "cat" or species == "feline" or species == "fel":
        dsg = st.number_input("Oxy dosage: 0.25 - 1 IU / dose")
        give = (dsg / 10)
        print = (f"Oxytocin 10IU: {give:.2f}ml IM/SQ PRN")
    st.write (print)
    return print

def atro():
        dsg = st.number_input("Dosage: 0.02 - 0.04 mg/kg")
        choose_cons = st.selectbox(
            "Please choose concentration available: ",
            ("1mg/ml" , "0.65mg/ml (Atrosite)"),
            index=None,
            placeholder="Select concentration...",
        )
        if choose_cons == "1mg/ml":
            cons = 1
        elif choose_cons == "0.65mg/ml (Atrosite)":
            cons = 0.65
        give = (weight * dsg / cons)
        if cons == 0.65:
            print = (f"Atropine {choose_cons}: {give:.2f}ml SQ/IM as ordered.")
        else:
            print = (f"Atropine {choose_cons}: {give:.2f}ml IV/IM as ordered.")
        st.write (print)
        return print

def actea():
    print = ("Actea: \nApply a thin layer on gums and teeth for 14 days. May be used as maintenance.\n ")
    st.write(print)
    return print

def profo():
    if species == "dog" or species == "canine" or species == "can" or species == "c":
        dsg = st.number_input("Please choose Propofol dosage: 2 - 6 mg/kg")
        give = (weight * dsg / 10)
        print = (f"Propofol 10mg/ml: {give:.2f}ml VERY SLOW IV - TITRATE TO EFFECT!")
        st.write (print)
        return print

    elif species == "cat" or species == "feline" or species == "fel":
        dsg = st.number_input("Please choose Propofol dosage: 4 - 8 mg/kg")
        give = (weight * dsg / 10)
        print = (f"Propofol 10mg/ml: {give:.2f}ml VERY SLOW IV - TITRATE TO EFFECT!")
        st.write (print)
        return print
    
    

def cleve():
    give = (weight * 20 / 100)
    print = (f"Leve: {give:.2f}ml IV TID")
    st.write (print)
    return print
           

def cmetro():
    dsg = st.number_input("Dosage? 5 - 25:")
    give = (weight * dsg / 5)
    print = (f"Metro: {give:.2f}ml IV BID")
    st.write (print)
    return print

def zole():
    if species == "dog" or species == "canine" or species == "can" or species == "c":
        dsg = st.number_input("Please choose Zoletil dosage: \n2.2 - 4.4 mg/kg")
        give = (weight * dsg / 50)
        max = (weight * 4.4 / 50)
        print = (f"Zoletil50: \nInject {give:.2f}ml IM/IV. \nDO NOT EXCEED {max}ml!")
    if species == "cat" or species == "feline" or species == "fel":
        dsg = st.number_input("Please choose Zoletil dosage: \n9.7 - 15.8 mg/kg")
        give = (weight * dsg / 50)
        max = (weight * 72 / 50)
        print = (f"Zoletil50: \nInject {give:.2f}ml IM/IV. \nDO NOT EXCEED A TOTAL OF {max}ml!")
    st.write (print)
    return print



def mupiro():
    print = ("Mupirocin: \nApply a thin layer on wound 2 - 3x a day for 14 days or until resolved. \n ")
    st.write (print)
    return print

def dermclens():
    print = ("Dermclens: \nSpray on affected area/s 2 - 3x a day for 14 days. Can be used as needed. \n ")
    st.write (print)
    return print

def soluneb():
    print =  ("Soluneb: \nUse 2 ml for nebulization 2 - 3 times a day for 14 days.\n ")
    st.write (print)
    return print

def thrombeat():
    give = (weight * 10 / 25)
    print = (f"Thromb Beat: \nGive {give:.1f}ml once a day for 14 days.\n ")
    st.write (print)
    return print 

def sangobion():
    give = (weight * 10 /30)
    if give < 1:
        st.write("Please choose a different brand. Thank you!")
    elif give >= 1:
        print = (f"Sangobion: \nGive {give:.0f} cap/s once a day for 14 days.\n ")
        st.write (print)
        return print



def bromhex():
    give = (weight * 2 / 0.8)
    print =  (f"Bromhexine 800mcg/ml: \nGive {give:.1f}ml twice a day for 7 days. \nThen give {give /2 :.1f}ml twicea day for 7 days.\n ")
    st.write (print)
    return print


def broncure():
    if weight < 9:
        print = ("BronCure: \nGive 3 ml twice a day for 7 days.\n ")
    if weight >= 9 and weight <=20:
        print = ("BronCure: \nGive 4 ml twice a day for 7 days.\n ")
    else:
        print = ("BronCure: \nGive 5 ml twice a day for 7 days.\n ")
    st. write (print)
    return print

def hemoglo():
    dsg = st.number_input("Please choose Ferrous sulfate dosage: 100 - 300 mg/dog")
    give = (dsg / 80)
    print = (f"Hemoglo-Aide Plus: \nGive {give:.1f}ml once a day for 14 days.\n ")
    st.write (print)
    return print


def hemacare():
    dsg = st.number_input("Please choose Ferrous sulfate dosage: 100 - 300 mg/dog")
    give = (dsg / 50)
    print = (f"Hemacare-Fe: \nGive {give}ml once a day for 14 days.\n ")
    st.write (print)
    return print



def activim():
    if weight <=5:
        print = ("Activim: \nGive about 1 inch once a day as supplement.\n ")
    elif weight <=10:
        print = ("Activim: \nGive about 2 inches once a day as supplement.\n ")
    elif weight > 10:
        print = ("Activim: \nGive about 3 inches once a day as supplement.\n ")
    st. write (print)
    return print



def cerenia():
    give = (weight / 10)
    print = (f"Cerenia: {give:.2f}ml SQ SID or PRN")
    st. write (print)
    return print


def filgrastim():
    dsg = st.number_input("Please choose Fligrastim dosage: 1 - 5 mcg/ml")
    give =  (weight * dsg / 600)
    print = (f"Filgrastim 300IU/0.5ml: \nInject {give:.2f}ml SQ SID for 3 - 5 days.\n ")
    st.write (print)
    return print

def cfilgrastim():
    give =  (weight * 5 / 600)
    print = (f"Filgrastim 300IU/0.5ml: \nInject {give:.2f}ml SQ SID for 5 days.\n ")
    st.write (print)
    return print
    

def cepo():
    give = (weight * 100 / 4000)
    print = (f"Epoetin alfa 4000IU/ml: \nInject {give:.2f}ml SQ three times a week as maintenance.")
    st.write (print)
    return print


def epo():
    dsg = st.number_input("Please choose Epoeitin alfa: 50 - 100 IU/kg")
    give =  (weight * dsg / 4000)
    print = (f"Epoetin alfa 4000IU/ml: \nInject {give:.2f}ml SQ three times a week as maintenance.\n ")
    st.write (print)
    return print


def orni():
    if weight < 5:
        print = ("Ornipural: Give 2 ml SLOW IV BID")
    elif weight <= 10:
        print = ("Ornipural: Give 3 ml SLOW IV BID")
    elif weight <= 15:
        print = ("Ornipural: Give 4 ml SLOW IV BID")
    else:
        print = ("Ornipural: Give 5 ml SLOW IV BID")
    st.write (print)
    return print

def fercob():
    give = (weight * 0.05)
    print = (f"Fercobsang: {give:.2f}ml \nPO SID")
    st. write (print)
    return print

    
def ctolfine():
    give = (weight / 10)
    print = (f"Tolfine: {give:.2f}ml IV SID")
    st. write (print)
    return print


def dupha():
    give = (weight * 1.5)
    print = (f"Dupha: {give:.2f}ml IV BID")
    st. write (print)
    return print


def confinetramadol():
    give = (weight / 10)
    freq = st.text_input("BID to TID?").lower()
    if freq == "bid":
        print = (f"Tramadol: {give:.2f}ml IV BID")
    elif freq == "tid":
        print = (f"Tramadol: {give:.2f}ml IV TID")
    st. write (print)
    return print

def confinedexa():
    give = (weight / 10)
    print = (f"Dexa: {give:.2f}ml \nIV SID for 7 days. \nThen {give / 2 :.2f}ml SID for 7 days.")
    st. write (print)
    return print

def confinemarbo():
    give = (weight / 10)
    print = (f"Marbo: {give:.2f}ml IV SID")
    st. write (print)
    return print


def confineampi():
    give = (weight / 10)
    print = (f"Ampi: {give:.2f}ml IV BID")
    st. write (print)
    return print

def cyclo():
    dsg = st.number_input("Please choose Cyclosporine dosage: 5 - 10 mg/kg")
    prep = st.text_input("Please choose preparation available: \nCAPSULE (50mg) or ORAL LIQUID (100mg/ml)").lower()
    if prep == "capsule" or prep == 50 or prep == "cap" or prep == "caps":
        cons = 50
        give = (weight * dsg / cons)
        if give < 1:
            print = ("Please choose a different preparation or lower dosage. Thank you!")
            st.write (print)
            return print
        else:
            print = (f"Cyclosporine 50mg capsule: \nGive {give} cap/s twice a day for 14 days. Give with or after meals.\n ")
            st.write (print)
            return print
    elif prep == "liquid":
        cons = 100
        give = (weight * dsg / cons)
        print = (f"Cyclosporine 100mg/ml: \nGive {give:.1f}ml twice a day for 14 days. Give with or after meals.\n ")
        st.write(print)
        return print




def leve():
    dsg = st.number_input("Please choose Levetiracetam dosage: 20 - 40 mg/kg \n(Recommended starting dose: 20mg/kg)")
    prep = st.text_input("Please choose preparation: Tablet or Oral Liquid").lower()
    if prep == "tab" or prep == "tablet" or prep == "tabs":
        cons = 500
        give = int(round_half_up((weight * dsg / cons)*4)) / 4
        if give == 0.25:
            tab = ("1/4")

        elif give == 0.5:
            tab = ("1/2")

        elif give == 0.75:
            tab = ("3/4")

        elif give == 1:
            tab = ("1")

        elif give == 1.25:
            tab = ("1 and 1/4")

        elif give == 1.5:
            tab = ("1 and 1/2")

        elif give == 1.75:
            tab = ("1 and 3/4")

        elif give == 2:
            tab = ("2")
    
        elif give == 2.25:
            tab = ("2 and 1/4")
    
        elif give == 2.5:
            tab = ("2 and 1/2")

        elif give == 2.75:
            tab = ("2 and 3/4")
        
        elif give == 3:
            tab = ("3")
        print = (f"Levetiracetam 500mg: \nGive {tab} tab/s every 8 hours as maintenance.\n ")

    else:
        cons = 100
        give = (weight * dsg /cons)
        print = (f"Levetiracetam 100ml/ml: \nGive {give:.1f}ml every 8 hours as maintenance.\n ")
    st.write(print)
    return print


def same():
    give = int(round_half_up((weight * 18 / 200)*4)) / 4
    if give == 0.25:
        tab = ("1/4")

    elif give == 0.5:
        tab = ("1/2")

    elif give == 0.75:
        tab = ("3/4")
    
    elif give == 1:
        tab = ("1")

    elif give == 1.25:
        tab = ("1 and 1/4")

    elif give == 1.5:
        tab = ("1 and 1/2")

    elif give == 1.75:
        tab = ("1 and 3/4")
    
    elif give == 2:
        tab = ("2")

    elif give == 2.25:
        tab = ("2 and 1/4")
    
    elif give == 2.5:
        tab = ("2 and 1/2")

    elif give == 2.75:
        tab = ("2 and 3/4")

    elif give == 3:
        tab = ("3")
    print = (f"SAMe: \nGive {tab} tab/s once a day for 14 days. \nGive on an empty stomach.\n ")
    st.write (print)
    return print

def cardiovet():
    if weight >=15:
        give = ("CardioVet: \nGive 2 tabs twice a day as maintenance.\n ")
    else:
        give = ("CardioVet: \nGive 1 tab twice a day as maintenance.\n ")
    st.write (give)
    return give
    


def alumag():
    dsg = st.number_input("Please choose Aluminum & Magnesium hydroxide dosage: \n10 - 30 mg/kg")
    give = (weight * dsg / 40)
    print = (f"Aluminum & Magnesium hydroxide 200mg/100mg/5ml: \nGive {give:.1f}ml before or with every meal for 14 days.\n ")
    st.write (print)
    return  print




def melox():
    dsg = (weight * 0.1 / 1.5)
    give = (f"Meloxicam 1.5mg/ml: \nDay 1: {dsg * 2 :.2f}ml once. \nThen give {dsg:.2f}ml once a day for 5 - 7 days.\n ")
    st.write (give)
    return give


            
def renalp():
    if weight <= 2.5:
        give = ("Renal P: Mix 1 small scoop with every meal as maintenance.\n ")
    elif weight < 10:
        dsg = (weight / 2.5)
        give = (f"Renal P: Mix {dsg} small scoop/s with every meal as maintenance.\n ")
    elif weight >= 10:
        dsg = (weight / 10)
        give = (f"Renal P: Mix {dsg:.0f} big scoop/s with every meal as maintenance.\n ")
    st.write (give)
    return give

def renaln():
    if weight <= 2.5:
        give = ("Renal N: Mix 1 small scoop with every meal as maintenance.\n ")
    elif weight < 10:
        dsg = (weight / 2.5)
        give = (f"Renal N: Mix {dsg:.0f} small scoop/s with every meal as maintenance.\n ")
    elif weight >= 10:
        dsg = (weight / 10)
        give = (f"Renal N: Mix {dsg:.0f} big scoop/s with every meal as maintenance.\n ")
    st.write (give)
    return give

def renalcombi():
    if weight <= 2.5:
        give = ("Renal Combi: Mix 1 small scoop with every meal as maintenance.\n ")
    elif weight < 10:
        dsg = (weight / 2.5)
        give = (f"Renal Combi: Mix {dsg:.0f} small scoop/s with every meal as maintenance.\n ")
    elif weight >= 10:
        dsg = (weight / 10)
        give = (f"Renal Combi: Mix {dsg:.0f} big scoop/s with every meal as maintenance.\n ")
    st.write (give)
    return give


def hepatiale():
    which_hepatiale = st.selectbox(
            "Hepatiale Forte: Liquid or Capsule?",
            ("Liquid" , "Capsule" ),
            index=None,
            placeholder="...",
        )
    if which_hepatiale == "Capsule":
        if weight <= 5:
            hepagive = ("Hepatiale Forte: \nGive 1 capsule once a day for 14 days. May be used as a supplement. \n ")
            st.write (hepagive)
            return hepagive
        else:
            hepa = round(1 * weight / 5)
            hepagive = (f"Hepatiale Forte: \nGive {hepa} capule/s once a day for 14 days. May be used as a supplement. \n ")
            st.write (hepagive)
            return hepagive  
    elif which_hepatiale == "Liquid":
        dsg = (weight * 5 / 10)
        hepagive = (f"Hepatiale Forte: \nGive {dsg:.1f}ml once a day for 14 days. May be used as a supplement. \n ")
        st.write (hepagive)
        return hepagive


def entero():
    if weight >=40:
        x = 8
    elif weight >=26:
        x = 6
    elif weight >= 11:
        x = 4
    else:
        x = 2
    enterogive = (f"EnteroProtek:\nGive {x}ml once to twice a day for 14 days. May be used as a supplement. \nGIVE ONLY ONCE A DAY if given with antibiotics.\n ")
    st.write (enterogive)
    return enterogive



def round_half_up(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier + 0.5) / multiplier

def generate_pdf(results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    
    # Add image as header
    image_path = "/mount/src/tfp_calc/tfplogo.png"
    pdf.image(image_path, x=10, y=8, w=180, h = 30)

    rx_path = "/mount/src/tfp_calc/rxsign.png"
    pdf.image(rx_path, x= 10, y=70, w=30, h = 30)

    
    pdf.ln(30)  # Move to the next line
    indent = 4  # Set the indentation level
    pdf.cell(indent)
    pdf.cell(80, 10, txt=f"Patient Name: {patientname}", ln =False, align='L')
    pdf.cell(100, 10, txt=f"    {datetime.now().strftime('%m-%d-%Y')}", ln=True, align="R") 
    pdf.cell(indent)
    pdf.cell(200, 10, txt=f"Species: {species}", ln=True, align='L')
    pdf.cell(indent)
    pdf.cell(200, 10, txt=f"Weight: {weight} kg", ln=True, align='L')

    # Adjust the y-coordinate for the text to start below the image
    pdf.set_y(100)
    
    for index, result in enumerate(results, start=1):
        pdf.multi_cell(200, 8, txt=f"({index}) {result}")
        pdf.ln(0.05)

    
    pdf.output(f"{patientname} Rx.pdf")
    


def gaba():
    dsg = st.number_input("Please choose Gabapentin dosage: 5 - 30 mg/mkg")
    cons = 100
    give = dsg * weight / cons
    gabaprint =  (f"Gabapentin 100mg: \nGive {give:.0f} cap/s once to thrice a day for 14 days.\n ")
    st.write (gabaprint)
    return gabaprint



def previcox():
    dsg = 5
    if weight < 11.35:
        cons = 57
    elif weight >= 11.35:
        cons = 227
    give = int(round_half_up((weight * dsg / cons)*4)) / 4
    if give == 0.25:
        tab = ("1/4")

    elif give == 0.5:
        tab = ("1/2")

    elif give == 0.75:
        tab = ("3/4")

    elif give == 1:
        tab = ("1")
    
    elif give == 2:
        tab = ("2")

    elif give == 1.25:
        tab = ("1 and 1/4")

    elif give == 1.5:
        tab = ("1 and 1/2")

    elif give == 1.75:
        tab = ("1 and 3/4")
    
    elif give == 2.25:
        tab = ("2 and 1/4")
    
    elif give == 2.5:
        tab = ("2 and 1/2")

    elif give == 2.75:
        tab = ("2 and 3/4")

    elif give == 3:
        tab = ("3")
    if cons == 57:
        previcoxprint = (f"Previcox 57mg: \nGive {tab} tab/s once a day for 7 - 14 days.\n ")
        st.write (previcoxprint)
    elif cons == 227:
        previcoxprint = (f"Previcox 227mg: \nGive {tab} tab/s once a day for 7 - 14 days.\n ")
        st.write (previcoxprint)
    return previcoxprint
    

def fluid():
    if weight <= 5:
        maintenancef = 60
    elif weight > 5 and weight <= 15:
        maintenancef = 50
    else :
        maintenancef = 40
    maintenancerate = maintenancef * weight
    dehydration = st.number_input("Please indicate dehydration percentage: ")
    dehydrationrate = dehydration * 10 * weight
    ongoinglosses = st.number_input("Pleae input volume (ml) of any ongoing losses: \n \n(vomiting, diarrhea, bleeding) \n")
    fluidrate = (maintenancerate + dehydrationrate + ongoinglosses) / 24
    printfluidrate = ((f"Fluid rate: {fluidrate:.1f} ml/hr"))
    st.write (printfluidrate)
    return printfluidrate
    

def vincristine():
    dsg = st.number_input("Please choose Vincristine dosage: 0.5 -  0.75 mg/m2")
    cons = 1
    give = (BSA * dsg / cons)
    print = (f"Vincristine 1mg: {give:.2f} ml IV once a week or according to chemo protocol.")
    st.write (print)
    return print

def doxo():
    if weight >= 15:
        give = (BSA * 30 / 2)
    elif weight < 15:
        give = (weight * 1 / 2)
    print = (f"Doxorubicin  2mg/ml: Mix {give:.2f} ml with 25 - 100ml of NSS. Then infuse IV for 15 - 20 mins. \nGive every three weeks or according to chemo protocol.")
    st.write (print)
    return print

def metro():
    dsg = st.number_input("Please choose Metronidazole dosage: 10 - 25 mg/kg")
    cons = 25
    give = (weight * dsg / cons)
    print = (f"Metronidazole 25mg/ml: \nGive {give:.1f} ml twice a day for 14 days.\n ")
    st.write(print)
    return print

def cotrimet():
    if species == "dog" or species == "canine":
        cotrimetdsg = st.number_input("Please choose COtrimoxazole dosage: 30 - 45mg/kg")
    else:
        cotrimetdsg = 15
    cotrimetcons = 20
    cotrimetgive  = (weight * cotrimetdsg / cotrimetcons)
    printcotrimet = (f"Cotrimoxazole + Metronidazole 20mg/ml: \nGive {cotrimetgive:.1f} ml twice a day for 14 days.\n ")
    st.write (printcotrimet)
    return printcotrimet


def bsa():
    st.write (f"BSA = {BSA:.3f}")
    return BSA

def cri():
    #choose drug then show dosage per hour?
    dsg_per_hr = st.number_input("Please indicate drug dosage per hour in mg: " , step=0.0001 , format="%.5f")
    fluidrate = st.number_input("Please indicate fluid rate in ml per hour: ")
    bottle_volume = st.number_input("Please indicate the volume of bottle or carrier: ")
    drugcons = st.number_input("Please indicate drug conentration in mg: ")
    crigive = (dsg_per_hr * weight / fluidrate * bottle_volume / drugcons)
    printcri = (f"Remove {crigive:.1f} ml from {bottle_volume} ml of carrier, then add {crigive:.1f} ml.")
    st.write (printcri)
    return printcri


def enro():
    enrocons = 20
    if species == "dog" or species == "canine":
        enrodsg = st.number_input("Please choose Enrofloxacin dosage: 5 - 20mg/kg")
        enrogive = (weight * enrodsg / enrocons)
        printenro = (f"Enrofloxacin 20mg/ml: \nGive {enrogive:.1f} ml once to twice a day for 14 days.\n ")
        st.write (printenro)
        return printenro

    elif species == "cat" or species == "feline":
        enrodsg = st.number_input("Please choose Enrofloxacin dosage: 2.5mg/kg(BID) or 5mg/kg(SID)")
        if enrodsg == 2.5:
            enrogive = (weight * enrodsg / enrocons)
            printenro = (f"Enrofloxacin 20mg/ml: \nGive {enrogive:.1f} ml twice a day for 14 days.\n ")
            st.write (printenro)
            return printenro
        else:
            enrogive = (weight * enrodsg / enrocons)
            printenro = (f"Enrofloxacin 20mg/ml: \nGive {enrogive:.1f} ml once a day for 14 days.\n ")
            st.write (printenro)
            return printenro
    
    

def spiro():
    spirodsg = 2
    spirocons = 25
    spirogive = int(round_half_up((weight * spirodsg / spirocons)*4)) / 4
    if spirogive == 0.25:
        tab = ("1/4")

    elif spirogive == 0.5:
        tab = ("1/2")

    elif spirogive == 0.75:
        tab = ("3/4")

    elif spirogive == 1:
        tab = ("1")

    elif spirogive == 1.25:
        tab = ("1 and 1/4")

    elif spirogive == 1.5:
        tab = ("1 and 1/2")

    elif spirogive == 1.75:
        tab = ("1 and 3/4")
    
    elif spirogive == 2:
        tab = ("3")

    elif spirogive == 2.25:
        tab = ("2 and 1/4")
    
    elif spirogive == 2.5:
        tab = ("2 and 1/2")

    elif spirogive == 2.75:
        tab = ("2 and 3/4")
    
    elif spirogive == 3:
        tab = ("3")
    spiros = (f"Spironolactone 25mg: \nGive {tab} tab/s once a day for 7-14 days.\n ")
    st.write (spiros)
    return spiros
    

def furo():
    furocons = st.number_input("Please choose concentration available: \n20 or 40mg")
    furodsg = st.number_input("Please choose Furosemide dosage: 2 - 4mg/kg")
    give = int(round_half_up((weight * furodsg / furocons)*4)) / 4
    if give == 0.25:
        tab = ("1/4")

    elif give == 0.5:
        tab = ("1/2")

    elif give == 0.75:
        tab = ("3/4")
    
    elif give == 1:
        tab = ("1")

    elif give == 1.25:
        tab = ("1 and 1/4")

    elif give == 1.5:
        tab = ("1 and 1/2")

    elif give == 1.75:
        tab = ("1 and 3/4")
    
    elif give == 2:
        tab = ("2")
    
    elif give == 2.25:
        tab = ("2 and 1/4")
    
    elif give == 2.5:
        tab = ("2 and 1/2")

    elif give == 2.75:
        tab = ("2 and 3/4")

    elif give == 3:
        tab = ("3")
    furoprint = (f"Furosemide {furocons}mg: \nGive {tab} tab/s twice to thrice a day for 7-14 days.\n ")
    st.write (furoprint)
    return furoprint

def galibor():
    ursodsg = st.number_input("Please choose Ursodiol dosage: 10 - 15mg/kg")
    ursocons = 25
    ursogive = (weight * ursodsg / ursocons)
    ursoprint = (f"Ursodeoxycholic Acid 125mg/5ml: \nGive {ursogive:.1f} ml once a day for 15 - 30 days.\n ")
    st.write (ursoprint)
    return ursoprint


def urso():
    ursodsg = st.number_input("Please choose Ursodiol dosage: 13 - 15mg/kg")
    ursocons = 300
    give = int(round_half_up((weight * ursodsg / ursocons)*4)) / 4
    if give == 0.25:
        tab = ("1/4")

    elif give == 0.5:
        tab = ("1/2")

    elif give == 0.75:
        tab = ("3/4")
    
    elif give == 1:
        tab = ("1")

    elif give == 1.25:
        tab = ("1 and 1/4")

    elif give == 1.5:
        tab = ("1 and 1/2")

    elif give == 1.75:
        tab = ("1 and 3/4")
    
    elif give == 2:
        tab = ("2")
    
    elif give == 2.25:
        tab = ("2 and 1/4")
    
    elif give == 2.5:
        tab = ("2 and 1/2")

    elif give == 2.75:
        tab = ("2 and 3/4")

    elif give == 3:
        tab = ("3")
    ursoprint = (f"Ursodiol 300mg: \nGive {tab} tab/s once to twice a day for 14 days.\n ")
    st.write (ursoprint)
    return ursoprint


def benazepryl():
    benazepryldsg = st.number_input("Please choose Benazepryl (Fortekor/Aceptor) dosage: 0.25 - 0.5mg/kg: ")
    benazeprylcons = 5
    benazeprylgive = int(round_half_up((weight * benazepryldsg / benazeprylcons)*4)) / 4
    if benazeprylgive == 0.25:
            tab = ("1/4")
                       
    elif benazeprylgive == 0.5:
        tab = ("1/2")

    elif benazeprylgive == 0.75:
        tab = ("3/4")

    elif benazeprylgive == 1:
        tab = ("1")

    elif benazeprylgive == 1.25:
        tab = ("1 and 1/4")

    elif benazeprylgive == 1.5:
        tab = ("1 and 1/2")

    elif benazeprylgive == 1.75:
        tab = ("1 and 3/4")

    elif benazeprylgive == 2:
        tab = ("2")

    elif benazeprylgive == 2.25:
        tab = ("2 and 1/4")

    elif benazeprylgive == 2.5:
        tab = ("1 and 1/2")
    
    elif benazeprylgive == 2.75:
        tab = ("1 and 3/4")
    
    elif benazeprylgive == 3:
        tab = ("3")

    benaprint = (f"Benazepryl HCl (Fortekor/Aceptor) 5mg: \nGive {tab} tab/s once to twice a day as maintenance.\n ")
    st.write (benaprint)
    return benaprint

def cefurox():
    cefuroxdsg = st.number_input("Please choose Cefuroxime axetil dosage: 10 - 20mg/kg: ")
    cefuroxcons = 50
    cefuroxgive = (weight * cefuroxdsg / cefuroxcons)
    cefuprint = (f"Cefuroxime axetil 250mg/5ml: \nGive {cefuroxgive:.1f} ml twice a day for 14 days.\n ")
    st.write (f"Cefuroxime axetil 250mg/5ml: \nGive {cefuroxgive:.1f} ml twice a day for 14 days.")
    return cefuprint


#GUI taking patient info
#coamoxiclav stuff
def pimo():
    pimodsg = st.number_input("Please choose Pimobendan dosage: 0.25 - 0.3mg/kg: " , key="pimodsg")
    pimogive_1 = (weight * pimodsg)
    if pimogive_1 < (2.3):
        pimocons = 1.25
        pimogive_2 = int(round_half_up((pimogive_1 / pimocons)*4)) / 4
        if pimogive_2 == 0.25:
            pimotab = ("1/4")
                       
        elif pimogive_2 == 0.5:
            pimotab = ("1/2")

        elif pimogive_2 == 0.75:
            pimotab = ("3/4")
        
        elif pimogive_2 == 1:
            pimotab = ("1")

        elif pimogive_2 == 1.25:
            pimotab = ("1 and 1/4")

        elif pimogive_2 == 1.5:
            pimotab = ("1 and 1/2")

        elif pimogive_2 == 1.75:
            pimotab = ("1 and 3/4")

        elif pimogive_2 == 2:
            pimotab = ("2")

        elif pimogive_2 == 2.25:
            pimotab = ("1 and 1/4")
        
        elif pimogive_2 == 2.5:
            pimotab = ("1 and 1/2")
        
        elif pimogive_2 == 2.75:
            pimotab = ("1 and 3/4")
        
        elif pimogive_2 == 3:
            pimotab = ("3")
            
        
        pimoprint = (f"Pimobendan 1.25mg: \nGive {pimotab} tab twice a day as maintenance. \n ")
        st.write (pimoprint)

    elif pimogive_1 >= (2.3) and pimogive_1 < (5):
        pimocons = 2.5
        pimogive_2 = int(round_half_up((pimogive_1 / pimocons)*4)) / 4
        if pimogive_2 == 0.25:
            pimotab = ("1/4")
                       
        elif pimogive_2 == 0.5:
            pimotab = ("1/2")

        elif pimogive_2 == 0.75:
            pimotab = ("3/4")
        
        elif pimogive_2 == 1:
            pimotab = ("1")

        elif pimogive_2 == 1.25:
            pimotab = ("1 and 1/4")

        elif pimogive_2 == 1.5:
            pimotab = ("1 and 1/2")

        elif pimogive_2 == 1.75:
            pimotab = ("1 and 3/4")

        elif pimogive_2 == 2:
            pimotab = ("2")

        elif pimogive_2 == 2.25:
            pimotab = ("1 and 1/4")
        
        elif pimogive_2 == 2.5:
            pimotab = ("1 and 1/2")
        
        elif pimogive_2 == 2.75:
            pimotab = ("1 and 3/4")
        
        elif pimogive_2 == 3:
            pimotab = ("3")

        st.write (f"Pimobendan 2.5mg: \nGive {pimotab} tab twice a day as maintenance. \n ")
        pimoprint = (f"Pimobendan 2.5mg: \nGive {pimotab} tab twice a day as maintenance.\n ")

    elif pimogive_1 >= (5) and pimogive_1 < (10):
        pimocons = 5
        pimogive_2 = int(round_half_up((pimogive_1 / pimocons)*4)) / 4
        if pimogive_2 == 0.25:
            pimotab = ("1/4")
                       
        elif pimogive_2 == 0.5:
            pimotab = ("1/2")

        elif pimogive_2 == 0.75:
            pimotab = ("3/4")
        
        elif pimogive_2 == 1:
            pimotab = ("1")

        elif pimogive_2 == 1.25:
            pimotab = ("1 and 1/4")

        elif pimogive_2 == 1.5:
            pimotab = ("1 and 1/2")

        elif pimogive_2 == 1.75:
            pimotab = ("1 and 3/4")

        elif pimogive_2 == 2:
            pimotab = ("2")

        elif pimogive_2 == 2.25:
            pimotab = ("1 and 1/4")
        
        elif pimogive_2 == 2.5:
            pimotab = ("1 and 1/2")
        
        elif pimogive_2 == 2.75:
            pimotab = ("1 and 3/4")
        
        elif pimogive_2 == 3:
            pimotab = ("3")
        pimoprint = (f"Pimobendan 5mg: \nGive {pimotab} tab twice a day as maintenance. \n ")
        st.write (pimoprint)


    elif pimogive_1 >= (10):
        pimocons = 10
        pimogive_2 = int(round_half_up((pimogive_1 / pimocons)*4)) / 4
        if pimogive_2 == 0.25:
            pimotab = ("1/4")
                       
        elif pimogive_2 == 0.5:
            pimotab = ("1/2")

        elif pimogive_2 == 0.75:
            pimotab = ("3/4")
        
        elif pimogive_2 == 1:
            pimotab = ("1")

        elif pimogive_2 == 1.25:
            pimotab = ("1 and 1/4")

        elif pimogive_2 == 1.5:
            pimotab = ("1 and 1/2")

        elif pimogive_2 == 1.75:
            pimotab = ("1 and 3/4")

        elif pimogive_2 == 2:
            pimotab = ("2")

        elif pimogive_2 == 2.25:
            pimotab = ("1 and 1/4")
        
        elif pimogive_2 == 2.5:
            pimotab = ("1 and 1/2")
        
        elif pimogive_2 == 2.75:
            pimotab = ("1 and 3/4")
        
        elif pimogive_2 == 3:
            pimotab = ("3")
        pimoprint = (f"Pimobendan 10mg: \nGive {pimotab} tab twice as maintenance.\n ")
        st.write (pimoprint)

    return pimoprint


def retromad():
    if species == "feline" or species == "cat":
        retromad_dz = st.text_input("Enter Disease: \n\nFeLV \nFIV \n\nFPV \nFCV \n\nFIP \nFHV\n").strip().lower()
        if retromad_dz == "felv" or retromad_dz == "fiv" :
            retromaddsg = 0.3
            retromadgive = (retromaddsg * weight)
            st.write (f"RetroMad1: \nInject {(retromadgive / 2):.1f} ml SQ every 8 hours for 90 days. \nOr give {retromadgive:.1f} ml orally every 8 hours for 90 days.\n ")
            retroprint = (f"RetroMad1: \nInject {(retromadgive / 2):.1f} ml SQ every 8 hours for 90 days. \nOr give {retromadgive:.1f} ml orally every 8 hours for 90 days.\n ")
            return retroprint

        elif retromad_dz == "fip" or retromad_dz == "fpv" or retromad_dz == "fcov" or retromad_dz == "corona" or retromad_dz == "parvo"  :
            retromaddsg = 0.5
            retromadgive = (retromaddsg * weight)
            if retromad_dz == "fip" or retromad_dz == "fcov" or retromad_dz == "corona" :
                st.write (f"RetroMad1: \nInject {retromadgive:.1f} ml SQ every 8 hours for 40 days.\n ")
                retroprint = (f"RetroMad1: \nInject {retromadgive:.1f} ml SQ every 8 hours for 40 days.\n ")
                return retroprint

            elif retromad_dz == "fpv" or retromad_dz == "parvo" :
                st.write (f"RetroMad1: \nInject {retromadgive:.1f} ml SQ every 8 hours for 10 days.\n ")
                retroprint = (f"RetroMad1: \nInject {retromadgive:.1f} ml SQ every 8 hours for 10 days.\n ")
                return retroprint
            

        elif retromad_dz == "fhv" or retromad_dz == "herpes" or retromad_dz == "fcv" :
            retromaddsg = 0.5
            retromadgive = (retromaddsg * weight)
            st.write (f"RetroMad1: \nInject {(retromadgive / 2):.1f} ml SQ every 8 hours for 10 - 20 days. \nOr give {retromadgive:.1f} ml orally every 8 hours for 10 -20 days.\n ")
            retroprint = (f"RetroMad1: \nInject {(retromadgive / 2):.1f} ml SQ every 8 hours for 10 - 20 days. \nOr give {retromadgive:.1f} ml orally every 8 hours for 10 -20 days.\n ")
            return retroprint

    elif species == "canine" or species == "dog":
        retromad_dz = st.text_input("Enter Disease: \n\nCDV \n\nCPV \n\n").strip().lower()
        if retromad_dz == "cdv" or retromad_dz == "distemper" :
            retromaddsg = 0.5
            retromadgive = (retromaddsg * weight)
            st.write (f"RetroMad1: \nInject {(retromadgive / 2):.1f} ml SQ every 8 hours for 15 days. \n\Or give {retromadgive:.1f} ml orally every 8 hours for 15 days.\n ")
            retroprint = (f"RetroMad1: \nInject {(retromadgive / 2):.1f} ml SQ every 8 hours for 15 days. \n\Or give {retromadgive:.1f} ml orally every 8 hours for 15 days.\n ")
            return retroprint

        elif retromad_dz == "cpv" or retromad_dz == "parvo" :
            retromaddsg = 0.5
            retromadgive = (retromaddsg * weight)
            st.write (f"RetroMad1: \nInject {retromadgive:.1f} ml SQ every 8 hours for 10 days.\n ")
            retroprint = (f"RetroMad1: \nInject {retromadgive:.1f} ml SQ every 8 hours for 10 days.\n ")
            return retroprint


def gs():
    gsdsg = st.number_input("Please choose GS dosage: \n6mg/kg (Wet and Dry FIP) \n10mg/kg (Neurological and Ocular)")
    gscons = 20
    gsgive = (weight * gsdsg / gscons)
    gsprint = (f"GS: \nInject {gsgive:.1f} ml SQ once a day for 84 days.\n ")
    st.write (gsprint)
    return gsprint



def cotri():
    if species == "dog" or species == "canine":
        cotridsg = st.number_input("Please choose dosage: 30 - 45mg/kg")
    else:
        cotridsg = 15
    cotricons = 40
    cotrigive  = (weight * cotridsg / cotricons)
    st.write (f"Cotrimoxazole 20mg/ml: \nGive {cotrigive:.1f} ml twice a day for 14 days.\n ")
    cotriprint = (f"Cotrimoxazole 20mg/ml: \nGive {cotrigive:.1f} ml twice a day for 14 days.\n ")
    return cotriprint


def itra():
    itradsg = st.number_input("Please choose Itraconazole dosage: 5 -10mg/kg: ")
    itracons = 100
    itragive = int(round_half_up((weight * itradsg / itracons)*4)) / 4
    st.write (f"Itraconazole 100mg: \nGive {itragive} tab/s once to twice a day for 14 days.\n ")
    itraprint = (f"Itraconazole 100mg: \nGive {itragive} tab/s once to twice a day for 14 days.\n ")
    return itraprint


def coamox():
    coamoxdsg = st.number_input("Please choose Co-amoxiclav dosage: 15 - 20mg/kg: ")
    coamoxcons = 62.5
    coamoxgive = (weight * coamoxdsg / coamoxcons)
    drugprintcoamox = (f"Co-amoxiclav 312.5mg/5ml: \nGive {coamoxgive:.1f} ml twice a day for 14 days.\n ")
    st.write(drugprintcoamox)
    return drugprintcoamox
    

#if coamox_count == "1"
#st.write(copy_coamox)




#copy the written prescription (done?)
#paste the written prescription in a different zone


#pred stuff
def pred():
    preddsg = st.number_input("Please choose Prednisone dosage: 0.5 - 1 mg/kg: ")
    predcons = st.number_input("Please choose Prednisone concentration: \n\n2mg/ml (10mg/5ml LIQUID)\n\n 5mg (TABLET)\n\n10mg (TABLET)\n\nPlease input NUMBERS ONLY")
    if predcons == 2:
        predgive = (weight * preddsg / predcons)
        drugprintpred = (f"Prednisone 10mg/5ml: \nGive {predgive:.1f} ml twice a day for 5 days. Then give {((predgive) / 2):.1f} ml once a day for another 5 days. \n ") 
    elif predcons == 5:
        predgive = int(round_half_up((weight * preddsg / predcons)*4)) / 4
        if predgive == 0.25:
            tab = ("1/4")
                            
        elif predgive == 0.5:
            tab = ("1/2")

        elif predgive == 0.75:
            tab = ("3/4")
        
        elif predgive == 1:
            tab = ("1")

        elif predgive == 1.25:
            tab = ("1 and 1/4")

        elif predgive == 1.5:
            tab = ("1 and 1/2")

        elif predgive == 1.75:
            tab = ("1 and 3/4")
        
        elif predgive == 1.75:
            tab = ("1 and 3/4")
        
        elif predgive == 2:
            tab = ("2")
        
        elif predgive == 2.25:
            tab = ("2 and 1/4")
        
        elif predgive == 2.5:
            tab = ("2 and 1/2")
        
        elif predgive == 2.75:
            tab = ("2 and 3/4")

        elif predgive == 3:
            tab = ("3")
        drugprintpred = (f"Prednisone 5mg: \nGive {tab} tab/s twice a day for 5 days. Then give {tab} tab/s once a day for another 5 days. \n ") 
    elif predcons == 10:
        predgive = int(round_half_up((weight * preddsg / predcons)*4)) / 4
        if predgive == 0.25:
            tab = ("1/4")
                            
        elif predgive == 0.5:
            tab = ("1/2")

        elif predgive == 0.75:
            tab = ("3/4")
        
        elif predgive == 1:
            tab = ("1")

        elif predgive == 1.25:
            tab = ("1 and 1/4")

        elif predgive == 1.5:
            tab = ("1 and 1/2")

        elif predgive == 1.75:
            tab = ("1 and 3/4")
        
        elif predgive == 1.75:
            tab = ("1 and 3/4")
        
        elif predgive == 2:
            tab = ("2")
        
        elif predgive == 2.25:
            tab = ("2 and 1/4")
        
        elif predgive == 2.5:
            tab = ("2 and 1/2")
        
        elif predgive == 2.75:
            tab = ("2 and 3/4")

        elif predgive == 3:
            tab = ("3")
        drugprintpred = (f"Prednisone 10mg: \nGive {tab} tab/s twice a day for 5 days. Then give {tab} tab/s once a day for another 5 days. \n ")
    st.write (drugprintpred)
    return drugprintpred
    

def prednisolone():
    prednisolonedsg = st.number_input("Please choose Prednisone dosage: 0.5 - 1 mg/kg: ")
    prednisolonecons = 3
    prednisolonegive = (weight * prednisolonedsg / prednisolonecons)
    st.write (f"Prednisolone 15mg/5ml: \nGive {prednisolonegive:.1f} ml twice a day for 5 days. \nThen give {((prednisolonegive) / 2):.1f} ml once a day for another 5 days.\n ")
    prednisoloneprint = (f"Prednisolone 15mg/5ml: \nGive {prednisolonegive:.1f} ml twice a day for 5 days. \nThen give {((prednisolonegive) / 2):.1f} ml once a day for another 5 days.\n ")
    return prednisoloneprint


    
#doxy stuff
def doxy():
    doxydsg = st.number_input("Please choose Doxycycline dosage: 5mg/kg(BID) or 10mg/kg(SID)")
    doxycons =  20
    doxygive = (weight * doxydsg / doxycons)
    if doxydsg == 5:
        drugprintdoxy = (f"Doxcycline 100mg/5ml: \nGive {doxygive:.1f} ml twice a day for 14 days.\n ")
        st.write (drugprintdoxy)
        return drugprintdoxy
    
    else:
        drugprintdoxy = (f"Doxcycline 100mg/5ml: \nGive {doxygive:.1f} ml once a day for 14 days.\n ")
        st.write (drugprintdoxy)
        return drugprintdoxy
    

    
def doxyko():
    doxykodsg = 5
    doxykocons =  100
    doxykogive = int(round_half_up((weight * doxykodsg / doxykocons)*4)) / 4
    if doxykogive == 0.25:
        tab = ("1/4")
                        
    elif doxykogive == 0.5:
        tab = ("1/2")

    elif doxykogive == 0.75:
        tab = ("3/4")
    
    elif doxykogive == 1:
        tab = ("1")

    elif doxykogive == 1.25:
        tab = ("1 and 1/4")

    elif doxykogive == 1.5:
        tab = ("1 and 1/2")

    elif doxykogive == 1.75:
        tab = ("1 and 3/4")
    
    elif doxykogive == 1.75:
        tab = ("1 and 3/4")
    
    elif doxykogive == 2:
        tab = ("2")
    
    elif doxykogive == 2.25:
        tab = ("2 and 1/4")
    
    elif doxykogive == 2.5:
        tab = ("2 and 1/2")
    
    elif doxykogive == 2.75:
        tab = ("2 and 3/4")

    elif doxykogive == 3:
        tab = ("3")

    st.write (f"Doxcycline 100mg: \nGive {tab} tab/s twice a day for 14 days. OR give {((doxykogive) * 2)} tab/s once a day for 14 days. \nSPACE 4 - 6 hours between iron supplements.\n ")
    doxykoprint = (f"Doxcycline 100mg: \nGive {tab} tab/s twice a day for 14 days. OR give {((doxykogive) * 2)} tab/s once a day for 14 days. \nSPACE 4 - 6 hours between iron supplements.\n ")
    return doxykoprint


#clindastuff
def clinda():
    clindadsg = st.number_input("Please choose Clindamycin dosage: 10 - 15 mg/kg: ")
    clindacons = st.text_input("Please choose available Clindamycin preparation of choice: \n55mg/ml(LIQUID) or 150mg(TABLET)").lower()
    if clindacons == "55" or clindacons == "liq" or clindacons == "liquid" :
        cons = 55
        clindagive = (weight * clindadsg / cons)
        st.write (f"Clindamycin 55mg/ml: \nGive {clindagive:.1f} ml once to twice a day for 14 days.\n ")
        clindaprint = (f"Clindamycin 55mg/ml: \nGive {clindagive:.1f} ml once to twice a day for 14 days.\n ")
    else:
        cons = 150
        clinda150give = int(round_half_up((weight * clindadsg / cons)*4)) / 4
        st.write (f"Clindamycin 150mg: \nGive {clinda150give} tab/s 2 -3x a day for 7 - 14 days.\n ")
        clindaprint = (f"Clindamycin 150mg: \nGive {clinda150give} tab/s 2 -3x a day for 7 - 14 days.\n ")
    return clindaprint



#marbo stuff
def marbo():
    marbodsg = st.number_input("Please choose Marbofloxacin dosage: 2.75 - 5.5 mg/kg: ")
    marbocons = st.number_input("Please choose concentration available of your choice: \n25mg or 50mg")
    give = int(round_half_up((weight * marbodsg / marbocons)*4)) / 4
    if give == 0.25:
        tab = ("1/4")

    elif give == 0.5:
        tab = ("1/2")

    elif give == 0.75:
        tab = ("3/4")
    
    elif give == 1:
        tab = ("1")

    elif give == 1.25:
        tab = ("1 and 1/4")

    elif give == 1.5:
        tab = ("1 and 1/2")

    elif give == 1.75:
        tab = ("1 and 3/4")
    
    elif give == 2:
        tab = ("2")
    
    elif give == 2.25:
        tab = ("2 and 1/4")
    
    elif give == 2.5:
        tab = ("2 and 1/2")

    elif give == 2.75:
        tab = ("2 and 3/4")

    elif give == 3:
        tab = ("3")
    st.write (f"Marbofloxcacin {marbocons:.0f}mg: \nGive {tab} tab/s once a day for 7 - 14 days.\n ")
    marboprint = (f"Marbofloxcacin {marbocons:.0f}mg: \nGive {tab} tab/s once a day for 7 - 14 days.\n ")
    return marboprint

#maropitant stuff
def maropitant():
    maropitantdsg = 2
    maropitantcons = st.number_input("Please choose concentration available of your choice: \n24 or 60mg")
    maropitantgive = int(round_half_up((weight * maropitantdsg / maropitantcons)*4)) / 4
    if maropitantgive == 0.25:
        tab = ("1/4")
                        
    elif maropitantgive == 0.5:
        tab = ("1/2")

    elif maropitantgive == 0.75:
        tab = ("3/4")
    
    elif maropitantgive == 1:
        tab = ("1")

    elif maropitantgive == 1.25:
        tab = ("1 and 1/4")

    elif maropitantgive == 1.5:
        tab = ("1 and 1/2")

    elif maropitantgive == 1.75:
        tab = ("1 and 3/4")
    
    elif maropitantgive == 2:
        tab = ("2")
    
    elif maropitantgive == 2.25:
        tab = ("2 and 1/4")

    elif maropitantgive == 2.5:
        tab = ("2 and 1/2")

    elif maropitantgive == 2.75:
        tab = ("2 and 3/4")
    
    elif maropitantgive == 3:
        tab = ("3")
    
    st.write (f"Maropitant {maropitantcons:.0f}mg: \nGive {tab} tab/s once a day for 14 days.\n ")
    maropitantprint = (f"Maropitant {maropitantcons:.0f}mg: \nGive {tab} tab/s once a day for 14 days.\n ")
    return maropitantprint



if __name__ == "__main__":
    main()


# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
# if uploaded_file is not None:
#     Save the uploaded file to a temporary location
# '''
# file_extension = uploaded_file.name.split('.')[-1]
# temp_file_path = f"temp_image.{file_extension}"

# with open(temp_file_path, "wb") as f:
#     f.write(uploaded_file.getbuffer())

# # Print the file path to verify
# print(f"File saved to: {temp_file_path}")

# # Generate PDF with the uploaded image
# results = ["Sample result 1", "Sample result 2"]
# generate_pdf(results, temp_file_path)
# st.success("PDF generated successfully!")

# #Print the file path to verify
# print(f"File saved to: {temp_file_path}")
# print(f"File exists: {os.path.exists(temp_file_path)}")
# '''

