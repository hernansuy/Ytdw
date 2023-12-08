import yt_dlp

def descargar_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return info['title']

# Ejemplo de uso
url_video = 'https://www.youtube.com/watch?v=T7H9xEuTKhQ'
titulo_video = descargar_video(url_video)
print(f'Se descargó el video: {titulo_video}')
