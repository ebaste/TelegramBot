# TelegramBot
This project its to create an echo bot for Telegram

##The BotFather is the manager of the BotSystem

BotFather

BotFather is the one bot to rule them all. It will help you create new bots and change settings for existing ones.

Create a new bot
Use the /newbot command to create a new bot. The BotFather will ask you for a "name" and "username", then generate an authorization token for your new bot.

it's a little tricky that you need two names. The important name it´s username. It's the way the people will call your bot.

The name of your bot will be displayed in contact details and elsewhere.

The Username is a short name, to be used in mentions and telegram.me links. Usernames are 5-32 characters long and are case insensitive, but may only include Latin characters, numbers, and underscores. Your bot's username must end in ‘bot’, e.g. ‘tetris_bot’ or ‘TetrisBot’.

The token is a string along the lines of 110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw that will be required to authorize the bot and send requests to the Bot API.

Generate an authorization token for your bot
If your existing token is compromised or you lost it for some reason, use the /token command to generate a new one.

### Bot generation example:

Ebaste
/newbot

BotFather
Alright, a new bot. How are we going to call it? Please choose a name for your bot.

Ebaste
xyzbot

BotFather
Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.

Ebaste
xyz_bot

BotFather
Sorry, this username is already taken. Think of something different.

Ebaste
zyx_bot

BotFather
Done! Congratulations on your new bot. You will find it at telegram.me/zyx_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands.

Use this token to access the HTTP API:
116169643:AAGHoOYKNAjvCH1YtTaKGzUYn1tXQLA6rx8

For a description of the Bot API, see this page: https://core.telegram.org/bots/api

Ebaste
/token

BotFather
Choose a bot to generate a new token.

Ebaste
@zyx_bot

BotFather
You can use this token to access HTTP API:
9999999999:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

For a description of the Bot API, see this page: https://core.telegram.org/bots/api

## Comunicating with your bot

You should call the telegram yourBot API to get info about the messages it receives:

### Making requests

All queries to the Telegram Bot API must be served over HTTPS and need to be presented in this form: https://api.telegram.org/bot<token>/METHOD_NAME. Like this for example:

*Important: bot its bot, not the name of your bot.

#### The first call
With this call, remembert to put your own bot access key

> https://api.telegram.org/bot<accesskey>/getMe 

> https://api.telegram.org/bot9999999999:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/getMe 

> https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe

We support GET and POST HTTP methods. Use either URL query string or application/x-www-form-urlencoded or multipart/form-data for passing parameters in Bot API requests.

The response contains a JSON object, which always has a Boolean field ‘ok’ and may have an optional String field ‘description’ with a human-readable description of the result. If ‘ok’ equals true, the request was successful and the result of the query can be found in the ‘result’ field. In case of an unsuccessful request, ‘ok’ equals false and the error is explained in the ‘description’. An Integer ‘error_code’ field is also returned, but its contents are subject to change in the future.

In this case you will get something like this.
> {"ok":true,"result":{"id":116169643,"first_name":"xyzbot","username":"zyx_bot"}}

All methods in the Bot API are case-insensitive.
All queries must be made using UTF-8.

#### Getting chat input

There are two mutually exclusive ways to get chat input. Incoming updates are stored on the server until the bot receives them either way, but they will not be kept longer than 24 hours.

Regardless of which option you choose, you will receive JSON-serialized Update objects as a result.

GetUpdates: it's an active option. You need to call Telegram to get info
SetWebhook: it's a pasive option. telegram will make a post call ehenever he receives a message.

Update
This object represents an incoming update.

|Field|Type|Description|
----------------------
|update_id|Integer|The update‘s unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you’re using Webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order.|
|message|Message|Optional. New incoming message of any kind — text, photo, sticker, etc.|


##### getUpdates

With getUpdates you can setup a pooling mechanism to pool data from the bot and process it, we will use this method in our examples (only to obtain a chat_id).


getUpdates
Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.

|Parameters|Type|Required|Description|
-------------------------------------
|offset|Integer|Optional|Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id.|
|limit|Integer|Optional|Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100|
|timeout|Integer|Optional|Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling|

Notes
1. This method will not work if an outgoing webhook is set up.
2. In order to avoid getting duplicate updates, recalculate offset after each server response.


##### Respuestas

If there are not mesaages, you receive this

```
{"ok":true,"result":[]}
```
If there are mesaages, you receive something like this

In thes case, two messages, the beggining of the conversation and the message "hola".

```
{ "ok":true,
  "result":[{	"update_id":857746941,
			"message":{	"message_id":1,
						"from":{	"id":4175328,
								"first_name":"Ebaste",
								"username":"EBaste"},
								"chat":{	"id":4175328,
										"first_name":"Ebaste",
										"username":"EBaste"},
								"date":1439291435,
								"text":"\/start"}},
		{	"update_id":857746942,
			"message":{	"message_id":2,
						"from":{	"id":4175328,
								"first_name":"Ebaste",	
								"username":"EBaste"},
								"chat":{	"id":4175328,
										"first_name":"Ebaste",
										"username":"EBaste"},
								"date":1439291440,
								"text":"Hola"}}]}
```

##### setWebhook

With setWebhook we can setup a "callback" url where the bot will push everything received into a conversation. 

Use this method to specify a url and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts.

If you'd like to make sure that the Webhook request comes from Telegram, we recommend using a secret path in the URL, e.g. www.example.com/<token>. Since nobody else knows your bot‘s token, you can be pretty sure it’s us.

|Parameters|Type|Required|Description|
--------------------------------------
|url|String|Optional|HTTPS url to send updates to. Use an empty string to remove webhook integration|
Notes
1. You will not be able to receive updates using getUpdates for as long as an outgoing webhook is set up.
2. We currently do not support self-signed certificates.
3. Ports currently supported for Webhooks: 443, 80, 88, 8443.

### Sending messages

To send a message:
```
curl -s -X POST https://api.telegram.org/bot<token>/sendMessage -d text="A message from your bot" -d chat_id=4175328 
```

## Bot Commands
The remaining commands are pretty self-explanatory:

/setname – change your bot's name.
/setdescription — changes the bot's description, a short text of up to 512 characters, describing your bot. Users will see this text at the beginning of the conversation with the bot, titled ‘What can this bot do?’.
/setabouttext — changes the bot's about info, an even shorter text of up to 120 characters. Users will see this text on the bot's profile page. When they share your bot with someone, this text will be sent together with the link.
/setuserpic — changes the bot‘s profile pictures. It’s always nice to put a face to a name.
/setcommands — changes the list of commands supported by your bot. Each command has a name (must start with a slash ‘/’, alphanumeric plus underscores, no more than 32 characters, case-insensitive), parameters, and a text description. Users will see the list of commands whenever they type ‘/’ in a conversation with your bot.
/setjoingroups — determines whether your bot can be added to groups or not. Any bot must be able to process private messages, but if your bot was not designed to work in groups, you can disable this.
/setprivacy — determines which messages your bot will receive when added to a group. With privacy mode disabled, the bot will receive all messages. We recommend leaving privacy mode enabled.
/deletebot — deletes your bot and frees its username.
Please note, that it may take a few minutes for changes to take effect.

## References:

### Telegram

#### Telegram Bot Platform - User description
https://telegram.org/blog/bot-revolution

#### Bots: An introduction for developers - Programmers description
https://core.telegram.org/bots

#### Telegram Bot API
https://core.telegram.org/bots/api

### Getting started with telegram bots -Tutorial-
https://unnikked.ga/getting-started-with-telegram-bots
