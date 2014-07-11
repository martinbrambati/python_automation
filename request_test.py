import requests
from BeautifulSoup import BeautifulSoup
from num2words import num2words

class User():
	#url_prod = 'http://192.168.6.80:5000'
	url = 'http://localhost:5000'
	units = {"one":1, "two":2, "three":3, "four":4, "five":5, 
			"six":6, "seven":7, "eight":8, "nine":9, "zero":0}
	

	def __init__(self, username, email, password, cookies=None):
		self.username = username
		self.email = email
		self.password = password
		self.cookies = cookies

	def test_register(self):
		data = {'username': self.username, 'email': self.email,'password':self.password,'password2':self.password}
		r = requests.post(self.url + '/register', data)
		if r.status_code == 200:
			print "Register OK!"

	def test_login(self):
		data = {'username': self.username, 'password':self.password}
		r = requests.post(self.url + '/login', data)
		if r.status_code == 200:
			print "Login OK!"
		self.cookies = r.cookies

	def test_publish(self, message):
		#Buscar captcha
		r = requests.get(self.url + '/', cookies=self.cookies)
		parsed_html = BeautifulSoup(r.text)
		operation = parsed_html.find(id='captcha').text[:-2]
		captcha = num2words(eval(operation,self.units)).replace('-',' ')
		data = {'text':message, 'captcha':captcha}
		r = requests.get(self.url + '/add_message', data, cookies=self.cookies)

		

personita = User("Test1","test@test.com","123")
#personita.test_register()
personita.test_login()
personita.test_publish("mensaje")