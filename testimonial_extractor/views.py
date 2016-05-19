from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
from BeautifulSoup import BeautifulSoup
import re
import urllib2
import json,os
import requests
import urlparse



class Testimonial():
    def __init__(self, name, image, text):
        self.name = name
        self.image = image
        self.text = text



def sample(request):
    return render(request, "sample.html")

def start(request):
    path = request.path
    path = os.path.split(path)[1]
    print path
    s = requests.Session()
    base_url = "http://students.nitk.ac.in"
    r = s.get("http://students.nitk.ac.in/smriti/profiles/"+path)
    soup = BeautifulSoup(r.text)    
    name = soup.findAll("h4")[0].text

    print "==============="
    print name
    print "==============="

    profile_image_url = base_url+soup.findAll("img", {"class":"circle responsive-img"})[0].attrs[1][1]
    print profile_image_url

    testimonials_urls = soup.findAll("a", attrs = {"href": re.compile("/smriti/testimonial/.")})
    urls = []
    all_testimonials = []    
    for url in testimonials_urls:
        request_url = base_url+url.attrs[0][1]
        r = s.get(request_url)
        soup = BeautifulSoup(r.text)
        testi_name = soup.findAll("h4")[1].text
        testi_image_url = base_url+soup.findAll("img", {"class":"circle responsive-img"})[1].attrs[1][1]
        div = soup.findAll("div", {"class":"flow-text container"})[0]
        testimonial = div.text
        print testi_name
        print testi_image_url
        testimonial = testimonial.encode('ascii', 'ignore')
        testimonial = testimonial.encode('ascii', 'replace')
        testimonial = testimonial.encode('ascii', 'xmlcharrefreplace')
        testi = Testimonial(testi_name, testi_image_url, testimonial)
        all_testimonials.append(testi)
    return render(request, "index.html", {"name": name, "image": profile_image_url, "testimonials": all_testimonials})
