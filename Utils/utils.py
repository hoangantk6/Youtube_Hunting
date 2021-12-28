from datetime import datetime
import pandas as pd
import pytz
from google.colab import data_table
import os


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

def display_table(df):
  """
  display table in Google Colab
  """
  return data_table.DataTable(df, num_rows_per_page=10)

def what_date_today():
  today = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
  today = today.strftime("%Y-%m-%d %H:%M:%S")
  return today

def save_image(plt, folder_path, file_name):
  """
  save matpplotlib image into .jpg file 
  """
  file_path = os.path.join(folder_path, file_name)
  plt.savefig(file_path)
  print(f'File is saved to {file_name} in Google Drive at {file_path}')
