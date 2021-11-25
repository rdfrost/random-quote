import sys
from time import strftime, gmtime

import json
from random import choice

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

# Define current time
curr_time = strftime("%H:%M:%S", gmtime())

# Pick random quote from JSON source
with open("./quotes.json") as f:
    q = json.loads(f.read())
result = choice(q)

# Define chosen quote result
quote = result['Quote']
author = result['Author']
source = result['Source']
detail = result['Author'] + ", " + result['Source']

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/main.qml')
# engine.rootObjects()[0].setProperty('currTime', curr_time)
engine.rootObjects()[0].setProperty('quote', quote)
engine.rootObjects()[0].setProperty('author', author)
engine.rootObjects()[0].setProperty('source', source)
engine.rootObjects()[0].setProperty('detail', detail)

print(detail)

sys.exit(app.exec())