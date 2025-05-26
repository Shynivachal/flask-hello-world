# Asianet News Stream Server

This Flask application serves the latest `.m3u8` URL for the Asianet News YouTube live stream.

## Deployment

You can deploy this application on platforms like [Railway](https://railway.app/) or [Render](https://render.com/).

### Steps:

1. Fork this repository.
2. Deploy to your preferred platform.
3. Access the stream at `https://your-domain.com/asianet.m3u8`.

## Notes

- The application caches the stream URL and refreshes it every 24 hours.
- Ensure `yt-dlp` is installed and accessible in your deployment environment.
