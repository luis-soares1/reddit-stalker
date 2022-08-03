from abc import ABC, abstractmethod
from email.policy import default
from pyfiglet import figlet_format
from apihandler.insult_api_handler import InsultAPIHandler as api
from pyfiglet import figlet_format as f
import praw

class CommentAbstractClass(ABC):
    
    @abstractmethod
    def comment() -> None:
        pass
    

class CommentInteractionAbstractClass(ABC):

    @abstractmethod
    def upvote_comment() -> None:
        pass
    
    @abstractmethod
    def downvote_comment() -> None:
        pass


class BotActionsExcpCommentAbstractClass(ABC):

    @abstractmethod
    def bot_instance():
        pass

    @abstractmethod
    def block_user():
        pass

    @abstractmethod
    def unblock_user():
        pass

    @abstractmethod
    def fetch_user_last_comment():
        pass

    @abstractmethod
    def check_for_new_comments():
        pass

    @abstractmethod
    def get_user_comments_txt():
        pass

    @abstractmethod
    def _get_user(usr_name: str):
        pass

    @abstractmethod
    def _fetch_specific_comment():
        pass

    @abstractmethod
    def _fetch_user_comments():
        pass

class BotCommentAbstractClass(ABC):

    @abstractmethod
    def post_comment(self, _reddit: praw.Reddit, comment_to_reply_id: str) -> None:
        pass

    @abstractmethod
    def delete(self, _reddit: praw.Reddit, comment_id: str) -> None:
        pass



class CommentBot(BotCommentAbstractClass):
    
    def __init__(self) -> None:
        super().__init__()

    def post_comment(self, _reddit: praw.Reddit, comment_to_reply_id: str) -> None:
        message = CommentText.comment()
        _reddit.comment(comment_to_reply_id).reply(body=message)

    def delete(self, _reddit: praw.Reddit, comment_id: str) -> None:
        _reddit.comment(comment_id).delete()

class CommentText(CommentAbstractClass):
    
    txt = f"I am a bot that was programmed to stalk you. Still in beta,\
            but I will follow every commment of yours and insult you. Check it out: " 

    @staticmethod
    def comment() -> str:
        return CommentText.txt + api.request_data()
class CommentHyperlink(CommentAbstractClass):
   
    def comment(self) -> None:
        pass

class CommentAsImage(CommentAbstractClass):
    
    def comment(self) -> None:
        pass

class CommentAsASCII(CommentAbstractClass):
    
    def comment(self) -> None:
        return f(text=str(CommentText.comment().split(" ")[-2]), font="standard")
    
class StalkingBot(BotActionsExcpCommentAbstractClass):
    
    def __init__(self) -> None:
        self.reddit = self.bot_instance()
        super().__init__()

    def bot_instance(self):
        return praw.Reddit(
            "bot1", user_agent="Stalking Bot:v1.0.0 (by u/NetflixPremium)"
            )
    
    def block_user(self):
        pass

    def unblock_user(self):
        pass
    
    def get_user_comments_txt(self, usr: str):
        return self._fetch_user_comments(self._get_user(usr))

    def fetch_user_last_comment(self, usr: str):
        for key in self.get_user_comments_txt(usr).keys():
            return key

    def check_for_new_comments(self):
        pass

    def _get_user(self, usr_name: str):
        return self.reddit.redditor(usr_name).name
        
    def _fetch_specific_comment(self, comment_id: str):
        return self.reddit.comment(comment_id).body

    def _fetch_user_comments(self, usr) -> dict:
        """_summary_

        Returns:
            dict: returns a dict with {comment_id: comment in text}
        """
        comment_ids = (c.id for c in self.reddit.redditor(usr).comments.new())
        return {c_id: self.reddit.comment(c_id).body[:10] for c_id in comment_ids}
        


    
    
    

# bot = StalkingBot()
# a = bot.get_user_comments_txt("homemestupendo")



sb = StalkingBot()
a = sb.fetch_user_last_comment("homemestupendo")
print(a)

cb = CommentBot()
cb.post_comment(sb.reddit, a)

# cb = CommentBot()
# cb.post_comment(sb.reddit, )



# c = CommentAsASCII()
# print(c.comment())
# print(text.__dict__)

    




    


    


    


