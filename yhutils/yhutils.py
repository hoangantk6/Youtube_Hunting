def pytube_search_object_to_url(result_object):
  """
  convert a pytube url object into string url
  """
  str_result = str(result_object)
  return f"https://www.youtube.com/watch?v={str_result.split('videoId=')[-1][:-1]}"

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