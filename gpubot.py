#!/usr/bin/env python
# coding: utf-8

# In[19]:


from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time


# In[20]:


wd = wd.Chrome()
wd.implicitly_wait(5)

test_link = 'https://www.bestbuy.com/site/samsung-58-class-7-series-led-4k-uhd-smart-tizen-tv/6401726.p?skuId=6401726'
gpu_link = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442'


# In[21]:


wd.get(test_link)


# In[22]:


add_to_cart_button = wd.find_element_by_xpath('//*[@class="fulfillment-add-to-cart-button"]/div/div/button')
add_to_cart_button_state = add_to_cart_button.get_attribute("data-button-state")


# In[23]:


while True:
    if add_to_cart_button_state == 'SOLD_OUT':
        print(add_to_cart_button_state)
        wd.refresh()
        add_to_cart_button = wd.find_element_by_xpath('//*[@class="fulfillment-add-to-cart-button"]/div/div/button')
        add_to_cart_button_state = add_to_cart_button.get_attribute("data-button-state")
        time.sleep(10)
    else:
        print('Clicked')
        add_to_cart_button.click()
        break
        


# In[24]:


wd.execute_script('window.open('');')
wd.switch_to.window(wd.window_handles[1])
wd.get('https://youtu.be/uw_qPfgTxuI')
play_button = wd.find_element_by_xpath('//*[@id="movie_player"]/div[5]/button')
play_button.click()


# In[ ]:





# In[ ]:





# In[ ]:




