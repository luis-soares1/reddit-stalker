from abc import ABC, abstractmethod
import praw

class CommentAbstractClass(ABC):

    bag_of_words = []
    
    @abstractmethod
    def comment() -> None:
        pass
    
    @abstractmethod
    def post_comment() -> None:
        pass

    @abstractmethod
    def edit() -> None:
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

    def bot_instance():
        pass

    def block_user():
        pass

    def unblock_user():
        pass

    def _get_user(usr_name: str):
        pass

    def _fetch_user_comments():
        pass


class CommentIntermediateImpl(CommentAbstractClass):
    
    def post_comment() -> None:
        pass

    def delete() -> None:
        pass

class CommentText(CommentIntermediateImpl):
        
    def comment() -> None:
        pass
    
    def edit() -> None:
        pass

class CommentHyperlink(CommentIntermediateImpl):
   
    def comment() -> None:
        pass

    def edit() -> None:
        pass

class CommentAsImage(CommentIntermediateImpl):
    
    def comment() -> None:
        pass
    
    def edit() -> None:
        pass


class CommentAsASCII(CommentIntermediateImpl):
    
    def comment() -> None:
        pass
    
    def edit() -> None:
        pass


class StalkingBot(UserAbstractClass):
    
    def bot_instance():
        reddit = praw.Reddit(
                "bot1", user_agent="Stalking Bot:v1.0.0 (by u/NetflixPremium)"
                )



    




    


    


    


