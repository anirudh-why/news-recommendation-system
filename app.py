import requests
from bs4 import BeautifulSoup

def scrape_page(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', class_='articles')
    page_data = []

    for article in articles:
        title_element = article.find('div', class_='title')
        title = title_element.get_text(strip=True) if title_element else 'N/A'
        
        url_element = title_element.find('a') if title_element else None
        article_url = url_element['href'] if url_element else 'N/A'
        
        description_element = article.find('p')
        description = description_element.get_text(strip=True) if description_element else 'N/A'
        
        date_element = article.find('div', class_='date')
        date = date_element.get_text(strip=True) if date_element else 'N/A'
        
        page_data.append({
            'title': title,
            'url': article_url,
            'description': description,
            'date': date
        })

    return page_data 

def scrape_all_pages(base_url, total_pages):
    all_articles = []

    for page in range(1, total_pages + 1):
        page_url = f"{base_url}/page/{page}/"
        print(f"Scraping page: {page_url}")
        page_articles = scrape_page(page_url)
        all_articles.extend(page_articles)

    return all_articles

base_url = "https://indianexpress.com/latest-news"

total_pages = 10

all_articles = scrape_all_pages(base_url, total_pages)

for article in all_articles:
    print(f"Title: {article['title']}")
    print(f"URL: {article['url']}")
    print(f"Description: {article['description']}")
    print(f"Date: {article['date']}\n")


##### webscraping done



import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


all_articles = pd.DataFrame(all_articles)

model = SentenceTransformer('all-MiniLM-L6-v2') 


all_articles['content'] = all_articles['title'] + " " + all_articles['description']
all_articles['embedding'] = all_articles['content'].apply(lambda x: model.encode(x))


num_topics = 10
kmeans = KMeans(n_clusters=num_topics, random_state=0)
all_articles['topic'] = kmeans.fit_predict(list(all_articles['embedding']))


def get_user_preferences():
    mood = input("Enter your mood (e.g., happy, curious, serious): ").strip().lower()
    interests = input("Enter your interests, separated by commas: ").strip().lower().split(",")
    return mood, [interest.strip() for interest in interests]


def create_user_profile(interests):
    interests_embedding = model.encode(" ".join(interests))
    return interests_embedding


def recommend_articles(user_profile, mood, num_recommendations=10):

    all_articles['similarity'] = all_articles['embedding'].apply(lambda x: cosine_similarity([user_profile], [x])[0][0])

    recommended_articles = all_articles.sort_values(by='similarity', ascending=False).head(num_recommendations)
    return recommended_articles


user_mood, user_interests = get_user_preferences()
user_profile = create_user_profile(user_interests)


recommended_articles = recommend_articles(user_profile, user_mood)


for _, article in recommended_articles.iterrows():
    print(f"Title: {article['title']}")
    print(f"URL: {article['url']}")
    print(f"Description: {article['description']}")
    print(f"Date: {article['date']}")
    print(f"Topic: {article['topic']}\n")