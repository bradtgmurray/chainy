from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseServerError, HttpResponseRedirect
from django.core.urlresolvers import reverse

from chainy_web.chainyapp.models import Chain, Post

def main(request):
    chain_list = Chain.objects.all()

    return render_to_response('chainyapp/templates/main.html', 
        {'chain_list' : chain_list})

def chains(request):
    if request.method == 'POST':
        try:
            new_chain_name = request.POST['name']
            c = Chain(name= request.POST['name'])
            c.save()

            redirect_url = reverse('chainy_web.chainyapp.views.main')
            return HttpResponseRedirect(redirect_url)
        except (KeyError):
            return HttpResponseServerError('name not specified')
    else:
        return HttpResponseServerError('Only allow POST to this page, NYI')

def chain(request, chain_id):
    if request.method == 'GET':
        chain = get_object_or_404(Chain, pk=chain_id)
    
        return render_to_response('chainyapp/templates/chain.html', 
            {'chain' : chain})

def post(request, chain_id, post_num):
    chain = get_object_or_404(Chain, pk=chain_id)
    post = get_object_or_404(Post, chain=chain_id, post_num=post_num)

    return render_to_response('chainyapp/templates/post.html',
        {'post': post})
