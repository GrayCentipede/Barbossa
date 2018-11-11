# Barbossa
Barbossa is a youtube to mp3 converter that allows you to modify the mp3 on the go.

## Requirements
* Python >= 3.5.2
* mutagen >= 1.41.1
* Python Gtk+3 >= 3.4
* youtube-dl >= 2018.10.5

# Run Barbossa
Simply go to the directory where Barbossa was installed
```
cd ./path/to/Barbossa
```
And run:
```
python3 -m src.main
```

# FAQ
### I tried to download a youtube video but couldn't, why?
Some youtube videos as of today can not be downloaded, this may be due to copyright reasons or others.
The way you can identify this problem is at the moment when youtube-dl fails to download a js/html player.
For more information visit the following github issue [forum](https://github.com/rg3/youtube-dl/issues/18091)

### Barbossa crashed, what do i do now?
Just close the application and reopen it. (Or force it close.)


# Bugs
Some of the known bugs are:
* Application has a small chance of crashing out of nowhere (due to some GTK and threads issues)
* The application's log screen tends to get giant when an error occurs.

# Copyright issues
As a matter of policy (as well as legality), Barbossa does not include support for services that specialize in infringing copyright. Barbossa is not responsible for the misuse of the application.
