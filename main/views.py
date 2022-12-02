from django.db.models import Q
from django.shortcuts import render
from .models import Material, Authors, Number, News, Contacts


def index_main(requests):
    cont = Contacts.objects.get(id=1)
    num = Number.objects.exclude(draft=True).earliest('-published')
    news = News.objects.order_by('-published')[:4]
    context = {'num': num, 'news': news, 'cont': cont}

    return render(requests, 'm/index.html', context)


def index_authors(requests):
    cont = Contacts.objects.get(id=1)
    authors = Authors.objects.filter(draft=False)
    context = {'authors': authors, 'cont': cont}
    return render(requests, 'authors/index.html', context)


def index_author(requests, author_id):
    cont = Contacts.objects.get(id=1)
    author = Authors.objects.get(id=author_id)
    mat = Material.objects.filter(auth__id=author.id)
    context = {'author': author, 'mat': mat, 'cont': cont}
    return render(requests, 'author/index.html', context)


def index_about(requests):
    cont = Contacts.objects.get(id=1)
    context = {'cont': cont}
    return render(requests, 'contacts/index.html', context)


def index_news(requests):
    cont = Contacts.objects.get(id=1)
    news = News.objects.all().order_by('-published')
    context = {'news': news, 'cont': cont}
    return render(requests, 'news/index.html', context)


def index_new(requests, new_id):
    cont = Contacts.objects.get(id=1)
    new = News.objects.get(id=new_id)
    context = {'new': new, 'cont': cont}
    return render(requests, 'new/index.html', context)


def index_numbers(requests):
    cont = Contacts.objects.get(id=1)
    numbers = Number.objects.filter(draft=False)
    context = {'numbers': numbers, 'cont': cont}
    return render(requests, 'numbers/index.html', context)


def index_number(requests, number_id):
    cont = Contacts.objects.get(id=1)
    num = Number.objects.get(id=number_id)
    mat = Material.objects.filter(number=num.id)
    context = {'num': num, 'cont': cont, 'mat': mat}
    return render(requests, 'number/index.html', context)


def index_serch_result(requests):
    no_result = ''
    query = requests.GET.get('q')
    s = str(query).title().split(' ')
    s1 = str(query).lower().split(' ')
    s2 = str(query).upper().split(' ')
    s3 = s + s1 + s2
    mat = Material.objects.filter(Q(name__contains=s3[0]) & Q(draft=False))
    author = Authors.objects.filter(Q(name=s3[0]) | Q(soname=s3[0]) & Q(draft=False))
    for i1, i in enumerate(s3):
        if i1 == 0:
            continue
        if mat:
            mat.union(Material.objects.filter(Q(name__contains=i) & Q(draft=False)))
        if not mat:
            mat = Material.objects.filter(Q(name__contains=i) & Q(draft=False))
        if author:
            author.union(Authors.objects.filter(Q(name=i) | Q(soname=i) & Q(draft=False)))
        if not author:
            author = Authors.objects.filter(Q(name=i) | Q(soname=i) & Q(draft=False))

    if not mat and not author:
        no_result = f'по запросу "{query}" ничего не найдено'
    context = {'mat': mat, 'author': author, 'query': query, 'no_result': no_result}
    return render(requests, 'search/index.html', context)


def index_search(requests):
    return render(requests, 'search/index.html')