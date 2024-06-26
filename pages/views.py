from django.shortcuts import render, redirect
from questions.models import Question, Option
from category.models import Category
from django.http import JsonResponse
import random
from django.contrib import messages
from django.utils import timezone
from.models import Contact

def index(request, category):
    questions = list(Question.objects.filter(category_id=category))
    random.shuffle(questions)
    random_questions = questions[:5]  # Change the number (5) to the desired number of random questions to display

    context = {
        'questions': random_questions
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def submitcontact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        description = request.POST['description']

    # Check if the email is already exist
        # Check if the email and date combination already exists
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timezone.timedelta(days=1)
        if Contact.objects.filter(email=email, date__range=(today_start, today_end)).exists():
            messages.error(request, 'You have already submitted a message with this email today. Please wait for response!')
            return render(request, 'pages/contact.html')

    contact = Contact(
        name = name,
        email = email, 
        subject = subject,
        description = description,

    )

    contact.save()
    messages.success(request, 'Your message has been submitted')
    return render(request, 'pages/contact.html')

def dashboard(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'pages/dashboard.html', context)

from django.core.exceptions import ObjectDoesNotExist
def submit_quiz(request):
    if request.method == 'POST':
        # Process submitted answers and calculate the score
        score = 0
        answers = []
        total_questions = 0

        total_questions_str = request.POST.get('total_questions')
        total_questions = int(total_questions_str)

        for question_id in request.POST.keys():
            if question_id.startswith('q'):
                selected_option_id = request.POST.get(question_id)
                try:
                    question = Question.objects.get(id=question_id[1:])
                    selected_option = Option.objects.get(id=selected_option_id)
                except ObjectDoesNotExist:
                    # Handle the case when the Question or Option object does not exist
                    # You can display an error message or handle it based on your requirements
                    question = None
                    selected_option = None

                if question and selected_option and selected_option.is_correct:
                    score += 1

                answers.append({
                    'question': question.text if question else 'N/A',
                    'selected_option': selected_option.text if selected_option else 'N/A',
                    'is_correct': selected_option.is_correct if selected_option else False,
                    'explanation': question.explanation if question else 'N/A'
                })

        # Calculate the score percentage
        score_percentage = round((score / total_questions) * 100, 2)
        context = {
            'score': score,
            'total_questions': total_questions,
            'answers': answers,
            'score_percentage': score_percentage,
        }
        return render(request, 'pages/result.html', context)

    else:
        return redirect('index')



def result(request, score, total_questions, correct_answers):
    context = {
        'score': score,
        'total_questions': total_questions,
        'correct_answers': correct_answers
    }
    return render(request, 'pages/result.html', context)