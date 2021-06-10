import requests
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from tqdm import tqdm
#from tqdm import tqdm_notebook

total = 45
newest = 930
freq = np.array([0] * total)

print('Crawling...')
for i in tqdm(range(1, 30)):
    source = requests.get("https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" + str(i)).text
    soup = BeautifulSoup(source, "html.parser")
    hotKeys = soup.select("span.ball_645")

    for key in hotKeys:
        num = int(key.text)
        freq[num-1] += 1

hist = plt.bar(np.arange(45)+1, freq, color='r')
plt.title('The number of lotto numbers')
plt.xticks(np.arange(45)+1)
plt.show()
