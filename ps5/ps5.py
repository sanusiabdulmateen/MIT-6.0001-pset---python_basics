# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1
# TODO: NewsStory

class NewsStory(object):
    """
    Represents a single news story from a RSS feed.
    """
    def __init__(self, guid, title, description, link, pubdate):
        """
        guid: A globally unique identifier for this story.
        title: The news story's headine.
        description: A summary of the news story.
        link: A link to a website with the entire story.
        pubdate: Date the news was published.
        """
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        """
        :returns: The Globally Unique Identifier of the NewsStory object.
        :return type: str
        """
        return self.guid
    
    def get_title(self):
        """
        :returns: The title of the NewsStory object.
        :return type: str
        """
        return self.title
    
    def get_description(self):
        """
        :returns: The description of the NewsStory object.
        :return type: str
        """
        return self.description
    
    def get_link(self):
        """
        :returns: The link of the NewsStory object.
        :return type: str
        """
        return self.link
    
    def get_pubdate(self):
        """
        :returns: The publication date of the NewsStory object.
        :return type: str
        """
        return self.pubdate
    
#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger

class PhraseTrigger(Trigger):
    """
    Represents a trigger for a phrase.
    """
    def __init__(self, phrase):
        """
        :param phrase: The phrase for the trigger; words should only be
                       separated by a space.
        :type phrase: str
        """
        self.phrase = phrase

    def is_phrase_in(self, text):
        """
        Checks if the phrase, separated only by spaces or punctuation, is in
        the provided text.

        :param phrase: The text to find the phrase in.
        :type phrase: str
        :returns: Whether or not the phrase in the text.
        :rtype: bool
        """
        punct = string.punctuation 
        no_punct_text = ''.join(char if char not in punct else ' ' for char in text )
        cleaned_text = ' '.join(no_punct_text.lower().split()) 
        no_punct_phrase = ''.join(char if char not in punct else ' ' for char in self.phrase )
        cleaned_phrase = ' '.join(no_punct_phrase.lower().split())
        
        # Split the cleaned text and phrase into lists of words 
        text_words = cleaned_text.split() 
        phrase_words = cleaned_phrase.split()
        
        # Check if all words in the phrase appear in the text in the same order 
        phrase_index = 0 
        for word in text_words: 
            if word == phrase_words[phrase_index]: 
                phrase_index += 1 
                if phrase_index == len(phrase_words): 
                    return True 
            else:
                # Reset the phrase index if the words are not in order
                phrase_index = 0
        return False                      

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    """
    Represents a trigger for a phrase in a news story's title.
    """
    def __init__(self,phrase):
        """
        :param phrase: The phrase for the trigger; words should only be
                       separated by a space.
        :type phrase: str
        """
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        """
        Checks if the phrase is in the provided news story's title.

        :param story: The story to check the publication date for.
        :type story: NewsStory
        :returns: Whether or not the phrase in the news story's title.
        :rtype: bool
        """
        return PhraseTrigger.is_phrase_in(self, story.get_title())

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self,phrase):
        """
        Represents a trigger for a phrase in a news story's description.
        """
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        """
        Checks if the phrase is in the provided news story's description.

        :param story: The story to check the publication date for.
        :type story: NewsStory
        :returns: Whether or not the phrase in the news story's description.
        :rtype: bool
        """
        return PhraseTrigger.is_phrase_in(self, story.get_description())

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, date_string):
        """
        Represents a trigger for a certain time.
        """
        time = datetime.strptime(date_string, "%d %b %Y %H:%M:%S")\
            .replace(tzinfo=pytz.timezone("EST"))

        self.time = time

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    """
    Represents a trigger for a news story published before a certain time.
    """
    def __init__(self, date_string):
        """
        :param time: The time for the trigger following the format of
                     "%d %b %Y %H:%M:%S" in the EST time zone.
        :type time: str
        """
        TimeTrigger.__init__(self, date_string)

    def evaluate(self, story):    
        """
        Checks if the provided news story is published before the trigger's
        time.

        :param story: The story to check the publication date for.
        :type story: NewsStory
        :returns: Whether or not the story was published before the trigger's
                  time.
        :rtype: bool
        """
        result = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

        return result < self.time
    
