#!/usr/bin/env python
# -*- coding: utf-8 -*-

##   Basic example of Telegram API calls
##   IMPORTANT: You should add the token value in the file config.py  
##   You need to install requests and JSON modules 

import requests
import json

from secret import TOKEN

## Call Telegram to get updates

def telegram_getUpdates():    

## Info de los headers, respuesta en JSON y clave de acceso: Recuerda cambiarla

    headers = {'Accept': 'application/json'}
    endpoint = "https://api.telegram.org/bot"+TOKEN+"/getUpdates"

    r = requests.get( endpoint, headers=headers)

    while r.status_code == 503: 
        print 'error 503'
        time.sleep(6)
        r = requests.get( endpoint+query,  headers=headers)

    if r.status_code == 200:
        results = r.json()
        return (results)
    else:
        return False


## La función que llama a las APIs

def telegram_message(message,chat_id):    

	headers = {}
	payload = {'text': message, 'chat_id': chat_id}
	endpoint = "https://api.telegram.org/bot"+TOKEN+"/sendMessage"
	r = requests.post( endpoint, data=payload,  headers=headers)

	while r.status_code == 503: 
		print 'error 503'
		time.sleep(6)
		r = requests.post( endpoint, data=json.payload,  headers=headers)

	if r.status_code == 200:
		results = r.json()
		return (results)
	else:
		return False

## This is the beginning of the program 

## Open the file with the maxUpdate info 
f = open("MaxUpdate.log", "r")
maxRead = f.read()
max = int(maxRead)
f.close()

response = telegram_getUpdates()
lista = response.get('result')
lista.reverse()
while lista != [] :
	item  = lista.pop()
	message = item.get('message')
	update_id = int(item.get('update_id'))
	message_id = int(message.get('message_id'))
	if update_id > max:
		text = message.get('text')
		chat = message.get('chat').get('id')
		response2 = telegram_message(text,chat)
		max = update_id


## Open the file to write the maxUpdate info 
maxWrite = str(max)
f = open("MaxUpdate.log", "w")
f.write(maxWrite)
# print max
f.close()


