from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
import requests
import sound as so
import facerecognize as rec

def do_start(bot:Bot,update:Update):
	bot.send_message(
		chat_id=update.message.chat_id, #267995731,
		text="Привет, отправь мне голосовое сообщение или фото",
		)

def do_echo(bot:Bot,update:Update):
	bot.send_message(
		chat_id=update.message.chat_id, #267995731,
		text="Отправь мне голосовое сообщение или фото",
		)

def voice_handler(bot:Bot,update:Update):
	file = bot.getFile(update.message.voice.file_id)
	s=str(file.file_path)
	s=s[len(s)-6:len(s)-4]

	#file.download('voice.ogg')
	myfile=requests.get(file.file_path)
	open('./sound/'+str(update.message.chat_id)+'_'+s+'.ogg', 'wb').write(myfile.content)
	so.convert('./sound/'+str(update.message.chat_id)+'_'+s+'.ogg',str(update.message.chat_id)+'_'+s+'.ogg',update.message.chat_id)
	bot.send_message(
		chat_id=update.message.chat_id, #267995731,
		text='Конвертировано',
		)

def photo_handler(bot:Bot,update:Update):
	file = bot.getFile(update.message.photo[-1].file_id)
	s=str(file.file_path)
	r=s[len(s)-4:len(s)]
	s=s[len(s)-6:len(s)-4]
	myfile=requests.get(file.file_path)
	open('./photo/'+str(update.message.chat_id)+'_'+s+r, 'wb').write(myfile.content)
	a=rec.recognize('./photo/'+str(update.message.chat_id)+'_'+s+r)
	if(int(a)>0):
		text1="Лиц обнаружено: "+str(a)+", фото сохранено "
		bot.send_photo(update.message.chat_id, photo=open('./photo/'+str(update.message.chat_id)+'_'+s+r, 'rb'))
	else:
		text1="Лиц не обнаружено, фото не сохранено"
	bot.send_message(
		chat_id=update.message.chat_id, #267995731,
		text=text1,
		)


def main():
	bot=Bot(
		token = "1332541954:AAFIRCqSSE7XS1bK1mBAXwRiOIi7UCOeP-A",
		base_url="https://telegg.ru/orig/bot",
		#base_url="https://telegg.ru/Savesoundbot"

		)
	updater=Updater(
		bot=bot,
		#use_context=True,
		)
	start_handler=CommandHandler("start",do_start)
	message_handler=MessageHandler(Filters.text,do_echo)
	updater.dispatcher.add_handler(start_handler)
	updater.dispatcher.add_handler(message_handler)
	updater.dispatcher.add_handler(MessageHandler(Filters.voice, voice_handler))
	updater.dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))
	updater.start_polling()
	updater.idle()

if __name__=="__main__":
	main()


