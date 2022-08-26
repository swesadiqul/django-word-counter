from django.shortcuts import render, redirect


# create views
def home(request):
    if request.method == "POST":
        text = request.POST['text']
        if text != "":
                
            word = len(text.split())
            char_with_space = len(text)
            char_without_space = char_with_space - text.count(" ")
            sentense = text.count(".")
            i = True

        else:
            return redirect("/")

    else:
        return redirect("/")
    
    context = {
        'text':text,
        'word':word,
        'char_with_space':char_with_space,
        'char_without_space':char_without_space,
        'sentence':sentense,
        'i':i,
    }
    return render(request, 'home.html', context)


def blog(request):
    return render(request, 'blog.html')
