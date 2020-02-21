import requests
from bs4 import BeautifulSoup
import smtplib
import schedule
import time

URL = 'https://www.amazon.ca/Logitech%C2%AE-Master-Wireless-Graphite-910-005131/dp/B071YZJ1G1/ref=sr_1_3?crid=BWH318H2WY5H&keywords=logitech%2Bmx%2Bmaster%2B2s&qid=1582087046&sprefix=logitech%2Bmx%2B%2Caps%2C227&sr=8-3&th=1'

headers = {
    "User-Agent":
    '### your user agent ###'
}


def check_price():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[5:10])

    if (converted_price < 60):
        send_email()

    print(converted_price)
    print(title.strip())


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('### your email ###', '### your email password ###')

    Subject = ' Time to buy the logitech mx master now! '
    body = ' Check the link in here.        https://www.amazon.ca/Logitech%C2%AE-Master-Wireless-Graphite-910-005131/dp/B071YZJ1G1/ref=sr_1_3?crid=BWH318H2WY5H&keywords=logitech%2Bmx%2Bmaster%2B2s&qid=1582087046&sprefix=logitech%2Bmx%2B%2Caps%2C227&sr=8-3&th=1'

    msg = f"Subject: {Subject} \n\n {body}"

    server.sendmail('### your email ###', '### your email ###', msg)

    print(' Email sent! ')

    server.quit()


schedule.every().day.at("12:27").do(check_price)

while True:
    schedule.run_pending()
    time.sleep(1)