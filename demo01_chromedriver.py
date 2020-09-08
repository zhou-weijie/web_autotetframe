from frameworks.basePage import Browser
from time import sleep

driver = Browser('firefox')
driver.maxWindow()
driver.openUrl('https://www.baidu.com')
sleep(3)

# 通过xpath找到输入框，并输入搜索内容,然后点击搜索按钮
driver.findElementsByXpath('//*[@id="kw"]').send_keys('新梦想软件教育')
driver.findElementsByXpath('//*[@id="su"]').click()
sleep(10)
driver.backBrowser()
sleep(10)

# # 通过css找到输入框，并输入搜索内容
# driver.findElementsByCss('#kw').send_keys('新梦想软件教育')
# driver.findElementsByCss('#su').click()

# 通过class_name找到输入框，并输入搜索内容
# driver.findElementsByClassname('s_ipt').send_keys('新梦想软件教育')
# driver.findElementsByClassname('bg s_ipt_wr quickdelete-wrap').click()  # 报错，无法通过classname找到“百度一下”的按钮

# 通过tag_name找到输入框并输入内容
# driver.findElementsByTagname().send_keys('新梦想软件教育')

# # 通过id找到输入框并输入内容
# driver.findElementsById('kw').send_keys('新梦想软件教育')
# driver.findElementsById('su').click()

# # 通过name找到输入框并输入内容
# driver.findElementsByName('wd').send_keys('新梦想软件教育')

# 打印右上角链接的文本内容
elements = driver.findElementsById('u1')
text_list = elements.text.split('\n')
print(text_list)

# 通过linktext找到超链接，并点击
driver.findElementsByLink('抗击肺炎').click()
sleep(3)
windows = driver.getAllWindows()
driver.switchToOtherWindows(windows[0])
sleep(3)

for text in text_list[1:7]:
    driver.findElementsByLink(text).click()
    sleep(3)
    driver.backBrowser()
    sleep(3)

driver.closeBrowser()
driver.closeBrowser()
