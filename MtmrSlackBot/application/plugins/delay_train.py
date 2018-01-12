from slackbot.bot import listen_to

@listen_to('電車遅れてる？')
def train(message):
    import urllib
    import json

    url = 'https://rti-giken.jp/fhc/api/train_tetsudo/delay.json'
    html = urllib.request.urlopen(url)
    jsonfile = json.loads(html.read().decode('utf-8'))

    for json in jsonfile:
        name = json['name']
        company = json['company']
        text = company + name + 'が遅延してるでー'
        message.send(text)
