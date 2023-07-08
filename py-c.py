
from bs4 import BeautifulSoup
import requests
best={'name': '6 PC HP 8300 DC Smal ', 'category': 'Ordinateurs portables', 'place': 'Tunis, il y a 5 minutes', 'price': '540', 'link': 'https://www.tayara.tn/fr/item/631611c4b050776c5a3d72ff/'}
kkk=0
def price_tab(t):
          s=''
          for i in t :
              s+=str(i.text)
          return s
while best['name'] =='6 PC HP 8300 DC Smal ':
      kkk+=1
      html_file=requests.get('https://www.tayara.tn/fr/search/?category=Informatique+et+Multimedia').text 
#print(html_file)
      soup =BeautifulSoup(html_file,'lxml')
      produces=soup.find_all('article' , class_='mx-auto')
      produces_list=[]
      for produce in produces :
         
         produce_name=produce.find('h2')
         produce_place=produce.find_all('span',class_='line-clamp-1 text-3xs font-normal text-neutral-400')
         produce_price=produce.find_all('span',class_="mr-1")
         produce= {
        'name':produce_name.text ,
        'category':produce_place[0].text,
        'place':produce_place[1].text,
        'price':price_tab(produce_price),
        'link':'https://www.tayara.tn'+produce.a['href']
         }
         if produce['category']=='Ordinateurs portables':produces_list.append(produce)
      m=99999999999999999999999999999999999999999999
      k=-1 ; index=0
      for i in produces_list:
         k+=1
         if i['price']:
           p=int(i['price'])
         else :
            p=0
         if 0<p<m:
             m=int(i['price'])
             index=k
      print(kkk,produces_list)
      best=produces_list[index]
      
      

      
print(best)