from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')
conv = open('chats.txt','r').readines()

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
    request = input('you: ')
    response = bot.get_response(request)
    print('Bot: ', response)