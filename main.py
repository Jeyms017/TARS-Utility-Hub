from app.core import organizer
from app.core import downloader

def show_menu():
    print("\n" + "=" * 30)
    print("      TARS UTILITY HUB")
    print("=" * 30)
    print("1. Download Video (yt-dlp)")
    print("2. Organize Downloads Folder")
    print("q. Quit")
    print("=" * 30)

def main():
    while True:
        show_menu()
        choice = input("Select an option: ").strip().lower()

        if choice == "1":
            try:
                downloader.run()
            except Exception as e:
                print("An error occurred in Downloader:", e)
        elif choice == "2":
            try:
                organizer.organize()
            except Exception as e:
                print("An error occurred in Organizer:", e)
        elif choice == "q" or choice == "":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or q.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")
