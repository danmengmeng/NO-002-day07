import os
import sys

import allure

sys.path.append(os.getcwd())



class Test01:
    @allure.severity("blocker")
    @allure.step("点击新增")
    def test001(self):
        allure.attach("新增输入一个地址","")
        allure.attach("新增输入一个用户名", "")
        allure.attach("新增输入一个电话号码", "")
        allure.attach("新增输入一个紧急联系人", "")
        print("test001被执行")

    @allure.step("002被测试")
    @allure.severity("trivial")
    def test002(self):
        print("test002被执行")

    @allure.step("003被测试")
    @allure.severity("critical")
    def test003(self):
        print("断言失败，截图并写入报告")
        with open("./image/file.png","rb")as f:
            allure.attach("失败原因：",f.read(),allure.atture_type.PNG)
            assert 0

    def test004(self):
        print("test004被执行")