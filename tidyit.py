from pathlib import Path
import shutil

Downloads_folder = Path.home() / "Downloads"

print(Downloads_folder.exists())

FOLDER_MAP = {
    "Photos":    [".jpg", ".jpeg", ".png", ".gif", ".bmp",
                  ".svg", ".webp", ".tiff", ".heic", ".raw"],
    "Music":     [".mp3", ".wav", ".flac", ".aac", ".ogg",
                  ".wma", ".m4a", ".opus", ".aiff"],
    "Videos":    [".mp4", ".mkv", ".avi", ".mov", ".wmv",
                  ".flv", ".webm", ".m4v", ".mpeg", ".3gp"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx",
                  ".ppt", ".pptx", ".txt", ".csv", ".md", ".epub"],
    "Archives":  [".zip", ".rar", ".7z", ".tar", ".gz",
                  ".bz2", ".iso"],
    "Programs":  [".exe", ".msi", ".apk", ".deb", ".pkg"],
    "Code":      [".py", ".js", ".ts", ".html", ".css",
                  ".json", ".sql", ".sh", ".bat", ".java"],
    "Fonts":     [".ttf", ".otf", ".woff", ".woff2"],
    "Torrents":  [".torrent"],
}



for item in Downloads_folder.iterdir():
    if item.is_file():
        ext = item.suffix.lower()
        for folder, extensions in FOLDER_MAP.items():
            if ext in extensions:
                target_folder = Downloads_folder / folder
                target_folder.mkdir(exist_ok=True)
                shutil.move(str(item), str(target_folder / item.name))
                print(f"Moved {item.name} to {target_folder}")
                break
            