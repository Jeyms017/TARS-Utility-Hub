import os
import sys
import subprocess
import json

def has_ytdlp() -> bool:
    try:
        subprocess.run(["yt-dlp", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

def select_format(url: str) -> str:
    format_ids = []

    # Fetch video information
    try:
        print("Fetching video information...")
        result = subprocess.run(["yt-dlp", url, "--dump-json"], capture_output=True, text=True, check=True)
        output = json.loads(result.stdout)
    except Exception as e:
        print("Error fetching video information:", e)
        return ""

    formats = output.get("formats", [])
    if not formats:
        print("No formats found.")
        return ""

    # Print available formats
    print("\nAvailable Formats:")
    for index, fmt in enumerate(formats):
        resolution = fmt.get("resolution") or "audio only"
        extension = fmt.get("ext", "unknown")
        print(f"{index} - Resolution: {resolution} - Extension: {extension}")
        format_ids.append(fmt.get("format_id"))

    # Ask the user to choose
    choice = input("\nSelect a format number (or press Enter to quit): ").strip()
    if choice == "":
        return ""

    try:
        choice_index = int(choice)
        return format_ids[choice_index]
    except Exception:
        print("Invalid selection.")
        return ""


def confirm_download() -> bool:
    choice = input("\nDo you want to proceed with the download? (y/n): ").strip().lower()
    return choice == "y" or choice == "yes"

def download_video(url: str, format_id: str):
    print(f"\nDownloading video (format: {format_id})...")
    try:
        subprocess.run(["yt-dlp", "-f", format_id, url], check=True)
        print("\nDownload completed successfully!")
    except Exception as e:
        print("\nDownload failed:", e)

def run():
    if not has_ytdlp():
        print("yt-dlp is not installed. Please install it first.")
        return

    while True:
        url = input("\nEnter the URL of the video you want to download (or 'q' to quit): ").strip()
        if url == "" or url.lower() == "q":
            print("Exiting...")
            break

        format_id = select_format(url)
        if format_id == "":
            print("Format selection cancelled.")
            continue

        if confirm_download():
            download_video(url, format_id)
        else:
            print("Download cancelled.")

if __name__ == "__main__":
    run()
