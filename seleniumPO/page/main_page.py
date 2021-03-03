
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 企业微信主页面
from seleniumPO.page.add_member_page import AddMemberPage
from seleniumPO.page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member_page(self):
        """
        添加成员
        :return:
        """
        # click add member
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        # return AddMemberPage()
        return AddMemberPage(self.driver)