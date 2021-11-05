from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View



class Signup(View):

	def get(self , request):
		return render(request , 'signup.html')

	def post(self , request):
		first_name = request.POST.get('firstname')
		last_name = request.POST.get('lastname')
		contact = request.POST.get('contact')
		email = request.POST.get('email')
		password = request.POST.get('password')
        #new page value not deleted
		value = {'first_name':first_name , 'last_name':last_name , 'contact':contact  , 'email':email}
        #validation
		customer = Customer(first_name = first_name, last_name = last_name , contact = contact , email = email , password = password)
		error_message = self.validateCustomer(customer)

		if not error_message:
			customer.password = make_password(customer.password)
			customer.register()
			return redirect('homepage')
		else:
			data = {'error' : error_message , 'values' : value}
			return render(request , 'signup.html' , data)

	def validateCustomer(self , customer):
		error_message = None
		if not customer.first_name:
			error_message = "First Name required.!!!"
		elif len(customer.first_name) < 2:
			error_message = "FIRST NAME MUST BE OF 4 CHARACTER "
		elif not customer.last_name:
			error_message = "LAST NAME REQUIRED!!!!"
		elif len(customer.last_name) < 2:
			error_message = "LAST NAME MUST BE OF 4 CHARACTER "
		elif not customer.contact:
			error_message = "CONTACT INFO REQUIRED!!!!"
		elif len(customer.contact) < 9:
			error_message = "CONTACT INFO MUST BE OF 10 CHARACTER "
		elif not customer.email:
			error_message = "EMAIL REQUIRED!!!!"
		elif len(customer.email) < 4:
			error_message = "EMAIL IS NOT VALID!!!"
		elif not customer.password:
			error_message = "PASSWORD REQUIRED!!!!"
		elif len(customer.password) < 4:
			error_message = "PASSWORD MUST BE OF 4 CHARACTER "
		elif customer.isExists():
			error_message = 'EMAIL ALREADY EXISTS!!!'

		return error_message