import matplotlib.pyplot as plt

def bar_plot(data, xlabel, ylabel, title):
  """
  Plot bar chart
  @param data: dict(label: frequency)
  """
  total = 0
  x_axis = list(data.keys())
  y_axis = list(data.values())

  for i in y_axis:
    total += i

  fig = plt.figure(figsize = (10, 5))
  
  # creating the bar plot
  plt.bar(x_axis, y_axis, color ='maroon', width = 0.4)

  for i, v in enumerate(y_axis):
    plt.text(i-0.15, v+0.2, str(f"{round(v/total*100,2)}%"), color='blue', fontweight='bold')

  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)
  return plt