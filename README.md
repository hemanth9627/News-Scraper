# News Aggregator API

## Overview
The News Aggregator API is a Flask-based application that scrapes, processes, and serves news articles. It provides a RESTful API to retrieve, filter, and search news articles based on various criteria like keywords, categories, or specific article IDs. The project also includes a Postman collection for easy testing of the API endpoints.

## Features
- **Retrieve All Articles**: Fetch a list of all news articles.
- **Search by Keyword**: Search for articles that contain a specific keyword in their title or summary.
- **Filter by Category**: Filter articles based on categories such as "Sports", "Technology", etc.
- **Retrieve by ID**: Get specific articles using their unique IDs.
- **Postman Collection**: A pre-configured collection is provided for easy API testing.

## Prerequisites
Before setting up the project, make sure you have the following installed:
- Python 3.x
- pip (Python package manager)

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/news-aggregator-api.git
cd news-aggregator-api

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt

### Step 3: Running the Application
```bash
python3 Rest_API.py
