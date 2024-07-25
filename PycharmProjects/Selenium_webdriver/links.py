from pytube import YouTube


def download_yt_video(url, save_to):
    youtube = YouTube(url)
    video = youtube.streams.get_audio_only()
    video.download(output_path=save_to)


download_yt_video(url="https://youtu.be/xvfDN_Ga2_M", save_to="Downloads")
