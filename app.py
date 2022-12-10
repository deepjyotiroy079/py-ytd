from pytube import YouTube, Playlist
import argparse
from pytube.cli import on_progress

def download_video(url):
	y_object = YouTube(url, on_progress_callback=on_progress)
	y_object = y_object.streams.get_highest_resolution()
	try:
		y_object.download()
	except:
		print("There has been an error while downloading Youtube video!")
		
	print("Download is completed\n")

# download from the playlist
def download_playlist(playlist_url):
	playlist = Playlist(playlist_url)
	print('Number of videos in playlist : {}'.format(len(playlist.video_urls)))
	
	for video in playlist.videos:
		print(video.title)
		download_video(video.watch_url)


ap = argparse.ArgumentParser()
"""
python app.py --type video / playlist --url <link>

if type == video then download video
else if type is playlist
	then get all the video links and then download video
"""
ap.add_argument('-t', '--type', type=str, help='type of download - video / playlist')
ap.add_argument('-u', '--url', type=str, help='link to the video / playlist')

# ap.add_argument("-u", "--url", type=str, help="url to the youtube video")
# ap.add_argument("-p", "--playlist", type=str, help="url of the playlist")	
args = vars(ap.parse_args())

if args['type'] == 'video':
	# download one single video
	download_video(args['url'])
elif args['type'] == 'playlist':
	download_playlist(args['url'])




