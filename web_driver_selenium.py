from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class MiniTwit(object):
	urls = {'base':'http://localhost:5000',
			'register':'/register',
			'login':'/login',
			'publish':'/publish'}
	
	def __init__(self, user, password, email):
		self.user = user
		self.password = password
		self.email = email
		self.driver = webdriver.Firefox()
		self.actions = ActionChains(self.driver)

	def sign_up(self):
		self.driver.get(MiniTwit.urls['base'] + MiniTwit.urls['register'])
        #username
		username = self.driver.find_element_by_name("username")
		username.send_keys(self.user)
        #Email
		email = self.driver.find_element_by_name("email")
		email.send_keys(self.email)
        #Password
		password = self.driver.find_element_by_name("password")
		password.send_keys(self.password)
        #Password2
		password2 = self.driver.find_element_by_name("password2")
		password2.send_keys(self.password)
    	#Submit
		submit = self.driver.find_element_by_xpath("//input[@type='submit']")
		self.actions.click(submit)
		self.actions.perform()
		
		#assert title_to_assert in self.driver.

	def login(self, title_to_assert):
		self.driver.get(MiniTwit.urls['base'] + MiniTwit.urls['login'])
        #username
		username = self.driver.find_element_by_name("username")
		username.send_keys(self.user)
        #Password
		password = self.driver.find_element_by_name("password")
		password.send_keys(self.password)
        #Submit
		submit = self.driver.find_element_by_xpath("//input[@type='submit']")
		self.actions.click(submit)
		self.actions.perform()
		
	
	def close(self):
		self.driver.close()



#Test
test = MiniTwit('usuario3', 'password3', 'ma3@massa.com')
test.sign_up()
test.login('You were logged in')
test.close()