import requests
# to download the webpage that contains the newest qiestion in stackoverflow
from bs4 import BeautifulSoup 

response = requests.get("https://stackoverflow.com/questions")
# reading the contents of the website 
soup = BeautifulSoup(response.text, "html.parser") # returns the html content of this webpage 
# css selector finds an element in html document
questions = soup.select(".question-summary")
for question in questions:
#print(questions[0]. get("id", 0))#
# select-one does npt return a list instead returns an anchor 
# using getText 
    summary = question.select_one(".question-hyperlink").getText()
    print(summary)
    # to print the vote of each question we do 
    votes = question.select_one(".vote-count-post"). getText()
    print(votes)