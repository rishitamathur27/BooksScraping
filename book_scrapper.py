from bs4 import BeautifulSoup
import requests
import csv

f= csv.writer(open('booksname.csv', 'w'))
f.writerow(["Title", "Author"])

pages=[]
for i in range(1,2):      #for taking 1 and 2 pages
    url='https://thegreatestbooks.org/?page='+str(i)
    pages.append(url)

print(pages)
title=[]
author=[]

for urls in pages:
    page= requests.get(urls)
    soup= BeautifulSoup(page.text,'html.parser')

    book= soup.find(class_='list-unstyled')
    book_a=book.find_all('a')

    #for i in range(len(book_a)):
      #  print(i)
       # print(book_a[i])
   # print(book_a)

    k=""

    for i in range(0,len(book_a),4):
        b= str(book_a[i]).partition('>')[2]
        for m in range(len(b)):
            if b[m]=='<':
                break
            k=k+b[m]
        print(k)
        title.append(k)
        k=""


    l=""

    for j in range(1, len(book_a), 4):
        a = str(book_a[j]).partition('>')[2]
        for n in range(len(a)):
            if b[n] == '<':
                break
            l = l + b[n]
        print(l)
        title.append(l)
        l = ""

    for(Title, Author) in zip(title, author):
        f.writerow([Title, Author])
    f=csv.writer(open('boook.csv','w'))
    f.writerow([Title, Author])



