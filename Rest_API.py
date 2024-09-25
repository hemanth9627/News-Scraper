from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)


df = pd.read_csv('categorized_news_articles.csv', encoding='utf-8-sig')

df.columns = df.columns.str.strip()

print("Column Names:", df.columns.tolist()) 
print("NaN Values in Columns:", df.isnull().sum())  

@app.route('/articles', methods=['GET'])
def get_articles():

    category = request.args.get('category')
    filtered_articles = df

    if category:
        filtered_articles = df[df['Category'].str.contains(category, case=False, na=False)]

 
    articles = []
    for index, row in filtered_articles.iterrows():
        articles.append({
            'id': index,
            'Title': row.get('Title'),
            'Summary': row.get('Summary'),
            'Publication Date': row.get('Publication Date'),
            'Source': row.get('Source'),
            'URL': row.get('URL'),
            'Category': row.get('Category'),
        })

    return jsonify(articles)
@app.route('/articles/<int:id>', methods=['GET'])
def get_article_by_id(id):
 
    if id < 0 or id >= len(df):
        return jsonify({'error': 'Article not found'}), 404

    row = df.iloc[id]  
    article = {
        'id': id,
        'Title': row.get('Title'),
        'Summary': row.get('Summary'),
        'Publication Date': row.get('Publication Date'),
        'Source': row.get('Source'),
        'URL': row.get('URL'),
        'Category': row.get('Category'),
    }

    return jsonify(article)


@app.route('/search', methods=['GET'])
def search_articles():
    keyword = request.args.get('keyword')
    
    if not keyword:
        return jsonify({'error': 'No keyword provided'}), 400

   
    df['Title'] = df['Title'].astype(str)
    df['Summary'] = df['Summary'].astype(str)

    
    filtered_articles = df[
        df['Title'].str.contains(keyword, case=False) | 
        df['Summary'].str.contains(keyword, case=False)
    ]

    
    articles = []
    for index, row in filtered_articles.iterrows():
        articles.append({
            'id': index,
            'Title': row.get('Title'),
            'Summary': row.get('Summary'),
            'Publication Date': row.get('Publication Date'),
            'Source': row.get('Source'),
            'URL': row.get('URL'),
            'Category': row.get('Category'),
        })

    return jsonify(articles)


if __name__ == '__main__':
    app.run(debug=True)
