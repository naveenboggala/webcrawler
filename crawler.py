import csv
import requests
from bs4 import BeautifulSoup

## url and parameters
url = "http://news.ycombinator.com/"
params = {"params":"query=facebook&hitsPerPage=25&page=0&getRankingInfo=1&minWordSizefor1Typo=5&minWordSizefor2Typos=9&tagFilters=%5B%22story%22%5D&numericFilters=%5B%5D&advancedSyntax=true&queryType=prefixNone","apiKey":"8ece23f8eb07cd25d40262a1764599b1","appID":"UJ5WYC0L7X"}

## getting response using python requests module
response  = requests.get(url, params=params)

## reading data
data = response.text

## creating a beautiful soap object
soup = BeautifulSoup(data)

## opening a csv file to write data

with open('analytics.csv', 'a') as csv_file:

    try:
        ## getting all elements which have title and subtext as class
        for value in soup.findAll(True, {'class':['title', 'subtext']}):

            csv_list = []
            title, result_url, user, points = '', '', '', ''  
            ## getting title and url and writting to csv in third and fourth columns
            if value.find('a') and value.find('a').parent.attrs == {'class' : ['title']}:
                title = str(value.find('a').text.encode('utf-8'))
                csv_list.append(title)
                result_url = str(value.find('span', {'class' : 'comhead'}).text.encode('utf-8'))
                csv_list.append(result_url)

            ## getting user and points and writting to csv in third and fourth columns
            if value.find('a') and value.find('a').parent.attrs == {'class' : ['subtext']}:
                user = str(value.find('a').text.encode('utf-8'))
                csv_list.append(user)
                points = str(value.find('span').text.encode('utf-8'))
                csv_list.append(points)

            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(csv_list)

    except AttributeError:
        pass

## closing file object
csv_file.close()
