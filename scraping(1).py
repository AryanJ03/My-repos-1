from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
print('Okay lets start web scraping!!!')
# requests the source of the webpage
source = requests.get('https://www.thecompleteuniversityguide.co.uk/league-tables/rankings').text
soup = BeautifulSoup(source, 'lxml')
# html5lib is a parser library . lxml can also be used but i cant install

# print("This is the university website homepage")

# print(soup.prettify()) prints the code in a indented and neat format.

uni_table = soup.find('table')

# print(uni_table.prettify()) prints the html of the table
print('These are the top 130 universities')
uni_list = uni_table.tbody.text
#print('What is this?')
#print(uni_list) this is uni rank and name and stds all together.

csv_file = open('league_table.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Rank', 'Institution name'])


uni_rank_list = []
for ranks in uni_table.findAll('td', class_='league-table-rank'):
   uni_rank = ranks.text
   print(uni_rank)
   csv_writer.writerow([uni_rank])
   uni_rank_list.append(uni_rank) # only the ranks

uni_names_list=[]

for unikenaam in uni_table.findAll('td', class_='league-table-institution-name'):
   uni_names = unikenaam.a.text
   print(uni_names)
   csv_writer.writerow([uni_names])
   uni_names_list.append(uni_names) # only uni names



#this is from edureka.com but not working error is index should have a value
#df = pd.DataFrame({'Rank': uni_rank, 'Name': uni_names})
#df.to_csv('uni_table.csv', index=False, encoding='utf-8')







entry_stds_list = []

for stds in uni_table.findAll('td', class_='league-table-column-value'):
   entry_stds = stds.text
   print(entry_stds)
   csv_writer.writerow([entry_stds])
   entry_stds_list.append(entry_stds)
print(str(entry_stds_list))

csv_file.close()
'''

final_std_list = []

for standards in entry_stds_list:
   final_std_list.append(standards.strip())
#print(final_std_list)




# to print out the csv file in the console
df = pd.read_csv('league_table.csv')
print(df)



#csv_writer.writerow([uni_rank_list, uni_names_list, entry_stds_list])

#print(uni_rank_list)
#print(uni_names_list)

'''