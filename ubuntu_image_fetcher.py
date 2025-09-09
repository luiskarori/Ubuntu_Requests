"""
Ubuntu-Inspired Image Fetcher
--------------------------------
"I am because we are" – Ubuntu

This script connects to the global community of the internet,
fetches images shared publicly, and organizes them respectfully
for later appreciation.
"""

import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # 🌐 Community: Ask the user for a URL
    url = input("Enter the URL of an image to fetch: ").strip()

    # Create directory for images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # ✨ Respect: Try fetching the resource
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad HTTP responses

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:  # if URL doesn’t end with a file
            filename = "downloaded_image.jpg"

        save_path = os.path.join(save_dir, filename)

        # Save file in binary mode
        with open(save_path, "wb") as f:
            f.write(response.content)

        print(f"✅ Image saved successfully at: {save_path}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL format. Please include http:// or https://")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Try again later.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    fetch_image()
