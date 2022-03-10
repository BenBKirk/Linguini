
from database.database import DatabaseHelper
from database.user import User
import re

class Highlighters:
    def __init__(self):
        self.user_id = User().get_user_id()
        pass

    def find_appropriate_highlighter_id(self,word,confidence):
        if self.is_word_actually_a_phrase(word):
            confidence = confidence + "-sent"
        with DatabaseHelper() as db:
            id = db.fetch_one("SELECT id FROM highlighters WHERE user_id = ? AND name =?",(self.user_id,confidence))[0]
        return id
        

    def is_word_actually_a_phrase(self,word):
        pattern = re.compile("\s") #this is a regex that matches any whitespace
        if re.search(pattern, word):
            return True
        return False
