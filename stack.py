import requests
import re
from bs4 import BeautifulSoup
# download the webpage that has got the newest questions 
# creating a response object to get the endpoint of questions from stackoverflow.
response = requests.get("https://stackoverflow.com/questions")

# creating a soup object using the Beautiful soup class to get the html requests file in a text(string)
# and the html.parser because our file is html.
soup = BeautifulSoup(response.text, "html.parser")
# using a css selector to select the question summary as it is the base anchor 

questions = soup.select(".question-summary")
# select one does not return it as a list and only selects one 
# question_hyperlink is the anchor of the question according to the question 
# getText returns only the question Text 
# print only python related questions 

python = [ 'python', "django", "flask"]
for question in questions:
    answer = question.select_one(".question-hyperlink").getText().lower()
    vote = question.select_one(".vote-count-post").getText().lower()
    words = answer.split()
    for word in words:
        if word in python:
            print(' '.join(map(str, words)))
            print(vote)
