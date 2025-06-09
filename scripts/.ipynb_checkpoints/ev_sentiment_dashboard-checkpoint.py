{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1a79e4da-6497-4816-9f47-4332f304d5c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (1.30.0)\n",
      "Requirement already satisfied: pandas in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (2.2.3)\n",
      "Requirement already satisfied: plotly in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (5.9.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: importlib-metadata<8,>=1.4 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (7.0.1)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (23.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (10.4.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\users\\yousuf\\appdata\\roaming\\python\\python311\\site-packages (from streamlit) (4.25.3)\n",
      "Requirement already satisfied: pyarrow>=6.0 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (18.0.0)\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\yousuf\\appdata\\roaming\\python\\python311\\site-packages (from streamlit) (13.7.1)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: tzlocal<6,>=1.1 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (2.1)\n",
      "Requirement already satisfied: validators<1,>=0.2 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (0.18.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (3.1.37)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (6.3.3)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from pandas) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: toolz in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from importlib-metadata<8,>=1.4->streamlit) (3.17.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.17.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\yousuf\\appdata\\roaming\\python\\python311\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\yousuf\\appdata\\roaming\\python\\python311\\site-packages (from requests<3,>=2.27->streamlit) (3.6)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\yousuf\\appdata\\roaming\\python\\python311\\site-packages (from requests<3,>=2.27->streamlit) (2.2.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\yousuf\\appdata\\roaming\\python\\python311\\site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\yousuf\\appdata\\roaming\\python\\python311\\site-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\yousuf\\appdata\\roaming\\python\\python311\\site-packages (from rich<14,>=10.14.0->streamlit) (2.17.2)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from validators<1,>=0.2->streamlit) (5.1.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\yousuf\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.0 -> 25.1.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit pandas plotly\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e056488b-7ed4-4146-a59d-fb9e7b4a54cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import os\n",
    "import pandas as pd\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "68131b96-29bb-45f9-9714-af809be5ff43",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.set_page_config(page_title=\"Reddit Posts about EV Sentiment Analysis Dashboard\", layout=\"wide\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2335b859-a49f-4893-8ca9-08b0ae9e6d03",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Title\n",
    "st.title(\"Electric Vehicle Sentiment Analysis on Reddit\")\n",
    "st.markdown(\"Explore public sentiment and brand discussions in EV-focused Reddit communities.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "21a2cc5c-4877-4712-bb5d-2602afeaefcf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>subreddit</th>\n",
       "      <th>title</th>\n",
       "      <th>selftext</th>\n",
       "      <th>created_utc</th>\n",
       "      <th>upvotes</th>\n",
       "      <th>num_comments</th>\n",
       "      <th>url</th>\n",
       "      <th>full_text</th>\n",
       "      <th>clean_text</th>\n",
       "      <th>brand</th>\n",
       "      <th>sentiment_label</th>\n",
       "      <th>sentiment_score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>electricvehicles</td>\n",
       "      <td>Audi Went To China To Build Cars. China Rebuil...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2025-06-02 14:34:41</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>https://insideevs.com/news/761013/china-audi-r...</td>\n",
       "      <td>Audi Went To China To Build Cars. China Rebuil...</td>\n",
       "      <td>audi went to china to build cars china rebuilt...</td>\n",
       "      <td>unknown</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>0.514342</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>electricvehicles</td>\n",
       "      <td>What can we actually do with EV batteries once...</td>\n",
       "      <td>Hey everyone,\\n\\nI’m exploring the idea of reu...</td>\n",
       "      <td>2025-06-02 12:41:52</td>\n",
       "      <td>2</td>\n",
       "      <td>9</td>\n",
       "      <td>https://www.reddit.com/r/electricvehicles/comm...</td>\n",
       "      <td>What can we actually do with EV batteries once...</td>\n",
       "      <td>what can we actually do with ev batteries once...</td>\n",
       "      <td>generic_ev</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>0.572889</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          subreddit                                              title  \\\n",
       "0  electricvehicles  Audi Went To China To Build Cars. China Rebuil...   \n",
       "1  electricvehicles  What can we actually do with EV batteries once...   \n",
       "\n",
       "                                            selftext          created_utc  \\\n",
       "0                                                NaN  2025-06-02 14:34:41   \n",
       "1  Hey everyone,\\n\\nI’m exploring the idea of reu...  2025-06-02 12:41:52   \n",
       "\n",
       "   upvotes  num_comments                                                url  \\\n",
       "0        5             0  https://insideevs.com/news/761013/china-audi-r...   \n",
       "1        2             9  https://www.reddit.com/r/electricvehicles/comm...   \n",
       "\n",
       "                                           full_text  \\\n",
       "0  Audi Went To China To Build Cars. China Rebuil...   \n",
       "1  What can we actually do with EV batteries once...   \n",
       "\n",
       "                                          clean_text       brand  \\\n",
       "0  audi went to china to build cars china rebuilt...     unknown   \n",
       "1  what can we actually do with ev batteries once...  generic_ev   \n",
       "\n",
       "  sentiment_label  sentiment_score  \n",
       "0         Neutral         0.514342  \n",
       "1         Neutral         0.572889  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Load data\n",
    "df = pd.read_csv(r\"C:\\Users\\yousuf\\source\\DataAnalysisProjects\\AutomotiveProject\\dataset\\reddit_ev_posts_cleaned_df_sentimentscore.csv\")\n",
    "df.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "afa704d8-d82c-435d-86ac-78596d70608d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['created_utc'] = pd.to_datetime(df['created_utc'])\n",
    "df['date'] = df['created_utc'].dt.date\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "97ea6bfc-4899-43fd-987e-7e1512555930",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>subreddit</th>\n",
       "      <th>title</th>\n",
       "      <th>selftext</th>\n",
       "      <th>created_utc</th>\n",
       "      <th>upvotes</th>\n",
       "      <th>num_comments</th>\n",
       "      <th>url</th>\n",
       "      <th>full_text</th>\n",
       "      <th>clean_text</th>\n",
       "      <th>brand</th>\n",
       "      <th>sentiment_label</th>\n",
       "      <th>sentiment_score</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>electricvehicles</td>\n",
       "      <td>Audi Went To China To Build Cars. China Rebuil...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2025-06-02 14:34:41</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>https://insideevs.com/news/761013/china-audi-r...</td>\n",
       "      <td>Audi Went To China To Build Cars. China Rebuil...</td>\n",
       "      <td>audi went to china to build cars china rebuilt...</td>\n",
       "      <td>unknown</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>0.514342</td>\n",
       "      <td>2025-06-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>electricvehicles</td>\n",
       "      <td>What can we actually do with EV batteries once...</td>\n",
       "      <td>Hey everyone,\\n\\nI’m exploring the idea of reu...</td>\n",
       "      <td>2025-06-02 12:41:52</td>\n",
       "      <td>2</td>\n",
       "      <td>9</td>\n",
       "      <td>https://www.reddit.com/r/electricvehicles/comm...</td>\n",
       "      <td>What can we actually do with EV batteries once...</td>\n",
       "      <td>what can we actually do with ev batteries once...</td>\n",
       "      <td>generic_ev</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>0.572889</td>\n",
       "      <td>2025-06-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>electricvehicles</td>\n",
       "      <td>General Questions and Purchasing Advice Thread...</td>\n",
       "      <td>**Need help choosing an EV, finding a home cha...</td>\n",
       "      <td>2025-06-02 14:00:58</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>https://www.reddit.com/r/electricvehicles/comm...</td>\n",
       "      <td>General Questions and Purchasing Advice Thread...</td>\n",
       "      <td>general questions and purchasing advice thread...</td>\n",
       "      <td>generic_ev</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>0.618695</td>\n",
       "      <td>2025-06-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>electricvehicles</td>\n",
       "      <td>EV Batteries Got 20% Cheaper Last Year</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2025-06-02 13:55:19</td>\n",
       "      <td>97</td>\n",
       "      <td>13</td>\n",
       "      <td>https://insideevs.com/news/761338/ev-battery-c...</td>\n",
       "      <td>EV Batteries Got 20% Cheaper Last Year</td>\n",
       "      <td>ev batteries got 20 cheaper last year</td>\n",
       "      <td>generic_ev</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>0.600215</td>\n",
       "      <td>2025-06-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>electricvehicles</td>\n",
       "      <td>Thoughts on Automakers having control over you...</td>\n",
       "      <td>There has been a recent uproar regarding Zeekr...</td>\n",
       "      <td>2025-06-02 09:47:23</td>\n",
       "      <td>8</td>\n",
       "      <td>17</td>\n",
       "      <td>https://www.reddit.com/r/electricvehicles/comm...</td>\n",
       "      <td>Thoughts on Automakers having control over you...</td>\n",
       "      <td>thoughts on automakers having control over you...</td>\n",
       "      <td>generic_ev</td>\n",
       "      <td>Negative</td>\n",
       "      <td>0.649813</td>\n",
       "      <td>2025-06-02</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          subreddit                                              title  \\\n",
       "0  electricvehicles  Audi Went To China To Build Cars. China Rebuil...   \n",
       "1  electricvehicles  What can we actually do with EV batteries once...   \n",
       "2  electricvehicles  General Questions and Purchasing Advice Thread...   \n",
       "3  electricvehicles             EV Batteries Got 20% Cheaper Last Year   \n",
       "4  electricvehicles  Thoughts on Automakers having control over you...   \n",
       "\n",
       "                                            selftext         created_utc  \\\n",
       "0                                                NaN 2025-06-02 14:34:41   \n",
       "1  Hey everyone,\\n\\nI’m exploring the idea of reu... 2025-06-02 12:41:52   \n",
       "2  **Need help choosing an EV, finding a home cha... 2025-06-02 14:00:58   \n",
       "3                                                NaN 2025-06-02 13:55:19   \n",
       "4  There has been a recent uproar regarding Zeekr... 2025-06-02 09:47:23   \n",
       "\n",
       "   upvotes  num_comments                                                url  \\\n",
       "0        5             0  https://insideevs.com/news/761013/china-audi-r...   \n",
       "1        2             9  https://www.reddit.com/r/electricvehicles/comm...   \n",
       "2        1             0  https://www.reddit.com/r/electricvehicles/comm...   \n",
       "3       97            13  https://insideevs.com/news/761338/ev-battery-c...   \n",
       "4        8            17  https://www.reddit.com/r/electricvehicles/comm...   \n",
       "\n",
       "                                           full_text  \\\n",
       "0  Audi Went To China To Build Cars. China Rebuil...   \n",
       "1  What can we actually do with EV batteries once...   \n",
       "2  General Questions and Purchasing Advice Thread...   \n",
       "3            EV Batteries Got 20% Cheaper Last Year    \n",
       "4  Thoughts on Automakers having control over you...   \n",
       "\n",
       "                                          clean_text       brand  \\\n",
       "0  audi went to china to build cars china rebuilt...     unknown   \n",
       "1  what can we actually do with ev batteries once...  generic_ev   \n",
       "2  general questions and purchasing advice thread...  generic_ev   \n",
       "3              ev batteries got 20 cheaper last year  generic_ev   \n",
       "4  thoughts on automakers having control over you...  generic_ev   \n",
       "\n",
       "  sentiment_label  sentiment_score        date  \n",
       "0         Neutral         0.514342  2025-06-02  \n",
       "1         Neutral         0.572889  2025-06-02  \n",
       "2         Neutral         0.618695  2025-06-02  \n",
       "3         Neutral         0.600215  2025-06-02  \n",
       "4        Negative         0.649813  2025-06-02  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "db515f78-c595-44a6-8b1b-048ad41e0c1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sidebar filters\n",
    "with st.sidebar:\n",
    "    st.header(\"Filter by Date Range\")\n",
    "    min_date = df['date'].min()\n",
    "    max_date = df['date'].max()\n",
    "    date_range = st.date_input(\"Select Date Range\", [min_date, max_date])\n",
    "\n",
    "# Apply date filter\n",
    "df = df[(df['date'] >= date_range[0]) & (df['date'] <= date_range[1])]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "7af7d7c9-34d1-4dd9-bf7c-072e9d301201",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>subreddit</th>\n",
       "      <th>title</th>\n",
       "      <th>selftext</th>\n",
       "      <th>created_utc</th>\n",
       "      <th>upvotes</th>\n",
       "      <th>num_comments</th>\n",
       "      <th>url</th>\n",
       "      <th>full_text</th>\n",
       "      <th>clean_text</th>\n",
       "      <th>brand</th>\n",
       "      <th>sentiment_label</th>\n",
       "      <th>sentiment_score</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>electricvehicles</td>\n",
       "      <td>Audi Went To China To Build Cars. China Rebuil...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2025-06-02 14:34:41</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>https://insideevs.com/news/761013/china-audi-r...</td>\n",
       "      <td>Audi Went To China To Build Cars. China Rebuil...</td>\n",
       "      <td>audi went to china to build cars china rebuilt...</td>\n",
       "      <td>unknown</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>0.514342</td>\n",
       "      <td>2025-06-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>electricvehicles</td>\n",
       "      <td>What can we actually do with EV batteries once...</td>\n",
       "      <td>Hey everyone,\\n\\nI’m exploring the idea of reu...</td>\n",
       "      <td>2025-06-02 12:41:52</td>\n",
       "      <td>2</td>\n",
       "      <td>9</td>\n",
       "      <td>https://www.reddit.com/r/electricvehicles/comm...</td>\n",
       "      <td>What can we actually do with EV batteries once...</td>\n",
       "      <td>what can we actually do with ev batteries once...</td>\n",
       "      <td>generic_ev</td>\n",
       "      <td>Neutral</td>\n",
       "      <td>0.572889</td>\n",
       "      <td>2025-06-02</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          subreddit                                              title  \\\n",
       "0  electricvehicles  Audi Went To China To Build Cars. China Rebuil...   \n",
       "1  electricvehicles  What can we actually do with EV batteries once...   \n",
       "\n",
       "                                            selftext         created_utc  \\\n",
       "0                                                NaN 2025-06-02 14:34:41   \n",
       "1  Hey everyone,\\n\\nI’m exploring the idea of reu... 2025-06-02 12:41:52   \n",
       "\n",
       "   upvotes  num_comments                                                url  \\\n",
       "0        5             0  https://insideevs.com/news/761013/china-audi-r...   \n",
       "1        2             9  https://www.reddit.com/r/electricvehicles/comm...   \n",
       "\n",
       "                                           full_text  \\\n",
       "0  Audi Went To China To Build Cars. China Rebuil...   \n",
       "1  What can we actually do with EV batteries once...   \n",
       "\n",
       "                                          clean_text       brand  \\\n",
       "0  audi went to china to build cars china rebuilt...     unknown   \n",
       "1  what can we actually do with ev batteries once...  generic_ev   \n",
       "\n",
       "  sentiment_label  sentiment_score        date  \n",
       "0         Neutral         0.514342  2025-06-02  \n",
       "1         Neutral         0.572889  2025-06-02  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "faf44367-141c-4caf-9703-5eaa8b0b8883",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\yousuf\\anaconda3\\Lib\\site-packages\\plotly\\express\\_core.py:1979: FutureWarning: When grouping with a length-1 list-like, you will need to pass a length-1 tuple to get_group in a future version of pandas. Pass `(name,)` instead of `name` to silence this warning.\n",
      "  sf: grouped.get_group(s if len(s) > 1 else s[0])\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Sentiment distribution\n",
    "st.subheader(\"Overall Sentiment Distribution\")\n",
    "sent_fig = px.histogram(df, x='sentiment_label', color='sentiment_label', title=\"Overall Sentiment\", width=700)\n",
    "st.plotly_chart(sent_fig, use_container_width=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f6cafb62-0b83-45a7-a010-323add38ab24",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\yousuf\\anaconda3\\Lib\\site-packages\\plotly\\express\\_core.py:1979: FutureWarning:\n",
      "\n",
      "When grouping with a length-1 list-like, you will need to pass a length-1 tuple to get_group in a future version of pandas. Pass `(name,)` instead of `name` to silence this warning.\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Sentiment by brand\n",
    "st.subheader(\"🏷 Sentiment Distribution by Brand\")\n",
    "brand_fig = px.histogram(df, x='brand', color='sentiment_label', barmode='group', width=900,\n",
    "                         title=\"Sentiment by Brand\")\n",
    "st.plotly_chart(brand_fig, use_container_width=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "976323e1-0ce3-4162-ab58-d204a0607545",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\yousuf\\anaconda3\\Lib\\site-packages\\plotly\\express\\_core.py:1979: FutureWarning:\n",
      "\n",
      "When grouping with a length-1 list-like, you will need to pass a length-1 tuple to get_group in a future version of pandas. Pass `(name,)` instead of `name` to silence this warning.\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Sentiment trend over time\n",
    "st.subheader(\"Sentiment Trend Over Time\")\n",
    "trend = df.groupby([\"date\", \"sentiment_label\"]).size().reset_index(name='count')\n",
    "line_fig = px.line(trend, x=\"date\", y=\"count\", color=\"sentiment_label\", title=\"Sentiment Trend Over Time\")\n",
    "st.plotly_chart(line_fig, use_container_width=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "aa4424c4-8758-489a-aa0a-9dae401ccc24",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\yousuf\\anaconda3\\Lib\\site-packages\\plotly\\express\\_core.py:1979: FutureWarning:\n",
      "\n",
      "When grouping with a length-1 list-like, you will need to pass a length-1 tuple to get_group in a future version of pandas. Pass `(name,)` instead of `name` to silence this warning.\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Brand mentions\n",
    "st.subheader(\"Most Mentioned Brands\")\n",
    "brand_count = df['brand'].value_counts().reset_index()\n",
    "brand_count.columns = ['brand', 'count']\n",
    "bar_fig = px.bar(brand_count, x='brand', y='count', title=\"Brand Mention Frequency\", color='brand')\n",
    "st.plotly_chart(bar_fig, use_container_width=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "b2d00048-7a2c-4073-9cd0-9e8cbc3a7551",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Top comments\n",
    "st.subheader(\"💬 Top Positive and Negative Comments\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "7c19f76d-48c7-463e-8938-7a3885fc7a76",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Positive comments\n",
    "st.markdown(\"#### 👍 Top Positive Comments\")\n",
    "pos_comments = df[df['sentiment_label'] == 'Positive'].sort_values(by='sentiment_score', ascending=False).head(5)\n",
    "for idx, row in pos_comments.iterrows():\n",
    "    st.success(f\"**{row['brand'].capitalize()}**: {row['full_text'][:300]}...\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "fdbe10a2-7a0b-4124-90db-4cb5fc3297ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Negative comments\n",
    "st.markdown(\"#### 👎 Top Negative Comments\")\n",
    "neg_comments = df[df['sentiment_label'] == 'Negative'].sort_values(by='sentiment_score', ascending=False).head(5)\n",
    "for idx, row in neg_comments.iterrows():\n",
    "    st.error(f\"**{row['brand'].capitalize()}**: {row['full_text'][:300]}...\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7183433a-40b2-4489-9ef5-83e958edeebc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.markdown(\"---\")\n",
    "st.caption(\"Built with ❤️ using Reddit data, Hugging Face NLP, and Streamlit\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b516aafc-f25c-4af2-b60c-386f23de67cd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
