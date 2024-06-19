# Article-Analyser
Project : Financial Text Extraction, Summarization and Sentiment Analysis
Project Overview
The Article Analyzer is a Streamlit web application designed to perform text extraction, summarization, and sentiment analysis on articles from the Business Today website. This application leverages web scraping techniques and pre-trained NLP models from the Hugging Face Transformers library to deliver insightful analyses of financial news articles.

Features - 
Text Extraction: Extracts the main content and heading of articles from Business Today URLs.
Text Summarization: Summarizes the extracted article text using the BART model.
Sentiment Analysis: Analyzes the sentiment of the summarized text using the FinBERT model.
Technologies Used
Python: The core programming language.
Streamlit: Framework for creating the interactive web application.
BeautifulSoup: Library for web scraping.
Transformers: Hugging Face library for NLP tasks.
Requests: Library for making HTTP requests.

Project Structure - 
main.py: The main Streamlit application file.
utils.py: Contains utility functions for scraping, summarizing, and sentiment analysis.
requirements.txt: Lists the Python dependencies required for the project.
