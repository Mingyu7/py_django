import form
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect

from pybo.models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    """
    pybo 목록 출력
    """
    page = request.GET.get('page','1') # 페이지
    question_list = Question.objects.order_by('-create_date') # 내림차순 정렬
    # context = {'question_list': question_list}

    # 페이징 처리
    paginator = Paginator(question_list,10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj,'page':page}
    return render(request, 'pybo/question.html', context)


def detail(request, question_id):
    """
       pybo 내용 출력
       """
    # question = Question.objects.get(id=question_id)  # question_id에 해당하는 객체 추출
    question = get_object_or_404(Question, pk=question_id) # question_id에 해당하는 객체 추출
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)  # question_id에 해당하는 객체 추출
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

def answer_create (request, question_id):
    """
    pybo에 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)