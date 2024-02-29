import os
import requests
from instabot import Bot

# Function to authenticate with Instagram
def authenticate_instagram(username, password):
    bot = Bot()
    bot.login(username=username, password=password)

# Function to retrieve images or videos from a local directory
def retrieve_media(directory):
    media_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".mp4"):
            media_files.append(os.path.join(directory, filename))
    return media_files

# Function to post media to Instagram with a caption
def post_to_instagram(bot, media_files, caption):
    for media_file in media_files:
        bot.upload_photo(media_file, caption=caption)
    print("Post(s) uploaded successfully!")

def main():
    # Instagram credentials
    username = "your_username"
    password = "your_password"

    # Authenticate with Instagram
    authenticate_instagram(username, password)

    # Directory containing media files
    media_directory = "/path/to/media_directory"

    # Retrieve media files from the directory
    media_files = retrieve_media(media_directory)

    # Caption for the posts
    caption = "Check out this awesome photo/video!"

    # Post media to Instagram
    bot = Bot()
    post_to_instagram(bot, media_files, caption)

if __name__ == "__main__":
    main()
