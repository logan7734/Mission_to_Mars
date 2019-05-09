# Import Dependecies 
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 
import time


mars_info = {}

def init_browser():
    driver_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **driver_path, headless=False)


# NASA MARS NEWS
def scrape_mars_news():

    browser = init_browser()

    # Visit Nasa news url through splinter module
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)

    # HTML Object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the latest element that contains news title and news_paragraph
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # Dictionary entry from MARS NEWS
    mars_info['news_title'] = news_title
    mars_info['news_paragraph'] = news_p

    # FEATURED IMAGE
def scrape_mars_image():
    browser = init_browser()
    # Visit Mars Space Images through splinter module
    image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


    # Visit Mars Space Images through splinter module
    browser.visit(image_url_featured)
    time.sleep(1)
    # HTML Object
    html = browser.html  

    # HTML Object 
    html_image = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_image, 'html.parser')

    # Retrieve background-image url from style tag 
    featured_image_url  = soup.find('article')['style']
    image = featured_image_url[23:len(featured_image_url)-3]

    browser = init_browser()
    main_url = 'https://www.jpl.nasa.gov'

    # Concatenate website url with scrapped route
    featured_image_url = main_url + image

    # Display full link to featured image
    featured_image_url 

    # Dictionary entry from FEATURED IMAGE
    mars_info['featured_image_url'] = featured_image_url 
      
    # Mars Weather 
def scrape_mars_weather():
    browser = init_browser()
    # Visit Mars Weather Twitter through splinter module
    weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather)
    time.sleep(1)
    # HTML Object 
    tweets = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(tweets, 'html.parser')

    # Find all elements that contain tweets
    mars_weather = soup.find("p", class_="TweetTextSize").text

    # Dictionary entry from WEATHER TWEET
    mars_info['mars_weather'] = mars_weather
    

    # Visit Mars facts url 
def scrape_mars_facts():
    browser = init_browser()
    facts_url = 'http://space-facts.com/mars/'
    browser.visit(facts_url)
    time.sleep(1)
    # Use Panda's `read_html` to parse the url
    mars_facts = pd.read_html(facts_url)

    # Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
    mars_df = mars_facts[0]

    # Assign the columns `['Description', 'Value']`
    mars_df.columns = ['Description','Value']

    # Save html code to folder Assets
    mars_df = mars_df.to_html()

    # Dictionary entry from MARS FACTS
    mars_info['mars_facts'] = mars_df

    # MARS HEMISPHERES
def scrape_mars_hemispheres():
    browser = init_browser()
    # Visit hemispheres website through splinter module 
    astrology_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astrology_url)
    time.sleep(1)
    # HTML Object
    # HTML Object
    html_hemispheres = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_hemispheres, 'html.parser')

    # Retreive all items that contain mars hemispheres information
    items = soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls 
    hemisphere_image_urls = []

    # Store the main_ul 
    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    # Loop through the items previously stored
    for i in items: 
        # Store title
        title = i.find('h3').text
        
        # Store link that leads to full image website
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
        
        # Visit the link that contains the full image website 
        browser.visit(hemispheres_main_url + partial_img_url)
        
        # HTML Object of individual hemisphere information website 
        partial_img_html = browser.html
        
        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = BeautifulSoup( partial_img_html, 'html.parser')
        
        # Retrieve full image source 
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        
        title = "a"
        img_url = "b"
        # Append the retreived information into a list of dictionaries 
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

        
    time.sleep(1)

    mars_info["hiu"] = hemisphere_image_urls

    # Return mars_data dictionary 
    browser.quit()
    return mars_info
