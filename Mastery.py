#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json 
## Khoi tao
options = webdriver.ChromeOptions();
options.add_argument("--start-maximized");


def lol_crawling():
    ## Execute the program
    print("Developed by Maximusss - Last updated: 10:42 p.m 1st March 2021");
    big_data = [];
    browser = webdriver.Chrome("chromedriver.exe",options=options);
    browser.get("https://lmssplus.com/top-thong-thao");
    champion_length = len(browser.find_elements_by_class_name("selectChampionForTop_champion__2HZfg"));
    time.sleep(1);
    
    for c in range(0,2):
        print("Start!");
        browser.get("https://lmssplus.com/top-thong-thao");
        time.sleep(1);
        
        champion = browser.find_elements_by_class_name("selectChampionForTop_champion__2HZfg")[c];
        time.sleep(1);
        
        champion_name = browser.find_elements_by_css_selector(".selectChampionForTop_champion__2HZfg span")[c].get_attribute("innerHTML");
        champion.click();
        print(champion_name);
        time.sleep(3);
        
        rank_points_list = len(browser.find_elements_by_class_name("cell-top-rank"));
        mini_data = [];
        
        ## Get points list
        for i in range(3,33):
            if((i+1)%3 == 0):
                champion_point = browser.find_elements_by_class_name("cell-top-rank")[i];
                value = champion_point.get_attribute("innerHTML");
                summoner = {
                    'highest': int(value.replace(",","")),
                    'second_highest': 0,
                    'rank': '',
                    'champion': champion_name,
                    'games': 0,
                    'age': 0,
                    'win_rate': 0
                };
                mini_data.append(summoner);
                
        ## Get rank of these players
        rank_name_list = len(browser.find_elements_by_class_name("cell-name-displayname"));
        
        for j in range (0,10):
            time.sleep(3);
            player = browser.find_elements_by_class_name("cell-name-displayname")[j];
            player.click();
            
            time.sleep(3);
            player_rank = browser.find_elements_by_class_name("rankBox_rankName__VcGiL")[0];
            
            if(player_rank.get_attribute("innerHTML") == "Unranked"):
                rank = browser.find_elements_by_class_name("rankPrev_rankRowRightName__31zdy")[0].get_attribute("innerHTML");
            else:
                 rank = player_rank.get_attribute("innerHTML");
            
            second_point = browser.find_elements_by_class_name("masteries_tqOneSortDetail__2VgWs")[0].get_attribute("innerHTML");
            games = browser.find_elements_by_class_name("statsPreview_statBox__2HNrA span:nth-of-type(1)")[0].get_attribute("innerHTML");
            age = browser.find_elements_by_class_name("statsPreview_statBox__2HNrA span:nth-of-type(1)")[1].get_attribute("innerHTML");
            win_rate = browser.find_elements_by_class_name("statsPreview_statBox__2HNrA span:nth-of-type(1)")[2].get_attribute("innerHTML");
            
            mini_data[j]["second_highest"] = int(second_point.split(" ")[0].replace(",",""));
            mini_data[j]["rank"] = rank;
            mini_data[j]["games"] = int(games);
            mini_data[j]['age'] = int(age);
            mini_data[j]['win_rate'] = float(win_rate);
            browser.back();
        big_data.extend(mini_data);
        print(mini_data);
    return big_data;
    ## End the program!
print(lol_crawling());

