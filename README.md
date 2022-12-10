# A Youtube Downloader

A simple python script that downloads individual videos as well as playlists.

# Usage

Create a virtual environment
```bash
python -m venv env
```

Activate the virtual environment
```bash
.\env\Script\activate.bat
```

Installing dependencies
```bash
pip install pytube 
```

For Video
```bash
python app.py --type video --url <url> 
```
For Playlist
```bash
# for playlist
python app.py --type playlist --url <url for playlist> 
```