from django.http import HttpResponse

def main(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def chain(request, chain_id):
    return HttpResponse("Viewing chain detail " + chain_id)
