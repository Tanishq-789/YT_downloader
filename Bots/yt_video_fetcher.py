import yt_dlp

def fetch_top_video(keywords):
    query = f"ytsearch:{' '.join(keywords)}"  # Ensure YouTube search
    print(f"🔍 Searching YouTube for: {query}")  # Debugging statement

    ydl_opts = {
        'quiet': False,  # Show logs
        'extract_flat': False,  # Allow full metadata extraction
        'noplaylist': True,  # Avoid fetching playlists
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(query, download=False)  # Perform search

        if 'entries' in result and result['entries']:
            top_video = result['entries'][0]  # Get first video
            print(f"🎥 Found Video: {top_video['title']} ({top_video['webpage_url']})")  # Debugging output
            return top_video['webpage_url']  # Return video URL

    print("❌ No video found.")
    return None
