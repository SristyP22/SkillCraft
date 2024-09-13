import requests
from bs4 import BeautifulSoup
import pandas as pd

# Example URL (replace with your target e-commerce website)
url = "https://example.com/products"

# Fetch the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract product information (adjust selectors as needed)
product_names = [item.text for item in soup.select(".product-name")]
product_prices = [item.text for item in soup.select(".product-price")]
product_ratings = [item.text for item in soup.select(".product-rating")]

# Create a DataFrame
product_data = pd.DataFrame({
    "Name": product_names,
    "Price": product_prices,
    "Rating": product_ratings
})

# Save to CSV
product_data.to_csv("product_info.csv", index=False)

print("Product information saved to product_info.csv")
