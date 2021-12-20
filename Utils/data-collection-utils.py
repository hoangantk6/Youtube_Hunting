from datetime import datetime
import pandas as pd
import pytz

def save_database(df, file_path):
  """
  save dataframe into a .csv file
  """
  df.to_csv(file_path, index=False)
  print('Database is saved to', file_path)

def update_database(original_df, new_df):
  """
  append new dataframe to old dataframe and avoid duplications in primary key
  """
  return original_df.append(new_df, ignore_index=True)

def display_table(df, data_table):
  """
  display table in Google Colab
  """
  return data_table.DataTable(df, num_rows_per_page=10)

def what_date_today():
  today = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
  today = today.strftime("%Y-%m-%d %H:%M:%S")
  return today

# ---- pyyoutube ----
# CHANNEL
def channel_id_to_dict(api, channel_id):
  """
  return a Youtube-api dictionary of a channel from channel_id
  """
  channel_by_id = api.get_channel_info(channel_id=channel_id)
  return channel_by_id.items[0].to_dict()

def channel_dict_to_df(channel_dict):
  """
  convert Youtube-api channel dictionary into a dataframe
  """
  channel = {}
  channel['channel_name'] = channel_dict['snippet']['title']
  channel['keywords'] = channel_dict['brandingSettings']['channel']['keywords']
  channel['id'] = channel_dict['id']
  channel['created_time'] = channel_dict['snippet']['publishedAt']
  channel['channel_url'] = f"https://www.youtube.com/channel/{channel['id']}/videos"
  channel['description'] = channel_dict['brandingSettings']['channel']['description']
  channel['num_subscriber'] = channel_dict['statistics']['subscriberCount']
  channel['num_video'] = channel_dict['statistics']['videoCount']
  channel['num_view'] = channel_dict['statistics']['viewCount']
  try:
    channel['topic_category'] = ", ".join(channel_dict['topicDetails']['topicCategories'])
  except:
    channel['topic_category'] = None
  channel['thumbnail_default'] = channel_dict['snippet']['thumbnails']['default']['url']
  channel['thumbnail_high'] = channel_dict['snippet']['thumbnails']['high']['url']
  channel['thumbnail_medium'] = channel_dict['snippet']['thumbnails']['medium']['url']
  channel['last_update'] = what_date_today()
  return pd.DataFrame([channel])

# VIDEO
def video_id_to_dict(api, video_id):
  """
  return a Youtube-api dictionary of a video from video_id
  """
  video_by_id = api.get_video_by_id(video_id=video_id)
  return video_by_id.items[0].to_dict()

def video_dict_to_df(video_dict):
  """
  convert Youtube-api video dictionary into a dataframe
  """
  video = {}
  video['video_name'] = video_dict['snippet']['title']
  video['id'] = video_dict['id']
  video['video_url'] = f"https://www.youtube.com/watch?v={video['id']}"
  video['channel_id'] = video_dict['snippet']['channelId']
  video['channel_name'] = video_dict['snippet']['channelTitle']
  video['video_file_name'] = None
  video['description'] = video_dict['snippet']['description']
  video['num_like'] = video_dict['statistics']['likeCount']
  video['num_dislike'] = video_dict['statistics']['dislikeCount']
  video['num_view'] = video_dict['statistics']['viewCount']
  video['published_time'] = video_dict['snippet']['publishedAt']
  try:
    video['tags'] = ", ".join(video_dict['snippet']['tags'])
  except:
    video['tags'] = None
  try:
    video['video_topic_category'] = ", ".join(video_dict['topicDetails']['topicCategories'])
  except:
    video['video_topic_category'] = None
  video['duration'] = video_dict['contentDetails']['duration']
  video['projection'] = video_dict['contentDetails']['projection']
  video['definition'] = video_dict['contentDetails']['definition']
  video['thumbnail_default'] = video_dict['snippet']['thumbnails']['default']['url']
  video['thumbnail_medium'] = video_dict['snippet']['thumbnails']['medium']['url']
  video['thumbnail_high'] = video_dict['snippet']['thumbnails']['high']['url']
  video['thumbnail_standard'] = video_dict['snippet']['thumbnails']['standard']['url']
  video['last_update'] = what_date_today()

  return pd.DataFrame([video])

# ---- pytube ----
def search_object_to_url(result_object):
  """
  convert a pytube url object into string url
  """
  str_result = str(result_object)
  return f"https://www.youtube.com/watch?v={str_result.split('videoId=')[-1][:-1]}"

def search_by_keyword(keyword, Search, url_list, today):
  """
  return a dataframe of urls searched by keyword
  """
  video_url_list = []
  search_query_list = []
  extracted_date_list = []
  video_file_name_list = []

  s = Search(keyword)
  for search_object in s.results:
    url = search_object_to_url(search_object)
    # if the url not seen in the database
    if url not in url_list:
      video_url_list.append(url)
      search_query_list.append(f'keyword: {keyword}')
      extracted_date_list.append(today)
      video_file_name_list.append('')

  return pd.DataFrame(
              {
                  'video_url': video_url_list,
                  'extracted_date': extracted_date_list,
                  'search_query': search_query_list, 
                  'video_file_name': video_file_name_list
              }
          )

def search_by_channel(channel_url, Channel, url_list, today):
  """
  return a dataframe of urls searched by channel
  """
  video_url_list = []
  search_query_list = []
  extracted_date_list = []
  video_file_name_list = []

  c = Channel(channel_url)
  for url in c.video_urls:
    if url not in url_list:
      video_url_list.append(url)
      search_query_list.append(f'channel: {c.channel_name}')
      extracted_date_list.append(today)
      video_file_name_list.append('')

  return pd.DataFrame(
              {
                  'video_url': video_url_list,
                  'extracted_date': extracted_date_list,
                  'search_query': search_query_list, 
                  'video_file_name': video_file_name_list
              }
          )
