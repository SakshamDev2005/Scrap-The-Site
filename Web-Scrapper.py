from bs4 import BeautifulSoup as bs
import requests as re

link = bs(re.get('https://syberverse.netlify.app').text,'html.parser')

while True:
  print('1 - See HTML Code\n2 - Title of Site\n3 - Extract A Tags\n4 - Show Paragraphs')
  ch = int(input('\nEnter your choice ->'))

  if ch == 1:
    print(link.prettify) # it will show you the whole html code

  elif ch == 2:
    print(link.title.string) #it will get title from link and convert into string removing title tag from it's sides

  elif ch == 3:
    for i in link.find_all('a'):  #it will run a loop and present you all links related to a tags and using "['href']" will give you links provided to a tags
      print(i['href']) #you can use '.text' instead of href which will give you text 

  elif ch == 4:
    v = 1
    for i in link.find_all('p'):  #it will run a loop and present you all links related to a tags and using "['href']" will give you links provided to a tags
      print(f'{v})' + i.text , end = '\n') #you can use '.text' instead of href which will give you text 
      v+=1

  elif ch == 5:
    break

  else:
    print('Invalid Option')
