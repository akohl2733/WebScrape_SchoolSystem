from bs4 import BeautifulSoup
import requests
import pandas as pd


# find link to website that contains the largest college systems in the US
# using wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_the_largest_United_States_colleges_and_universities_by_enrollment'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# located table manually within code and find all html associated with table
# first find all the titles/headers
# split into individual headers in list
table = soup.find_all('table')[2]
school_table = table.find_all('th')
school_table_titles = [ school.text.strip() for school in school_table[1:] ]


# bring in dataframe to visualize headers and data
# find actual column data 
df = pd.DataFrame(columns=school_table_titles)
column_data = table.find_all('tr')


# go through column data and find individual pieces of row
# break it down to individual rows then add to dataframe if in AK territory
for row in column_data[2:]:
    row_data = row.find_all('td')
    ivd = [ data.text.strip() for data in row_data]
    if ivd[-2] == 'Florida' or ivd[-2] == 'Florida' or ivd[-2] == 'North Carolina' or ivd[-2] == 'South Carolina' or ivd[-2] == 'Texas' or ivd[-2] == 'Tennessee' or ivd[-2] == 'Virginia' or ivd[-2] == 'Georgia' or ivd[-2] == 'Missouri' or ivd[-2] == 'Mississippi' or ivd[-2] == 'Alabama' or ivd[-2] == 'Oklahoma' or ivd[-2] == 'Illinois' or ivd[-2] == 'Arkansas' or ivd[-2] == 'Kansas':
        df.loc[ivd[1]] = ivd


# turn dataframe into a csv file
df.to_csv(r'C:\Users\akohl\OneDrive\Desktop\python\WebScrapingPractice\LargeHE.csv', index=False)




