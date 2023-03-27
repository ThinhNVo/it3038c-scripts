import webbrowser
import re, sys

# Ask the user to enter a movie name:
print('Name a movie then I search it for you:')
titles = str(input())
if len(titles) == 0:
    print('Enter the title again or I will go to sleep:')
    titles = str(input())
if len(titles) == 0:
    sys.exit(2)

# Ask the user to enter a year 
print('Enter the year or leave blank for the movie:')
year = str(input()).strip()
while not year.isnumeric():
    if len(year) == 0:
        break
    year = input("Please enter a year not words: ")

# Ask for the names of author
print("Enter the name of authors or leave a blank for the movie:")
authors = str(input()).strip()
if authors.isnumeric == True or authors == "":
    authors = ""

# strip all trailing spaces of input and put toghether the inputs
if len(year) != 0 and len(authors) != 0:
    titles = titles.rstrip()
    year = year.rstrip()
    authors = authors.rstrip()
    search = titles + " " + year + " " + authors
elif len(year) == 0 and len(authors) != 0:
    titles = titles.rstrip()
    authors = authors.rstrip()
    search = titles + " " + authors
elif len(year) != 0 and len(authors) == 0:
    titles = titles.rstrip()
    year = year.rstrip()
    search = titles + " " + year
else: 
    titles = titles.rstrip()
    search = titles

#Search for the user
url = (f"https://www.imdb.com/find?q={search.replace(' ', '+').strip()}&ref_=nv_sr_sm")
webbrowser.open(url)
