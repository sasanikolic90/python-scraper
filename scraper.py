import requests
from bs4 import BeautifulSoup
import smtplib, ssl
from email.message import EmailMessage

 # Port for SSL.
port = 465 
smtp_server = "smtp.gmail.com"
# Construct email.
email = EmailMessage()
email['Subject'] = 'Canyon bikes'
email['From'] = "6rodney6@gmail.com"
email['To'] = "6rodney6@gmail.com"

URL = 'https://www.canyon.com/en-si/outlet/road-bikes/?cgid=outlet-road&prefn1=pc_familie&prefn2=pc_rahmengroesse&prefv1=Ultimate&prefv2=XL'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Find the bikes.
bikes = soup.find_all('li', class_='productGrid__listItem')

count=0
msg = ''
for bike in bikes:
    count += 1
    # Each bike is a new BeautifulSoup object.
    title_elem = bike.find('div', class_='productTile__productName')
    price_elem = bike.find('div', class_='productTile__priceSale')
    msg += title_elem.text.strip() + ': <strong>' + price_elem.text.strip() + '</strong><br>'

email.set_content('The bikes available are ' + str(count) + ':<br> ' + msg, subtype='html')

# Let the user enter the email password.
password = input("Type your password and press enter: ")

# Create a secure SSL context and send the email.
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(email['From'], password)
    server.send_message(email)

# Success message.
print('Email was sent to ' + email['To'])
