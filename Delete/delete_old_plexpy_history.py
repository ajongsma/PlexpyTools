### WARNING: This script has not been tested! ###
#   1. Set api_sql = 1 in the config.ini file.
#   2. Install the requests module for python.
#       pip install requests
#   3. Use some method to run the script on a schedule.
#
#   Notes - config.ini settings:
#   Enable the API under Settings > Access Control and remember your API key.
#   Shutdown PlexPy and open your config.ini file in a text editor.
#   Set api_sql = 1 in the config file.
#   Start PlexPy.
#
#   Usage:
#   python delete_old_plexpy_history.py
#   
#   Source: https://gist.github.com/JonnyWong16/cb1b53e71b89d2159313
###

import requests
import urllib

## EDIT THESE SETTINGS ##
PLEXPY_URL = 'http://localhost:8181/' # Your PlexPy URL
PLEXPY_APIKEY = '#####' # Your PlexPy API Key
HISTORY_DAYS_TO_KEEP = 365

## CODE BELOW ##
query = 'DELETE FROM session_history WHERE datetime(started, "unixepoch", "localtime") < datetime("now", "-{0} days", "localtime");'.format(HISTORY_DAYS_TO_KEEP)
data = {'apikey': PLEXPY_APIKEY,
        'cmd': 'sql',
        'query': query}
url = PLEXPY_URL.rstrip('/') + '/api/v2?' + urllib.urlencode(data)
response = requests.post(url)
print 'Deleting session_history            : ' +response.text

query = 'DELETE FROM session_history_media_info WHERE id NOT IN (SELECT id FROM session_history);'.format(HISTORY_DAYS_TO_KEEP)
data = {'apikey': PLEXPY_APIKEY,
        'cmd': 'sql',
        'query': query}
url = PLEXPY_URL.rstrip('/') + '/api/v2?' + urllib.urlencode(data)
response = requests.post(url)
print 'Deleting session_history_media_info : ' +response.text

query = 'DELETE FROM session_history_metadata WHERE id NOT IN (SELECT id FROM session_history);'.format(HISTORY_DAYS_TO_KEEP)
data = {'apikey': PLEXPY_APIKEY,
        'cmd': 'sql',
        'query': query}
url = PLEXPY_URL.rstrip('/') + '/api/v2?' + urllib.urlencode(data)
response = requests.post(url)
print 'Deleting session_history_metadata   : ' + response.text
