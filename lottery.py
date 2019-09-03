import requests
from bs4 import BeautifulSoup
import pandas as pd

def lottoName(name):
    res = requests.post("https://www.taiwanlottery.com.tw/lotto/"+name+"/history.aspx")
    soup = BeautifulSoup(res.text,'html.parser')
    #第一區號碼
    winNums1 = soup.select("td[class='td_w font_black14b_center']")
    #第二區號碼
    winNums2 = soup.select("td[class='td_w font_red14b_center']")
    numbers1,numbers2 = pd.Series(),pd.Series()
    for num1 in winNums1:
        numbers1 = numbers1.append(pd.Series([num1.text])).reset_index(drop=True)
    for num2 in winNums2:
        numbers2 = numbers2.append(pd.Series([num2.text])).reset_index(drop=True)
    winN = []
    for i in range(6,12):
        winN.append(numbers1[i].strip())
    print(','.join(winN))
    print(numbers2[1].strip())

if __name__ == '__main__':
    print('最新大樂透號碼：')
    lottoName('Lotto649')
    print('最新威力彩號碼：')
    lottoName('superlotto638')
