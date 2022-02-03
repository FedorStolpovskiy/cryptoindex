from requests import Request, Session
import json



def get_data(url, parameters, headers):
    session = Session()
    session.headers.update(headers)


    response = session.get(url, params = parameters)
    data = json.loads(response.text)

        
    datas = []

    for i in range(0, 10):
        datas.append([])

    for i in range(0, 10):
        datas[i].append(str(data["data"][i]["name"]))
        datas[i].append(str(data["data"][i]["quote"]["USD"]['price']))
        datas[i].append(str(data["data"][i]["quote"]["USD"]['market_cap']))

    return datas


def actual_value(datas):
    actual = 0
    for i in datas:
        actual += float(i[1]) * float(i[2])


    return actual


def start_value(file):
    with open(file, 'r') as k:
        startdata = json.load(k)

    startdatas = sort_startdata(startdata)
    startval = 0
    for i in startdatas:
        startval += float(i[1]) * float(i[2])
 

    return startval



def sort_startdata(startdata):
    startdatas = []
    for i in range(0, 10):
        startdatas.append([])

    for i in range(0, 10):
        startdatas[i].append(str(startdata["data"][i]["name"]))
        startdatas[i].append(str(startdata["data"][i]["quote"]["USD"]['price']))
        startdatas[i].append(str(startdata["data"][i]["quote"]["USD"]['market_cap']))

    return startdatas



datas = get_data('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest', {"limit" : "10", "cryptocurrency_type" : "coins"}, {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': 'your cmc-api key'})
actual = actual_value(datas)
startvalue = start_value('startdata.json')
print(actual / startvalue)