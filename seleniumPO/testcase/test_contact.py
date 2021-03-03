from seleniumPO.page.main_page import MainPage


class TestContact:
    def setup(self):
        self.mainpage = MainPage()

    def test_addmember(self):
        username = "测试08"
        account = "888888"
        phonenumber = "13888888888"
        page = self.mainpage.goto_add_member_page()
        page.add_member(username, account, phonenumber)
        names = page.get_member()
        assert username in names