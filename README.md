# 🐦 Tweet Generator Agent

An interactive Tweet Generator built with **Google's Gemini API** and **Jupyter Widgets**. This tool allows users to generate tweet-sized content based on a given **topic**, **tone**, **audience**, and **hashtags**.

---

## 🚀 Features

- 🎯 Custom input fields for:
  - **Topic**
  - **Tone** (Informative, Motivational, Casual, Professional)
  - **Audience**
  - **Hashtags**
- 💡 Generates tweets under 280 characters
- ⚡ Fast, Gemini-powered content using `models/gemini-2.5-flash`
- 🖼️ User-friendly interface with `ipywidgets`
- 📦 Standalone Python script (`TweetGeneratorAgent.py`)

---
## 📦 Installation

1. Clone the repository:
   git clone https://github.com/yourusername/tweet-generator-agent.git
   cd tweet-generator-agent
2. Install dependencies:
   pip install google-generativeai ipywidgets
3.(Optional) Enable widgets in Jupyter if running there:
   jupyter nbextension enable --py widgetsnbextension
   
## 🔐 API Key Setup
1. Go to Google AI Studio (https://aistudio.google.com/apikey) and generate your Gemini API Key.
2. Paste it into your .py file or (recommended) store it securely using environment variables.

## ▶️ How to Run

1.Open the script in any Python environment that supports GUI or widget rendering (like Jupyter Lab or VS Code interactive mode):
  python tweet_generator.py

2.Fill in the required fields in the widget form.
3.Click "Generate Tweet"
4.View your tweet in the output cell.

## Screenshot
<img width="1518" height="419" alt="image" src="https://github.com/user-attachments/assets/24591a29-3515-47db-8a96-67f701ea3fe4" />

👤 Author
Dhruv Gupta
B.Tech CSE (AI & ML) @ Galgotias University
📧 dhruvguptag7@gmail.com


