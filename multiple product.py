import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

MY_EMAIL = "YOUR_eMAIL" #Enter your Email  
MY_PASSWORD = "YOUR_PASSWORD" #Enter your PassWord     

urls = [
    {
        "url": "https://www.amazon.in/Airdopes-141-Playtime-Resistance-Bluetooth/dp/B09N3ZNHTY/ref=sr_1_1?_encoding=UTF8&s=electronics&sr=1-1",
        "threshold": 800
    },
    {
        "url": "https://www.amazon.in/Godrej-EDGE-CLS-5-0-GPGR/dp/B0BS6RFKKL/ref=sr_1_2_sspa?_encoding=UTF8&rps=1&s=kitchen&sr=1-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3Nl",
        "threshold": 9900
    }
]

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.8"
}

def send_email(product_name, price, url):
    html_body = f"""
    <html>
        <body>
            <h2>Amazon Price Alert!</h2>
            <p>The price for your product has dropped!</p>
            <p>{product_name}</p>
            <a href="{url}">Click here to view the product</a>
            <p>Current Price: ₹{price:.2f}</p>
            <p>Go check it out before the price changes!</p>
        </body>
    </html>
    """
    msg = EmailMessage()
    msg['Subject'] = "Amazon Price Alert!"
    msg['From'] = MY_EMAIL
    msg['To'] = ", ".join([
        "Sendemail@gmail.com", # More Email Can Add here.

    ])
    # msg['To'] = "mithillobby@gmail.com"
    msg.set_content("This email requires an HTML-compatible email client.")
    msg.add_alternative(html_body, subtype='html')
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.send_message(msg)

any_email_sent = False

for product in urls:
    try:
        response = requests.get(product["url"], headers=header)
        soup = BeautifulSoup(response.content, "html.parser")
        price_tag = soup.find(name="span", class_="a-offscreen")
        if not price_tag:
            print(f"Price not found for {product['url']}")
            continue
        price = price_tag.get_text()
        price_without_currency = price.split("₹")[1]
        remove_comma = price_without_currency.replace(",", "")
        price_as_float = float(remove_comma)
        title_tag = soup.find("title")
        product_name = title_tag.get_text() if title_tag else "No Title"

        print(price_as_float, product_name)

        if price_as_float < product["threshold"]:
            print("Send an email")
            send_email(product_name, price_as_float, product["url"])
            any_email_sent = True
    except Exception as e:
        print(f"Error processing {product['url']}: {e}")

if not any_email_sent:
    print("No email sent")
