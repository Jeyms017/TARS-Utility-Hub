# TARS Utility Hub

A modular, beginner-friendly Python utility collection.

## Project Structure

```text
TARS-Utility-Hub/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── app/
    ├── __init__.py
    └── core/
        ├── __init__.py
        ├── organizer.py
        ├── downloader.py
        └── clipboard.py
```

## Features

- **Download Video**: Uses `yt-dlp` to download video and audio from various platforms by prompting for formats.
- **Organize Downloads**: Tidy up your computer's `Downloads/` directory into categorized subfolders (Photos, Music, Videos, Documents, Archives, Programs, Code, Fonts, Torrents).

## Getting Started

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the entry point script:
   ```bash
   python main.py
   ```
