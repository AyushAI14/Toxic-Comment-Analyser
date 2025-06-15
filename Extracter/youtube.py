from urllib.parse import urlparse, parse_qs
from youtube_comment_downloader import YoutubeCommentDownloader


class YtCommentExtracter:
    def __init__(self):
        self.downloader = YoutubeCommentDownloader()


    def extract_video_id(url):
        parsed_url = urlparse(url)
        # print(parsed_url)
        if 'youtu.be' in parsed_url.netloc:
            return parsed_url.path.strip('/')

        return None
    
    def get_youtube_comments(self,video_url, max_comments=100):
        if 'youtu.be' in video_url:
            video_id=self.extract_video_id(video_url)
        else:
            video_id = video_url.split('v=')[-1]

        comments = []
        for comment in self.downloader.get_comments_from_url(f"https://www.youtube.com/watch?v={video_id}"):
            comments.append(comment['text'])
            if len(comments) >= max_comments:
                break
        return comments


s  = YtCommentExtracter()
print(s.get_youtube_comments("https://www.youtube.com/watch?v=INxnoCQxfsI"))