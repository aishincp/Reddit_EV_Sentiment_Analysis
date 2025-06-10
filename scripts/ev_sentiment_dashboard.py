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
st.title("EV Sentiment Analysis using Reddit Posts")
st.markdown("Explore public sentiment and brand discussions in EV-focused Reddit communities.")

# Loading final data with sentiment details
df = pd.read_csv(r"data/reddit_ev_cleaned_sentiment_score_df.csv")

# Prepare date column
df['created_utc'] = pd.to_datetime(df['created_utc'])
df['date'] = df['created_utc'].dt.date

# Sidebar filters
with st.sidebar:
    st.header("Filter by Date Range")
    min_date = df['date'].min()
    max_date = df['date'].max()
    date_range = st.date_input("Select Date Range", [min_date, max_date])
    
    st.header("Filter by Brand")
    unique_brands = sorted(df['brand'].unique())
    brands_multiselect = st.multiselect("Choose Brand(s)", options=["All"] + unique_brands, default=["All"])

    # Determine selected brands for filtering
    if "All" in brands_multiselect or not brands_multiselect:
        selected_brands = unique_brands
    else:
        selected_brands = brands_multiselect

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

    if len(selected_brands) == 1:
        selected_brand_logo = selected_brands[0].lower()
        logo_path = brand_logos.get(selected_brand_logo, brand_logos["unknown"])
        st.image(logo_path, caption=selected_brands[0].capitalize(), width=150)
    else:
        st.image(brand_logos["generic_ev"], caption="Multiple Brands", width=150)

# Filter by selected brands
df = df[df['brand'].isin(selected_brands)]

# Apply date filter
df = df[(df['date'] >= date_range[0]) & (df['date'] <= date_range[1])]

# Summary
st.write(f"Currently showing {len(df)} posts for: **{', '.join(selected_brands)}**")

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
# st.subheader("Top Positive and Negative Comments")


# Positive comments
# st.markdown("#### 👍 Top Positive Comments")
# pos_comments = df[df['sentiment_label'] == 'Positive'].sort_values(by='sentiment_score', ascending=False).head(5)
# for idx, row in pos_comments.iterrows():
#     st.success(f"**{row['brand'].capitalize()}**: {row['full_text'][:300]}...")

# Negative comments
# st.markdown("#### 👎 Top Negative Comments")
# neg_comments = df[df['sentiment_label'] == 'Negative'].sort_values(by='sentiment_score', ascending=False).head(5)
# for idx, row in neg_comments.iterrows():
#     st.error(f"**{row['brand'].capitalize()}**: {row['full_text'][:300]}...")


st.markdown("---", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align: center; color: grey;'>Built with ❤️ by DataInsighTive</p>",
    unsafe_allow_html=True
)




