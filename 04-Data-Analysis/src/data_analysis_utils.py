import matplotlib.pyplot as plt


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

def bar_plot(data, xlabel, ylabel, title, orientation='verticle', xrotation=0, figsize=(10,5)):
  """
  Plot bar chart
  @param data: dict(<label>: <frequency>)
  """
  total = 0
  x_axis = list(data.keys())
  y_axis = list(data.values())

  for i in y_axis:
    total += i

  plt.figure(figsize=figsize)
  
  # creating the bar plot
  if orientation=='verticle':
    plt.bar(x_axis, y_axis, color ='maroon', width = 0.4)

    for i, v in enumerate(y_axis):
      plt.text(i-0.15, v+0.2, str(f"{round(v/total*100,2)}%"), color='blue', fontweight='bold')

  else:
    plt.barh(x_axis, y_axis, color ='maroon')

    for i, v in enumerate(y_axis):
      plt.text(v+0.2, i-0.15, str(f"{round(v/total*100,2)}%"), color='blue', fontweight='bold')

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