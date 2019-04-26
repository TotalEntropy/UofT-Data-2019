import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser

executable_path = {'executable_path': '../resources/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# # News

url_news = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

browser.visit(url_news)

html_news = browser.html
soup_news = bs(html_news, 'html.parser')

print(soup_news.prettify())

news_title = soup_news.find_all('div', class_='content_title')[0].a.contents[0]
print(news_title)

news_p = soup_news.find_all('div', class_='rollover_description_inner')[0].contents[0]
print(news_p)


# # Image

url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

browser.visit(url_img)


html_img = browser.html
soup_img = bs(html_img, 'html.parser')

print(soup_img.prettify())



featured_image_url = (soup_img.find('article', class_='carousel_item')['style'].replace("background-image: url('",'').replace("');",''))
print(featured_image_url)

url_img_final = 'https://www.jpl.nasa.gov' + featured_image_url


# # Twitter

url_twitter = 'https://twitter.com/marswxreport?lang=en'

browser.visit(url_twitter)



html_twitter = browser.html
soup_twitter = bs(html_twitter, 'html.parser')

print(soup_twitter.prettify())


latest_tweets = soup_twitter.find_all('div', class_='js-tweet-text-container')

for tweet in latest_tweets: 
    weather_tweet = tweet.find('p').text
    if 'Sol' and 'low' and 'high' and 'pressure' in weather_tweet:
        tweet.find('p').a.decompose()
        weather_tweet = tweet.find('p').text
        print(weather_tweet)
        break
    else: 
        pass


# # Facts

url_fact = 'https://space-facts.com/mars/'

mars_facts = pd.read_html(url_fact)

facts_df = mars_facts[0]
facts_df.head()



facts_df.columns = ['Description', 'Value']
facts_df.set_index('Description', inplace=True)
facts_df
facts_df.to_html()


# # Hemispheres


url_hem = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(url_hem)

html_hem = browser.html
soup_hem = bs(html_hem, 'html.parser')

print(soup_hem.prettify())

hemisphere_image_urls = []

hem = soup_hem.find_all('div', class_='item')

for item in hem:
    title = item.find('h3').text
    partial_url = item.find('a', class_='itemLink product-item')['href']
    url = 'https://astrogeology.usgs.gov' + partial_url
    browser.visit(url)
    soup = bs(browser.html, 'html.parser')
    img_url = soup.find('div', class_='downloads').li.a['href']
    hemisphere_image_urls.append({'title':title, 'img_url':img_url})

hemisphere_image_urls