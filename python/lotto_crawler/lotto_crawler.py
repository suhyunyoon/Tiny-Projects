import requests
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from tqdm import tqdm
#from tqdm import tqdm_notebook

# Get newest lotto draw number
source = requests.get("https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=").text
soup = BeautifulSoup(source, "html.parser")
newest = int(soup.select("select#dwrNoList option")[0].text)

# initialize arrays
total = 45
records = np.zeros((newest, total))

print('Crawling...')
for i in tqdm(range(newest, 0, -1)):
    # parsing
    source = requests.get("https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" + str(i)).text
    soup = BeautifulSoup(source, "html.parser")
    hotKeys = soup.select("span.ball_645")
    
    # count ith balls
    balls = list(map(lambda x: int(x.text)-1, hotKeys))
    records[i-1, balls] += 1

hist = plt.bar(np.arange(45)+1, np.sum(records, axis=0), color='r')
plt.title('The number of lotto numbers')
plt.xticks(np.arange(45)+1)
plt.show()
