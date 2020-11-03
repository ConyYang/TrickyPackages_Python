import random


def testNumber():
    value1 = random.random()
    value2 = random.uniform(1, 10)
    value3 = random.randint(1, 6)
    print(value1)
    print("Random Floating number between 1 and 10 : {}".format(value2))
    print("Random Int number between 1 and 6: {}".format(value3))


def choiceTest():
    greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
    greet = random.choice(greetings)
    print(greet + ', Yubei!')


choiceTest()
