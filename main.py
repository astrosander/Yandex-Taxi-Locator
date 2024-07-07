import requests
import numpy as np
import divise, time, PlotMap
import sys
import random

def add_randomness(variable, error_percentage=1):
    error = variable * (error_percentage / 100) * random.uniform(-1, 1)
    return variable + error

# Define the URL and the data to be sent
url = "https://ya-authproxy.taxi.yandex.com/integration/turboapp/v1/nearestdrivers"
data = {
    "point": [29.240033, 52.032928],
    "classes": ["econom"],
    "current_drivers": [],
    "id": "81e92ba6708e4a3598a536f5fed3e54d",
    "is_retro": False,
    "simplify": False
}

# Define the headers to be sent with the request
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en",
    "Content-Type": "application/json",
    "Cookie": "yashr=9218767861713628152; yandexuid=2647646071713560256; yuidss=2647646071713560256; receive-cookie-deprecation=1; my=YwA=; i=rEbZQnMgVqtKmnpt/SddThNmtS6YTaoASgM9OTSeA+g1L/27X7jVpre9LCngDiyTHnDhqDkAjRV4cf6qbTkGRSKUl2w=; yp=4294967295.skin.s#1732223099.szm.1_25:1536x864:1536x730#1719047097.ygu.1#1720301252.yu.2647646071713560256; ymex=1722806852.oyu.2647646071713560256#2028988152.yrts.1713628152#2028988152.yrtsi.1713628152; _ym_isad=2; is_gdpr=0; is_gdpr_b=CNa0CBDwhQIoAg==; _ym_uid=1720271949277434274; _ym_d=1720271955; gdpr=0; bh=EkAiTm90L0EpQnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjEyNiIsICJHb29nbGUgQ2hyb21lIjt2PSIxMjYiGgUieDg2IiIQIjEyNC4wLjYzNjcuMjAyIioCPzAyAiIiOgkiV2luZG93cyJCCCIxNS4wLjAiSgQiNjQiUl0iQ2hyb21pdW0iO3Y9IjEyNC4wLjYzNjcuMjAyIiwgIkdvb2dsZSBDaHJvbWUiO3Y9IjEyNC4wLjYzNjcuMjAyIiwgIk5vdC1BLkJyYW5kIjt2PSI5OS4wLjAuMCJaAj8wYN/PpbQG; _yasc=qEUE+IKxUkMu6lQr7v6AYJsRpKny3TYKHvXHNFlE6VBH141fs2Ml30PPE2ECaaiiKjobFw==",
    "Origin": "https://taxi.yandex.com",
    "Referer": "https://taxi.yandex.com/",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Csrf-Token": "Xq7HriJSA6jWKMQVy6Ar9zXVOYo=:1720280191",
    "X-Request-Id": "1f404782-d8c5-42f7-9291-4ae76704b6a2",
    "X-Taxi": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 turboapp_taxi",
    "X-Yataxi-Userid": "81e92ba6708e4a3598a536f5fed3e54d",
    "X-Yatraceid": "1f404782d8c542f792914ae76704b6a2"
}



PointA=[37.353293, 55.571427]
PointB=[37.854111, 55.920065]

# PointA=[29.151358, 52.007652]
# PointB=[29.270607, 52.103733]
coord=divise.Devise(PointA, PointB, 0.01)

printed_positions = set()
done_drive = set()

DurBetween = 1
UpdateTime = 60
LastSeenTime = [time.time()-DurBetween for _ in range(len(coord))]
LastSeenTime1 = [time.time()-DurBetween for _ in range(len(coord))]
PrevName = int(time.time()//UpdateTime)


def BackUp(TextArray, name):
    with open(f"data/{name}.txt", 'w') as file:
        try:
            for string in TextArray:
                file.write(string + '\n')
        except:
            pass

def are_different(array1, array2):
    for i in range(len(array1)):
        if array1[i] == array2[i]:
            return False  

    return True

def CheckforUpdate():
    global LastSeenTime1
    while True:
        # while are_different(LastSeenTime, LastSeenTime1):
        if False:
            ksis = int(time.time()//UpdateTime)
            BackUp(printed_positions, ksis)
            printed_positions.clear()
            done_drive.clear()
            print(f"Saved {len(printed_positions)} coordinates" )
            
            LastSeenTime1=LastSeenTime
            PrevName = ksis
            # if ksis != PrevName: #back up of printed_positions


def DoUpdate(Points, i):
    while True:

        # while(time.time() - LastSeenTime[i] >= DurBetween):
        #     pass

        # dag=0
        # for cc in range(len(LastSeenTime)):
        #     if LastSeenTime1[cc] == LastSeenTime[cc]:
        #         dag+=1

        # print(dag)
        # LastSeenTime[i] = time.time()
        # print(i)
        # pass

        # print(i)
        for PointC in Points:
            print(coord.index(PointC))
            pass
            # print(f"{LastSeenTime[i]} {time.time()}")
            data['point'] = PointC
            try:
                response = requests.post(url, headers=headers, json=data)
                response_json = response.json()
                
                LastSeenTime[i] = time.time()
                for driver in response_json.get('drivers', []):
                    if driver['id'] not in done_drive:
                        done_drive.add(driver['id'])
                        for position in driver.get('positions', []):
                            position_str = f"{position['lat']} {position['lon']}"
                            printed_positions.add(position_str)
                            
                            break
            except:
                pass
        break

        # try:
            # data['point'] = PointC
            # response = requests.post(url, headers=headers, json=data)

            # response_json = response.json()
            # print(response_json)

        #     for driver in response_json.get('drivers', []):
        #         with open(f"data/ew.txt", 'w') as file:
        #             file.write(str(i) + '\n')
        #             LastSeenTime[i] = time.time()
        #         break
        #         # if driver['id'] not in done_drive:
        #         #     done_drive.add(driver['id'])
        #         #     for position in driver.get('positions', []):
        #         #         position_str = f"{position['lat']} {position['lon']}"
            
        #         #         if position_str not in printed_positions:
        #         #             printed_positions.add(position_str)
        #         #             break
        # except Exception as e:
        #     print(e)
        #     time.sleep(2)
        #     pass



import threading

MinDiff=99.00

print(len(coord))
num = 10

def split_array(array, num_parts):
    part_size = len(array) // num_parts
    remainder = len(array) % num_parts
    
    sub_arrays = []
    start = 0
    for i in range(num_parts):
        end = start + part_size + (1 if i < remainder else 0)
        sub_arrays.append(array[start:end])
        start = end
    
    return sub_arrays


splitted = split_array(coord, 100)
threads = []

for i, item in enumerate(splitted):
    thread = threading.Thread(target=DoUpdate, args=(item, i))
    thread.start() 
    threads.append(thread)

# thread = threading.Thread(target=CheckforUpdate)
# thread.start() 
# threads.append(thread)

for thread in threads:
    thread.join()

# print(split_array(coord, num))


# def Attemp(Funct, arr):
    # threads = []

    # for i in range(len(arr)):
    #     thread = threading.Thread(target=Funct, args=(arr[i], i, ))
    #     thread.start() 
    #     threads.append(thread)

    # for thread in threads:
    #     thread.join()





# while True:
#     coord=divise.Devise(PointA, PointB, 0.02)
#     last = time.time()

#     while (len(done_drive) < 1000):
#         Attemp(DoUpdate, coord)

#     # print(len(printed_positions))
#     SafetoTxt(printed_positions)
#     print(f"{len(done_drive)} {time.time() - last}")
#     time.sleep(1)
#     printed_positions.clear()
#     done_drive.clear()

