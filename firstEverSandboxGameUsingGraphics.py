import webbrowser
import time
import random

while True:
      sites = random.choice(['theuselessweb.com', 'giphy.com/gifs/jennifer-lawrence-gif-antoine-dodson-Pgy4Na8aRyBuE', 'rekt.net', 'trollface.dk'])
      visit = "http://{}".format(sites)
      webbrowser.open(visit)
      seconds = random.randrange(5, 10)
      time.sleep(seconds)
