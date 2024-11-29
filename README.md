# Personalized News Recommendation System

## Project Overview

This project is a sophisticated news recommendation system that scrapes news articles from Indian Express, clusters them into topics, and provides personalized article recommendations based on user preferences and mood.

## Features

- Web scraping of news articles from Indian Express
- Topic clustering using K-Means algorithm
- Personalized recommendation using semantic similarity
- User mood and interest-based article suggestions

## Prerequisites

- Python 3.8+
- pip package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/news-recommendation-system.git
cd news-recommendation-system
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- requests
- beautifulsoup4
- pandas
- scikit-learn
- sentence-transformers

## Create a `requirements.txt`
You can generate this by running:
```bash
pip freeze > requirements.txt
```

## Usage

1. Run the script:
```bash
python app.py
```

2. When prompted, enter:
   - Your current mood
   - Your interests (comma-separated)

## How It Works

1. **Web Scraping**: Extracts articles from Indian Express across multiple pages
2. **Embedding**: Converts articles to semantic embeddings
3. **Clustering**: Groups articles into topics using K-Means
4. **Recommendation**: Matches articles to user profile using cosine similarity

## Customization

- Adjust `num_topics` to change the number of topic clusters
- Modify `num_recommendations` to control recommendation count
- Change the embedding model by replacing `'all-MiniLM-L6-v2'`

## Limitations

- Requires internet connection
- Performance depends on web page structure
- Recommendation quality varies with input

## Future Improvements

- Add caching mechanism for scraped articles
- Implement more advanced recommendation algorithms
- Create a web interface
- Add error handling for web scraping

## Contact

Your Name - anirudh.why@example.com

Project Link: [[https://github.com/anirudh-why/news-recommendation-system](https://github.com/anirudh-why/news-recommendation-system)]
