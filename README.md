ARTICLE ANALYZER - 
Project Overview

Welcome to the **Article Analyzer** project! In this project, I created a web application that extracts, summarizes, and analyzes the sentiment of articles from the Business Today website. The application leverages natural language processing (NLP) techniques and is built using Streamlit, an open-source app framework. The primary goal of this project is to provide a user-friendly interface for extracting and processing textual data from financial news articles.

Features

1. URL Input and Validation:
   - The application allows users to input URLs from the Business Today website.
   - It validates the URL to ensure it belongs to the Business Today domain.

2. Web Scraping:
   - The app scrapes the article's content from the provided URL.
   - It extracts the main heading and content paragraphs while filtering out irrelevant sections.

3. Text Summarization:
   - The app generates a concise summary of the article's content.
   - It uses the BART (Bidirectional and Auto-Regressive Transformers) model for summarization.

4. Sentiment Analysis:
   - The app analyzes the sentiment of the summarized text.
   - It uses the FinBERT model, specifically fine-tuned for financial sentiment analysis, to classify the sentiment as positive, negative, or neutral.

Technical Details

1. Streamlit for Web Interface:
   - Streamlit is used to create the interactive web interface.
   - The app includes text input fields, spinners for loading indicators, and sections to display results.

2. Web Scraping with BeautifulSoup:
   - The `BeautifulSoup` library is used to parse HTML content and extract relevant data from the article's web page.
   - The scraper captures the main heading and body text while excluding non-informative sections like ads and navigation links.

3. Text Summarization with Transformers:
   - The `transformers` library by Hugging Face is used to load and apply the BART model for summarization.
   - The model generates a summary that captures the essence of the article within a specified length.

4. Sentiment Analysis with FinBERT:
   - The `transformers` library is also used to load the FinBERT model and tokenizer.
   - FinBERT, fine-tuned for financial text, is utilized to perform sentiment classification on the summarized text.
   - The sentiment analysis pipeline provides a label (positive, negative, or neutral) and a confidence score for the prediction.

Project Structure - 

- main.py:
  - Contains the Streamlit app logic.
  - Handles user input, calls utility functions, and displays results.

- utils.py:
  - Contains utility functions for web scraping, text summarization, and sentiment analysis.
  - `scrape_article(url)`: Scrapes and processes the article content from the given URL.
  - `summarize_text(text)`: Summarizes the provided text using the BART model.
  - `analyze_sentiment(text)`: Analyzes the sentiment of the provided text using the FinBERT model.

- requirements.txt:
  - Lists all the Python dependencies required to run the project.
  - Includes libraries like `streamlit`, `beautifulsoup4`, `requests`, and `transformers`.


Conclusion - 

This project demonstrates the integration of web scraping, text summarization, and sentiment analysis into a cohesive web application. By leveraging modern NLP techniques and an interactive user interface, the Article Analyzer provides a powerful tool for quickly extracting and understanding key information from financial news articles.

![image](https://github.com/DSTAR15/Article-Analyser/assets/128448451/42fb88f5-3419-4c9b-a59f-ae69e9a01eef)
![image](https://github.com/DSTAR15/Article-Analyser/assets/128448451/02b241e1-493d-48ed-a97a-573fbc6f796c)


