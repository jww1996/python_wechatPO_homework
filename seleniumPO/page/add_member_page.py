from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from seleniumPO.page.base_page import BasePage

# 添加联系人页面
class AddMemberPage(BasePage):

    def add_member(self, username, account, phonenumber):
        """
        添加联系人详细信息
        :return:
        """
        # 输入姓名
        self.find(By.ID, 'username').send_keys(username)
        # 输入帐号
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        # 输入手机号
        self.find(By.ID, 'memberAdd_phone').send_keys(phonenumber)
        # 点击保存 当页面上有多个相同属性的元素时，通过find_element找到的是第一个元素
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return True

    def get_member(self):
        """
        获取所有的联系人姓名
        :return:
        """
        # 添加显示等待(expected_conditions.element_to_be_clickable判断元素是否可以点击)
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.member_colRight_memberTable_th_Checkbox')))
        locator = (By.CSS_SELECTOR, '.member_colRight_memberTable_th_Checkbox')
        self.wait_for_click(10, locator)
        # find_elements 查找页面上的相同属性的所有元素，[element1,element2......]
        elss_list = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        names = []
        for ele in elss_list:
            names.append(ele.get_attribute("title"))
        return names