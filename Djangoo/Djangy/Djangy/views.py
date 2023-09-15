from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("hellllo")
    return render(request, "index.html" )
    

def contact(request):
    request.POST.get('text', 'default')
    return render(request,"dev.html")

def about(request):

    return render(request, "prac.html")

def login(request):
    punctuation= '''~`#,^*-{]'."/\?:\=-)(*&%$#@!~_+|\?><,.:"{}[]);'''
    hidden_text=request.POST.get('text', 'default')

    tick = request.POST.get('check', 'off')
    tick1 = request.POST.get('check1', 'off')
    tick2 = request.POST.get('check2', 'off')
    tick3 = request.POST.get('check3', 'off')
    tick4 = request.POST.get('check4', 'off')
    if tick == 'on': 
        value=''
        for char in hidden_text:
            if char not in punctuation:
                value = value + char
        params = {'key':value,'chk':'box'}
        hidden_text = value
        # return render(request, 'analyze.html', params)
       
    if tick1 == 'on': 
        value=''
        for char in hidden_text:
            if char != '\n' and char!= '\r' :
                value = value + char 
        params = {'key':value,'chk':'box'}
        hidden_text = value
        # return render(request, 'analyze.html', params)
    
    if tick2 == 'on': 
        value=''
        for char in hidden_text:
            value= value + char.upper()
        # for char2 in value:
        #         value = value + char2.upper()
        params = {'key':value,'chk':'box'}
        hidden_text = value
        # return render(request, 'analyze.html', params)
    
    if tick3 == 'on': 
        value=''
        for index, char in enumerate(hidden_text):
            if not(hidden_text[index] == " " and hidden_text[index + 1]) == " ":
              value = value + char
        params = {'key':value,'chk':'box'}
        hidden_text = value
        # return render(request, 'analyze.html', params)
    
    if tick4 == 'on': 
        value=len(hidden_text)
        params = {'key':value,'chk':'box'}
        hidden_text = value
        # return render(request, 'analyze.html', params)
    
    if tick != 'on' and tick1 != 'on' and tick2 != 'on' and tick3 != 'on' and tick4 != 'on' :
        return HttpResponse("select any option..")


    
    return render(request, 'analyze.html', params)