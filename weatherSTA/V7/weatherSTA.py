import requests
import time
from bs4 import BeautifulSoup

cycle = 5

target=[
   ['BaoShan',
    'https://www.cwb.gov.tw/V7/observe/24real/Data/C0D58.htm'],
   ['Hsinchu',
    'https://www.cwb.gov.tw/V7/observe/24real/Data/46757.htm'], 
   ['WuFeng',
    'https://www.cwb.gov.tw/V7/observe/24real/Data/72D08.htm'],     
]

def fetchHtml(url):
    headers = {
     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
	}
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    return res.text

def get_element(soup, tag, class_name):
    data = []
    table = soup.find(tag, attrs={'class':class_name})
    rows = table.find_all('tr')
    del rows[0]
    for row in rows:
        first_col = row.find_all('th')
        if first_col == []: return
        cols = row.find_all('td')
        cols.insert(0, first_col[0])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) 
    return data    

def fetch_data():
    d_tmp=[]
    for region in target:     
        soup = BeautifulSoup(fetchHtml(region[1]), "lxml")
        data = get_element(soup, 'table','BoxTable')

        if data:
        # [location, Temp, Humidity, Rain, Wind]
            one_loc = [region[0], float(data[0][1]), float(data[0][8]), float(data[0][10]), float(data[0][5][:data[0][5].index('|')])]
        else: 
            one_loc = [region[0], None, None, None, None]
        d_tmp.append(one_loc)
        time.sleep(3)
    return d_tmp    

if __name__ == '__main__':
    '''
    for region in target:     
        soup = BeautifulSoup(fetchHtml(region[1]), "lxml")
        data = get_element(soup, 'table','BoxTable')
        print('Temperature:', float(data[0][1]) )   
        print('Humidity:', float(data[0][8]) )   
        print('Rain:', float(data[0][10]) )   
        print('Wind:', float(data[0][5][:data[0][5].index('|')]) )   
    '''
    print(fetch_data())







