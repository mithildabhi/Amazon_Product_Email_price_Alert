# 🛒 Amazon Product Email Price Alert

Track Amazon product prices and get instant email alerts when your favorite items drop below your desired price!

## ✨ Features

- **Monitor Multiple Products:** Track as many Amazon products as you want by simply adding their URLs and price thresholds.
- **Instant Email Alerts:** Receive a beautifully formatted email when a product’s price drops below your set value.
- **Easy Customization:** Just update the product list and your email credentials—no coding required!
- **Secure & Reliable:** Uses Gmail’s secure SMTP with TLS encryption for sending notifications.

## 🚀 How It Works

1. **Configure Your Products:** Add Amazon product URLs and your target prices in the `urls` list.
2. **Run the Script:** The script checks each product’s current price.
3. **Get Notified:** If the price drops below your threshold, you receive an email alert with product details and a direct link.

## 📝 Usage

1. **Clone the Repository**
    ```
    git clone https://github.com/yourusername/amazon-price-alert.git
    cd amazon-price-alert
    ```

2. **Install Requirements**
    ```
    pip install requests beautifulsoup4
    ```

3. **Edit Your Credentials**
    - Open the script and set your email and app password:
      ```
      MY_EMAIL = "YOUR_EMAIL"
      MY_PASSWORD = "YOUR_PASSWORD"
      ```
    - Update the `urls` list with your desired products and price thresholds.

4. **Run the Script**
    ```
    python amazon_price_alert.py
    ```

## ⚙️ Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

## 📧 Gmail Setup

> **Note:** For Gmail, you may need to generate an [App Password](https://support.google.com/accounts/answer/185833?hl=en) and enable "Allow less secure apps" or use OAuth2 for enhanced security.

## 🛡️ Disclaimer

- This script is for personal use and educational purposes only.
- Frequent scraping may violate Amazon’s terms of service; use responsibly.
- Email credentials are required for sending notifications—keep them secure!


## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

MIT License

---

**Happy saving! 🛍️ If you find this project helpful, give it a ⭐ and share with fellow deal hunters!**

