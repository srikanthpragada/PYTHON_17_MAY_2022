import requests

resp = requests.get("http://worldtimeapi.org/api/timezone/Asia/Kolkata")
if resp.status_code != 200:
    print('Sorry! Could not get UTC and local date and time!')
    exit()

details = resp.json()
print('UTC ' , details['utc_datetime'])
print('IST ' , details['datetime'])
