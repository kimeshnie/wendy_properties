import re
from django.db.models import Q
from django.shortcuts import render
from .models import Listings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from mysite.forms import ContactForm



def home_page(request):
    return render(request, 'mysite/home_page.html', {})


def post_featured(request):
    featured_listings = Listings.objects.filter(featured=True)
    return render(request, 'mysite/home_page.html', {'featured_listings': featured_listings})

def normalize_query(query_string,
    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
    normspace=re.compile(r'\s{2,}').sub):

    return [normspace('',(t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):

    q=Q()	
    query = None 
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None 
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search_for_something(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['suburb', 'bedrooms', 'price'])
        found_entries = Listings.objects.filter(entry_query).order_by('price')

    return render_to_response('mysite/properties.html',
            { 'query_string': query_string, 'found_entries': found_entries },
            context_instance=RequestContext(request)
        )    

def detailed_listing(request, pk):
    details = get_object_or_404(Listings, pk=pk)
    return render(request, 'mysite/detailed_listing.html', {'details': details})    


#def contact_form(request):
 #   contact_details = ContactForm
  #  return render(request, 'mysite/detailed_listing.html', {'contact_details': contact_details})    