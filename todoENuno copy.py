import requests
import json
import telebot 
from config import *
from calidda import *
from sedapal import *
from luz import *
import requests
from asyncio.windows_events import NULL
from cgitb import text
import time
from typing import Text
bot_token  = '5668749695:AAEk3WQEN35LzW-ONBcOJvwFvt1Q7784S54'
#instanciamos el bot de telegram
bot=telebot.TeleBot(bot_token)
#responde al comando /start

###########################################################################################
#API - TOTTUS:
urltottus="https://www.tottus.com.pe/api/content/skuList?productsList=41876528"
#https://www.tottus.com.pe/api/content/skuList?productsList=41876528
#https://www.tottus.com.pe/api/product-search?q=41876528
apitottus = requests.get(urltottus)
json_data_tottus = json.loads(apitottus.content)
marcaT=json_data_tottus["results"][0]["attributes"]["marca"]
nombreprodT=json_data_tottus["results"][0]["name"]
codprodT=json_data_tottus["results"][0]["productId"]
codskuT=json_data_tottus["results"][0]["sku"]
enlaceT=json_data_tottus["results"][0]["slug"]
enlaceTo=(f"https://www.tottus.com.pe/{enlaceT}/p")
precioON=float(json_data_tottus["results"][0]["prices"]["currentPrice"])
precioRE=float(json_data_tottus["results"][0]["prices"]["regularPrice"])
image=json_data_tottus["results"][0]["images"][0]
listatottus=json_data_tottus["results"][0]["prices"]
contador=len(listatottus)

if contador<=4:
    test =(f"Código SKU: {codskuT}\nPrecio Online: {precioON}\nPrecio Normal :{precioRE}\nCon CMR : Sin Descuento\n✅Link: {enlaceTo}")

else:
    cmr=float(json_data_tottus["results"][0]["prices"]["cmrPrice"])
    test =(f"Código SKU: {codskuT}\nPrecio Online: {precioON}\nPrecio Normal :{precioRE}\nCon CMR :{cmr}\n✅Link: {enlaceTo}")


###########################################################################################
#API - PLAZA VEA:

urlvea="https://www.plazavea.com.pe/api/catalog_system/pub/products/search/?fq=productId:47350"
apivea = requests.get(urlvea)
json_data_vea = json.loads(apivea.content)

marcaV=json_data_vea[0]["brand"]
nombreprodV=json_data_vea[0]["productName"]
codprodV=json_data_vea[0]["productId"]
codskuV=json_data_vea[0]["productReferenceCode"]
enlaceV=json_data_vea[0]["link"]
preOnlineV=float(json_data_vea[0]["items"][0]["sellers"][0]["commertialOffer"]["Price"])
preRealV=float(json_data_vea[0]["items"][0]["sellers"][0]["commertialOffer"]["ListPrice"])
stockV=json_data_vea[0]["items"][0]["sellers"][0]["commertialOffer"]["AvailableQuantity"]
msgvea=(f"📮📮📮PLAZA VEA📮📮📮\nCódigo de Producto: {codprodV}\nPrecio Online: {preOnlineV}\nPrecio Normal :{preRealV}\nStock : {stockV}\n✅Link : {enlaceV}")
###########################################################################################
#API - METRO:

urlmetro="https://www.metro.pe/api/catalog_system/pub/products/search?ft=752336"
api = requests.get(urlmetro)
json_data = json.loads(api.content)

marca=json_data[0]["brand"]
nombreprod=json_data[0]["productName"]
codprod=json_data[0]["productReferenceCode"]
codsku=json_data[0]["items"][0]["itemId"]
enlace=json_data[0]["link"]
preOnline=float(json_data[0]["items"][0]["sellers"][0]["commertialOffer"]["Price"])
preReal=float(json_data[0]["items"][0]["sellers"][0]["commertialOffer"]["ListPrice"])
stockM=json_data[0]["items"][0]["sellers"][0]["commertialOffer"]["AvailableQuantity"]
msgmetro=(f"🔥🔥🔥METRO🔥🔥🔥\nCódigo de Producto: {codprod}\nPrecio Online: {preOnline}\nPrecio Normal :{preReal}\nStock : {stockM}\n✅Link : {enlace}")

###########################################################################################
#API - WONG:

urlwong="https://www.wong.pe/api/catalog_system/pub/products/search/?ft=752338"
apiwong = requests.get(urlwong)
json_data_wong = json.loads(apiwong.content)

