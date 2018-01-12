# -*- coding: utf-8 -*-

from slackbot.bot import respond_to, listen_to

from dialogue_system.bot import Bot

bots = {}


def create_or_read(user_id):
    return bots[user_id] if user_id in bots else Bot()


def save_bot(bot, user_id):
    bots[user_id] = bot

from slackbot.bot import respond_to, listen_to

@listen_to('プログラミング')
@listen_to('分散システム')
@listen_to('データベース')
@listen_to('情報工学実験')
@listen_to('オペレーティングシステム')
def hello(message):
    message.reply('参考程度に見してくれんけ？')

@listen_to('増田')
@listen_to('ますだ')
@listen_to('マスダ')
@listen_to('masuda')
@listen_to('msd')
@listen_to('祟芳')
@listen_to('たかよし')
@listen_to('タカヨシ')
def masuda(message):
    message.reply('増田ク～ン')

@listen_to('(.*)です')
@listen_to('(.*)だよ')
def hello(message, something):
    message.reply('\n{0}ク～ン。\nmtmr特製しそカツ丼食べる？'.format(something))


@respond_to('(.*)')
def food(message, something):
    body = message.body
    text, ts, user_id = body['text'], body['ts'], body['user']
    bot = create_or_read(user_id)
    reply_message = bot.reply(text)
    save_bot(bot, user_id)
    message.reply(reply_message)

"""
@respond_to('(.*)')
def food(message, something):
    body = message.body
    text, ts, user_id = body['text'], body['ts'], body['user']
    bot = create_or_read(user_id)
    reply_message = bot.reply(text)
    save_bot(bot, user_id)
    message.reply(reply_message)"""
