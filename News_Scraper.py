import requests
import csv
from bs4 import BeautifulSoup

def scrape_bbc_news(url):
    # URL of the BBC News website
    
    headers = {
        'User-Agent': 'Your User Agent Here',  # Replace with your User-Agent
        'Accept': 'application/json'
    }
    
    # Send a GET request to fetch the page
    response = requests.get(url, headers=headers)
    
    # Initialize a list to hold article data
    articles_data = []

    # Check if the page was fetched successfully
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <h2> tags that are part of news articles
        # articles = soup.find_all('p')
        articles = soup.find_all('h2')
        
        # Print total articles found for debugging
        print(f"Found {len(articles)} <h2> tags.")
        
        # Iterate through each <h2> and extract the title and link
        for article in articles:
            print(f"H2 Content: {article}")  # Print the entire <h2> content for inspection
            
            # Try finding the closest <a> tag in various ways
            a_tag = article.find_previous('a')  # Look for a previous <a> tag
            if not a_tag:
                a_tag = article.find_next('a')  # Look for a next <a> tag

            if a_tag:
                title = article.get_text(strip=True)  # Get the text from the <h2>
                link = a_tag['href']
                
                # Ensure the link is correctly formatted
                if not link.startswith('http'):
                    if 'cnn' in url:
                        link = 'https://edition.cnn.com' + link
                    else:
                        link = 'https://www.bbc.com' + link
                
                # Append the title and link as a tuple to the articles_data list
                if 'cnn' in url:
                        articles_data.append((title, '', '', 'CNN', link))
                else:
                    articles_data.append((title, '', '', 'BBC', link))
                print(f'Title: {title}, Link: {link}')  # Print each article for confirmation
            else:
                print("No <a> tag found associated with this <h2>")
    else:
        print(f"Error: {response.status_code}, {response.text}")
    
    return articles_data  # Return the collected data


if __name__ == "__main__":
    # Open the CSV file and write the header and data
    url1='https://edition.cnn.com/'
    url2 = 'https://www.bbc.com/news'
    with open('news_articles.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Summary', 'Publication Date', 'Source', 'URL'])
        articles = scrape_bbc_news(url1)+scrape_bbc_news(url2)  # Collect data
        if articles:  # Check if articles list is not empty
            writer.writerows(articles)  # Write the rows of data collected from scraping
        else:
            print("No articles found.")
