import random
import string
import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .models import Link, ClickCount
from .forms import LinkCreationForm


BASE_URL = 'http://localhost:8000/'



def random_string(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def index(request):
    context = dict()
    context['link_creation_form'] = LinkCreationForm()
    return render(request, 'page/index.html', context)


def hide_link_create(request):
    context = dict()
    link_creation_form = LinkCreationForm(request.POST or None)
    if request.method == "POST":
        if link_creation_form.is_valid():
            new_link = link_creation_form.save(commit=False)
            new_link.owner = request.user
            new_link.hide_link = f"{BASE_URL}{random_string()}"
            print(new_link.hide_link)
            new_link.save()

            context['link_creation_form'] = LinkCreationForm(instance=new_link)
            return render(request, "page/index.html", context)
    
    return render(request, "page/index.html", context)


def user_link_info(request):
    context = dict()
    links = Link.objects.filter(
        owner = request.user
    )

    context['links'] = links
    return render(request, 'page/user_link_info.html', context)


def link_forward(request, hide_link):
    print(hide_link)
    hide_link = BASE_URL + hide_link
    link = Link.objects.get(hide_link=hide_link)
    today = datetime.date.today()
    click_count, created = ClickCount.objects.get_or_create(
        link=link,
        date=today,
    )
    if not created:
        click_count.save()
        click_count = click_count

    click_count.count += 1
    click_count.save()

    ip = request.META.get('REMOTE_ADDR', None)
    print(f"Tıklanma : {click_count.count}")
    print(f"browser : {request.user_agent.browser.family}")
    print(f"işletim sistemi : {request.user_agent.os.family}")
    return redirect(link.exact_link)


def link_delete(request, id):
    link = get_object_or_404(Link, id=id)
    link.delete()
    return redirect('user_link_info')