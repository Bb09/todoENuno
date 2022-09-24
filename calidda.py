import json
from config import *
import requests
import json


###########################################################################################
#API - CALIDDA PISO1:
urlpiso1="https://appadmin.calidda.com.pe/BackOV/api/Bill/ListPendingBill?clientCode=949109"
apipiso1 = requests.get(urlpiso1)
json_piso1 = json.loads(apipiso1.content)
lista1=json_piso1["data"]
long_lista1=bool(lista1)
###########################################################################################
#API - CALIDDA PISO1:
urlpiso2="https://appadmin.calidda.com.pe/BackOV/api/Bill/ListPendingBill?clientCode=949110"
apipiso2 = requests.get(urlpiso2)
json_piso2 = json.loads(apipiso2.content)
lista2=json_piso2["data"]
long_lista2=bool(lista2)
#print(long_lista2)
###########################################################################################
#API - CALIDDA LT 34:
urlpiso3="https://appadmin.calidda.com.pe/BackOV/api/Bill/ListPendingBill?clientCode=951690"
apipiso3 = requests.get(urlpiso3)
json_piso3 = json.loads(apipiso3.content)
lista3=json_piso3["data"]
long_lista3=bool(lista3)

################################################################################################################################
try:

    id=json_piso1["data"][0]["id"]                  #piso1
    codigo1=json_piso1["data"][0]["clientCode"]     #piso1
    cliente1=json_piso1["data"][0]["clientName"]       #piso1
    numDoc1=json_piso1["data"][0]["numberDocument"]     #piso1
    vencimiento1=json_piso1["data"][0]["dueDate"].replace('T00:00:00','')       #piso1
    emision1=json_piso1["data"][0]["issueDate"].replace('T00:00:00','')     #piso1
    monto=float(json_piso1["data"][0]["pendingDebt"])       #piso1

    mensaje1=(f"🔷🔷PISO 1🔷🔷\nCódigo de Cliente: {codigo1}\nCliente: {cliente1}\nNumero de Recibo :{numDoc1}\nFecha de Emision : {emision1}\nFecha de Vencimiento: {vencimiento1}\nMonto a Pagar: S/.{monto}")
####################################################################################
    id2=json_piso2["data"][0]["id"]#piso 2
    codigo2=json_piso2["data"][0]["clientCode"]#piso 2
    cliente2=json_piso2["data"][0]["clientName"]#piso 2
    numDoc2=json_piso2["data"][0]["numberDocument"]#piso 2
    vencimiento2=json_piso2["data"][0]["dueDate"].replace('T00:00:00','')#piso 2
    emision2=json_piso2["data"][0]["issueDate"].replace('T00:00:00','')#piso 2
    monto2=float(json_piso2["data"][0]["pendingDebt"])#piso 2
    mensaje2=(f"🔷🔷PISO 2🔷🔷\nCódigo de Cliente: {codigo2}\nCliente: {cliente2}\nNumero de Recibo :{numDoc2}\nFecha de Emision : {emision2}\nFecha de Vencimiento: {vencimiento2}\nMonto a Pagar: S/.{monto2}")
####################################################################################
    id3=json_piso3["data"][0]["id"]#piso3
    codigo3=json_piso3["data"][0]["clientCode"]#piso3
    cliente3=json_piso3["data"][0]["clientName"]#piso3
    numDoc3=json_piso3["data"][0]["numberDocument"]#piso3
    vencimiento3=json_piso3["data"][0]["dueDate"].replace('T00:00:00','')#piso3
    emision3=json_piso3["data"][0]["issueDate"].replace('T00:00:00','')#piso3
    monto3=float(json_piso3["data"][0]["pendingDebt"])#piso3
    mensaje3=(f"🔷🔷LT.34🔷🔷\nCódigo de Cliente: {codigo3}\nCliente: {cliente3}\nNumero de Recibo :{numDoc3}\nFecha de Emision : {emision3}\nFecha de Vencimiento: {vencimiento3}\nMonto a Pagar: S/.{monto3}")
    msgcalidda=(f"RECIBOS CALIDDA\n\n{mensaje1}\n\n{mensaje2}\n\n{mensaje3}")
###################################################################################    
except:
    msgcalidda=(f"RECIBOS CALIDDA\n\n🔥RECIBO PAPA PISO 1: Está al dia, no hay facturacion\n\n🔥RECIBO PAPA PISO 2: Está al dia, no hay facturacion\n\n🔥RECIBO LT.34: Está al dia, no hay facturacion\n")

