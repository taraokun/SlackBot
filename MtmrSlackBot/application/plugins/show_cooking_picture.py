from slackbot.bot import listen_to

@listen_to('勝負飯')
def train(message):
    import sys
    import os
    import re
    import random

    from slacker import Slacker

    dir = os.getcwd() + '\\application\\plugins\\pictures'# カレントディレクトリのパスを取得

    files = os.listdir(dir)# ファイルのリストを取得
    count = 0# カウンタの初期化
    for file in files:# ファイルの数だけループ
        index = re.search('.jpg', file)# 拡張子がjpgのものを検出
        if index:# jpgの時だけ（今回の場合は）カウンタをカウントアップ
            count = count + 1
    # API token
    token = os.environ.get('SLACK_API_KEY', '')
    # 投稿するチャンネル名
    c_name = message._body['channel']

    # 投稿する画像ファイルへのパス(パラメタから取得)
    f_path = dir + '\\cooking' + str(random.randint(1,count)) + ".jpg"

    #random.randint(1,100)
    # 投稿
    slacker = Slacker(token)
    #slacker.files.upload(f_path, channels=[c_name], title='タイトル')
    slacker.files.upload(f_path, channels=[c_name], title='勝負飯！')
