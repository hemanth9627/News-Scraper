import pandas as pd


df = pd.read_csv('news_articles.csv')  


print("Columns in DataFrame:", df.columns.tolist())


categories = {
    'Sports': ['football', 'basketball', 'cricket', 'tennis', 'hockey', 'sports', 'team','cup','bat'],
    'Politics': ['election', 'government', 'policy', 'vote', 'congress', 'senate', 'president','debate'],
    'Technology': ['tech', 'AI', 'software', 'hardware', 'gadget', 'innovation', 'internet'],
    'Health': ['health', 'virus', 'disease', 'treatment', 'vaccine', 'COVID', 'pandemic'],
    'Entertainment': ['movie', 'music', 'celebrity', 'show', 'TV', 'entertainment', 'Hollywood'],
    'Business': ['market', 'business', 'economy', 'finance', 'investment', 'company', 'trade'],
    'World News': ['world', 'international', 'foreign', 'global'],
    'Science': ['science', 'research', 'study', 'discovery', 'environment'],
    'Other': []  
}


def categorize_article(title):
    title_lower = title.lower()
    for category, keywords in categories.items():
        if any(keyword in title_lower for keyword in keywords):
            print(f"Title: '{title}' categorized as: {category}") 
            return category
    print(f"Title: '{title}' categorized as: Other")  
    return 'Other'  


df['Category'] = df['Title'].apply(categorize_article)  


output_filename = 'categorized_news_articles.csv'
df.to_csv(output_filename, index=False)

print(f"Categorized articles saved to {output_filename}")
