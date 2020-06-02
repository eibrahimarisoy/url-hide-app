import datetime
import random
import string

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import LinkCreationForm
from .models import Browser, Click, Link, OperatingSystem

BASE_URL = 'http://localhost:8000/'


def index(request):
    context = dict()
    context['link_creation_form'] = LinkCreationForm()
    return render(request, 'page/index.html', context)


@login_required
def hide_link_create(request):
    context = dict()
    link_creation_form = LinkCreationForm(request.POST or None)
    if request.method == "POST":
        if link_creation_form.is_valid():
            new_link = link_creation_form.save(commit=False)
            new_link.owner = request.user
            new_link.save(request)

            print(new_link.hide_link)
            context['link_creation_form'] = LinkCreationForm(
                instance=new_link
                )
            return render(request, "page/index.html", context)
    
    return render(request, "page/index.html", context)


def user_link_info(request):
    context = dict()
    links = Link.objects.filter(
        owner = request.user
    )
    context['links'] = links
    return render(request, 'page/user_link_info.html', context)


def link_forward(request, slug):
    link = get_object_or_404(Link, slug=slug)
    
    # increment click count
    click_count, created = Click.objects.get_or_create(
         link=link,
         date=datetime.date.today(),
    )
    if not created:
        click_count.save()
        click_count = click_count

    click_count.count += 1
    click_count.save()

    # added browser type to db
    Browser.objects.create(
        link=link,
        name=request.user_agent.browser.family,
        click_time=timezone.now()
    )
    # added operating system name to db
    OperatingSystem.objects.create(
        link=link,
        name=request.user_agent.os.family,
        click_time=timezone.now()
    )
    return redirect(link.exact_link)


def link_delete(request, id):
    link = get_object_or_404(Link, id=id)
    link.delete()
    return redirect('user_link_info')


def link_statistics(request, id):
    context = dict()
    link = get_object_or_404(Link, id=id)

    browser_queryset = Browser.objects.filter(link=link)
    browsers_info = []
    for browser in browser_queryset.values('name').distinct():
        item = {
            'name': browser.get('name'),
            'click_count': browser_queryset.filter(
                        name=browser.get('name')
                        ).count()
        }
        browsers_info.append(item)

    os_queryset = OperatingSystem.objects.filter(link=link)
    os_info = []

    for os in os_queryset.values('name').distinct():
        item = {
            'name': os.get('name'),
            'click_count': os_queryset.filter(
                name=os.get('name')
                ).count()
        }
        os_info.append(item)

    context['browsers_info'] = browsers_info
    context['os_info'] = os_info
    context['link'] = link
    return render(request, 'page/link_statistics.html', context)
