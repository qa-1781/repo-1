
class LaunchPage():
    def __init__(self,driver):
        self.driver = driver

        self.driver.find_element(By.ID,"onetrust-accept-btn-handler").click()

         self.driver.find_element(By.XPATH,"//a[@id='flights']").click()

         self.driver.find_element(By.XPATH,"//div[@class='css-1ibfpg6']//button[1]").click()

         self.driver.find_element(By.XPATH, "//span[@class='css-rh2lq6']").click()

         dep_am = self.driver.find_element(By.XPATH, "//input[@placeholder='Airport or city']")
         dep_am.send_keys("Amsterdam")

         dep_am = self.driver.find_element(By.XPATH, "//label[contains(@for,'__bui')]")

         dep_am.click()

         self.driver.find_element(By.XPATH,'//div//button[3][@type="button"]').click()

         going_to = self.driver.find_element(By.XPATH,"//div//input[@placeholder='Airport or city']")

         going_to.send_keys("New")

         search_results = self.driver.find_elements(By.XPATH,'//div//ul[@class="css-1eonra"]/li')   # 1 of 13
         print(len(search_results))
         for results in search_results:         #for loop
              print(results.text)
              if "New York" in results.text:
                   results.click()
                   time.sleep(4)
                   break

         origin = self.driver.find_element(By.XPATH,"//button[@placeholder='Depart – Return']")
         origin.click()
         time.sleep(4)
         self.driver.find_element(By.XPATH,"//span[@aria-label='13 April 2023']").click()
         time.sleep(2)
         self.driver.find_element(By.XPATH,"//span[@aria-label='19 May 2023']//span[contains(text(),'19')]").click()
         time.sleep(2)
         self.driver.find_element(By.XPATH, '//div//button[contains(@class,"Actionable-module__root___lQCcK Button-module__root___puEjU Button-module__root--variant-primary___rQ8Eq Button-module__root--size-medium___Fcsd5 Button-module__root--wide-false___ngEa+ Button-module__root--variant-primary-action___yZcy0 css-5rnpiv undefined")]').click()
         time.sleep(10)
