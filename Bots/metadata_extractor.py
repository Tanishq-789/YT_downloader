from googleapiclient.discovery import build


def get_video_metadata(video_id):
    """
    Fetch metadata for a given YouTube video.

    Args:
        video_id (str): The ID of the YouTube video.

    Returns:
        dict: A dictionary containing metadata such as title, description, duration, etc.
    """
    # Replace with your YouTube Data API key
    API_KEY = "YOUR_API_KEY"
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Fetch video details
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    response = request.execute()

    if not response["items"]:
        return {"error": "Video not found or invalid video ID"}

    # Extract metadata
    video = response["items"][0]
    metadata = {
        "title": video["snippet"]["title"],
        "description": video["snippet"]["description"],
        "published_at": video["snippet"]["publishedAt"],
        "channel_title": video["snippet"]["channelTitle"],
        "duration": video["contentDetails"]["duration"],  # ISO 8601 duration
        "view_count": video["statistics"].get("viewCount", "N/A"),
        "like_count": video["statistics"].get("likeCount", "N/A"),
        "comment_count": video["statistics"].get("commentCount", "N/A"),
        "video_url": f"https://www.youtube.com/watch?v={video_id}"
    }

    return metadata



