from pathlib import Path
import shutil

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

def organize(downloads_folder=None):
    if downloads_folder is None:
        downloads_folder = Path.home() / "Downloads"
    else:
        downloads_folder = Path(downloads_folder)

    if not downloads_folder.exists():
        print(f"Folder does not exist: {downloads_folder}")
        return

    print(f"Tidying up: {downloads_folder}")
    moved_count = 0

    for item in downloads_folder.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            for folder, extensions in FOLDER_MAP.items():
                if ext in extensions:
                    target_folder = downloads_folder / folder
                    target_folder.mkdir(exist_ok=True)
                    shutil.move(str(item), str(target_folder / item.name))
                    print(f"Moved {item.name} to {target_folder}")
                    moved_count += 1
                    break
    
    print(f"Tidying completed. Moved {moved_count} files.")

if __name__ == "__main__":
    organize()
