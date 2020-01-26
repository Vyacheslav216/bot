from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters



def voice_handler(bot:Bot):
   file = bot.getFile('AwACAgIAAxkBAANFXitfdmqtqrxWPMSJnep2VycZ-pQAAvwGAAIPxGBJtuUIc-15rLUYBA')
   print ("file_id: " + str('AwACAgIAAxkBAANFXitfdmqtqrxWPMSJnep2VycZ-pQAAvwGAAIPxGBJtuUIc-15rLUYBA'))
   file.download('voice.ogg')


def main():
	bot=Bot(
		token = "1080454982:AAEhI4zgqTtq08PAE6hO5cv14FB57gDT_zk",
		base_url="https://telegg.ru/orig/bot",
		#base_url="https://telegg.ru/Savesoundbot"

		)
	voice_handler(bot)

if __name__=="__main__":
	main()


