from django.shortcuts import render, HttpResponse
from django.views.generic import View

# Create your views here.
class Message(View):
    def get(self, request):
        print('Message#get')
        context = {}
        return render(request, 'messages/index.html', context)

    def post(self, request):
        print('Message#post')
        print(request.POST['message_text'])
        return HttpResponse('<h1>Message submitted {}</h1>'.format(request.POST['message_text']))

