# explore/explore.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# 1. Load the data
df = pd.read_csv("data/metadata.csv", low_memory=False)

# 2. Explore
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing values (top 10):")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# 3. Clean/prepare
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['title'] = df['title'].fillna("")

# 4. Analysis
# Papers per year
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,4))
sns.barplot(x=year_counts.index, y=year_counts.values, color="skyblue")
plt.title("Publications by Year")
plt.show()

# Top journals
top_journals = df['journal'].value_counts().head(10)
print("\nTop Journals:\n", top_journals)

# Wordcloud of titles
text = " ".join(df['title'].astype(str))
wc = WordCloud(width=800, height=400, background_color="white").generate(text)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
