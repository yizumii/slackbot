from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

@listen_to('おやすみ')
def listen_func(message):
    message.reply('おやすみ～')
