from datetime import datetime
from threading import Timer
import requests
# 打印时间函数
url = 'http://172.16.254.6/drcom/login?callback=dr1589985374636&DDDDD=18146702513%40telecom&upass=512512&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=1589985359545'
headers = {
    'Host': '172.16.254.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'close',
    'Referer': 'http://172.16.254.6/a79.htm?isReback=1',
    'PHPSESSID': 'ut2q1fnsj2t0go70uj78f61ja6'
}
def printTime(inc):
    print(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"),'30s')
    r = requests.get(url, headers=headers)
    t = Timer(inc, printTime, (inc,))
    t.start()
printTime(30)