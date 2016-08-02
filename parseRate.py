import urllib.request
from datetime import datetime, date, time
from bs4 import BeautifulSoup

moneyType ='JPY'
alarmRate = 0.3030 #init last_rate to assume 0.3030
def getCurrentRate():
    todayDate = date.today()
    todayStr = todayDate.__str__()
    todayArray = todayStr.split("-")
    parseUrl = 'http://rate.bot.com.tw/Pages/UIP004/UIP00421.aspx' \
               '?lang=zh-TW&whom1='+moneyType+'&whom2=&date='+todayStr.replace('-','')+\
               '&entity=1&year=2016&month='+todayArray[1]+'&term=99&afterOrNot=0&view=1'

    with urllib.request.urlopen(parseUrl) as response:
        html_ = response.read().decode('utf-8')

    soup = BeautifulSoup(html_, "html.parser")
    # list = soup.findAll('tr')
    list = soup.find_all('tr')
    rateDict = dict()
    for line in list:
        if(line.get('class')!=None):
            _time = line.find_all('td')[0].next
            _rate = line.find_all('td')[3].next
            rateDict[str(_time)] = float(_rate)
    try:
        if len(rateDict) > 0:
            #newly update time
            last_time = (sorted(rateDict.keys())[len(rateDict.keys())-1])
            #newly rate of JPY
            last_rate = rateDict[last_time]
        else:
            last_rate = None
    except IndexError as ie:
        print("IndexError {}".format(ie.args))
        last_rate = None

    return last_rate
