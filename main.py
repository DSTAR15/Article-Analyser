import streamlit as st
import logging
from utils import scrape_article, summarize_text, analyze_sentiment

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO

# Streamlit app title
st.title("ARTICLE ANALYZER")

# Text input for URL
url = st.text_input("", placeholder="Please enter Business Today URL:")

# Main logic based on URL input
if url:
    if "businesstoday.in" in url:
        logging.info("Valid URL entered: %s", url)

        # Scraping the article
        with st.spinner("Scraping the article..."):
            logging.info("Scraping the article from URL: %s", url)
            content_dict = scrape_article(url)

        # If content successfully scraped
        if content_dict:
            st.subheader("Article Content")
            st.markdown(f"<h3 style='color: white;'> {content_dict['Heading']}</h3>", unsafe_allow_html=True)
            st.write(content_dict['Content'])

            # Summarizing the article
            with st.spinner("Summarizing the article..."):
                logging.info("Summarizing the article content...")
                summary = summarize_text(content_dict['Content'])
            st.subheader("Summary")
            st.write(summary)

            # Analyzing sentiment of the summary
            with st.spinner("Analyzing sentiment..."):
                logging.info("Analyzing sentiment...")
                sentiment = analyze_sentiment(summary)

            # Displaying sentiment analysis results
            st.subheader("Sentiment Analysis")
            if sentiment:
                for result in sentiment:
                    label = result['label']
                    score = result['score']
                    st.write(f"**Sentiment:** {label}")
                    st.write(f"**Confidence Score:** {score:.2f}")
    else:
        st.markdown("<p style='color: red; font-weight: bold;'>&#x26A0; INVALID URL</p>", unsafe_allow_html=True)
        logging.warning("Invalid URL entered: %s", url)
else:
    st.write("Please enter a valid URL to get started.")
