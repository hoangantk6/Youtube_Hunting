## Method
### Data collection

todo: not bias by the animals. why 50 videos.

For data collection, our inital purpose was to collect a manageable sample of videos and their related metadata and comments from an intersection of topics related to hunting with air-rifle and air-rifle market in Vietnam. Ackownledging the constraint of time and human resources, we decided to analyze only 50 representative videos. To leverage computation power to accomplish the tasks automatically, we used Youtube API through two python packages, namely, 'pytube' [citation] (for searching and querying Youtube videos) and 'pyyoutube' [citation] (for extracting Youtube video metadata). Moreover, we used scripting function of Google Sheets to extract comments and populate them into seperated sheets.

For the collection of 50 sampling videos, to avoid any bias towards any specific kind targeted animals (e.g., birds, squirrels, etc), we firstly searched for videos from two search queries "pcp săn bắn" (meaning "pcp hunting" in Vietnamese) and "pcp săn bắt" (meaning "pcp hunting and capture" in Vietnamese). We chose these two queries because it covered general theme of hunting and air-rifle (by doing extensive content exploratory on Youtube we found that 'pcp' is the word standing for air-rifle in Vietnam). We retrieved the first 20 videos from each result. After removing duplications, there were 34 unique videos left. We then extracted the list of tags used by those 34 videos and picked the one that appeared the most, which was "pcp condor" (appeared 5 times). This selection helped us widen the search while maintaining the similarity among the first 34 videos. We repeated the first step in which we collected the first 20 videos resulted from that keyword, which added 20 more unique videos. In total, we found 54 videos around the theme pcp and hunting. After that, we collected the list of unique channels of those 54 videos, which resulted in 48 unique channels. Next, we manually removed channels that did not meet any of the three criteria: (1) videos produced by Vietnamese in Vietnam, (2) authentic content (i.e., not a reup), and (3) related to/focused on hunting with rifles. The cleansing returned 36 unique targeted channels. We then populated all videos from those 36 channels into a spreadsheet, which resulted in 3081 videos. After that, we shuffled and pick a sample of 50 videos for analysis.

For the collection of metadata, we utilized a python package named 'pyyoutube' [citation] to extract Youtube video metadata. We collected the following video metadata with pyyoutube:  video title, video id, video url, video description, number of likes, number of views, published time, Youtube topic categories. As Youtube disabled public view of number of dislikes on November 10th, 2021 and from API on December 13th, 2021 [citation], we had to use a browser add-on named Return YouTube Dislike (RYD) on Firefox [https://returnyoutubedislike.com/] to estimates the number of dislikes of that videos. As described by the developers, they used a combination of dislikes archival to return archived dislikes or extrapolation for videos that has not been archived. We extracted the dislikes on January 3rd, 2021, so it was likely that the dislikes were the extrapolatory result.

For the collection of comments, 



### Data annotation
we avoid keyword-based tagging but relies on the kind of information provided in the comments.


Chọn những con bị bắn, dù chết hay ko, mà có dấu hiệu bị dính đạn hoặc bị thương.
### Data analysis