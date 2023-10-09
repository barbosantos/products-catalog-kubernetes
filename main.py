import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://handlaprivatkund.ica.se/stores/1003777/categories?source=navigation"
)
soup = BeautifulSoup(page.content, "html.parser")
soup = soup.find_all("div", {"class", "base__Body-sc-1mnb0pd-34 gRNUPx"})

data = pd.DataFrame(
    columns=["product_name", "description1", "description2", "description3"]
)
for elements in soup:
    new_row = {
        "product_name": elements.contents[0].text,
        "description1": elements.contents[1].text,
        "description2": elements.contents[2].text,
        "description3": elements.contents[3].text,
    }
    data = data._append(new_row, ignore_index=True)

data.to_csv("products.csv", index=False)
# Write the DataFrame to an Excel file
