 #!/usr/bin/python                            
# -*- coding: utf-8 -*-
import telebot
from telebot import types
from telebot import util
import redis as r
import urllib
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")
##########################################################
redis = r.StrictRedis(host='localhost', port=6379, db=0) #
##########################################################
TOKEN = '359855193:AAEL3lSBqPv8EmQcGQafa7-fazq9t6FrsA0' ##TOKEN - توکن                                #
bot = telebot.TeleBot(TOKEN)                             #
##########################################################
print("\n \033[01;31mBot Is Online Now! :D\n ---------------------\033[0m")
mk = types.InlineKeyboardMarkup()
mk.add(types.InlineKeyboardButton('👤 کانال ما 👥', url='t.me/ApiBotsNews'))
mk.add(types.InlineKeyboardButton('👤 سازنده 👥', url='t.me/HiddenDev'))
##########################################################
@bot.message_handler(commands=['start'])
def welc(m):
  bot.reply_to(m, 'سلام {}\nبه ربات تبدیل متن به صدا خوش اومدی\nمتنتو بفرست تا برات به صدا تبدیلش کنم\nمتنت باید انگلیسی باشه'.format(m.from_user.first_name), reply_markup=mk)
##########################################################
@bot.message_handler(func=lambda message: True)
def tovoice(m):
   urllib.urlretrieve('http://tts.baidu.com/text2audio?lan=en&ie=utf-8&text={}'.format(m.text), "{}.ogg".format(m.from_user.id))
   voice = open('{}.ogg'.format(m.from_user.id))
   bot.send_voice(m.chat.id, voice, caption='Your Text ~~> {}'.format(m.text), reply_to_message_id=m.message_id, reply_markup=mk)
   os.remove("{}.ogg".format(m.from_user.id))
#########################################################
bot.polling(True)