import driver as driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class automate:

    def launchwebsite1(self):
        driver.get("https://nbl.one/feed")
        driver.maximize_window()

    def questsearch(self):
        var = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div/div/div/section/div[2]/div/main/section[2]/div/div/section[1]/article/section/div/h1"))).text
        if var==" ":
            print("QUEST IS NOT PRESENT")
        else:
            print("QUEST IS PRESENT: ", var)


    def launchwebsite2(self):
        driver.get("https://nbl.one/gigs/listings/careers1/demo-talk-test-engineer-1")
        driver.maximize_window()

    def goto_login(self):
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='navbar-sign-in']"))).click()
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='login-modal-continue-with-email']"))).click()
        time.sleep(2)

        # validation of correct page opening
        act_title = driver.title
        exp_title = "Nbyula - Demo Talk - Test Engineer by Careers@Nbyula"
        try:
            var = (act_title == exp_title)
            print("WEBSITE SUCCESSFULLY LAUNCHED")
        except:
            print("website opening un-successfull")
        print("-----------------------------------------------------")
        time.sleep(2)

    def login(self):
        username = "1ms19ec097@gmail.com" #enter your username
        password = "12345678" #enter your password where the cource is not booked yet
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[1]/div/input"))).send_keys(username)
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Continue']"))).click()
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/input"))).send_keys(password)
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Continue']"))).click()
        time.sleep(2)

        # validation of Logged in message
        checkpoint = driver.find_element(By.ID, "navbar-profile-dropdown")
        try:
            var = (checkpoint.is_displayed() == False)
            print("LOGIN SUCCESSFULL")
        except:
            print("Login un-successfull")
        time.sleep(2)

    def buy(self):
        # wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div/section/section[1]/section[2]/section[2]/div/section/section/section[2]/button/span"))).click()
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='skylift-proceed-to-purchase']"))).click()
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/section/section[1]/section[3]/section[3]/button"))).click()
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/section/div[2]/div/input"))).send_keys("7029169357")
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/section/div[3]/button"))).click()
        time.sleep(10)

        # validation for successfully book of seat
        act_title = driver.title
        exp_title = "Skylift Conversation | Nbyula"
        try:
            var = (act_title == exp_title)
            print("BOOKING SUCCESSFULL")
        except:
            print("BOOKING un-successfull")
        print("-----------------------------------------------------")
        time.sleep(2)

    def launchwebsite3(self):
        driver.get("https://nbl.one/listings")
        driver.maximize_window()

    def find_titleAndprice(self):
        time.sleep(1)
        post1 = wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='IELTS Assessments | Writing Task 1']"))).text
        print("TITLE:", post1)
        post1price = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/section/section/div/p/span[1]/span"))).text
        print("PRICE:", post1price)
        time.sleep(1)
        post2 = wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='May 18th Classroom']"))).text
        print("TITLE:", post2)
        post2price = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'₹7820.4')]"))).text
        print("PRICE:", post2price)
        time.sleep(1)
        post3 = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'I will share tips on where to search & how to nego')]"))).text
        print("TITLE:", post3)
        post3price = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='carousel__container']/div/div/div/div[3]/div/div/div/div/section/section/div/p/span[1]/span"))).text
        print("PRICE:", post3price)
        time.sleep(1)

    def close(self):
        driver.quit()


if __name__ == '__main__':
    # To bypass the message-"your connection is not private" on non-secure page OR (click Advanced) if any there
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    # open chrome
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 2)
    obj = automate()
    print("#################### FIRST TASK STARTED ####################")
    # FIRST TASK - TO FIND QUEST/ANY POST IS THERE OR NOT - validate if there is at least 1 quest.
    obj.launchwebsite1()
    obj.questsearch()
    time.sleep(5)
    print("#################### FIRST TASK COMPLETED ####################")
    print("#################### SECOND TASK STARTED ####################")
    # SECOND TASK - try booking the skylift
    obj.launchwebsite2()
    obj.goto_login()
    obj.login()
    obj.buy()
    print("#################### SECOND TASK COMPLETED ####################")
    print("#################### THIRED TASK STARTED ####################")
    # THIRED TASK - scrape all the cards for title, price and link associated to each card
    obj.launchwebsite3()
    obj.find_titleAndprice()
    obj.close()
    print("#################### THIRED TASK COMPLETED ####################")