from django.shortcuts import render, redirect
from rest_framework import status

from .models import Survey_Form
from django.contrib import messages
from django.views.generic.base import View

# Create your views here.


class Survey_Create_View(View):

    def get(self, request):
        return render(request, 'surveyForm/newForm.html')

    def post(self, request):
        context = {
            'data': request.POST,
            'has_error': False
        }

        # data = request.POST
        name = request.POST.get('name', None)
        l_name = request.POST.get('l_name', None)
        age = request.POST.get('age', None)
        gender = request.POST.get('gender', None)
        relation = request.POST.get('relation', None)
        employment = request.POST.get('employment', None)
        pregnancy = request.POST.get('pregnancy', None)
        diet = request.POST.get('diet', None)

        first_food = request.POST.get('first_food', None)
        second_food = request.POST.get('second_food', None)
        third_food = request.POST.get('third_food', None)
        fourth_food = request.POST.get('fourth_food', None)
        fifth_food = request.POST.get('fifth_food', None)
        rating = request.POST.get('rating', None)

        if context['has_error']:
            return render(request, 'surveyForm/newForm.html', context=context, status=status.HTTP_400_BAD_REQUEST)

        user = Survey_Form(name=name, l_name=l_name, age=age, gender=gender, relation=relation, employment=employment,
                           pregnancy=pregnancy, diet=diet, first_food=first_food, second_food=second_food,
                           third_food=third_food, fourth_food=fourth_food, fifth_food=fifth_food, rating=rating)
        user.save()

        messages.add_message(request, messages.SUCCESS, 'Survey Filled Successfully! ')
        return redirect('survey')


class Survey_Dashboard(View):

    def get(self, request):
        query_results = Survey_Form.objects.all()
        labels = ['Married', 'UnMarried', 'Divorced', 'Widowed']
        data = []

        queryset = Survey_Form.objects.filter(relation='Married').count()
        data.append(queryset)
        queryset = Survey_Form.objects.filter(relation='UnMarried').count()
        data.append(queryset)
        queryset = Survey_Form.objects.filter(relation='Divorced').count()
        data.append(queryset)
        queryset = Survey_Form.objects.filter(relation='Widowed').count()
        data.append(queryset)

        labels2 = ['Vegetarian', 'Non-Vegetarian']
        data2 = []

        queryset = Survey_Form.objects.filter(diet='Vegetarian').count()
        data2.append(queryset)
        queryset = Survey_Form.objects.filter(diet='Non-Vegetarian').count()
        data2.append(queryset)

        male_count = Survey_Form.objects.all().filter(gender='Male').count()
        female_count = Survey_Form.objects.all().filter(gender='Female').count()
        employed_count = Survey_Form.objects.all().filter(employment='Employed').count()
        married_count = Survey_Form.objects.all().filter(relation='Married').count()
        vegetarian_count = Survey_Form.objects.all().filter(diet='Vegetarian').count()
        total = Survey_Form.objects.all().count()

        return render(request, 'surveyForm/dashboard.html',
                      {'male_count': male_count, 'female_count': female_count, 'total': total,
                       'employed_count': employed_count, 'married_count': married_count,
                       'vegetarian_count': vegetarian_count, 'labels': labels,
                       'data': data, 'labels2': labels2,
                       'data2': data2,'query_results':query_results})
