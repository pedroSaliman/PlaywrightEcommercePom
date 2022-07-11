from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import pytest
from pages.home import Home
from pages.search import Search
from pages.wish import Wish
from pages import info


@pytest.fixture(autouse=True)
def setup(page):
    home = Home(page)
    home.nav()
    home.Login(info.EMAIL,info.PASSWORD)

    
    # page.locator("//span[normalize-space()='My Account']").click()
    # page.locator("//a[normalize-space()='Login']").click()
    
    # page.locator("#input-email").fill("naveenanimation20@gmail.com")
    # page.locator("#input-password").fill("2521997")
    # page.locator("input[value='Login']").click()
    expect(home.vaild).to_have_text("My Account")
    yield
    page.close()

    












# def test_0(page):
#     home = Home(page)
#     home.changepass(info.PASSWORD,info.PASSWORD)


    ################# BEFORE USE POM 
    # page.locator("//a[normalize-space()='Change your password']").click()
    # page.locator("#input-password").fill("2521997")
    # page.locator("#input-confirm").fill("2521997")
    # page.locator("input[value='Continue']").click()

    # page.locator("//a[normalize-space()='Phones & PDAs']").click()
    # page.locator("//i[@class='fa fa-th-list']").click()
    # page.locator("//div[@id='content']//div[1]//div[1]//div[2]//div[2]//button[2]").click()
    # page.locator("//span[normalize-space()='My Account']").click()
    # page.locator("//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='My Account']").click()
    # page.locator("//a[normalize-space()='Edit Account']").click()
    # page.locator("#input-firstname").fill("mohamed")
    # page.locator("#input-lastname").fill("mahmoud")
    # page.locator("input[value='Continue']").click()
    # expect(page.locator("//div[@class='alert alert-success alert-dismissible']")).to_have_text(" Success: Your account has been successfully updated.")
    # page.locator("//a[@class='list-group-item'][normalize-space()='Wish List']").click()
    # page.locator("//a[@class='btn btn-danger']//i[@class='fa fa-times']").click()
    # page.wait_for_timeout(3000)
    ##############################################################

    
# def test_2(page):
#     home=Home(page)
#     home.edit(info.FNAME,info.LNAME)



def test_3(page):
    search= Search(page)
    search.searchphone()
    home = Home(page)
    home.wish()
    wish=Wish(page)
    wish.removebtn()

  













