#!/home/ar4414/miniconda3/bin/python

import requests
import telegram
from asyncio import run
from bs4 import BeautifulSoup

async def sendTelegramMsg(msg):
    apiKey = "6070191251:AAHviXeTzdrkxxFwiOFsar8OoYPFhPp8b0g"
    userId = "5945175982"
    bot = telegram.Bot(token=apiKey)
    await bot.send_message(userId, msg)

def queryLidt():
    url = "https://lidt.co.uk/fast-track-booking"
    with requests.Session() as s:
        res = s.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        centres = soup.find_all("select", attrs={"class":"form-select", "id":"testCentres"})
        locations = [opt1['value'] for opt in centres for opt1 in opt.find_all("option")]
        return list(filter(lambda x : x != "", locations))

availableTests = queryLidt()
viableTestCentres = ["Wood Green", "Tottenham", "Hendon", "Wanstead", "Mill Hill", "Barnet",
        "Wood-Green", "Mill-Hill"] 
if any(any(vtc in at for vtc in viableTestCentres) for at in availableTests):
    print("sent msg")
    run(sendTelegramMsg(availableTests))
