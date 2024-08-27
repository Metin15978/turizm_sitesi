from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count
from Login.forms import SaleForm
from Login.models import Customer, Sale
from Main.forms import CommentForm
from .models import *

# Create your views here.
def base(request):
    keyword = request.GET.get('keyword', '')
    budget = request.GET.get('budget', '')

    # İlk olarak tüm indirimli turları filtrelemeye başla
    discounted_tours = Tour.objects.filter(discount_price__isnull=False)

    # Filtreleme koşullarını uygula
    if keyword:
        discounted_tours = discounted_tours.filter(name__icontains=keyword)

    if budget:
        # 'budget' parametresi, indirimli fiyat üzerinden filtreleme yapacak
        try:
            budget_value = float(budget)
            discounted_tours = discounted_tours.filter(discount_price__lte=budget_value)
        except ValueError:
            # Eğer 'budget' geçerli bir sayı değilse, filtrelemeyi geç
            pass

    context = {
        'discounted_tours': discounted_tours
    }

    return render(request, 'Main/pages/base/base.html', context)

# **************************** About *****************************************************
def about(request):
    teams = TeamsModel.objects.all()
    return render(request, 'Main/pages/about/about-us.html', {'teams': teams})

# **************************** About *****************************************************

# **************************** Blog *****************************************************
def blog(request):
    items = Tour.objects.filter(is_delete=False).order_by('-created_date')
    # Her item için yorum sayısını sayma
    item_with_comment_count = items.annotate(comment_count=Count('comments'))
    
    context = {
        'items': items,
        'items': item_with_comment_count,
    }
    return render(request, 'Main/pages/blog/blog-masonry.html',context)

def blog_second(request, itemSlug):
    # Tour nesnesini alın
    tour = get_object_or_404(Tour, is_delete=False, slug=itemSlug)
    
    # İlgili Tour nesnelerini alın
    tours = Tour.objects.filter(is_delete=False, slug=itemSlug)
    
    for tour_item in tours:
        tour_item.city_list = ', '.join(item.location for item in tour_item.item.all())
    
    # İlgili Item nesnelerini almak için Tour nesnelerindeki ilişkili Item'ları sorgula
    items = Item.objects.filter(tours__in=tours).distinct()

    # Tüm ilgili yorumları getir
    comments = Comment.objects.filter(tour=tour)
    comment_count = comments.count()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.tour = tour
            comment.save()
            return redirect('standard-blog-post-with-image', itemSlug=itemSlug)
    else:
        form = CommentForm()
    
    context = {
        'tours': tours,
        'items': items,
        'tour_slug': tour.slug,
        'comments': comments,
        'comment_count': comment_count,
        'form': form,
    }
    
    return render(request, 'Main/pages/blog/standard-blog-post-with-image.html', context)

# **************************** Blog *****************************************************

# **************************** Gallery *****************************************************
def gallery(request):
    return render(request, 'Main/pages/gallery/gallery.html')

# **************************** Gallery *****************************************************

# **************************** Tour *****************************************************
def tour(request, itemSlug):
    # Tour nesnesini alın
    tour = get_object_or_404(Tour, is_delete=False, slug=itemSlug)
    
    # İlgili Tour nesnelerini alın
    tours = Tour.objects.filter(slug=tour.slug, is_delete=False)
    
    # Her tour için city_list'i güncelleyin
    for tour_item in tours:
        tour_item.city_list = ', '.join(item.location for item in tour_item.item.all())
    
    if request.user.is_authenticated:
        customer = get_object_or_404(Customer, user=request.user)
        
        # Kullanıcının daha önce satın alıp almadığını kontrol edin
        already_purchased = Sale.objects.filter(customer=customer, tours__in=tours, sold=True).exists()

        if request.method == 'POST' and not already_purchased:
            form = SaleForm(request.POST)
            if form.is_valid():
                sale = form.save(commit=False)
                sale.customer = customer
                sale.save()  # Önce `sale` nesnesini kaydedin
                sale.tours.set(tours)  # Ardından `tours` queryset'ini ayarlayın
                sale.sold = True
                sale.save()  # `tours` ile ilişkili olarak `sale` nesnesini tekrar kaydedin
                return redirect('base')
        else:
            form = SaleForm()
    else:
        customer = None
        already_purchased = False
        form = None
        
    context = {
        'tours': tours,  # 'tour' yerine 'tours' olarak güncellendi
        'tour_slug': tour.slug,  # slug'ı buradan alıyoruz
        'customer': customer,
        'form': form,
        'already_purchased': already_purchased,
    }
    return render(request, 'Main/pages/tour/east-europe.html', context)



def tourparis(request):
    return render(request, 'Main/pages/tour/paris.html')

def tourclassic(request):
    # Filtreleme parametrelerini al
    keyword = request.GET.get('keyword', '')
    budget = request.GET.get('budget', '')

    # İlk olarak tüm itemları filtrelemeye başla
    tour = Tour.objects.filter(is_delete=False).order_by('-created_date')

    # Filtreleme koşullarını uygula
    if keyword:
        tour = tour.filter(name__icontains=keyword)

    if budget:
        tour = tour.filter(price__lte=budget)

    context = {
        'tours': tour
    }

    return render(request, 'Main/pages/tour/tour-classic-fullwidth.html', context)

# **************************** Tour *****************************************************

# **************************** Login & Register *****************************************************
def login(request):
    return render(request, 'Login/login/login.html')

def register(request):
    return render(request, 'Login/register/register.html')
# **************************** Login & Register *****************************************************
