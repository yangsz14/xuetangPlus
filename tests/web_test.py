from django.contrib.auth.models import User
from django.test import LiveServerTestCase
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
selenium.__file__
import os
import json
import time
from django.test import *

class LoginTest(LiveServerTestCase):
    fixtures = ['authUsers.json','users.json','courses.json','posts.json','followUser.json','hasCourse.json','likePost.json']
    browser = None

    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()
        cls.browser = webdriver.PhantomJS()
        cls.client = Client()
        #cls.username = os.environ.get('username', '')
        #cls.password = os.environ.get('password', '')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(LoginTest, cls).tearDownClass()

    def test_login_without_input(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))

        self.browser.implicitly_wait(5)

        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("")

        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
        # self.browser.save_screenshot('4.png')
        self.assertIn('Error', self.browser.find_element_by_id('content').text)

    def test_login_with_wrong_input(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))

        self.browser.implicitly_wait(5)

        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013460")

        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("wrongpwd")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
       # self.browser.save_screenshot('3.png')
        self.assertIn('Error', self.browser.find_element_by_id('content').text)

    def test_login_with_right_input(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
        # self.browser.save_screenshot('fuck0.png')
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")
        # self.browser.save_screenshot('fuck1.png')

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)
        # self.browser.save_screenshot('fuck2.png')

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
        # self.browser.save_screenshot('fuck3.png')
        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

class BBSListTest(LiveServerTestCase):
    fixtures = ['authUsers.json','users.json','courses.json','posts.json','followUser.json','hasCourse.json','likePost.json']
    browser = None

    @classmethod
    def setUpClass(cls):
        super(BBSListTest, cls).setUpClass()
        cls.browser = webdriver.PhantomJS()
        cls.client = Client()
        #cls.username = os.environ.get('username', '')
        #cls.password = os.environ.get('password', '')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(BBSListTest, cls).tearDownClass()

    def test_bbslist_without_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, ''))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)

        print("self.browser",self.browser)
       # self.browser.save_screenshot('3.png')
        self.assertIn('用户登录', self.browser.find_element_by_id('content').text)

    def test_bbslist_with_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

class CoursePostListViewTest(LiveServerTestCase):
    fixtures = ['authUsers.json','users.json','courses.json','posts.json','followUser.json','hasCourse.json','likePost.json']
    browser = None

    @classmethod
    def setUpClass(cls):
        super(CoursePostListViewTest, cls).setUpClass()
        cls.browser = webdriver.PhantomJS()
        cls.client = Client()
        #cls.username = os.environ.get('username', '')
        #cls.password = os.environ.get('password', '')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(CoursePostListViewTest, cls).tearDownClass()

    def test_cplv_without_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/course/'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)

        print("self.browser",self.browser)
        self.browser.save_screenshot('3.png')
        self.assertIn('用户登录', self.browser.find_element_by_id('content').text)

    def test_cplv_with_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")
    
        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)
    
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/course/3'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('课程讨论区', self.browser.find_element_by_id('content').text)

class CoursePostDetailTest(LiveServerTestCase):
    fixtures = ['authUsers.json','users.json','courses.json','posts.json','followUser.json','hasCourse.json','likePost.json']
    browser = None

    @classmethod
    def setUpClass(cls):
        super(CoursePostDetailTest, cls).setUpClass()
        cls.browser = webdriver.PhantomJS()
        cls.client = Client()
        #cls.username = os.environ.get('username', '')
        #cls.password = os.environ.get('password', '')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(CoursePostDetailTest, cls).tearDownClass()
    
    def test_cpd_without_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/course/3/post/3'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        print("self.browser",self.browser)
       # self.browser.save_screenshot('3.png')
        self.assertIn('用户登录', self.browser.find_element_by_id('content').text)

    def test_cpd_with_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)
        self.browser.save_screenshot('3.png')
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/course/3'))
        except Exception as e:
            print("give Error:",str(e))
        self.browser.save_screenshot('4.png')
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('课程讨论区', self.browser.find_element_by_id('content').text)
    
    def test_cpd_like_with_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")
    
        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)
    
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/course/3/post/1'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        submit_button = self.browser.find_element_by_id('1')
        submit_button.click()
    
        self.assertIn('点赞', self.browser.find_element_by_id('content').text)
    
        submit_button.click()
    
        self.assertIn('取消', self.browser.find_element_by_id('content').text)
    
    def test_cpd_post_with_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")
    
        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)
    
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/course/1/post/1'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('课程讨论区', self.browser.find_element_by_id('content').text)
    
        self.browser.implicitly_wait(2)
    
        content_box = self.browser.find_element_by_id('id_PContent')
        content_box.send_keys("yaowan............................................................................")
    
        time.sleep(2)
        submit_button = self.browser.find_element_by_id('happyBtn0')
        submit_button.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

