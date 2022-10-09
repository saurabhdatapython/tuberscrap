from Constants import api_key
from googleapiclient.discovery import build
from Data_Collection.get_playlist_ids import get_playlist_ids
youtube_url = "https://www.youtube.com/c/sudhanshukumarall"

channelId =" sudhanshukumarall"
p =get_playlist_ids(channelId)
print(p)



