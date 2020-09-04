import webbrowser
import time
import pyautogui as gui
from numpy import loadtxt

text_file = open("numbers.txt", "r")
x = text_file.read()

mylist = x.split('"\n"')

mylist = list(dict.fromkeys(mylist))

wadefault= '91'
walist = []

for i in mylist:
	if i[0] == '0':
		i = i.replace('0', '', 1)
		i = i.replace(' ', '', 1)
	i = wadefault + i
	walist.append(i)

interval = 2

#message="Hello,%20We%20are%20from%20amaltas-exhibition.com.%20Details%20for%20collaborating:%20Premium%20stalls%20rs%206000%20for%20whole%20month%20with%2040%20product%20images%20and%20regular%20stalls%203000%20with%2030%20images%20pls%20visit%20our%20website%20www.amaltas-exhibition.com/stalls/"
message="Online Shopping Like never Before! Get the latest range of apparel’s, accessories, and more, Click the Link: https://www.amaltas-exhibition.com/stalls"

message = message.replace(' ', '%20')

#testnumbers= ["918329584644","919176594948"]


for i in walist:
 url = 'https://wa.me/{}?text={}'.format(i, message)
 webbrowser.open(url)
 time.sleep(3)
 gui.press('enter')
 time.sleep(interval)
