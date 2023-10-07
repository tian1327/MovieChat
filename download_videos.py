import os
import json
from pprint import pprint
# from tqdm import tqdm
from pytube import YouTube

# specify download directory
directory = 'src/examples/'

url_list = [
	'https://www.youtube.com/watch?v=GhxqIITtTtU',
	'https://www.youtube.com/watch?v=c472zg9k5vU',
	'https://www.youtube.com/watch?v=pYrj-3kMUHw',
	'https://www.youtube.com/watch?v=ZveF2b83Tc0'
]

videoCounter = 0
for url in url_list:
	key = url.split('=')[1]

	try:
		# Create a YouTube object with the provided URL
		yt = YouTube(url)
		
		# Filter the available video streams to get the highest resolution
		video = yt.streams.get_highest_resolution()
		
		# Download the video to the specified output path, rename the video as the key
		video.download(directory, key+'.mp4')
		videoCounter += 1		
		print(f'Downloaded {key}.mp4')
		

	except Exception as e:
		print(f'Error downloading {key}.mp4')