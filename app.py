# app/app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# --- Page setup ---
st.set_page_config(page_title="Research Papers Explorer", layout="wide")

# --- Load data ---
@st.cache_data
def load_data():
    return pd.read_csv("data/metadata.csv", low_memory=False)

df = load_data()

# --- Prepare data ---
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['title'] = df['title'].fillna("")

# --- App Title ---
st.title("📊 Research Papers Explorer")

# --- Show basic info ---
st.write("### Dataset Overview")
st.write(f"Number of records: **{df.shape[0]}**")
st.write(f"Number of columns: **{df.shape[1]}**")

# --- Publications per Year ---
st.write("### Publications by Year")
year_counts = df['year'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(x=year_counts.index, y=year_counts.values, color="skyblue", ax=ax)
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# --- Top Journals ---
st.write("### Top Journals")
top_journals = df['journal'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(y=top_journals.index, x=top_journals.values, palette="viridis", ax=ax)
ax.set_title("Top Journals (Top 10)")
ax.set_xlabel("Count")
ax.set_ylabel("Journal")
st.pyplot(fig)

# --- Wordcloud of Titles ---
st.write("### Wordcloud of Paper Titles")
text = " ".join(df['title'].astype(str))
wc = WordCloud(width=800, height=400, background_color="white").generate(text)

fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
