# 🎬 YT_downloader: Intelligent YouTube Video Downloading System

An AI-powered modular system for searching, analyzing, and downloading YouTube videos intelligently using keywords, region detection, and metadata extraction.

> 🔧 Built using `yt_dlp`, `Scikit-learn`, `YouTube Data API`, and modular bots for extensibility and clarity.

---

## 🚀 Features

- 🎯 **Keyword-Based Search**: Extracts relevant search terms using NLP.
- 🌍 **Region-Aware Results**: Detects user region via IP and fetches region-optimized content.
- 📊 **Metadata Extraction**: Gets video details (views, likes, duration, etc.) via YouTube Data API.
- 🎥 **Video & Audio Downloading**: Download in best available resolution or audio-only.
- 🪝 **Multi-Bot Coordination**: Each task handled by its own module — easy to extend or scale.
- 🪵 **Activity Logging**: All tasks are tracked with UUIDs for transparency and debugging.

---

## 🧠 Bot Modules Breakdown

### 🔹 `download_manager.py`
Handles downloading:
- Videos at a chosen resolution (`mp4` by default)
- Audio extraction (`mp3` via FFmpeg )

### 🔹 `input_processor.py`
Cleans and normalizes raw user input using regex for downstream NLP processing.

### 🔹 `keyword_extractor.py`
Uses `CountVectorizer` from `sklearn` to identify top 5 keywords from cleaned text.

### 🔹 `region_detector.py`
Detects user's current country using `ipinfo.io` to refine search results accordingly.

### 🔹 `yt_video_fetcher.py`
Searches YouTube using `yt_dlp` and returns the most relevant video link from the keyword query.

### 🔹 `metadata_extractor.py`
Uses **YouTube Data API v3** to fetch:
- Title
- Channel
- Views, Likes, Comments
- Duration & Publish Time

### 🔹 `log_manager.py`
Generates task IDs (UUID) and logs events/errors in `Logs/activity.log`.

### 🔹 `multi_bot_coordinator.py`
The brain of the operation — orchestrates all bots:
1. Processes input
2. Extracts keywords
3. Detects region
4. Fetches videos
5. Logs outputs

---

## 🗂️ Folder Structure

```

YT\_downloader/
├── Bots/                  # Core bot logic
├── Config/                # App config files (e.g., API keys)
├── Input/                 # Raw user input storage
├── Logs/                  # Activity & error logs
├── main.py                # Entry point
├── requirements.txt       # Python dependencies
└── README.md              # You’re here

````

---

## 🔧 Setup Instructions

1. **Clone the repo**:
```bash
git clone https://github.com/Tanishq-789/YT_downloader.git
cd YT_downloader
````

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. ## 🔑 Get a YouTube Data API Key (Required for `metadata_extractor.py`)

Follow these steps to obtain your API key:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. In the left-hand sidebar, navigate to **APIs & Services > Library**.
4. Search for **YouTube Data API v3** and click **Enable**.
5. Next, go to **APIs & Services > Credentials**.
6. Click **+ Create Credentials** and choose **API Key**.
7. Copy the generated key.

🔧 **Update your script:**

Open `metadata_extractor.py` and replace the placeholder with your API key:

```python
API_KEY = "your_api_key_here"
```
4. **Run the main coordinator:** 

```
python main.py
```

---

## 📌 Sample Usage

```python
from Bots.multi_bot_coordinator import main

output_path = "./downloads"
user_query = "top AI podcasts 2024"
api_key = "your_api_key"

video_urls = main(user_query, api_key, output_path)
print(video_urls)
```

---

## 🛠️ Technologies Used

| Category         | Tools & APIs                   |
| ---------------- | ------------------------------ |
| 🧠 NLP           | scikit-learn (CountVectorizer) |
| 📺 Video Search  | yt\_dlp                        |
| 📡 API           | YouTube Data API v3            |
| 📂 Downloading   | FFmpeg (via yt\_dlp)           |
| 🌐 Region Detect | ipinfo.io                      |
| 📋 Logging       | Python `logging` + UUID        |

---

## ⚠️ Disclaimer

This tool is for **educational purposes**. Please ensure compliance with YouTube’s [Terms of Service](https://www.youtube.com/t/terms) when using video or audio content from the platform.
This project was completed under the mentorship of Nikhil Bhaskaran under my Iotiot.in Internship.
---

## 👨‍💻 Author

**Tanishq Shinde**

🔗 [LinkedIn](https://www.linkedin.com/in/tanishq-shinde977/) | 🔍 [LeetCode](https://leetcode.com/u/Tanishq7-77/) | 🤖 [GitHub](https://github.com/Tanishq-789)

---

## ⭐ Star the Repo

If you found this helpful or interesting, consider giving it a ⭐ on GitHub!
