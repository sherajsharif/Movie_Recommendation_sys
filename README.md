# 🎬 Movie Recommendation System

A content-based Movie Recommender System that suggests similar movies based on a selected title using cosine similarity and NLP techniques. This web application is built using **Python**, **pandas**, **scikit-learn**, and **Streamlit** for a sleek, interactive frontend.

---

## 📸 Project Preview

![Movie Recommendation UI](./screenshot.png)

> *Screenshot of the deployed web app showing movie suggestions for “Avatar”*

---

## 🚀 Features

- Select any movie from the dropdown list
- Get top 5 similar movie recommendations instantly
- Movie posters displayed for each recommended title
- Responsive and visually appealing Streamlit UI
- Fast and interactive performance for great UX

---

## 📂 Dataset

This system uses a cleaned dataset based on [TMDb](https://www.themoviedb.org/) metadata containing:

- Movie titles
- Genres
- Cast
- Crew
- Tags (combined metadata)

**Sample Columns:**
- `id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`, `tags`

---

## ⚙️ How It Works

1. **Preprocessing:**
   - Combine relevant metadata (`overview`, `keywords`, `cast`, `crew`)
   - Convert text to lowercase, remove stopwords and apply stemming

2. **Vectorization:**
   - Use **CountVectorizer** to convert tags into vectors
   - Calculate **cosine similarity** between movies

3. **Recommendation:**
   - Based on similarity scores, suggest top 5 similar movies

---

## 💻 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Libraries:** pandas, numpy, scikit-learn, nltk, requests, PIL

---

## 🔧 Installation

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
streamlit run app.py
