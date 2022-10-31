from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(name='PyBot', read_only=True, logic_adapters=['chatterbot.logic.MathematiclEvaluation', 'chatterbot.logic.BestMatch'])