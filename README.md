# Ubuntu_Requests
# Ubuntu-Inspired Image Fetcher 🌍

> "I am because we are." – Ubuntu Philosophy  

This project is a Python script inspired by the spirit of **Ubuntu**, which emphasizes **community, respect, sharing, and practicality**.  

The script connects to the global web community, respectfully fetches shared images from URLs, and organizes them locally for later use and appreciation.  

---

## ✨ Features
- 🌐 **Community**: Connects to the internet to fetch resources  
- 🙏 **Respect**: Handles errors gracefully without crashing  
- 📦 **Sharing**: Saves all images in a structured `Fetched_Images` folder  
- ⚡ **Practicality**: Provides a simple and useful tool for image downloading  

---

## 🚀 How It Works
1. The program prompts the user for an image URL  
2. It creates a directory called **`Fetched_Images`** (if it doesn’t exist)  
3. It downloads the image using the **Requests** library  
4. The image is saved with its filename (or a default name if none exists)  
5. All errors (bad URL, HTTP issues, connection problems) are handled gracefully  

---

## 🛠️ Requirements
- Python 3.x  
- `requests` library  

Install dependencies:  
```bash
pip install requests
