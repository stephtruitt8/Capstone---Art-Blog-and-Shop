from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.

def blog_view(request):
    blog_posts = [
        {
            "title": "Finding Inspiration in Everyday Places",
            "category": "Studio Notes",
            "image": "img/images/blog1.jpg",
            "preview": "A short look into where creative ideas can come from.",
            "body": "Full blog post content goes here."
        },
        {
            "title": "Behind the Sketch",
            "category": "Process",
            "image": "img/images/blog2.jpg",
            "preview": "A look into rough ideas, sketches, and visual planning.",
            "body": "Full blog post content goes here."
        },
        {
            "title": "Why Story Art Matters",
            "category": "Story Art",
            "image": "img/images/blog3.jpg",
            "preview": "How characters, scenes, and emotions shape visual storytelling.",
            "body": "Full blog post content goes here."
        },
        {
            "title": "New Shop Ideas",
            "category": "Shop Update",
            "image": "img/images/blog4.jpg",
            "preview": "A preview of possible prints, apparel, and stickers.",
            "body": "Full blog post content goes here."
        },
        {
            "title": "Building BartoArts",
            "category": "Website",
            "image": "img/images/blog5.jpg",
            "preview": "Thoughts on building the site and shaping the brand.",
            "body": "Full blog post content goes here."
        },
        {
            "title": "Creative Motivation",
            "category": "Reflection",
            "image": "img/images/blog6.jpg",
            "preview": "A reminder to keep creating even when the process feels slow.",
            "body": "Full blog post content goes here."
        },
    ]

    paginator = Paginator(blog_posts, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/blog.html", {"page_obj": page_obj})