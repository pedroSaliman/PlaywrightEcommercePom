class Home:
     def __init__(self, page):
        self.page = page
        self.change =  page.locator("//a[normalize-space()='Change your password']")
        self.password1=page.locator("#input-password")
        self.password2=page.locator("#input-confirm")
        self.submit=    page.locator("input[value='Continue']")
        self.editpage=page.locator("//a[normalize-space()='Edit Account']")
        self.fname=page.locator("#input-firstname")
        self.lname=page.locator("#input-lastname")
        self.editclick=page.locator("input[value='Continue']")
        self.wishclick=page.locator("//a[@class='list-group-item'][normalize-space()='Wish List']")

        #          page.locator("//span[normalize-space()='My Account']").click()
        # page.locator("//a[normalize-space()='Login']").click()
        
        # page.locator("#input-email").fill("naveenanimation20@gmail.com")
        # page.locator("#input-password").fill("2521997")
        # page.locator("input[value='Login']").click()


        self.myaccount=page.locator("//span[normalize-space()='My Account']")
        self.login=page.locator("//a[normalize-space()='Login']")
        self.email=page.locator("#input-email")
        self.thepassword=page.locator("#input-password")
        self.loginbtn=page.locator("input[value='Login']")
        self.vaild=page.locator("h2:nth-child(1)")






        


     def Login(self,theemail,password):
        self.myaccount.click()
        self.login.click()
        self.email.fill(theemail)
        self.thepassword.fill(password)
        self.loginbtn.click()





     def nav(self):
        self.page.goto("https://naveenautomationlabs.com/opencart/")

    

     def changepass(self, pass1,pass2):
        self.change.click()
        self.password1.fill(pass1)
        self.password2.fill(pass2)
        self.submit.click()




     def edit(self,thefname,thelname):
        self.editpage.click()
        self.fname.fill(thefname)
        self.lname.fill(thelname)
        self.editclick.click()


     def wish(self):
        self.wishclick.click()





