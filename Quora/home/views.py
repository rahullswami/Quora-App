from django.shortcuts import render, redirect, get_object_or_404
from .models import Space, Question, Answer, Notification, Follow
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required(login_url='/accounts/login/')
def home(request):
    questions = Question.objects.all()
    spaces = Space.objects.all()
    user_notifications = Notification.objects.filter(user=request.user).order_by('-created_at')

    if request.method == 'POST':
        if 'question' in request.POST:
            ques = request.POST.get('question')
            image = request.FILES.get('image')
            message = request.POST.get('message')

            question = Question.objects.create(
                user=request.user,
                title=ques,
                content=message,
                image=image,
            )
            question.save()

            # Create notifications for all users except the one who posted the question
            users = User.objects.exclude(id=request.user.id)
            notification_message = f"{request.user.username} posted a new question: {ques}"
            notifications = [Notification(user=user, sender=request.user, notification_type='question_posted', message=notification_message) for user in users]
            Notification.objects.bulk_create(notifications)

            return redirect('home')

        elif 'answer' in request.POST:
            question_id = request.POST.get('question_id')
            question = get_object_or_404(Question, id=question_id)
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.user = request.user
                answer.question = question
                answer.save()

                # Create notification for the question owner
                if question.user != request.user:
                    notification_message = f"{request.user.username} answered your question: {question.title}"
                    Notification.objects.create(user=question.user, sender=request.user, notification_type='answer_posted', message=notification_message)

                return redirect('home')

    else:
        form = AnswerForm()

    return render(request, 'Quora.html', {'questions': questions, 'notifications': user_notifications, 'form': form, 'spaces': spaces})




@login_required(login_url='/accounts/login/')
def answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('answer', question_id=question.id)
    else:
        form = AnswerForm()

    answers = question.answers.all()
    return render(request, 'answer.html', {'question': question, 'form': form, 'answers': answers})



# following fucntions start 
@login_required(login_url='/accounts/login/')
def following(request):
    user = request.user
    followed_users = user.following.all()
    suggested_users = User.objects.exclude(id__in=followed_users.values_list('following_id', flat=True)).exclude(id=user.id)
    return render(request, 'following.html', {'followed_users': followed_users, 'suggested_users': suggested_users})

@login_required(login_url='/accounts/login/')
def follow(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    follow, created = Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('following')

@login_required(login_url='/accounts/login/')
def unfollow(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('following')


@login_required(login_url='/accounts/login/')
def notification(request):
    user_notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notifications.html', {'notifications': user_notifications})




@login_required(login_url='/accounts/login/')
def spaces(request):
    if request.method == 'POST':
        form = SpaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spaces')
    else:
        form = SpaceForm()
    
    all_spaces = Space.objects.all()
    return render(request, 'spaces.html', {'spaces': all_spaces, 'form': form})


@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    user_questions = Question.objects.filter(user=user)
    follower_count = Follow.objects.filter(following=user).count()
    user_answers = Answer.objects.filter(user=user)

    context = {
        'user_questions': user_questions,
        'user_answers': user_answers,
        'follower_count': follower_count,
    }

    return render(request, 'profile.html', context)





    # delete functionality 

@login_required(login_url='/accounts/login/')
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id, user=request.user)
    question.delete()
    return redirect('home')

@login_required(login_url='/accounts/login/')
def delete_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id, user=request.user)
    answer.delete()
    return redirect('home')

@login_required(login_url='/accounts/login/')
def delete_space(request, space_id):
    space = get_object_or_404(Space, id=space_id)
    space.delete()
    return redirect('spaces')