class AfterTrigger(TimeTrigger):
    """
    Represents a trigger for a news story published after a certain time.
    """
    def __init__(self, date_string):
        """
        :param time: The time for the trigger following the format of
                     "%d %b %Y %H:%M:%S" in the EST time zone.
        :type time: str
        """
        TimeTrigger.__init__(self, date_string)

    def evaluate(self, story):
        """
        Checks if the provided news story is published after the trigger's
        time.

        :param story: The story to check the publication date for.
        :type story: NewsStory
        :returns: Whether or not the story was published after the trigger's
                  time.
        :rtype: bool
        """ 
        result = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

        return result > self.time

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    """
    Represents a trigger that inverts the evaluation of the given trigger for a
    specific story, used to exclude stories that satisfy the given trigger.
    """
    def __init__(self, trigger):
        """
        :param trigger: The trigger to invert the evaluation for.
        :type trigger: Trigger
        """
        self.trigger = trigger

    def evaluate(self, story):
        """
        :param story: The news story to check.
        :type story: NewsStory
        """
        return not self.trigger.evaluate(story)

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    """
    Represents a trigger that checks if a specific story satisfies both given
    triggers.
    """
    def __init__(self, trigger1, trigger2):
        """
        :param trigger1: The first trigger to check.
        :type trigger1: Trigger
        :param trigger2: The second trigger to check.
        :type trigger2: Trigger
        """
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        """
        :param story: The news story to check.
        :type story: NewsStory
        :returns: Whether or not a specific story satisfies both triggers.
        :rtype: bool
        """
        result = self.trigger1.evaluate(story) and self.trigger2.evaluate(story)
        return result

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    """
    Represents a trigger that checks if a specific story satisfies at least one
    of the given triggers.
    """
    def __init__(self, trigger1, trigger2):
        """
        :param trigger1: The first trigger to check.
        :type trigger1: Trigger
        :param trigger2: The second trigger to check.
        :type trigger2: Trigger
        """
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        """
        :param story: The news story to check.
        :type story: NewsStory
        :returns: Whether or not a specific story satisfies one of the
        triggers.
        :rtype: bool
        """
        result = self.trigger1.evaluate(story) or self.trigger2.evaluate(story)
        return result

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    filtered_stories = []
    for story in stories:
        if any([trigger.evaluate(story) for trigger in triggerlist]):
            filtered_stories.append(story)

    return filtered_stories


#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    # dict for mapping triggers
    t_map = {'TITLE':TitleTrigger,
                        'DESCRIPTION':DescriptionTrigger,
                        'AFTER':AfterTrigger,
                        'BEFORE':BeforeTrigger,
                        'NOT':NotTrigger,
                        'AND': AndTrigger,
                        'OR':OrTrigger}
    # Initialize trigger dictionary, trigger list
    trigger_dict = {}
    trigger_list = [] 

    # Helper function to parse each line, create instances of Trigger objects,
    # and execute 'ADD'
    def line_reader(line):
        """
        function to parse each line, create instances of Trigger objects,
        and execute 'ADD'
        """
        data = line.split(',')
        if data[0] != "ADD":
            if data[1] == "OR" or data[1] == "AND":
                trigger_dict[data[0]] = t_map[data[1]](trigger_dict[data[2]],
                        trigger_dict[data[3]])
            else:
                trigger_dict[data[0]] = t_map[data[1]](data[2])
        else: 
            trigger_list[:] += [trigger_dict[t] for t in data[1:]]

    for line in lines:
        line_reader(line)
    
    return trigger_list

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

