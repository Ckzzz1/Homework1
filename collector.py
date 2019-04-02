import requests
import json


class Day:
  def __init__(self, month, day):
    self.month = month
    self.day = day

  def get_thing(self, types=1, page=1, rows=20):    #查询函数
    urls = 'http://api.avatardata.cn/HistoryToday/LookUp?key=' + '80877a2342194884a31f07bfc4c71282&yue=' + str(self.month) + '&ri=' + str(self.day) + '&type=' + str(types) + '&page=' + str(page) + '&rows=' + str(rows) + '&format=true'
    r = requests.get(urls)
    result = json.loads(s=r.content)

    return result
