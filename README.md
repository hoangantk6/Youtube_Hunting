# youtube-hunting

## Method
### Data collection

todo: why the 3 criteria. not bias by the animals. why 50 videos.

For the collection of videos, our purpose was to collect videos from a wide range of topics related to hunting and pcp in Vietnam. To leverage computation power to do that automatically, we used Youtube API through a python package named 'pytube' to search and query videos from Youtube automatically. Firstly, we searched for videos from two search queries "pcp săn bắn" (meaning "pcp hunting" in Vietnamese) and "pcp săn bắt" (meaning "pcp hunting and capture" in Vietnamese) and retrieved the first 20 videos from each result. After removing duplications, there were 34 unique videos left. We then extracted the list of tags used by those 34 videos and picked the one that appeared the most, which was "pcp condor" (appeared 5 times). We repeated the first step in which we collected the first 20 videos resulted from that keyword, which added 20 more unique videos. In total, we found 54 videos around the theme pcp and hunting. After that, we collected the list of unique channels of those 54 videos, which resulted in 48 unique channels. Next, we manually removed channels that did not meet any of the three criteria: (1) videos produced by Vietnamese in Vietnam, (2) authentic content (i.e., not a reup), and (3) related to/focused on hunting with rifles. The cleansing returned 36 unique targeted channels. We then populated all videos from those 36 channels into a spreadsheet, which resulted in 3081 videos. After that, we shuffled and pick a sample of 50 videos for analysis.



1. Search the first 20 videos with keyword "pcp săn bắn"
2. Search the first 20 videos with keyword "pcp săn bắt", pick ones that not duplicate from previous search (14 videos)
3. find the most tags from those 34 videos -> pcp condor (5 times)
4. Search the first 20 videos with keyword "pcp condor", pick ones that not duplicate from previous searches (20 videos)

5. remove channels that not (1) in Vietnam, (2) not authentic contents, (3) not related to/focused on hunting with rifles (12 channels)
6. From 36 unique channels, find all videos of them, get 3081 videos
7. Shuffle and pick 50 sample videos
--> not bias by the animals, e.g., birds

Example of removed channel:
+ PVN PCP	https://www.youtube.com/channel/UCqYj765zgZ_YyPme3GjSX3A
+ PVN PCP	https://www.youtube.com/channel/UCOAVWMWlga-muWFxfvuPA8w
+ Aviary PCP	https://www.youtube.com/channel/UCJ3nA6oOtLM7RWyYZz4l9kA
+ Trình TC	https://www.youtube.com/channel/UCCWGFE9To_kCnr8SYGw3bGA
+ Huỳnh Hải	https://www.youtube.com/channel/UCLqCQ8YutHNcKKZNCWQtTEg
+ Shop săn bẫy Tuấn Lan	https://www.youtube.com/channel/UCHRICXjbfqyE7dXqU6itv0g

https://returnyoutubedislike.com/ 


Chọn những con bị bắn, dù chết hay ko, mà có dấu hiệu bị dính đạn hoặc bị thương.

### Data annotation
we avoid keyword-based tagging but relies on the kind of information provided in the comments.


### Data analysis


### todo
+ [ ] double-check comment tag
+ [ ] state clearly error bar is 95% CI

# note
- tiếp xúc với hành vi bạo hành động vật ở trẻ có thể dẫn đến hành vi bạo lực với con người khi trưởng thành