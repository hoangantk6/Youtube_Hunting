// Extract Youtube comment thread into a Google Spreadsheet (GS) using GS Scripting extension.
// Reference: https://github.com/MAN1986/LearningOrbis/blob/master/scrapeCommentsWithReplies.gs

function comment_extractor_google_sheet(){
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var result=[['author_channel_id', 
                 'published_time', 
                 'comment_id', 
                 'video_id', 
                 'author_display_name',
                 'parent_comment_id', 
                 'num_like', 
                 'content']];
    var vid = ss.getSheets()[0].getRange(1,1).getValue();
    var nextPageToken=undefined;
    
    while(1){
     
        var data = YouTube.CommentThreads.list('snippet', {videoId: vid, maxResults: 100, pageToken: nextPageToken})
        nextPageToken=data.nextPageToken
        for (var row=0; row<data.items.length; row++) {
            result.push([
              data.items[row].snippet.topLevelComment.snippet.authorChannelId.value,
              data.items[row].snippet.topLevelComment.snippet.publishedAt,
              data.items[row].snippet.topLevelComment.id,
              data.items[row].snippet.topLevelComment.snippet.videoId,
              data.items[row].snippet.topLevelComment.snippet.authorDisplayName,
              data.items[row].snippet.topLevelComment.snippet.parentId,
              data.items[row].snippet.topLevelComment.snippet.likeCount,
              data.items[row].snippet.topLevelComment.snippet.textDisplay
            ]);
  
          // reply
          if(data.items[row].snippet.totalReplyCount>0){
            parent=data.items[row].snippet.topLevelComment.id
            var nextPageTokenRep=undefined
            while(1){
              var reply=YouTube.Comments.list('snippet', {videoId: vid, maxResults: 100, pageToken: nextPageTokenRep,parentId:parent})
              nextPageTokenRep=reply.nextPageToken;
              for (var i=reply.items.length-1;i>=0;i--){
                result.push([
                  reply.items[i].snippet.authorChannelId.value,
                  reply.items[i].snippet.publishedAt,
                  reply.items[i].id,
                  reply.items[i].snippet.videoId,
                  reply.items[i].snippet.authorDisplayName,
                  reply.items[i].snippet.parentId,
                  reply.items[i].snippet.likeCount,
                  reply.items[i].snippet.textDisplay
                ]);
              }
              if(nextPageTokenRep =="" || typeof nextPageTokenRep === "undefined"){
                break
              }
            } 
          }
        }   
      if(nextPageToken =="" || typeof nextPageToken === "undefined"){
        break;
      }
  }
  
  var newSheet=ss.insertSheet(ss.getNumSheets())
  newSheet.getRange(1, 1,result.length,result[0].length).setValues(result)
  
  }
  
  