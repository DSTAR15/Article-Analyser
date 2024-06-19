import streamlit as st
from utils import scrape_article, summarize_text, analyze_sentiment

st.title("FIN LENS")

url = st.text_input("Please enter Business Today URL:")

if url:
    if "businesstoday.in" in url:
        with st.spinner("Scraping the article..."):
            content_dict = scrape_article(url)

        if content_dict:
            st.subheader("Article Content")
            st.markdown(f"<h3 style='color: white;'> {content_dict['Heading']}</h3>", unsafe_allow_html=True)
            st.write(content_dict['Content'])

            with st.spinner("Summarizing the article..."):
                summary = summarize_text(content_dict['Content'])
            st.subheader("Summary")
            st.write(summary)

            with st.spinner("Analyzing sentiment..."):
                sentiment = analyze_sentiment(summary)

            st.subheader("Sentiment Analysis")
            if sentiment:
                for result in sentiment:
                    label = result['label']
                    score = result['score']
                    st.write(f"**Sentiment:** {label}")
                    st.write(f"**Confidence Score:** {score:.2f}")
    else:
        st.markdown("<p style='color: red; font-weight: bold;'>ERROR MESSAGE: INVALID URL</p>", unsafe_allow_html=True)
else:
    st.write("Please enter a valid URL to get started.")
