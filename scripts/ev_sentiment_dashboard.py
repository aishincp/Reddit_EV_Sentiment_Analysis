import streamlit as st
import os
import pandas as pd
import plotly.express as px
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from PIL import Image

base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up one directory


st.set_page_config(
    page_title="Reddit Posts about EV Sentiment Analysis Dashboard", 
    layout="wide",
    page_icon="📊"
    )

# Title
st.title("📊 Electric Vehicle Sentiment Analysis using Reddit Posts")
st.markdown("Explore public sentiment and brand discussions in EV-focused Reddit communities.")

# Load data
df = pd.read_csv(r"C:\Users\yousuf\source\DataAnalysisProjects\AutomotiveProject\dataset\reddit_ev_posts_cleaned_df_sentimentscore.csv")

# Filter by Date
df['created_utc'] = pd.to_datetime(df['created_utc'])
df['date'] = df['created_utc'].dt.date

# Brand filter
brands = ['All'] + sorted(df['brand'].unique())
selected = st.sidebar.selectbox("Filter by Brand", brands)

if selected != 'All':
    df = df[df['brand'] == selected]

# Sidebar filters
with st.sidebar:
    st.header("Filter by Date Range")
    min_date = df['date'].min()
    max_date = df['date'].max()
    date_range = st.date_input("Select Date Range", [min_date, max_date])
    
    st.header("Filter by Brand")
    brands = ['All'] + sorted(df['brand'].unique())
    selected = st.selectbox("Choose a Brand", brands)
    
    st.markdown("---")
    st.header("View Brand Logo")
    # Brand logos mapping
    brand_logos = {
    "tesla": "assets/logos/tesla.png",
    "mercedes": "assets/logos/mercedes.jpeg",
    "bmw": "assets/logos/BMW.png",
    "volkswagen": "assets/logos/vw.jpg",
    "byd": "assets/logos/byd.jpeg",
    "generic_ev": "assets/logos/EV.png",
    "unknown": "assets/logos/unknown.jpg"
    }
    selected_brand = selected if selected != 'All' else 'generic_ev'
    logo_path = brand_logos.get(selected_brand.lower(), "assets/logos/unknown.jpg")
    st.image(logo_path, caption=selected_brand.capitalize(), width=150)
    
    
# Apply date filter
df = df[(df['date'] >= date_range[0]) & (df['date'] <= date_range[1])]

# Apply Brand filter
if selected != 'All':
    df = df[df['brand'] == selected]
    
# Number of posts
st.write(f"Currently showing {len(df)} posts for: **{selected}**")



# Sentiment distribution
st.subheader("Overall Sentiment Distribution")
sent_fig = px.histogram(df, x='sentiment_label', color='sentiment_label', title="Overall Sentiment", width=700)
st.plotly_chart(sent_fig, use_container_width=True)



# Sentiment by brand
st.subheader("🏷 Sentiment Distribution by Brand")
brand_fig = px.histogram(df, x='brand', color='sentiment_label', barmode='group', width=900,
                         title="Sentiment by Brand")
st.plotly_chart(brand_fig, use_container_width=True)


# Sentiment trend over time
st.subheader("Sentiment Trend Over Time")
trend = df.groupby(["date", "sentiment_label"]).size().reset_index(name='count')
line_fig = px.line(trend, x="date", y="count", color="sentiment_label", title="Sentiment Trend Over Time")
st.plotly_chart(line_fig, use_container_width=True)


# Brand mentions
st.subheader("Most Mentioned Brands")
brand_count = df['brand'].value_counts().reset_index()
brand_count.columns = ['brand', 'count']
bar_fig = px.bar(brand_count, x='brand', y='count', title="Brand Mention Frequency", color='brand')
st.plotly_chart(bar_fig, use_container_width=True)

# Top comments
st.subheader("Top Positive and Negative Comments")


# Positive comments
st.markdown("#### 👍 Top Positive Comments")
pos_comments = df[df['sentiment_label'] == 'Positive'].sort_values(by='sentiment_score', ascending=False).head(5)
for idx, row in pos_comments.iterrows():
    st.success(f"**{row['brand'].capitalize()}**: {row['full_text'][:300]}...")

# Negative comments
st.markdown("#### 👎 Top Negative Comments")
neg_comments = df[df['sentiment_label'] == 'Negative'].sort_values(by='sentiment_score', ascending=False).head(5)
for idx, row in neg_comments.iterrows():
    st.error(f"**{row['brand'].capitalize()}**: {row['full_text'][:300]}...")


st.markdown("---")
st.caption("Built with ❤️ using Reddit data, Hugging Face NLP, and Streamlit")




