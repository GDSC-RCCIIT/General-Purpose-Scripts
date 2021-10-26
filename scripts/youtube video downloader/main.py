#import the package
from pytube import YouTube

#give the url here
url = input("> Input the url of your video here: ")
my_video = YouTube(url)

print("------------------------Title------------------------")
#your video title
print(my_video.title)

print("---------------------Thumbnail-----------------------")
#your video thumbnail
print(my_video.thumbnail_url)

#download the video
my_video = my_video.streams.get_highest_resolution()

my_video.download()