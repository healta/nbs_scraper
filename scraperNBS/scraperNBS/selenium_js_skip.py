from selenium import webdriver
from selenium.webdriver.common.by import By

offset = 0

links_added = 0

#reads the file of previously recorded links, 
#to check later if there are any new ones
with open ("articles.txt", "r") as f:
    links = f.readlines()

while True:
    counter = 0

    url = ('https://nbs.sk/en/press/news-overview/?table_post-list_params=%7B%22offset%22%3A{}%2C%22filter%22%3A%7B%22lang%22%3A%22en%22%7D%7D'.format(offset))

    driver = webdriver.Chrome()

    driver.get(url)
    
    elements = driver.find_elements(By.CSS_SELECTOR, "a.archive-results__item")

    for i in elements:
    
        #adding a new line at the end of the link
        #makes it so I can compare with the links already in the file
        #and I can add the new line here, instead of after the write.
    
        val = i.get_attribute("href") + "\n"
        
        if val not in links and "/news/" in val:
            with open ("articles.txt", "a") as f:
                f.write(val)
                links_added+=1
        else:
            counter+=1

    #checks if there are any links on the page
    #if there are none, there are no more articles to read
    #and the loop quits
    if len(elements)==0 or counter == 5:
        break

    driver.quit()

    #I noticed the URLs the site uses have an offset number
    #and I used it by incrementing it, instead of having
    #Selenium click on the next page, figured it's easy
    #and saves time, it's probably faster too
    offset+=5

if links_added == 0:
    print("No new links have been added.")
else:
    print(links_added, "new links have been aded.")