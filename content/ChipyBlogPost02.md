 Title: Chipy Mentorship (Part 2 of 3) 
 Date: 2017-05-xx 12:00 
 Category: Chipy, Python, Mentorship


# Updates and Fixes
 Since my last post, I finihsed up most of the login stuff, but it could use some polish and an email backend for accounts that need to be reset.  
 
 I have bootstrap working working from the CDN and I am slowly trying to make the site look better.  
 I found some good advice on Chinese font selection and CSS styling [here](URL) 

 I've since added all the database models to Django's admin. Doing that was a rather painless exercise. There is, however, plenty 
 of admin customization customization that could be done.  For now, what I have seems to sufice. 
 
 I showed my wife the full-text search.  She quickly and, quite happily I might add, broke it....  Looks like I need to add some tests.  
 The english definitions in CC-CEDICT are separated by "/" characters without spaces.  This format was the culprit.  When searching for an instances 
 of the word "hello" an occurence like ".../hello..." was not found.  I fixed this with a regex that substitues all the instances of "/" with "\s/\s".


# Next Project - Suggesting Items to Learn
 I really want the site to give the user meaningful characters (a single chinese character) and meaningful words (one or more chinese characters) to learn.
 To do that I either need a table of frequency of occurence of these items in chinese lanaguage.  Since I don't have one, I'll will have to make one.

 This has two main difficulties.  First, is the choice of corpus.  The documents I choose to analyze will impact the frequency of the words observed directly. 
 The second issue is that Chinese texts do not delimit words with a space. No significant whitespace?  That's not very ptyhonic.  Maybe golang would be a better
 choice for this project (China's most popluar language).

 I'm going to basically ignore the first issue and use Wikipedia until a fellow mentee mentioned [this](http://www.lancaster.ac.uk/fass/projects/corpus/UCLA/)

  I had a couple of options to deal with item two.  The first and probably standard way is to use 
  Standfords NLP package as a server or from within pythons NLTK package.  I was going to go this route and set it up NLP as service on my AWS instance.  The problem is java is a bit of a resource hog when it comes to memory. Just spinning up the segmenter and the JVM was enough to burn through the memory I had allocated on my EC2 t.nano instance.  Two steps forward, three steps back.  

 I did a brief search on github which lead me to a python package called [jieba](LINK). After a scanning through the README and a `quick pip install jieba`, I was back in business.   
  

 Having a library like this solves another issue I had. The full text search only worked well on an exact dictionary entry.  Entering an entire sentence
 and getting back a resonable result wasn't possible with previous implementation.  Segmenting the Chinese sentence and searching for each segement has yielded pretty reasonable results. 

 # Implemenation - How to do a SQL Query in a 1,000 Lines of Code or More
 So when you look at the [hanyu.pro](https://www.hanyu.pro) the functionality maynot look all that stellar.  This little site is, in fact, hours and hours of work.  I've found deploying a site to AWS and hardening it too be far more work than I had initally imagined.  I can see why services like google appengine and heruko are
 so popular for smaller projects. I have spent at least 4 hours working on AWS deployment with my mentor and several hours more on my own fiddling and reading docs.  
 Django is a "framework for perfections for prefectionists with deadlines" to be sure, but every page you see is composed of a view, a model, and a template.  There's likely more there to get the data in to the database and maintain it.  

# Dev Ops Stuff...
Jordan helped me out a lot with AWS on the first go around.  I then spent a couple (frustrating) days getting aws, nginx, gunicorn, and django all playing 
nicely together.  

Jordan looked at my setup and noticed a fair amount of security stuff to address...
Okay, so it was only really two items.  There really should be a user with read only access setup to access and server the application.  
This techincally should prevent a hacker from getting in on the active account and modifing the code directly.  The other issue was getting an 
encryption service up and running so I could server HTTPS instead of HTTP.  This is important since I'm potentially dealing with other users' 
passwords.  

After two hours of messing around we were mostly done with rerouting http request to https as an exercise for me to complete.  


#WHAT ELSE????