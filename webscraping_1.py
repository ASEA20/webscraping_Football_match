import requests
from bs4 import BeautifulSoup
import csv
#date = input ('Please Enter The Date of Match  mm/dd/yy : ')
d = input ('Please Enter day of Match  dd : ')
m = input ('Please Enter month of Match  mm : ')
y = input ('Please Enter year of Match  yyyy : ')
page = requests.get(f'https://www.yallakora.com/match-center/?date={m}/{d}/{y}')

def main(page):
    
    #code to organize 
    src = page.content
    soup = BeautifulSoup(page.content,'lxml')
    #Details  of match 
    match_details =[]
    Leag_of_mat = soup.find_all("div",{'class':'matchCard'})
    
    def get_info(Leag_of_mat):
        
        #.contents[0] =) first div under div class='matchCard'
        #.find('h2').text show text in h2 
        #.text.strip() show text without space
        leag_title = Leag_of_mat.contents[1].find("h2").text.strip()
        all_mat = Leag_of_mat.contents[3].find_all("div",{'class':'item finish liItem'})
        num_of_mat = len(all_mat)
        
        for i in range(num_of_mat):
            #Teams Name
            
            team_A = all_mat[i].find('div',{'class':'teams teamA'}).text.strip()
            team_B = all_mat[i].find('div',{'class':'teams teamB'}).text.strip()
            
            #Score
            mat_result = all_mat[i].find('div', {'class':'MResult'}).find_all('span', {'class':'score'})
            score = f"{mat_result[0].text.strip()} - {mat_result[1].text.strip()} "
             
            # match time
            mat_time = all_mat[i].find('div', {'class':'MResult'}).find('span', {'class':'time'}).text.strip()
            
            #add match info to match_details
            match_details.append({"championship":leag_title,
                                    "team_A":team_A,
                                    "team_B":team_B,
                                    "Match Time":mat_time,
                                    "score":score})
        
        
    for x in range(len(Leag_of_mat)):
        get_info(Leag_of_mat[x])
        
    #create csv file
    k = match_details[0].keys()
    with open('Desktop/csv_file.csv','w') as f:
        dict = csv.DictWriter(f, k)
        dict.writeheader()
        dict.writerows(match_details)
        print("f")
        

    

main(page)  