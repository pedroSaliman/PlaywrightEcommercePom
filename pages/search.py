class Search:
     def __init__(self, page):
        self.page = page
        self.phons=page.locator("//a[normalize-space()='Phones & PDAs']")
        self.filterphone=page.locator("//i[@class='fa fa-th-list']")
        self.wish=page.locator("//div[@id='content']//div[1]//div[1]//div[2]//div[2]//button[2]")
        self.myacountlistclick=page.locator("//span[normalize-space()='My Account']")
        self.myaccount=page.locator("//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='My Account']")



      


     def searchphone(self):
        self.phons.click()
        self.filterphone.click()
        self.wish.click()
        self.myacountlistclick.click()
        self.myaccount.click()
        





