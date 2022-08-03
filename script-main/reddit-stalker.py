from abc import ABC, abstractmethod
from pyfiglet import figlet_format
import praw

class CommentAbstractClass(ABC):
    
    @abstractmethod
    def comment() -> None:
        pass
    
    @abstractmethod
    def post_comment() -> None:
        pass

    @abstractmethod
    def delete() -> None:
        pass



class CommentInteractionAbstractClass(ABC):

    @abstractmethod
    def upvote_comment() -> None:
        pass
    
    @abstractmethod
    def downvote_comment() -> None:
        pass


class UserAbstractClass(ABC):

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



class CommentIntermediateImpl(CommentAbstractClass):
    
    def __init__(self) -> None:
        super().__init__()

    def post_comment(self, _reddit: praw.Reddit, comment_to_reply_id: str) -> None:
        message = self.retrieve_comment()
        _reddit.comment(comment_to_reply_id).reply(body=message)

    def delete(self, _reddit: praw.Reddit, comment_id: str) -> None:
        _reddit.comment(comment_id).delete()


class CommentHyperlink(CommentIntermediateImpl):
   
    def comment() -> None:
        pass


class CommentAsImage(CommentIntermediateImpl):
    
    def comment() -> None:
        pass



class CommentAsASCII(CommentIntermediateImpl):
    
    def comment() -> None:
        pass
    

class StalkingBot(UserAbstractClass):
    
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

    def _get_user(self, usr_name: str):
        return self._reddit.redditor(usr_name).name
        
    def _fetch_specific_comment(self, comment_id: str):
        return self._reddit.comment(comment_id).body

    def _fetch_user_comments(self, usr) -> dict:
        """_summary_

        Returns:
            dict: returns a dict with {comment_id: comment in text}
        """
        comment_ids = (c.id for c in self._reddit.redditor(usr).comments.new())
        return {c_id: self._reddit.comment(c_id).body[:10] for c_id in comment_ids}
        

class InsultFactory:
    pass
    #@staticmethod
    
    

bot = StalkingBot()
a = bot.get_user_comments_txt("homemestupendo")

text = CommentIntermediateImpl()
text.post_comment()


# print(text.__dict__)

    




    


    


    


