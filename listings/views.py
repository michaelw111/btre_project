from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices 
# we are in listings, so no need to do listings.choices but .choices

# Create your views here.

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id) #pk: primary key

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    
    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords'] #Look for the field name in the form
        if keywords: #make sure it is not empty keywords
            queryset_list = queryset_list.filter(description__icontains=keywords) 
            #Use double underscore '__' for not-exact-match, the above means if description paragraph contains the keywords
    
    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city: #make sure it is not empty city
            queryset_list = queryset_list.filter(city__iexact=city)
            #iexact is not case sensitive; use exact if you want it be case sensitive
    #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state: #make sure it is not empty state
            queryset_list = queryset_list.filter(state__iexact=state)
            #iexact is not case sensitive; use exact if you want it be case sensitive  
    
    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms: #make sure it is not empty bedrooms
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
            #lte: less than or equals to, say if you pick 4, will give you all listings with up to 4 bedrooms

    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price: #make sure it is not empty price
            queryset_list = queryset_list.filter(price__lte=price)
            #lte: less than or equals to


    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)