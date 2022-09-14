from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

class mars_scrape():
    def __init__(self):
        print('init')
    
    def scrape_news(self):
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)
        url = "https://redplanetscience.com/"
        browser.visit(url)
        html = browser.html
        soup = bs(html, "html.parser")
        first_title = soup.find('div', class_='content_title').text
        first_paragraph = soup.find('div', class_='article_teaser_body').text
        browser.quit()
        return first_title, first_paragraph


    def scrape_image(self):
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)
        url = "https://spaceimages-mars.com/"
        browser.visit(url)
        html = browser.html
        soup = bs(html, "html.parser")
        img = soup.find('img', class_='headerimage fade-in')['src']
        browser.quit()
        img_url = url + img
        return img_url
    
    def scrape_table(self):
        tables = pd.read_html('https://galaxyfacts-mars.com')
        desired_table = tables[0]
        html = desired_table.to_html()
        return html
    
    def scrape_hemispheres(self, hemisphere):
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)
        base_url = "https://marshemispheres.com/"
        url = base_url+hemisphere
        browser.visit(url)
        html = browser.html
        soup = bs(html, "html.parser")
        images = soup.find_all('a')
        img = ''
        for info in images:
            if info.text == 'Original':
                img = info['href']
        text = soup.find('div', class_='cover')
        desired_text = text.h2.text
        title_text = desired_text.split()
        title = title_text[0]
        img_url = base_url + img
        browser.quit()
        return title, img_url
    
    def all_hemispheres(self):
        url_list = ['cerberus.html', 'schiaparelli.html', 'syrtis.html','valles.html']
        all_images = {}
        for url in url_list:
            title, img_url = self.scrape_hemispheres(url)
            all_images[title] = img_url
        return all_images
    
    def scrape(self):
        all_info = {}
        title, paragraph = self.scrape_news()
        img_url = self.scrape_image()
        table = self.scrape_table()
        hemispheres = self.all_hemispheres()
        all_info['title'] = title
        all_info['paragraph'] = paragraph
        all_info['Mars Image'] = img_url
        all_info['table'] = table
        all_info['hemispheres'] = hemispheres
        return all_info