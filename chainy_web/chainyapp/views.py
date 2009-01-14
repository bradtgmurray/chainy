from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from chainy_web.chainyapp.models import Chain, Post

def main(request):
    chain_list = Chain.objects.all()

    return render_to_response('chainyapp/templates/main.html', 
        {'chain_list' : chain_list})

def chain(request, chain_id):
    chain = get_object_or_404(Chain, pk=chain_id)
    
    return render_to_response('chainyapp/templates/chain.html', 
        {'chain' : chain})

def post(request, chain_id, post_num):
    chain = get_object_or_404(Chain, pk=chain_id)
    post = get_object_or_404(Post, chain=chain_id, post_num=post_num)

    return render_to_response('chainyapp/templates/post.html',
        {'post': post})
