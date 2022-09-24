from config import *
import requests
import json

####################################################################################
#API - SEDAPAL LT.37:
urlagua1="https://webapp16.sedapal.com.pe/OficinaComercialVirtual/api/suministros/detalle-nis"
apiagua1 = requests.post(urlagua1)
body1= {
  "nis_rad": "4140576",
  "flagChannel": "1"
}
h1 =  {
"Content-Type":"application/json"
}
api_agua1=requests.post(urlagua1,headers=h1,json=body1)
json_agua1 = json.loads(api_agua1.content)
codigo1=json_agua1["bRESP"]["nis_rad"]
estado1=json_agua1["bRESP"]["est_sum"]
deuda1=float(json_agua1["bRESP"]["total_deuda"])
nom1=json_agua1["bRESP"]["nom_cliente"]

urlagua2="https://webapp16.sedapal.com.pe/OficinaComercialVirtual/api/recibos/lista-recibos-deudas-nis"
apiagua2 = requests.post(urlagua2)
body2= {
  "nis_rad": "4140576",
  "page_num":1,
  "page_size":10
}
h2 =  {
"Content-Type":"application/json"
}
api_agua2=requests.post(urlagua2,headers=h2,json=body2)
json_agua2 = json.loads(api_agua2.content)
vencimiento=json_agua2["bRESP"][0]["vencimiento"].replace('-','/')

if deuda1==0:
    msg_pago1="Está al dia, no hay facturacion"
else:
    msg_pago1=deuda1
msg_agua1=(f"💦💦SEDAPAL LT.37💦💦\nNombre: {nom1}\nN° Suministro: {codigo1}\nEstado: {estado1}\nFecha Vencimiento: {vencimiento}\nTotal a Pagar: {msg_pago1}")
################################################################################################################################
####################################################################################
#API - SEDAPAL LT.37:
urlagua2="https://webapp16.sedapal.com.pe/OficinaComercialVirtual/api/suministros/detalle-nis"
apiagua2 = requests.post(urlagua1)
body2= {
  "nis_rad": "4140573",
  "flagChannel": "1"
}
h2 =  {
"Content-Type":"application/json"
}

api_agua2=requests.post(urlagua2,headers=h2,json=body2)
json_agua2 = json.loads(api_agua2.content)
codigo2=json_agua2["bRESP"]["nis_rad"]
estado2=json_agua2["bRESP"]["est_sum"]
deuda2=float(json_agua2["bRESP"]["total_deuda"])
nom2=json_agua2["bRESP"]["nom_cliente"]
####
urlagua4="https://webapp16.sedapal.com.pe/OficinaComercialVirtual/api/recibos/lista-recibos-deudas-nis"
apiagua4 = requests.post(urlagua4)
body4= {
  "nis_rad": "4140573",
  "page_num":1,
  "page_size":10
}
h4 =  {
"Content-Type":"application/json"
}
api_agua4=requests.post(urlagua4,headers=h4,json=body4)
json_agua4 = json.loads(api_agua4.content)
vencimiento4=json_agua4["bRESP"][0]["vencimiento"].replace('-','/')
####

if deuda2==0:
    msg_pago2="Está al dia, no hay facturacion"
else:
    msg_pago2=deuda2
msg_agua2=(f"💦💦SEDAPAL LT.34💦💦\nNombre: {nom2}\nN° Suministro: {codigo2}\nEstado:{estado2}\nFecha de Venciminto: {vencimiento4}\nTotal a Pagar: {msg_pago2}")
msgsedapal=(f"RECIBOS DE SEDAPAL\n\n{msg_agua1}\n\n{msg_agua2}")
################################################################################################################################
