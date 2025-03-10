from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

def get_transcript(video_url):
    """
    Fetches the transcript of a YouTube video.
    """
    try:
        video_id = video_url.split("v=")[1].split("&")[0]  # Extract Video ID
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry['text'] for entry in transcript])
        return transcript_text
    except NoTranscriptFound:
        return None
    except Exception as e:
        return f"Error: {str(e)}"
