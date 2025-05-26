from flask import Flask, redirect
from yt_dlp import YoutubeDL
import time

app = Flask(__name__)

CACHE = {}
CACHE_EXPIRY = 60 * 60 * 24  # 24 hours

YOUTUBE_URL = 'https://www.youtube.com/live/Ko18SgceYX8'

def get_stream_url():
    now = time.time()
    if 'url' in CACHE and now - CACHE['time'] < CACHE_EXPIRY:
        return CACHE['url']
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'forceurl': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(YOUTUBE_URL, download=False)
        stream_url = info['url']
        CACHE['url'] = stream_url
        CACHE['time'] = now
        return stream_url

@app.route('/')
def index():
    try:
        stream_url = get_stream_url()
        return redirect(stream_url)
    except Exception as e:
        return f"Error fetching stream: {str(e)}", 500

if __name__ == "__main__":
    app.run()
