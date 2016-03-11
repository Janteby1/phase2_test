from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseForbidden

from .models import WCard, BCard
# import pudb
import json
from django.http import JsonResponse
from random import randint


# Create your views here.
class Index(View):
    def get(self, request):
        # context = {}
        # # this line gets all the posts that we have in the db and orders them by most recent
        # w_cards = WCard.objects.filter(show=True)
        # b_cards = BCard.objects.filter(show=True)
        # # put all the posts into a context dict

        # context ["w_cards"] = w_cards
        # context ["b_cards"] = b_cards
        # # send them all to the template
        return render(request, "index.html")


class Pick_Black(View):
    def get(self, request):
        # if we just want an ajax request we dont need a seperate class 
        if request.is_ajax():   
            pk=randint(1, 90)  # randint is inclusive at both ends (randomly gives 1, 2 or 3)
            # do all the logic and filtering here, only get the comments that are shown and have the right id 
            cards = BCard.objects.filter(show=True)
            # put all the values into a json dictionary with a method called from the models
            cards = [card.to_json() for card in cards]
            # put the card into a context dict

            data = {
                "cards": cards[pk-1] }
            # not good --> I am returning all the cards then picking a random one rather than getting a randon one from the db
            return JsonResponse(data) # return a json object to the ajax request


class Pick_White(View):
    def get(self, request):
        # if we just want an ajax request we dont need a seperate class 
        if request.is_ajax():   
            # do all the logic and filtering here, only get the comments that are shown and have the right id 
            cards = WCard.objects.filter(show=True)
            # put all the values into a json dictionary with a method called from the models
            cards = [card.to_json() for card in cards]
            # put the card into a context dict

            cardslist = []
            # pick 5 cards randomly from what you returned from the db
            for i in range (0,5):
                pk=randint(1, 500)
                cardslist.append(cards[pk-1])

            data = {
                "cards": cardslist }

            # not good --> I am returning all the cards then picking a random one 
            # rather than getting a randon one from the db, here can cause doubles 
            return JsonResponse(data) # return a json object to the ajax request











