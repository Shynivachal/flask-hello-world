from flask import Flask, redirect
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def get_stream():
    url = 'https://www.youtube.com/live/Ko18SgceYX8?si=wxDFMuMrfEqd9CrM'
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'force_generic_extractor': False,
        'format': 'best[ext=m3u8]',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        stream_url = info_dict['url']
        return redirect(stream_url)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
