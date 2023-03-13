from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    Capatilze = request.POST.get('Capatilze', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''





    # Capitalize the given Text

    if Capatilze == 'on':
        analyze = ''
        for char in djtext:
            analyze = analyze + char.upper()

        params = {
            'analyze': 'Capitalize',
            'result': analyze,
        }
        print(djtext, Capatilze)
        djtext = analyze
        # return render(request, 'analyze.html', params)


    # Remove Puncuation

    if removepunc == 'on':
        analyze = ''
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char

        params = {
            'analyze': 'Remove Puncuations',
            'result': analyze,
        }
        djtext = analyze
        # return render(request, 'analyze.html', params)



    # New Line Remove
    if newlineremove == 'on':
        analyze = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyze = analyze + char


        params = {
            'analyze' : 'New Line Remove',
            'result' : analyze
        }
        djtext = analyze
        # return render(request, 'analyze.html', params)

    # Space Remove
    if spaceremove == 'on':
        analyze = ''
        for index , char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyze = analyze + char
        params = {
            'analyze': 'Extra Space Remover',
            'result': analyze
        }
        djtext = analyze
        # return render(request, 'analyze.html', params)


    # Character Count
    if charcount == 'on':
        analyze = ''
        count = 0
        for i in djtext:
            count = count + 1

        analyze = count
        params = {
            'analyze': 'Count Total number of Character',
            'result': "Total number of character in the string is : " + str(analyze)
        }
    if (Capatilze != 'on' and removepunc != 'on' and newlineremove != 'on' and spaceremove != 'on' and charcount != 'on'):
        return HttpResponse("Plesase Select any operation and try again!")

    return render(request, 'analyze.html', params)
