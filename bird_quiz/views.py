from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Bird

import json, http.client, urllib.request, urllib.parse, urllib.error, base64, random





def index(request):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '52e1f43aa3114e8b924af3f84693877b',
    }

    result_id = random.randrange(10)
    random_index = 0#random.randint(0, Bird.objects.count() - 1)
    correct_bird = Bird.objects.all()[random_index].common_name
    correct_index = random.randint(0, 4)
    wrong_indices = []
    choices = []

    for i in range(0,4):
        found_unique = False
        while not found_unique:
            check_index = random.randint(0, Bird.objects.count() - 1)
            if (check_index != random_index) and not (check_index in wrong_indices):
                wrong_indices.append(check_index)
                found_unique = True
                choices.append(Bird.objects.all()[check_index].common_name)


    print(len(choices))
    choices.insert(correct_index, correct_bird)
    print(len(choices))


    params = urllib.parse.urlencode({
        # Request parameters
        'q': correct_bird,
        'count': '10',
        'offset': '0',
        'mkt': 'en-us',
        'safeSearch': 'Moderate',
    })

    img_url = ""


    try:
        conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        parsed_data = json.loads(data)
        img_url = (parsed_data['value'][result_id]['thumbnailUrl'])
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    context = {
        'choices' : choices,
        'correct_index' : correct_index,
        'img_url' : img_url,
    }
    return render(request, 'bird_quiz/index.html', context)

def question(request):
    return HttpResponse("You're looking at a question")


