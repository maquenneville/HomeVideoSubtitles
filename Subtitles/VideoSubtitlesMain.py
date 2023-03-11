# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 00:35:16 2023

@author: marca
"""


import argparse
import os
from VideoTranscriptionHelpers import (
    convert_single_to_wav,
    transcribe_audio,
    generate_edited_response,
    add_transcript_to_video,
)



def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Convert video to WAV, transcribe speech, generate edited response, and add transcript to video.")
    parser.add_argument("video_file", help="Path to input video file")
    parser.add_argument("prompt", help="Prompt for edited response generation")
    parser.add_argument("--dialect", help="Dialect code for speech recognition (default is en-US)", default="en-US")
    parser.add_argument("--line-time", help="Duration of each line of transcript in seconds (default is 10)", type=int, default=10)
    args = parser.parse_args()

    # Convert the video to WAV format
    print("Converting video to WAV format...")
    audio_file = convert_single_to_wav(args.video_file)

    # Transcribe the speech in the audio file
    print("Transcribing speech...")
    transcript = transcribe_audio(audio_file, dialect_code=args.dialect)

    # Generate the edited response to the prompt
    print("Generating edited response...")
    final_transcript = generate_edited_response(transcript, dialogue=args.dialogue)

    # Add the transcript to the video
    print("Adding transcript to video...")
    add_transcript_to_video(final_transcript, args.video_file, line_time=args.line_time)

    # Clean up intermediate files
    os.remove(audio_file)

    print("Done!")

if __name__ == "__main__":
    main()

    