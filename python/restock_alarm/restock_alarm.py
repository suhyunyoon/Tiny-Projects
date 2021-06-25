import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import numpy as np
#from tqdm import tqdm
#from tqdm import tqdm_notebook

headers = {'User-Agent':'Mozilla/5.0'}
src_url = "https://store.musinsa.com/app/goods/1634431/0"

req_size = np.array(['M', 'L'])

while True:
    # parsing
    source = requests.get(src_url, headers=headers).text
    soup = BeautifulSoup(source, "html.parser")
    size_list = soup.select("select.option1 option")

    # parsing jaego_yn from size list
    size_list = list(filter(lambda x: x.attrs['value'] in req_size, size_list))
    size_list = list(map(lambda x: x.attrs['jaego_yn']=='Y', size_list))

    jaego = req_size[size_list]

    # print
    if len(jaego) > 0:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), jaego)
    time.sleep(2)
