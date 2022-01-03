import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

def list_to_freq(data_list):
    """
    Calculate the frequency of each distinct item in a list
    return a dictionary
    """
    freq = {}
    for item in data_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=False)}
    return freq

def bar_plot(data, xlabel, ylabel, title,
             confidence_interval=False,
             frequency=False, 
            #  value_annotation=True, 
             orientation='verticle', 
             xrotation=0, 
             color='maroon', 
             bar_width=0.4, 
             figsize=(10,5)):
  """
  Plot bar chart
  @param data: dict(<label>: <frequency>) in case frequency=False, data list otherwise.
  @param confidence_interval: (<proportion>, <confidence_level>)
  @param frequency: determine if the unit of y-axis is proportion
  """

  if frequency:
    data = np.array(data)
    data_freq = list_to_freq(data)
    total = 0
    x_axis = list(data_freq.keys())
    y_axis = np.array(list(data_freq.values()))
    
    total = 0
    for i in y_axis:
      total += i

    # convert to percentage
    if frequency: 
      y_axis = y_axis/total

    # calculate confidence interval
    error = []
    if confidence_interval:
      confidence_level = confidence_interval[1]
      for data_key in x_axis:
        error.append(get_confidence_interval(data==data_key, confidence_level))
    else:
      error = 0

  else:
    x_axis = list(data.keys())
    y_axis = list(data.values())
      

  plt.figure(figsize=figsize)
  
  # creating the bar plot 
  if orientation=='verticle':
    plt.bar(x_axis, y_axis, yerr=error, color=color, width=bar_width, capsize=5)

    # if value_annotation:
    #   for i, v in enumerate(y_axis):
    #     plt.text(i-0.15, v+0.2, str(f"{round(v/total*100,2)}%"), color='blue', fontweight='bold')

  else:
    plt.barh(x_axis, y_axis, xerr=error, color=color, capsize=5)

    # if value_annotation:
    #   for i, v in enumerate(y_axis):
    #     plt.text(v+0.2, i-0.15, str(f"{round(v/total*100,2)}%"), color='blue', fontweight='bold')

  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)
  plt.xticks(rotation=xrotation)
  return plt

def trend_plot(category_data, xlabel, ylabel, title, xrotation=0, figsize=(10,5)):
  """
  Display trend with line chart
  @param category_data: dict(<category>: {x: <x-axis>, y: <y-axis>})
  """
  plt.figure(figsize=figsize)

  for category in category_data.keys():
    plt.plot(category_data[category]['x'], 
             category_data[category]['y'], 
             label=category)

  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)
  plt.xticks(rotation=xrotation)
  plt.legend()
  return plt

def get_confidence_interval(sample, confidence_level):
  """
  calculate the confidence interval of sample mean without population std
  @param sample: data list (0|1 for proportion)
  @param confidence_level: level of confidence, e.g., 0.95

  @return the confidence error
  """
  sample = np.array(sample)
  sample_size = len(sample)
  sample_std = sample.std()
  t = st.t.ppf((1-confidence_level)/2, df=sample_size-1)
  return t*sample_std/np.sqrt(sample_size)