import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd
import csv


# statisticCategory = input("Which statistical category (rushing/passing):")
# season = input("For which year: ")



# Datset could have multiple pages.  We will set on page 1 to begin
p = 1



# payload = {"statisticCategory":statisticCategory.upper(),"seasonType":"REG","d-447263-p":str(p),"season":season}
# url = 'http://www.nfl.com'
# url = 'https://www.nfl.com/stats/player-stats/'
# url = 'https://www.giants.com/'
url = 'https://www.giants.com/team/stats/'
response = requests.get(url)


print("Response:", response.status_code,response.url) #200 means it went through
print()
print('-----------------------------------------------------------------------------------------------------------------')
print()

# response = requests.get(url,params=payload)
# print("Response:", response.status_code,response.url) #200 means it went through



giants_stats = BeautifulSoup(response.text,'html.parser')
# print(nfl.prettify)

giants_stats_body = giants_stats.body
# print(giants_stats_body)

nfl_div = giants_stats_body.find_all('div')
# print(giants_stats_body_div)

giants_stats_body_main_content = giants_stats_body.find(id="main-content")

print(giants_stats_body_main_content.prettify())
print()
print('<----------------------------------------------------------------------------------------------------------------->')
print()

# with open('first_name.csv') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow([first_name])



# #The website table is partitioned into multiple pages.  We need to know how many pages to iterate

offensive_passing_table = giants_stats_body_main_content.find("div", {"class": "nfl-o-teamstats"})
print(offensive_passing_table.prettify())
print()
print('<----------------------------------------------------------------------------------------------------------------->')
print()


headers = offensive_passing_table.find('thead')
print(headers)
print()
print('<----------------------------------------------------------------------------------------------------------------->')
print()

# pagingLinks = pagingText.findAll("a")
# pages = len(pagingLinks)
# print("Number of page links:",len(pagingLinks))


clean_headers = headers.find_all('th')
print(clean_headers)
print()
print('<----------------------------------------------------------------------------------------------------------------->')
print()

# #Get Header for the table


columnHeader = []

for c in clean_headers:
    columnHeader.append(c.text)
# columnHeader = [c.strip('<th scope="col">') for c in columnHeader]

print(columnHeader)
print()
print('<----------------------------------------------------------------------------------------------------------------->')
print()

# tableRows = []

# for pg in range(1,pages+1):
    
#     #pause our code for a second so that we are not spamming the website with requests. This helps us avoid getting flagged as a spammer.
#     time.sleep(1)
    
#     #update page number in payload
#     payload["d-447263-p"] = pg
#     response = requests.get(url,params=payload)
#     print("Page:",pg,"url:",response.url)
#     soup = BeautifulSoup(response.text,'html.parser')
#     table = soup.find('table', attrs={'id':'result'})
#     rows = table.find_all('tr')

#     for row in rows:
#         cols = row.find_all('td')
#         if cols:
#             cols = [ele.text.strip() for ele in cols]
#             tableRows.append([ele for ele in cols if ele]) # Get rid of empty values



# resultsDF = pd.DataFrame(tableRows, columns=columnHeader)
# display(resultsDF.head(),resultsDF.shape)



# #Save results to Excel
# baseFileName = "NFL_Stats_Demo_"

# resultsDF.to_excel(baseFileName + statisticCategory + "_" + season + ".xlsx",index=False)