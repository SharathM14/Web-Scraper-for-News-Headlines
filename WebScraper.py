import requests
from bs4 import BeautifulSoup

# Step 1: Fetch HTML from the news website
url = 'https://www.bbc.com/news'  # You can change this to any news site
response = requests.get(url)
html_content = response.text

# Step 2: Parse HTML and extract headlines
soup = BeautifulSoup(html_content, 'html.parser')

# Try common headline tags like <h2>, <h3>, and <title>
headline_tags = soup.find_all(['h2', 'h3', 'title'])

# Extract and clean text
headlines = [tag.get_text(strip=True) for tag in headline_tags if tag.get_text(strip=True)]

# Step 3: Save headlines to a .txt file
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for idx, headline in enumerate(headlines, start=1):
        file.write(f"{idx}. {headline}\n")

print(f"✅ {len(headlines)} headlines saved to 'a.txt'")
