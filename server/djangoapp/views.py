from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarDealer, CarMake, CarModel, DealerReview
from .restapis import get_dealers_from_cf, get_request, get_dealer_by_id_from_cf, get_dealer_review_from_cf, post_request
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    if request.method == "GET":
        return render(request, 'djangoapp/about.html')


# Create a `contact` view to return a static contact page
def contact(request):
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    # Handles POST request
    if request.method == "POST":
        # Get username and password from request.POST dictionary
        username = request.POST['username']
        password = request.POST['psw']
        # Try to check if provide credential can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid, call login method to login current user
            login(request, user)
            return redirect('djangoapp:index')
        else:
            # If not, return to login page again
            return render(request, 'djangoapp:index', context)
    else:
        return render(request, 'djangoapp:index', context)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect("djangoapp:index")

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    # If it is a GET request, just render the registration page
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    # If it is a POST request
    elif request.method == 'POST':
        # Get user information from request.POST
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))
        # If it is a new user
        if not user_exist:
            # Create user in auth_user table
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            # Login the user and redirect to course list page
            login(request, user)
            return redirect("djangoapp:index")
        else:
            return render(request, 'djangoapp/registration.html', context)

def get_dealerships(request):
    if request.method == "GET":
        context= {}
        url = "https://04f21472.us-south.apigw.appdomain.cloud/api/dealership"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        # Concat all dealer's short name
        context["dealership_list"] = dealerships
        # Return a list of dealer short name
        return render(request, 'djangoapp/index.html', context)
        
# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    print(dealer_id)
    if request.method == "GET":
        context = {}
        dealer_url = "https://04f21472.us-south.apigw.appdomain.cloud/api/dealership"
        
        dealership = get_dealer_by_id_from_cf(dealer_url, id=dealer_id)
        context["dealer"] = dealership

        review_url = "https://04f21472.us-south.apigw.appdomain.cloud/api/review" 
        reviews = get_dealer_review_from_cf(review_url, id=dealer_id)
        print(reviews)
        context["reviews"] = reviews

        return render(request, 'djangoapp/dealer_details.html', context)



# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
    context = {}
    if request.method == "POST":
        if request.user.is_authenticated:
            url = "https://04f21472.us-south.apigw.appdomain.cloud/api/review"
            review = ()
            review["name"] = request.username
            review["time"] = datetime.utcnow().isoformat()
            review["dealership"] = dealer_id
            review["review"] = request.review
            if request.purchase:
                review["purchase"] = request.purchase
                review["purchase_date"] = request.purchase_date
                review["car_make"] = request.car_make
                review["car_model"] = request.car_model
                review["car_year"] = request.car_year
            json_payload = ()
            json_payload["review"] = review
            post_request(url, json_payload, dealer=dealer_id )
        return redirect("djangoapp:dealer_details", id=id)
        


