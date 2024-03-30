from bs4 import BeautifulSoup as bs
import requests as re

def Entry():
  global link

  #Enter the website link
  link_site = input('Enter the link ->')

  try:
    link = bs(re.get(link_site).text,'html.parser')
  except:
    print('Error, Try Again')
    Entry()


def Para(ask=''):
  global link
  
  #See paragraphs
  if ask in ['y','yes']:
    p_id = input('Enter the ID Name ->')
    for i in link.find_all('p',id = p_id):
      print(i , end='\n')

  else:
    for i in link.find_all('p'):
      print(i , end = '\n') 

def A(ask=''):
  global link
  
  #See all a href tags
  if ask in ['y','yes']:
    a_id = input('Enter the ID Name ->')
    for i in link.find_all('a',id = a_id):
      print(i , end='\n')
      
  else:
    for i in link.find_all('a'):
      print(i)


def Div(ask=''):
  global link
  
  #see all div or find div
  if ask in ['y','yes']:
    div_id = input('Enter the ID Name ->')
    for i in link.find_all('div',id = div_id):
      print(i , end='\n')
    
  else:
    for i in link.find_all('div'):
      print(i , end = '\n')

def Sec(ask=''):
  global link
  
  #see all sec or find sec
  if ask in ['y','yes']:
    sec_id = input('Enter the ID Name ->')
    for i in link.find_all('section',id = sec_id):
      print(i , end='\n')
          
  else:
    for i in link.find_all('section'):
      print(i , end = '\n')


def Head(ask=''):
  global link
  
  #see all headings or find headings
  h = input('Enter the Heading tag ->')
  li = ['h1','h2','h3','h4','h5','h6','h']
  
  if h in li:
    if ask in ['y','yes']:
      sec_id = input('Enter the ID Name ->')

      for i in link.find_all(h,id = sec_id):
        print(i , end='\n')
          
    else:
      for i in link.find_all(h):
        print(i , end = '\n')
        
  else:
    print('Invalid Option')
  
v = "\n1 - See HTML Code\n2 - Title of Site\n3 - Extract Anchor Tags\n4 - Extract Paragraphs\n5 - Find Divisions\n6 - Find Sections\n7 - Find Headings\n8 - Change Link\n9 - Exit"


Entry()
while True:
  try:
    print(v)
    ch = int(input('\nEnter your choice ->'))
    
    if ch == 1:
      # See html code
      print(link.prettify)

    elif ch == 2:
      #See title of the website
      print(link.title.string)
        
    elif ch == 3:
      ask1 = input('Finding any specific Anchor Tag? ->')
      A(ask1)
  
    elif ch == 4:
      ask2 = input('Finding any specific Paragraph? ->')
      Para(ask2)
      
    elif ch == 5:
      ask3 = input('Finding any specific Div? ->')
      Div(ask3)
        
    elif ch == 6:
      ask4 = input('Finding any specific Sec? ->')
      Sec(ask4)

    elif ch == 7:
      ask5 = input('Finding any specific Heading? ->')
      Head(ask5)

    elif ch == 8:
      Entry()

    elif ch == 9:
      break
    
    else:
      print('Invalid Option')

  except:
    print('Error, Try Again')
    
