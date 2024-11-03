import requests
import numpy as np
import divise, time
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


PointA=[37.584843, 55.758472] #https://www.google.com/maps/place/55.758472+37.584843
PointB=[37.605252, 55.771669] #https://www.google.com/maps/place/55.771669+37.605252

coord=divise.Devise(PointA, PointB, 0.005)

printed_positions = set()
done_drive = set()

DurBetween = 1
UpdateTime = 60
LastSeenTime = [time.time()-DurBetween for _ in range(len(coord))]
LastSeenTime1 = [time.time()-DurBetween for _ in range(len(coord))]
PrevName = int(time.time()//UpdateTime)


from concurrent.futures import ThreadPoolExecutor

def process_point(PointC):
    data['point'] = PointC
    try:
        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()
        
        # LastSeenTime[i] = time.time()
        for driver in response_json.get('drivers', []):
            if driver['id'] not in done_drive:
                done_drive.add(driver['id'])
                for position in driver.get('positions', []):
                    position_str = f"{position['lat']} {position['lon']}"
                    printed_positions.add(position_str)
                    break
                    # print(position_str) 

    except Exception as e:
        print(PointC)
        process_point(PointC)
        pass

def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_point, Points)


while True:
    Points = coord
    LastSeenTime = [None] * len(Points)
    done_drive = set()
    printed_positions = set()
    
    main()

    # print(len(printed_positions))
    current_time_str = int(time.time())
    filename = f"data/{current_time_str}.txt"
    with open(filename, 'a') as f:
        f.write("\n".join(printed_positions))

    print(f"{int(time.time())} {len(done_drive)}")

    printed_positions.clear()
    done_drive.clear()