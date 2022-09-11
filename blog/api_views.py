import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from blog.models import Post


def post_to_dict(post):
    return {
        "pk": post.pk,
        "created_date": post.created_date,
        "published_date": post.published_date,
        "title": post.title,
        "slug": post.slug,
        "text": post.text,
    }


@csrf_exempt
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        posts_as_dict = [post_to_dict(p) for p in posts]
        return JsonResponse({"data": posts_as_dict})
    elif request.method == "POST":
        post_data = json.loads(request.body)
        post = Post.objects.create(**post_data)
        return HttpResponse(
            status=HTTPStatus.CREATED,
            headers={"Location": reverse("api_post_detail", args=(post.pk,))},
        )

    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":
        return JsonResponse(post_to_dict(post))
    elif request.method == "PUT":
        post_data = json.loads(request.body)
        for field, value in post_data.items():
            setattr(post, field, value)
        post.save()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)
    elif request.method == "DELETE":
        post.delete()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])
