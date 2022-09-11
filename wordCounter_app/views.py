from django.shortcuts import render, redirect
from django.http import JsonResponse


# create views
def home(request):
    # if request.method == "POST":
    #     text = request.POST['text']
    #     if text != "":
                
    #         word = len(text.split())
    #         char_with_space = len(text)
    #         char_without_space = char_with_space - text.count(" ")
    #         sentense = text.count(".")
    #         i = True

    #     else:
    #         return redirect("/")

    # else:
    #     return redirect("/")
    
    # context = {
    #     'text':text,
    #     'word':word,
    #     'char_with_space':char_with_space,
    #     'char_without_space':char_without_space,
    #     'sentence':sentense,
    #     'i':i,
    # }
    return render(request, 'home.html')


def blog(request):
    return render(request, 'blog.html')


def ajax_posting(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name != " ": #cheking if first_name and last_name have value
            # count_char = len(name)
            # count_word = len(name.split())
            word = len(name.split())
            char_with_space = len(name)
            char_without_space = char_with_space - name.count(" ")
            sentense = name.count(".")
            response = {
                'word':word,
                'char_with_space':char_with_space,
                'char_without_space':char_without_space,
                'sentense':sentense,
            }
            return JsonResponse(response) # return response as JSON
