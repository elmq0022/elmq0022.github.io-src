 Title: Chipy Mentorship (Part 1 of 3) 
 Date: 2017-04-20 12:00
 Category: Chipy, Python, Mentorship


# About the Chipy Mentorship
 If you are reading this you likely already know about the Chipy Mentorship Program and how great it is. If not, you really should check it out at [Chipy Mentor](https://chipymentor.org/).  Also, stop by and meet the people from [Chipy](http://chipy.org) that sponsor this event. 

 Personally, I think Chipy is one of the best meetups in the country, and they run one heck of a mentorship program as well. Essentially, they pair a volunteer mentor with a mentee who receives three months of guidance on a project of their choice. They also require participation in a variety of workshops, blog posts, and check-ins to make sure everyone stays on track.  


# My Mentor
 I'm really glad that I got paired with Jordan. Not only is he knowledgable about his craft, but he's also super helpful and patient. I really like the fact that he has us using a workflow similar to professional developers where I push my work to GitHub for his review and approval before any merges are made to the project's main branch. 
 
 Also, we both rock older Thinkpads laptops which I think is cool :).


# About My Project - Hanyu 
 I decided to build a web application that could help people learn Mandarin Chinese. Basically, the application will have a database of Chinese characters and phrases and recommend what a user should study next based on the Chinese they already know and the frequency of the character's usage in Chinese.


# The Development Stack
 I am using some pretty standard python web tech for this project. The heavy hitters are Django and PostgreSQL.  I am also using Git and GitHub for source control, and a splash of Bootstrap3 to make things look a little nicer.  The project is hosted on AWS with Nginx and Gunicorn serving pages. 


# Preparation
 I knew it would be unproductive to start this program without any preparation.  So, I worked through a good chunk of the following resources the month prior to the mentorship kickoff.  

 - [Lynda.com's Up and Running with Django](https://www.lynda.com/Django-tutorials/Up-Running-Python-Django/386287-2.html)
 - [The first 6 chapters of Django Core](http://djangobook.com/)
 - [Team Treehouse's Django Track](https://teamtreehouse.com/)
 - [The First 3 chapters of the ebook Pro Git](https://git-scm.com/book/en/v2)
 
This preperation has allowed me to ask my mentor reasonable questions about Django from the start and considerably accelerated my progress. 

By the way, if you want to get started in Django development, all these resources are inexpensive or freely available through the local library. 

  
# Progress
I've done quite a bit of work over the past few weeks. Prior to this post I was able to do the following:

- Setup a GitHub repository.  
- Setup a development environment.
- Learn some PostgreSQL.
- Setup an EC2 and an RDS instances on AWS.
- Register a domain name. 
- Build a Django management command to load the database from [CC-CEDICT](https://cc-cedict.org/wiki/start).
- Build a Django management command to update the database [CC-CEDICT](https://cc-cedict.org/wiki/start).
- Implement full text search over the entries in the database.
- Build Django views and forms to search the dictionary.
- Install and learn a little Bootstrap3 and django-bootstrap3 to make the site look better.
- Leveraged Django's class based views to build a user authentication app.  
- Setup this blog on GitHub Pages using [Pelican](https://blog.getpelican.com). 


# Populating the Database
 If this application is to be of any value, it needs a reasonably large source of Chinese words and their English equivalents.  Fortunately for me, there is a community project which creates and maintains [CC-CEDICT](https://cc-cedict.org/wiki/start).  For my first task, Jordan had me make a Django management command to load this data into a database. Here's the code that I wrote: 

```python
# This module will load the Entry table using the CC-CEDIct Chinese to English dictionary located
# at https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip

import io
import re
import zipfile

import requests
from django.core.management.base import BaseCommand, CommandError

from dictionary import models

class Command(BaseCommand):
    help = 'loads the online version of CC-CEDICT Chinese to English dictionary into the database'

    def __init__(self):
        super().__init__()
        # The CC-CEDICT dictionary is a work in progress.
        # The following regex pattern will match all well formed entries in the dictionary

        pattern = r'''
        (?P<traditional>\w+)                # first character
        \s+                                 # spaces
        (?P<simple>\w+)                     # second character
        \s+                                 # spaces
        \[                                  # start pronunc
        (?P<pin_yin>[a-z\d\s]+)             # pronunc pattern
        \]                                  # end pronunc
        \s+                                 # spaces
        /                                   # start the defintions 
        (?P<definitions>.+)                 # definitions
        /                                   # end the defintions 
        '''
        self.valid_entries = re.compile(pattern, re.M|re.I|re.X)
        self.url = r'https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip'

    def download_dict(self):
        # Download Chinese-English dictionary zip file and return the contents as a string.
        r = requests.get(self.url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()
        file_name = z.namelist()[0]
        with z.open(file_name) as f:
            text = f.read().decode("utf-8")
        return text

    def add_to_db(self, matches):
        count = 0
        entries = []

        for match in matches:
            entry = models.Entry(
                traditional=match['traditional'],
                simple=match['simple'],
                pin_yin=match['pin_yin'],
                definitions=match['definitions']
            )
            entries.append(entry)
            count += 1

        models.Entry.objects.bulk_create(entries)
        return count

    def handle(self, *args, **options):
        print("Downloading dictionary from {}.".format(self.url))
        text = self.download_dict()
        print("Download complete.")

        print("Deleting entries from database.")
        models.Entry.objects.all().delete()

        print("Entering data into database.")
        matches = self.valid_entries.finditer(text)
        count = self.add_to_db(matches)

        print("Complete. There were {} entries entered into the database.".format(count))
```

This did take several attempts on my part. My first iteration, for example, did not use Django's ```bulk_create``` function.  I figured hitting the database over and over would be inefficient, I didn't realize it would take hours to load.  Also, my intial code had two models, one for the Chinese entries and another for the English definitions.  That approach proved to be uncessarily complicated while not providing any tangible benefits.


# Conclusion
So far my mentorship is off to a great start, and I should have a useful project by the end.  If you want to see my work so far, checkout the live app at [hanyu.pro](http://hanyu.pro) or the code on [GitHub](https://github.com/elmq0022/hanyu).
