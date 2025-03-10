import streamlit as st
from backend.transcript_extractor import get_transcript
from backend.summarizer import summarize_text

st.set_page_config(page_title="YouTube Video Summarizer", layout="wide")

# 🌟 Main UI
st.title("🎥 YouTube Video Summarizer")
st.write("Extracts, transcribes, and summarizes YouTube videos instantly!")

# 📌 User Input
video_url = st.text_input("Enter YouTube Video URL:")

if st.button("Summarize"):
    if video_url:
        with st.spinner("Extracting transcript... ⏳"):
            transcript = get_transcript(video_url)
            if transcript is None:
                st.error("❌ No transcript available for this video.")
            elif transcript.startswith("Error:"):
                st.error(transcript)
            else:
                with st.spinner("Generating summary... 🤖"):
                    summary = summarize_text(transcript)
                    if summary.startswith("Error:"):
                        st.error(summary)
                    else:
                        st.subheader("📌 Lecture Summary")
                        st.write(summary)

                        # Save summary as a text file
                        summary_file = "summary.txt"
                        with open(summary_file, "w") as f:
                            f.write(summary)

                        # Download button
                        st.download_button(
                            label="📥 Download Summary",
                            data=summary,
                            file_name="summary.txt",
                            mime="text/plain",
                        )

# 🔹 Credit Note
st.markdown("---")
st.markdown("🔹 **Developed by Akash Shahade**")