class UserSelfInfoTest(LiveServerTestCase):
    fixtures = ['authUsers.json','users.json','courses.json','posts.json','followUser.json','hasCourse.json','likePost.json']
    browser = None

    @classmethod
    def setUpClass(cls):
        super(UserSelfInfoTest, cls).setUpClass()
        cls.browser = webdriver.PhantomJS()
        cls.client = Client()
        #cls.username = os.environ.get('username', '')
        #cls.password = os.environ.get('password', '')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(UserSelfInfoTest, cls).tearDownClass()

    def test_userselfinfo_without_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/me/2014013458'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)

        print("self.browser",self.browser)
       # self.browser.save_screenshot('3.png')
        self.assertIn('用户登录', self.browser.find_element_by_id('content').text)

    def test_userselfinfo_with_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

        try:
            self.browser.get('%s%s' % (self.live_server_url, '/me/2014013458'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('信息', self.browser.find_element_by_id('content').text)
    
    def test_userselfinfo_nick_with_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

        try:
            self.browser.get('%s%s' % (self.live_server_url, '/me/2014013458'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('信息', self.browser.find_element_by_id('content').text)

        nick_box = self.browser.find_element_by_id('changeNick')
        nick_box.send_keys("nicknameChanged23333")

        time.sleep(2)
        submit_button = self.browser.find_element_by_id('saveNick')
        submit_button.click()
        time.sleep(2)

        self.assertIn('2333', self.browser.find_element_by_id('content').text)

    def test_userselfinfo_like_with_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

        try:
            self.browser.get('%s%s' % (self.live_server_url, '/me/2014013458'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('信息', self.browser.find_element_by_id('content').text)

        click_url = self.browser.find_element_by_id('helikes')
        click_url.click()
        self.browser.implicitly_wait(2)
        self.assertIn('点赞', self.browser.find_element_by_id('content').text)

    def test_userselfinfo_answer_with_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

        try:
            self.browser.get('%s%s' % (self.live_server_url, '/me/2014013458'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('信息', self.browser.find_element_by_id('content').text)

        click_url = self.browser.find_element_by_id('heanswers')
        click_url.click()
        self.browser.implicitly_wait(2)
        self.assertIn('回答', self.browser.find_element_by_id('content').text)

    def test_userselfinfo_ask_with_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

        try:
            self.browser.get('%s%s' % (self.live_server_url, '/me/2014013458'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('信息', self.browser.find_element_by_id('content').text)

        click_url = self.browser.find_element_by_id('heasks')
        click_url.click()
        self.browser.implicitly_wait(2)
        self.assertIn('提问', self.browser.find_element_by_id('content').text)

class PostCoursePostTest(LiveServerTestCase):
    fixtures = ['authUsers.json','users.json','courses.json','posts.json','followUser.json','hasCourse.json','likePost.json']
    browser = None

    @classmethod
    def setUpClass(cls):
        super(PostCoursePostTest, cls).setUpClass()
        cls.browser = webdriver.PhantomJS()
        cls.client = Client()
        #cls.username = os.environ.get('username', '')
        #cls.password = os.environ.get('password', '')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(PostCoursePostTest, cls).tearDownClass()

    def test_postcoursepost_without_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/me'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)

        print("self.browser",self.browser)
       # self.browser.save_screenshot('3.png')
        self.assertIn('用户登录', self.browser.find_element_by_id('content').text)

    def test_postcoursepost_with_login_right_input(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

        try:
            self.browser.get('%s%s' % (self.live_server_url, '/post/3'))
        except Exception as e:
            print("give Error:",str(e))
        
        self.browser.implicitly_wait(2)

        title_box = self.browser.find_element_by_id('id_title')
        title_box.send_keys("Post of 2014013460")
    
        content_box = self.browser.find_element_by_id('id_content')
        content_box.send_keys("yaowan............................................................................")
        
        time.sleep(2)
        submit_button = self.browser.find_element_by_id('happyBtn0')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('2014013460', self.browser.find_element_by_id('content').text)

    def test_postcoursepost_with_login_without_title(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

        try:
            self.browser.get('%s%s' % (self.live_server_url, '/post/3'))
        except Exception as e:
            print("give Error:",str(e))
        
        self.browser.implicitly_wait(2)

        title_box = self.browser.find_element_by_id('id_title')
        title_box.send_keys("")
    
        content_box = self.browser.find_element_by_id('id_content')
        content_box.send_keys("yaowan............................................................................")
        
        time.sleep(2)
        submit_button = self.browser.find_element_by_id('happyBtn0')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('课程讨论区', self.browser.find_element_by_id('content').text)

    def test_postcoursepost_with_login_without_content(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

        try:
            self.browser.get('%s%s' % (self.live_server_url, '/post/3'))
        except Exception as e:
            print("give Error:",str(e))
        
        self.browser.implicitly_wait(2)

        title_box = self.browser.find_element_by_id('id_title')
        title_box.send_keys("Post of 2014013460")
    
        content_box = self.browser.find_element_by_id('id_content')
        content_box.send_keys("")
        
        time.sleep(2)
        submit_button = self.browser.find_element_by_id('happyBtn0')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('课程讨论区', self.browser.find_element_by_id('content').text)

    def test_postcoursepost_with_login_with_type2(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

        try:
            self.browser.get('%s%s' % (self.live_server_url, '/post/3'))
        except Exception as e:
            print("give Error:",str(e))
        
        self.browser.implicitly_wait(2)

        title_box = self.browser.find_element_by_id('id_title')
        title_box.send_keys("Post of 2014013463")
    
        content_box = self.browser.find_element_by_id('id_content')
        content_box.send_keys("yaowan............................................................................")
        
        time.sleep(2)
        submit_button = self.browser.find_element_by_id('happyBtn1')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('yaowan', self.browser.find_element_by_id('content').text)

class DrawTest(LiveServerTestCase):
    fixtures = ['authUsers.json','users.json','courses.json','posts.json','followUser.json','hasCourse.json','likePost.json']
    browser = None

    @classmethod
    def setUpClass(cls):
        super(CoursePostListViewTest, cls).setUpClass()
        cls.browser = webdriver.PhantomJS()
        cls.client = Client()
        #cls.username = os.environ.get('username', '')
        #cls.password = os.environ.get('password', '')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(CoursePostListViewTest, cls).tearDownClass()

    def test_draw_1(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")
    
        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)
    
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/course/3'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('课程讨论区', self.browser.find_element_by_id('content').text)

        click_draw = self.browser.find_element_by_id('draw1')
        click_draw.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(4)
        print("self.browser",self.browser)
    
        self.assertIn('笔记', self.browser.find_element_by_id('content').text)
    
    def test_draw_10(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")
    
        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)
    
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/course/3'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('课程讨论区', self.browser.find_element_by_id('content').text)

        click_draw = self.browser.find_element_by_id('draw10')
        click_draw.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(4)
        print("self.browser",self.browser)
    
        self.assertIn('笔记', self.browser.find_element_by_id('content').text)
    
    def test_draw_good(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")
    
        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)
    
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/course/3'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('课程讨论区', self.browser.find_element_by_id('content').text)


        click_draw = self.browser.find_element_by_id('drawgoood')
        click_draw.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(4)
        print("self.browser",self.browser)
    
        self.assertIn('笔记', self.browser.find_element_by_id('content').text)
    

class XuetangPostDetailTest(LiveServerTestCase):
    fixtures = ['authUsers.json','users.json','courses.json','posts.json','followUser.json','hasCourse.json','likePost.json']
    browser = None

    @classmethod
    def setUpClass(cls):
        super(CoursePostDetailTest, cls).setUpClass()
        cls.browser = webdriver.PhantomJS()
        cls.client = Client()
        #cls.username = os.environ.get('username', '')
        #cls.password = os.environ.get('password', '')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(CoursePostDetailTest, cls).tearDownClass()
    
    def test_xpd_without_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/notice'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        print("self.browser",self.browser)
       # self.browser.save_screenshot('3.png')
        self.assertIn('用户登录', self.browser.find_element_by_id('content').text)

    def test_xpd_with_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)
        self.browser.save_screenshot('3.png')
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/notice'))
        except Exception as e:
            print("give Error:",str(e))
        self.browser.save_screenshot('4.png')
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('公告', self.browser.find_element_by_id('content').text)
    
    def test_xpd_post_with_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")
    
        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)
    
        try:
            self.browser.get('%s%s' % (self.live_server_url, 'xpostdetail/78/notice'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('详情', self.browser.find_element_by_id('content').text)
    
        self.browser.implicitly_wait(2)
    
        content_box = self.browser.find_element_by_id('id_PContent')
        content_box.send_keys("yaowan............................................................................")
    
        time.sleep(2)
        submit_button = self.browser.find_element_by_id('happyBtn0')
        submit_button.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('yaowan', self.browser.find_element_by_id('content').text)

class PostXuetangPostTest(LiveServerTestCase):
    fixtures = ['authUsers.json','users.json','courses.json','posts.json','followUser.json','hasCourse.json','likePost.json']
    browser = None

    @classmethod
    def setUpClass(cls):
        super(PostCoursePostTest, cls).setUpClass()
        cls.browser = webdriver.PhantomJS()
        cls.client = Client()
        #cls.username = os.environ.get('username', '')
        #cls.password = os.environ.get('password', '')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(PostCoursePostTest, cls).tearDownClass()

    def test_postxuetangpost_without_login(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/complaint'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)

        print("self.browser",self.browser)
       # self.browser.save_screenshot('3.png')
        self.assertIn('用户登录', self.browser.find_element_by_id('content').text)

    def test_postxuetangpost_with_login_right_input(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

        try:
            self.browser.get('%s%s' % (self.live_server_url, '/postxpostdetail/complaint'))
        except Exception as e:
            print("give Error:",str(e))
        
        self.browser.implicitly_wait(2)

        title_box = self.browser.find_element_by_id('id_title')
        title_box.send_keys("Post of 2014013460")
    
        content_box = self.browser.find_element_by_id('id_content')
        content_box.send_keys("yaowan............................................................................")
        
        time.sleep(2)
        submit_button = self.browser.find_element_by_id('happyBtn0')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('2014013460', self.browser.find_element_by_id('content').text)

    def test_postxuetangpost_with_login_without_title(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

        try:
            self.browser.get('%s%s' % (self.live_server_url, '/postxpostdetail/complaint'))
        except Exception as e:
            print("give Error:",str(e))
        
        self.browser.implicitly_wait(2)

        title_box = self.browser.find_element_by_id('id_title')
        title_box.send_keys("")
    
        content_box = self.browser.find_element_by_id('id_content')
        content_box.send_keys("yaowan............................................................................")
        
        time.sleep(2)
        submit_button = self.browser.find_element_by_id('happyBtn0')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('请输入', self.browser.find_element_by_id('content').text)

    def test_postcoursepost_with_login_without_content(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")

        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)

        try:
            self.browser.get('%s%s' % (self.live_server_url, '/postxpostdetail/complaint'))
        except Exception as e:
            print("give Error:",str(e))
        
        self.browser.implicitly_wait(2)

        title_box = self.browser.find_element_by_id('id_title')
        title_box.send_keys("Post of 2014013460")
    
        content_box = self.browser.find_element_by_id('id_content')
        content_box.send_keys("")
        
        time.sleep(2)
        submit_button = self.browser.find_element_by_id('happyBtn0')
        submit_button.click()
        time.sleep(2)

        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)

        self.assertIn('请输入', self.browser.find_element_by_id('content').text)

class GoodPostTest(LiveServerTestCase):
    fixtures = ['authUsers.json','users.json','courses.json','posts.json','followUser.json','hasCourse.json','likePost.json']
    browser = None

    @classmethod
    def setUpClass(cls):
        super(CoursePostListViewTest, cls).setUpClass()
        cls.browser = webdriver.PhantomJS()
        cls.client = Client()
        #cls.username = os.environ.get('username', '')
        #cls.password = os.environ.get('password', '')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(CoursePostListViewTest, cls).tearDownClass()

    def test_goodpost(self):
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/login'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(5)
    
        name_box = self.browser.find_element_by_id('id_studentid')
        name_box.send_keys("2014013458")
    
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys("mp158269")
    
        time.sleep(2)
        submit_button = self.browser.find_element_by_css_selector('input.btn.btn-success.form_button')
        submit_button.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('学堂讨论区', self.browser.find_element_by_id('content').text)
    
        try:
            self.browser.get('%s%s' % (self.live_server_url, '/course/3/post/88'))
        except Exception as e:
            print("give Error:",str(e))
    
        self.browser.implicitly_wait(2)
        print("self.browser",self.browser)
    
        self.assertIn('帖子详情', self.browser.find_element_by_id('content').text)

        click_good = self.browser.find_element_by_id('89d')
        click_good.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(4)
        print("self.browser",self.browser)
    
        self.assertIn('取消', self.browser.find_element_by_id('content').text)
    
        click_good = self.browser.find_element_by_id('89d')
        click_good.click()
        time.sleep(2)
    
        self.browser.implicitly_wait(4)
        print("self.browser",self.browser)
    
        self.assertIn('采纳', self.browser.find_element_by_id('content').text)



