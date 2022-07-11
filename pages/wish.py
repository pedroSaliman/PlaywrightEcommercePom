class Wish:
    def __init__(self, page):
        self.page = page
        self.wishremoveproduct =  page.locator("//a[@class='btn btn-danger']//i[@class='fa fa-times']")




    def removebtn(self):
        self.wishremoveproduct.click()
        