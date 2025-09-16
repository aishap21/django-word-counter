from django.shortcuts import render
import operator


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'mainpage.html')


def counter(request):
    text = request.POST.get('text', '')
    wordlist = text.split()
    freq_counter = {}

    # Remove special characters and lowercase all words
    clean_wordlist = []
    for word in wordlist:
        clean_word = ""
        for char in word.lower():
            if char.isalnum():
                clean_word += char
        if len(clean_word) > 0:
            clean_wordlist.append(clean_word)

    # Count number of occurrences
    for word in clean_wordlist:
        if word in freq_counter:
            freq_counter[word] += 1
        else:
            freq_counter[word] = 1

    # Convert dictionary to a reverse sorted list.
    freq_list = sorted(freq_counter.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'countresults.html', {'text': text, 'length': len(clean_wordlist), 'freq': freq_list})
