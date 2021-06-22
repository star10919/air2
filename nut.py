import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

class Nutrition(object):
    url = 'https://terms.naver.com/list.naver?cid=59320&categoryId=59320'
    driver_path = 'c:/Program Files/Google/Chrome/chromedriver'
    dict = {}
    df = None
    food_name = []
    food_nut = []

    def scrap_name(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        all_div = BeautifulSoup(driver.page_source, 'html.parser')
        ls = all_div.find_all("div", {"class": "subject"})
        for i in ls:
            print(i.find("a").text)
            self.food_name.append(i.find("a").text)
        print(self.food_name)
        driver.close()

    def scrap_nut(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        all_div = BeautifulSoup(driver.page_source, 'html.parser')
        ls = all_div.find_all("p", {"class": "desc __ellipsis"})
        print(ls)
        for i in ls:
            print(i.text)


        '''
        for i in ls:
            print()
            self.food_nut.append(i.find("p").text)
        driver.close()

    def insert_dict(self):
        for i, j in zip(self.food_name, self.food_nut):
            self.dict[i] = j
            print(f'{i}:{j}')

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/food_nutrition.csv'
        self.df.to_csv(path, sep=',', na_rep='Nan')
'''
    @staticmethod
    def main():
        nut = Nutrition()
        while 1:
            menu = input('0-Exit\n1-print\n2-insert dict\n3-dataframe\n4-csv')
            if menu == '0':
                break
            elif menu == '1':
                nut.scrap_name()
                nut.scrap_nut()
            elif menu == '2':
                nut.insert_dict()
            elif menu == '3':
                nut.dict_to_dataframe()
            elif menu == '4':
                nut.df_to_csv()
            else:
                continue

Nutrition.main()