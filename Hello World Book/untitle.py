import urllib
import urllib.request
file = urllib.request.urlopen('http://helloworldbook.com/data/message.txt')
message = file.read()
print(message)