marcaw=json_data_wong[0]["brand"]
nombreprodw=json_data_wong[0]["productName"]
codprodw=json_data_wong[0]["productReferenceCode"]
codskuw=json_data_wong[0]["items"][0]["itemId"]
enlacew=json_data_wong[0]["link"]
preOnlinew=float(json_data_wong[0]["items"][0]["sellers"][0]["commertialOffer"]["Price"])
preRealw=float(json_data_wong[0]["items"][0]["sellers"][0]["commertialOffer"]["ListPrice"])
stockW=json_data_wong[0]["items"][0]["sellers"][0]["commertialOffer"]["AvailableQuantity"]
msgwong=(f"📛📛📛WONG📛📛📛\nCódigo de Producto: {codprodw}\nPrecio Online: {preOnlinew}\nPrecio Normal :{preRealw}\nStock : {stockW}\n✅Link : {enlacew}")


bot_chatID = '@PiratexBBreniec'
@bot.message_handler(commands=["ricocan"])
def cmd_start(message): 
    a=(f"{nombreprod}\n\n{msgmetro}\n\n{msgwong}\n\n☘️☘️☘️TOTTUS☘️☘️☘️\n{test}\n\n{msgvea}")
    #+'\nCódigo SKU: '+codsku+'\nLink: '+enlace+'\nPrecio Online: '+preOnline+'\nPrecio Normal: '+preReal+'\n\nMarca: '+marcaT+'\nProducto: '+nombreprodT+'\nCódigo de Producto: '+codprodT+'\nCódigo SKU: '+codskuT+'\nLink: '+enlaceTo+'\nPrecio Online: '+precioON+'\nPrecio Normal :'+precioRE+'\nCon CMR :'+cmr)
    enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendphoto?chat_id=' + bot_chatID + '&photo=' + image +"&caption="+a
    #enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + a
    #enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(enviar_text)
    print(response)
    #bot.reply_to(message."hola")
@bot.message_handler(commands=["recibos"])
def cmd_recibos(message): 
    msgfinal=(f'{msgluz}\n\n{msgcalidda}\n\n{msgsedapal}')
    #def telegram_bot_sendtext(bot_message):
    #enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendphoto?chat_id=' + bot_chatID + '&photo=' + image +"&caption="+msgfinal
    enviar_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_chatID+'&parse_mode=Markdown&text='+msgfinal
    #enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(enviar_text)
    print(response)
@bot.message_handler(func=lambda message: True)
def echo_message(message):

    if message.text.startswith("/"):
        urlreniec=(f"https://consulta.api-peru.com/api/dni/{message.text}/35e193dbbafc3640c82c51495a6beb84")
        bot.send_chat_action(message.chat.id,"typing")
        bot.reply_to(message,"Estamos buscando la informacion, unos segundos por favor")
        #bot.send_message(message.chat.id,"Estamos buscando la informacion, unos segundos por favor")   
        api = requests.get(urlreniec)
        json_data = json.loads(api.content)
        valido=json_data["success"]
        if valido==True:
            numero=json_data["data"]["numero"]
            nomcompleto=json_data["data"]["nombre_completo"]
            nom=json_data["data"]["nombres"]
            apat=json_data["data"]["apellido_paterno"]
            amat=json_data["data"]["apellido_materno"]
            sexo=json_data["data"]["sexo"]
            image='https://wongfood.vteximg.com.br/arquivos/ids/371274-1000-1000/Ricocan-Alimento-para-Perros-Adultos-Raza-Peque-a-Cordero-y-Cereales-Bolsa-15-Kg-1-34829214.jpg?v=637312320649570000'
            fechaNac=json_data["data"]["fecha_nacimiento"]
            mensaje =(f"Nombre Completo: {nomcompleto}\nDNI: {numero}\nNombre:{nom}\nApellido Paterno: {apat}\nApellido Materno: {amat}\nSexo: {sexo}\nFecha de Nacimiento: {fechaNac}")
        else :
            mensaje =(f"Dni incorrecto o no existe")
        bot_chatID = '@PiratexBBreniec' 
        #bot_chatID = '@chokaScraping'
        #bot_chatID = '@PiratexBBreniec'
        #bot_chatID = '182832113'
        a=(f"{mensaje}")
        #enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendphoto?chat_id=' + bot_chatID + '&photo=' + image +"&caption="+a
        enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + a
        #enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&caption='+ a
        bot.send_chat_action(message.chat.id,"typing")
        time.sleep(1)
        response = requests.get(enviar_text)
        print(response) 
    else:
        print("intenta de nuevo")

if __name__=='__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('fin')
    #respIm=requests.get(baseImage_url)   
    #return response.json()
#bot_chatID = '182832113' 
#bot_chatID = '@chokaScraping'
#bot_chatID = '@chokaScraping'