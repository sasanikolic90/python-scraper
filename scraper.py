import requests
from bs4 import BeautifulSoup
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "6rodney6@gmail.com"
receiver_email = "6rodney6@gmail.com"
message = """\
Subject: Canyon bikes

The bikes available are: \n"""

URL = 'https://www.canyon.com/en-si/outlet/road-bikes/?cgid=outlet-road&prefn1=pc_familie&prefn2=pc_rahmengroesse&prefv1=Ultimate&prefv2=XL'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

bikes = soup.find_all('li', class_='productGrid__listItem')

count=0
for bike in bikes:
    count += 1
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = bike.find('div', class_='productTile__productName')
    price_elem = bike.find('div', class_='productTile__priceSale')
    message += title_elem.text.strip() + ':' + price_elem.text.strip() + '\n'

# Send email here
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.encode('utf-8'))