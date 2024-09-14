import requests
from bs4 import BeautifulSoup
import pandas as pd

# Example URL (replace with your target e-commerce website)
url = "http://books.toscrape.com/"

# Conversion rate from GBP (used in this site) to INR (you can adjust this rate for CNY to INR)
GBP_TO_INR_RATE = 102.5  # Update to the latest rate if needed

# Fetch the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract product information
product_names = [item.text.strip() for item in soup.select("h3 a")]
product_prices_gbp = [item.text.strip() for item in soup.select(".price_color")]

# Convert prices from GBP to INR
product_prices_inr = []
for price in product_prices_gbp:
    # Assuming the price is in the format '£51.77', remove the '£' and convert to float
    price_gbp = float(price.replace('£', '').strip())
    # Convert the price from GBP to INR
    price_inr = price_gbp * GBP_TO_INR_RATE
    product_prices_inr.append(f"₹{price_inr:.2f}")  # Format as INR

# Extract product ratings (if available)
product_ratings = [item['class'][1] for item in soup.select(".star-rating")]

# Print the data to ensure correctness
print("Product Names: ", product_names)
print("Product Prices (INR): ", product_prices_inr)
print("Product Ratings: ", product_ratings)

# Create a DataFrame
product_data = pd.DataFrame({
    "Name": product_names,
    "Price (INR)": product_prices_inr,
    "Rating": product_ratings
})

# Save to CSV
product_data.to_csv("product_info_inr.csv", index=False)

print("Product information with INR prices saved to product_info_inr.csv")
