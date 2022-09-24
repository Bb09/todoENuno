from config import *
from calidda import *
from sedapal import *
from luz import *
import requests

msgfinal=(f'{msgluz}\n\n{msgcalidda}\n\n{msgsedapal}')
#def telegram_bot_sendtext(bot_message):
#enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendphoto?chat_id=' + bot_chatID + '&photo=' + image +"&caption="+msgfinal
enviar_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_chatID+'&parse_mode=Markdown&text='+msgfinal
#enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
response = requests.get(enviar_text)
print(response)
#respIm=requests.get(baseImage_url)   
#return response.json()
