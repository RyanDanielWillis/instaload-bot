# current issue with autoscraper not working correctly in loop


from autoscraper import AutoScraper

import csv

import requests
import bs4

import time



url1 = 'https://expoplaza-tuttofood.fieramilano.it/en/exhibitors/alfa-ath-d-koukoutaris-sa'

wanted_list = ['info@alfapastry.com']

scraper = AutoScraper()
result = scraper.build(url1, wanted_list)
print(result)

result2 = scraper.get_result_similar('https://expoplaza-tuttofood.fieramilano.it/en/exhibitors/a-pizza')

scraper.save('email-scrape-set')
print(result2)

result_list = [result, result2]

#main page
URLS = []
URL = 'https://expoplaza-tuttofood.fieramilano.it/en/exhibitors'

# Fetch all the HTML source from the url
response = requests.get(URL)
time.sleep(3)


# Parse HTML and extract links
soup = bs4.BeautifulSoup(response.text, 'html.parser')
links = soup.find_all("a")

# save dirty url list
for link in links:
    URLS.append(str(link.get('href')))

URLS.insert(0, 'Dirty URLS: --------  ')
print(URLS)

# clean URLs
clean_urls = []
for x in URLS:
    w = 1
    clean_url= 'https://expoplaza-tuttofood.fieramilano.it' + URLS[w]
    clean_urls.append(clean_url)
    w += 1
    

clean_urls.insert(0, 'Clean URLS : --------------')
print(clean_urls)

rows = []
#scrape emails from clean url list
for i in clean_urls:

    #setup scraper again
    url1 = 'https://expoplaza-tuttofood.fieramilano.it/en/exhibitors/alfa-ath-d-koukoutaris-sa'

    wanted_list = ['info@alfapastry.com']

    scraper = AutoScraper()
    scraper.build(url1, wanted_list)

    z = 1
    rows.append(scraper.get_result_similar(clean_urls[z]))
    z += 1
    time.sleep(2)

rows.extend(result_list)
# field names 
fields = ['Address', 'City', 'Country', 'Website', 'Stand', 'Phone', 'Email'] 
  
with open('email_scrape.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(rows)

