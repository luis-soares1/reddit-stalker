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

    def block_user():
        pass

    def unblock_user():
        pass

    def _get_user(usr_name: str):
        pass

    def _fetch_user_comments():
        pass




class CommentText(CommentAbstractClass):
        
    def comment() -> None:
        pass
    
    def post_comment() -> None:
        pass

    def edit() -> None:
        pass

    def delete() -> None:
        pass
class CommentHyperlink(CommentAbstractClass):
   
    def comment() -> None:
        pass
    
    def post_comment() -> None:
        pass

    def edit() -> None:
        pass

    def delete() -> None:
        pass
class CommentAsImage(CommentAbstractClass):
    
    def comment() -> None:
        pass
    
    def post_comment() -> None:
        pass

    def edit() -> None:
        pass

    def delete() -> None:
        pass

class CommentAsASCII(CommentAbstractClass):
    
    def comment() -> None:
        pass
    
    def post_comment() -> None:
        pass

    def edit() -> None:
        pass

    def delete() -> None:
        pass


    




    


    


    


