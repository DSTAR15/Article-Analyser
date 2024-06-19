import streamlit as st
from bs4 import BeautifulSoup as BS
import requests as req
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

def scrape_article(url):
    try:
        page = req.get(url)
        soup = BS(page.content, "html.parser")

        heading = soup.find('h1').get_text(strip=True) if soup.find('h1') else "Heading not found"
        # st.write(f"Heading: {heading}\n")

        content_dict = {'Heading': heading}

        main_content = ""
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            if 'class' not in paragraph.attrs:
                text = paragraph.get_text(strip=True)
                if text and "For reprint rights: Syndications Today" not in text and "Add Business Today to Home Screen" not in text and "Home" not in text and "Market" not in text and "BT TV" not in text and "Reels" not in text and "Menu" not in text:
                    main_content += text + " "

        content_dict['Content'] = main_content.strip()

        return content_dict
    except Exception as e:
        st.write("An error occurred:", e)
        return None

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def analyze_sentiment(text):
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
    sentiment_analyzer = pipeline("text-classification", model=model, tokenizer=tokenizer)
    sentiment = sentiment_analyzer(text)
    return sentiment