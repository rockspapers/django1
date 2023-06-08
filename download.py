from pytube import YouTube

link = input("enter link") 
yt = YouTube(link) 

downloader = yt.streams.filter(only_audio=True).get_audio_only()

downloader.download() 
print("finished downloading")
