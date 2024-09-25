import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv('news_articles.csv')  # Adjust the filename as necessary

# Display the columns to understand the structure
print("Columns in DataFrame:", df.columns.tolist())

# Step 2: Define categories with keywords
categories = {
    'Sports': ['football', 'basketball', 'cricket', 'tennis', 'hockey', 'sports', 'team','cup','bat'],
    'Politics': ['election', 'government', 'policy', 'vote', 'congress', 'senate', 'president','debate'],
    'Technology': ['tech', 'AI', 'software', 'hardware', 'gadget', 'innovation', 'internet'],
    'Health': ['health', 'virus', 'disease', 'treatment', 'vaccine', 'COVID', 'pandemic'],
    'Entertainment': ['movie', 'music', 'celebrity', 'show', 'TV', 'entertainment', 'Hollywood'],
    'Business': ['market', 'business', 'economy', 'finance', 'investment', 'company', 'trade'],
    'World News': ['world', 'international', 'foreign', 'global'],
    'Science': ['science', 'research', 'study', 'discovery', 'environment'],
    'Other': []  # Catch-all category
}

# Step 3: Function to categorize articles based on title
def categorize_article(title):
    title_lower = title.lower()
    for category, keywords in categories.items():
        if any(keyword in title_lower for keyword in keywords):
            print(f"Title: '{title}' categorized as: {category}")  # Debug statement
            return category
    print(f"Title: '{title}' categorized as: Other")  # Debug statement
    return 'Other'  # Default category

# Apply categorization to the DataFrame
df['Category'] = df['Title'].apply(categorize_article)  # Adjust 'Title' based on your column name

# Step 4: Save the results to a new CSV file
output_filename = 'categorized_news_articles.csv'
df.to_csv(output_filename, index=False)

print(f"Categorized articles saved to {output_filename}")
