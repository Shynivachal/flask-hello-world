from flask import Flask, Response
import subprocess
import time
import os

app = Flask(__name__)

YOUTUBE_VIDEO_ID = "Ko18SgceYX8"
CACHE_FILE = "stream_cache.m3u8"
CACHE_TIME = 60 * 60 * 24  # 24 hours

def fetch_stream_url():
    result = subprocess.run([
        "yt-dlp",
        f"https://www.youtube.com/watch?v={YOUTUBE_VIDEO_ID}",
        "-f", "96",  # HLS stream format
        "--get-url"
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        return result.stdout.decode().strip()
    else:
        return None

def update_cache():
    url = fetch_stream_url()
    if url:
        with open(CACHE_FILE, "w") as f:
            f.write(url)
        os.utime(CACHE_FILE, None)

def get_cached_url():
    if not os.path.exists(CACHE_FILE):
        update_cache()

    now = time.time()
    modified = os.path.getmtime(CACHE_FILE)
    if now - modified > CACHE_TIME:
        update_cache()

    with open(CACHE_FILE, "r") as f:
        return f.read().strip()

@app.route("/asianet.m3u8")
def asianet():
    stream_url = get_cached_url()
    m3u_content = f"""#EXTM3U
#EXTINF:-1 tvg-id="asianetnews" group-title="Malayalam",Asianet News HD
{stream_url}
"""
    return Response(m3u_content, mimetype='application/x-mpegURL')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
