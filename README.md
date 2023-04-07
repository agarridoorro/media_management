# media_management
Support for different scheduled tasks of a media server

## subtitles download
Automatic subtitle download using opensubtitles api rest. The process is simple, with a given configuration and a fixed schedule, scans all files in a base directory and recursivelly in its children. If the file has a video extension and doesn't have a file.es.srt asociated, tries to download the subtitle.

### Configuration
In config directory there are two files:
* auth.json: you have to fill your opensubtitles credentials and your API Key
* params.json: the url of the api, your video extensions and your language

## transmission cleaning
Automatic cleaning for transmission finished torrents.

### Configuration
In config directory there are two files:
* auth.json: you have to fill your transmission uername and password
* params.json: you have to fill your transmission host and port

## Schedule
The file with de cron schedule is mycron, (is a standar cronfile) and is inside de image, if you want to change shedule, you have to build the iamge

## Build the image
Go to the directory project and execute

`docker build -t package/image_name .`

## Run the container
Configure you DockerCompose file, put the UID and PGID of the user that owns de directories, put you timezone and finally the volumes

* config: is the base directory where config files reside. Each plugin creates his basic confiuration with mock values when his module is initialised.
* shows: is where the process scans for videos

```
version: "3.7"
services:
  subtitles:
    image: package/image_name
    container_name: subtitles
    environment:
      - PUID=1000 # User id
      - PGID=1000 # Group id
      - TZ=Europe/Madrid
    volumes:
      - /your/config/path:/config
      - /yout/shows/path:/shows
    restart: unless-stopped # This makes sure that the application restarts when it crashes
```

run the container

`docker-compose up -d`
