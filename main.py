from Bots.input_processor import process_input
from Bots.keyword_extractor import extract_keywords
from Bots.yt_video_fetcher import fetch_top_video
from Bots.download_manager import download_video, download_audio
from Bots.log_manager import generate_task_id, log_event, log_error

def main(user_input, base_output_path, format='mp4'):
    task_id = generate_task_id()
    try:
        log_event(task_id, "Process started.")

        # Step 1: Process input
        cleaned_input = process_input(user_input)

        # Step 2: Extract keywords
        keywords = extract_keywords(cleaned_input)

        # Step 3: Fetch top video
        video_url = fetch_top_video(keywords)
        if not video_url:
            log_error(task_id, "No video found.")
            return

        # Step 4: Ask user for download type (audio or video)
        download_type = input("What do you want to download? (audio/video): ").strip().lower()
        if download_type not in ['audio', 'video']:
            log_error(task_id, "Invalid download type selected.")
            print("Invalid choice. Please select 'audio' or 'video'.")
            return

        # Step 5: Ask user for resolution if video
        if download_type == 'video':
            resolution = input("Enter preferred resolution (e.g., 720, 1080, or 'best'): ").strip()
            log_event(task_id, f"User selected resolution: {resolution}")
            output_path = f"{base_output_path}/video_downloads"
            download_video(video_url, output_path, resolution, format)

        # Step 6: Handle audio download
        elif download_type == 'audio':
            audio_format = input("Enter preferred audio format (e.g., mp3, wav): ").strip()
            log_event(task_id, f"User selected audio format: {audio_format}")
            output_path = f"{base_output_path}/audio_downloads"
            download_audio(video_url, output_path, audio_format)

        log_event(task_id, "Process completed successfully.")
        print(f"Download completed and saved to {output_path}.")

    except Exception as e:
        log_error(task_id, str(e))
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    user_input = input("Enter keywords for the video search: ").strip()  # User provides the input here
    base_output_path = "Output"  # Base output folder
    main(user_input, base_output_path, format='mp4')
