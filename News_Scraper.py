import requests
import csv
from bs4 import BeautifulSoup

def scrape_bbc_news(url):
    
    
    headers = {
        'User-Agent': 'Your User Agent Here',  
        'Accept': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    
    
    articles_data = []

    
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        
        articles = soup.find_all('h2')
        
        
        print(f"Found {len(articles)} <h2> tags.")
        
        
        for article in articles:
            print(f"H2 Content: {article}")  
            
           
            a_tag = article.find_previous('a')  
            if not a_tag:
                a_tag = article.find_next('a')  

            if a_tag:
                title = article.get_text(strip=True)  
                link = a_tag['href']
                
                
                if not link.startswith('http'):
                    if 'cnn' in url:
                        link = 'https://edition.cnn.com' + link
                    else:
                        link = 'https://www.bbc.com' + link
                
                
                if 'cnn' in url:
                        articles_data.append((title, '', '', 'CNN', link))
                else:
                    articles_data.append((title, '', '', 'BBC', link))
                print(f'Title: {title}, Link: {link}')  
            else:
                print("No <a> tag found associated with this <h2>")
    else:
        print(f"Error: {response.status_code}, {response.text}")
    
    return articles_data  


if __name__ == "__main__":
    
    url1='https://edition.cnn.com/'
    url2 = 'https://www.bbc.com/news'
    with open('news_articles.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Summary', 'Publication Date', 'Source', 'URL'])
        articles = scrape_bbc_news(url1)+scrape_bbc_news(url2)  
        if articles:  
            writer.writerows(articles)  
        else:
            print("No articles found.")
