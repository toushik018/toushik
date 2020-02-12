import requests as r
import json

def formatting(data):
  symble = data['symbol']
  balance = data['balance']
  stake = data['stake']
  pending_unstake = data['pending_unstake']
  response = "Balance:{1}\nStake:{2}\nPending Unstake:{3}".format(symble,balance,stake,pending_unstake)
  return response

def search_user(user_name):
  url = 'https://steem-engine.rocks/tokens/APX/richlist?sort_field=balance&sort_order=desc'
  page = r.get(url)
  data = json.loads(page.content)
  s = data['richlist']
  for i in s:
    if user_name in i.values():
      data = formatting(i)
      return data
    else:
      pass

if __name__ == "__main__":
    print("hi")
