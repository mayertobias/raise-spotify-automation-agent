# raise-spotify-automation-agent


#### [The Spotify Web API](https://developer.spotify.com/web-api/)
The Spotify Web API allows applications to fetch lots of awesome data from the Spotify catalog, as well as manage
a user's playlists and saved music.  Some examples of of info you get are:
  - Track, artist, album, and playlist metadata and search
  - High-level audio features for tracks
  - In-depth audio analysis for tracks
  - Featured playlists and new releases
  - Music recommendations based on seed data

#### [Spotipy](http://spotipy.readthedocs.io/en/latest/) ([github](https://github.com/plamere/spotipy))
Spotipy is an awesome lightweight Python wrapper library for the Spotify Web API.  Using Spotipy, you can get any information
that you can get through the raw Web API.  The library does a bunch of the heavy lifting for things like authenticating
against the API, serializing request data, and deserialzing response data.


## Setup
#### Register Your Application With Spotify
In order to access certain features of the Web API, we need to tell spotify that we're a legitimate app.
To do this, go to https://developer.spotify.com/my-applications and create a new Application.

For the Redirect URI, add `http://localhost/` - It should look like this:
![spotify application page](https://raw.githubusercontent.com/markkohdev/spotify-api-starter/master/assets/spotify_api.png)

From that page, copy your ClientId and your ClientSecret and put them into a file called
`credentials.sh` in the root of this repo that looks like this:
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='http://localhost/'
```
For details about how the API authenticates your account with this, see
https://developer.spotify.com/web-api/authorization-guide/#authorization_code_flow

#### Install Dependencies
In order to run this program, we need to make sure python3, pip, and virtualenv are installed on your system.
To install this stuff, run
```
./setup.sh
source ~/.bashrc
```
_Note: If you approve, the setup script will add a line to your bashrc (your shell startup commands) which will
automatically activate your virtual enviroment when you `cd` into this directory, setting your enviroment variables and
using your isolated python environment._

## Running
To run the out of the box demo, simply run
```
make run
```

Once the program runs, you'll be prompted for your username, and your browser window will open.
Once you log in with Spotify, **you will be redirected to a 404 page - THIS IS TOTALLY FINE.**  Copy the URL that you're
redirected to and paste it into the terminal.

