import requests
from bs4 import BeautifulSoup

# URL of the news website (BBC as an example)
url = 'https://www.bbc.com/news'

# Set up headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept': 'text/html'
}

# Fetch the page
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all h2 tags
    articles = soup.find_all('h2')

    for article in articles:
        title = article.get_text().strip()  # Get the text and strip whitespace
        link = article.find_parent('a', href=True)  # Look for the parent <a> tag
        if link:
            article_url = link['href']
            # Check if the URL is relative or absolute
            if not article_url.startswith('http'):
                article_url = 'https://www.bbc.com' + article_url  # Construct full URL
            print(f"Title: {title}, Link: {article_url}")
else:
    print(f"Error: {response.status_code}, {response.text}")
