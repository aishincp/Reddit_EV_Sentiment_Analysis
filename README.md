# Reddit_EV_Sentiment_Analysis
Explore public sentiment and brand discussions in EV-focused Reddit communities using Reddit API, NLP, Streamlit, Azure Databricks, and Spark 

## Reddit EV Sentiment Dashboard
An interactive Streamlit web application that analyzes public sentiment around electric vehicles (EVs) using Reddit discussions. This project utilizes NLP and visualization techniques to compare brand perceptions across Tesla, Mercedes-Benz, BMW, Volkswagen, BYD, and other brands.

 
*Explore how users feel about electric cars, how sentiment changes over time, and what topics generate the most discussion, all based on real Reddit data.*

---

#### Screenshot

[Dashboard Preview](https://github.com/aishincp/Reddit_EV_Sentiment_Analysis/blob/main/assets/dashboard/Dashboard_Preview.pdf)

---

#### Live Demo

Try the app here: [Link](https://redditevsentimentanalysis-nc9xroxdw3ysnmpfxchmum.streamlit.app/)


#### Tech Stack
---
- Python
- Streamlit – for building the web dashboard
- Pandas – for data processing
- Plotly – for interactive charts
- Hugging Face Transformers – for sentiment classification
- Reddit API (PRAW) – to collect Reddit discussions
- Azure Blob (planned) – for cloud data storage
- Databricks / PySpark (planned) – for scalable processing

#### What Does This Dashboard Answer?

1. The project explores key questions like:
2. What is the overall sentiment towards electric vehicles on Reddit?
3. How does sentiment vary across different EV brands?
4. What are the most positive and negative comments users are sharing?
5. How has sentiment evolved (last 6–12 months)?

#### Which brands are most frequently discussed?

Highlights:
- Uses real Reddit data to reflect public perception of EVs
- Pretrained transformer model for accurate sentiment classification
- Brand tagging and filtering included
- Fully interactive and mobile-friendly dashboard
- Ready for cloud deployment and enterprise use case simulation

#### Optional Enhancements (Coming Soon)

- GPT-powered summarization of top comments
- Automated pipelines using Azure Data Factory
- Power BI or Streamlit Cloud deployment options
- Dockerized FastAPI version for serving the model as an API
