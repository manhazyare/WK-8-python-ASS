# WK-8-python-ASS

# CORD-19 Data Explorer

A simple project to explore and visualize COVID-19 research metadata using **Python, Pandas, and Streamlit**.

## Project Structure

WK 8/
│── app/ # Streamlit app
│ └── app.py
│
│── data/ # Dataset folder
│ └── metadata.csv # (Place dataset here)
│
│── Explore/ # Exploration scripts
│ └── explore.py
│
│── venv/ # Virtual environment (not uploaded to GitHub)
└── README.md

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd WK 8

2. Create and Activate Virtual Environment
python -m venv venv


On Windows (PowerShell):

venv\Scripts\activate


On Linux / macOS:

source venv/bin/activate

3. Install Requirements
pip install -r requirements.txt


If you don’t have requirements.txt yet, install manually:

pip install pandas matplotlib seaborn wordcloud streamlit

Usage
Explore Dataset in Console
python Explore/explore.py


This prints:

Shape of the dataset

Column names

Missing values

First rows

Top journals

Run the Streamlit Web App
streamlit run app/app.py


Local URL: http://localhost:8501

Network URL: http://<your-ip>:8501

The app lets you:

Filter by publication year

See number of publications by year

View top journals

Generate wordcloud of paper titles

Browse a sample of the data

Notes

Ensure data/metadata.csv is present in the data/ folder.

If you have a very large file, you can use metadata_sample.csv for quicker testing.

For best performance, use Python 3.9+.


---

👉 Do you want me to also create a **requirements.txt** for you so it’s easier to install everything in one go?
