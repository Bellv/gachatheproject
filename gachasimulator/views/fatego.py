from django.shortcuts import render
from django.views.generic import TemplateView

from ..forms import FgoGachaForm
from ..models import Characterfgo

from random import shuffle
import random


class GenerateGachaFGOView(TemplateView):
    template = 'fgo_gacha.html'

    def generate_gacha_pool_number(self):
        gacha_pool = []

        for i in range(0, 100):
            gacha_pool.append(i)
        
        #5star servant
        rnd_5_star_servant_list = random.sample(gacha_pool, 1)
        for rnd_pick in rnd_5_star_servant_list:
            gacha_pool.remove(rnd_pick)

		#4star servant
        rnd_4_star_servant_list = random.sample(gacha_pool, 3)
        for rnd_pick in rnd_4_star_servant_list:
            gacha_pool.remove(rnd_pick)

		#3star servant
        rnd_3_star_servant_list = random.sample(gacha_pool, 40)
        for rnd_pick in rnd_3_star_servant_list:
            gacha_pool.remove(rnd_pick)

		#5star craft essense
        rnd_5_star_craftessense_list = random.sample(gacha_pool, 4)
        for rnd_pick in rnd_5_star_craftessense_list:
            gacha_pool.remove(rnd_pick)

		#4star craft essense
        rnd_4_star_craftessense_list = random.sample(gacha_pool, 12)
        for rnd_pick in rnd_4_star_craftessense_list:
            gacha_pool.remove(rnd_pick)

		#3star craft essense
        rnd_3_star_craftessense_list = random.sample(gacha_pool, 40)
        for rnd_pick in rnd_3_star_craftessense_list:
            gacha_pool.remove(rnd_pick)

        return rnd_5_star_servant_list, rnd_4_star_servant_list, rnd_3_star_servant_list, rnd_5_star_craftessense_list, rnd_4_star_craftessense_list, rnd_3_star_craftessense_list

    def roll_gacha_case(self, rnd_5_star_servant_list, rnd_4_star_servant_list, rnd_3_star_servant_list, rnd_5_star_craftessense_list, rnd_4_star_craftessense_list, rnd_3_star_craftessense_list):
        #Gurantee Case
        gurantee_gacha_list = []
        gurantee_pool = rnd_5_star_servant_list + rnd_4_star_servant_list + rnd_5_star_craftessense_list + rnd_4_star_craftessense_list
        result_one_gurantee_list = random.sample(gurantee_pool, 1)
        for gacha_list_rnd in result_one_gurantee_list:
            gurantee_gacha_list.append(gacha_list_rnd)
        
        #Normal Case
        number_gacha_list = []
        normal_gacha_list = []
        for i in range(9):
            rnd_range = range(0,100)
            rnd_each = random.sample(rnd_range, 1)
            normal_gacha_list.append(rnd_each[0])

        number_gacha_list = gurantee_gacha_list + normal_gacha_list
        shuffle(number_gacha_list)

        star_gacha_list = []
        for i in number_gacha_list:
            if i in rnd_5_star_servant_list:
                star_gacha_list.append('5Ser')
            elif i in rnd_4_star_servant_list:
                star_gacha_list.append('4Ser')
            elif i in rnd_3_star_servant_list:
                star_gacha_list.append('3Ser')
            elif i in rnd_5_star_craftessense_list:
                star_gacha_list.append('5CE')
            elif i in rnd_4_star_craftessense_list:
                star_gacha_list.append('4CE')
            elif i in rnd_3_star_craftessense_list:
                star_gacha_list.append('3CE')

        return star_gacha_list

    def get(self, request):
        form = FgoGachaForm()

        return render(
            request,
            self.template,
            {
                'form': form
            }
        )

    def post(self, request):
        form = FgoGachaForm(request.POST)
        print ('belly')

        return render(
            request, 
            self.template,
            {
                'form': form
            }
        )

        
