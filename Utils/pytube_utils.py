import pandas as pd


def pytube_search_object_to_url(result_object):
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
    url = pytube_search_object_to_url(search_object)
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