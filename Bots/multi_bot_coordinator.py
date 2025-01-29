# Coordinates all bots to process the user request
from input_processor import process_input
from keyword_extractor import extract_keywords
from region_detector import detect_region
from yt_video_fetcher import fetch_top_videos
from log_manager import log_event, log_error


def main(user_input, api_key, output_path):
    try:
        log_event("Process started.")

        # Step 1: Process input
        cleaned_input = process_input(user_input)

        # Step 2: Extract keywords
        keywords = extract_keywords(cleaned_input)

        # Step 3: Detect region
        region = detect_region()

        # Step 4: Fetch videos
        videos = fetch_top_videos(keywords, region, api_key)

        # Step 5: Log and return results
        log_event(f"Videos fetched: {videos}")
        return videos
    except Exception as e:
        log_error(str(e))
        return []
