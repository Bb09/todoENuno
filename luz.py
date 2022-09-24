from config import *
import requests
import json
###########################################################################################
#API - RECIBO DE LUZ LT.37:
urlluz1="https://www.enel.pe/es/personas/consulta-ultimo-recibo-deluz.mdwedgeohl.getHistoricalInvoices.html?supplyCode=1166519&company=0"
apiluz1 = requests.get(urlluz1)
json_luz1 = json.loads(apiluz1.content)
###########################################################################################
#API - RECIBO DE LUZ LT.34:
urlluz2 = "https://www.enel.pe/es/personas/consulta-ultimo-recibo-deluz.mdwedgeohl.getHistoricalInvoices.html?supplyCode=1872952&company=0"
apiluz2 = requests.get(urlluz2)
json_luz2 = json.loads(apiluz2.content)
###########################################################################################
#VALORES DE RECIBO DE LUZ
###########################################################################################
#LT.37
numluz1=json_luz1["invoiceList"][0]["invoiceNumber"]
expluz1=json_luz1["invoiceList"][0]["expiryDate"]
emisionluz1=json_luz1["invoiceList"][0]["issueDate"]
montoluz1=json_luz1["invoiceList"][0]["amount"]
pdfluz1=json_luz1["invoiceList"][0]["pdfLink"]
msg1=(f'LUZ LT.37\nNumero de Boleta: {numluz1}\nFecha de Emision: {emisionluz1}\nFecha de vencimiento: {expluz1}\nMonto a Pagar: {montoluz1}\nRecibo Digital: {pdfluz1}\n')
#LT.34
numluz2=json_luz2["invoiceList"][0]["invoiceNumber"]
expluz2=json_luz2["invoiceList"][0]["expiryDate"]
emisionluz2=json_luz2["invoiceList"][0]["issueDate"]
montoluz2=json_luz2["invoiceList"][0]["amount"]
pdfluz2=json_luz2["invoiceList"][0]["pdfLink"]
msg2=(f'LUZ LT.34\nNumero de Boleta: {numluz2}\nFecha de Emision: {emisionluz2}\nFecha de vencimiento: {expluz2}\nMonto a Pagar: {montoluz2}\nRecibo Digital: {pdfluz2}')
msgluz=(f'RECIBOS DE LUZ\n\n{msg1}\n{msg2}')


