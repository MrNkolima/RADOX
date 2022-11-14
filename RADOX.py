import youtube_dl 
import os

os.chdir("/storage/emulated/0/music")
def run():
    video_url = input("\nWELCOME TO RADOX-YT\n Developed by Isack Philiph\n \nEnter youtube video url:")
      
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
  
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Contact me +255673182989\nDownload complete!!!... {}".format(filename))

if __name__=='__main__':
   run()
