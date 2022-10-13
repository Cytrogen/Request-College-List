import csv
import requests
from lxml import etree
from random import randint
from time import sleep

with open("college_list.csv", "w", newline='') as file:
    writer = csv.writer(file)
    
    head = ['College Rank', 'College Name']
    writer.writerow(head)
    
    page = 1

    while page < 10:
        if page == 1:
            url = "https://www.niche.com/colleges/search/best-colleges-for-computer-science/"
        else:
            url = f"https://www.niche.com/colleges/search/best-colleges-for-computer-science/?page={page}"
            
        header = {
            "User-Agent":"XXXXXXXXXXXXXXX",
            "Cookie": 'XXXXXXXXXXXXXX'}

        html = requests.get(url, headers=header).text
        html_etree = etree.HTML(html)

        count = 1
        while count < 50:
            Rank = html_etree.xpath(f'//*[@id="maincontent"]/main/div[1]/div[3]/section/ol/li[{count}]/div/div/a/div[2]/div[1]/text()')
            Name = html_etree.xpath(f'//*[@id="maincontent"]/main/div[1]/div[3]/section/ol/li[{count}]/div/div/a/div[2]/div[2]/h2/text()')
            
            Rank = str(Rank)
            Name = str(Name)
            
            Rank = Rank.replace("['", "")
            Rank = Rank.replace(" Best Colleges for Computer Science in America']", "")
            
            if Rank == "[]" and Name == "[]":
                print("空结果，继续！")
                count += 1
                continue
            elif "Sponsored Result" in Name:
                print("广告结果，继续！")
                count += 1
                continue
            else:
                print(Rank)
                print(Name)
                
            writer.writerow([Rank, Name])
            
            # sleep(randint(1, 2))
            count += 1
    
        page += 1