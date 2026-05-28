from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.


BLOG_POSTS = [
    {
        "slug": "finding-inspiration",
        "title": "How to Find Inspiration",
        "category": "Art",
        "content": "",
        "video_url": "https://youtu.be/cq3QBKbHUro?si=_zhd2rWjT13EAQrX",
        "preview": "A small reflection on how ordinary moments can turn into creative ideas.",
        "body": """

Please watch this video for some random inspiration!

Inspiration can come from places we do not always expect: a walk outside,
a conversation, a song, a sketch, or even a quiet moment.

Art does not always begin with a perfect idea. Sometimes it begins with
paying attention to small moments and letting them grow into something bigger.
"""
    },
    {
        "slug": "behind-the-sketchbook",
        "title": "Behind the Sketchbook",
        "category": "Process",
        "image": "img/images/project2.png",
        "preview": "A look into the messy, fun, and personal process behind creating art.",
        "body": """
The sketchbook is where ideas are allowed to be imperfect. It is a place
for testing, exploring, failing, and finding the shape of something new.

Before an artwork becomes finished, it usually starts as a loose thought,
a messy drawing, or a small idea worth following.
"""
    },
    {
        "slug": "building-a-creative-world",
        "title": "Building a Creative World",
        "category": "Story",
        "image": "img/images/project3.png",
        "preview": "Notes on storytelling, characters, imagination, and building visual worlds.",
        "body": """
A creative world is built through details: characters, colors, places,
conflicts, emotions, and the feeling you want people to remember.

Story art gives viewers something to wonder about. It creates the feeling
that there is more happening beyond the image.
"""
    },
    {
        "slug": "creating-with-purpose",
        "title": "Creating With Purpose",
        "category": "What's Your Vision?",
        "image": "img/images/project4.png",
        "preview": "A reminder to think about the feeling, message, and direction behind your work.",
        "body": """
Vision gives your art direction. It does not mean you need everything
figured out right away.

It simply means asking what you want the piece to say, feel like, or become.
Purpose can help guide your choices, from color and shape to character and mood.
"""
    },
    {
        "slug": "staying-creative-when-life-gets-loud",
        "title": "Staying Creative When Life Gets Loud",
        "category": "Focus Talk",
        "image": "img/images/project5.png",
        "preview": "Thoughts on focus, creative patience, and returning to your work.",
        "body": """
Creativity takes focus, but focus does not always mean forcing yourself.

Sometimes it means slowing down, clearing space, and giving yourself permission
to return to the work one step at a time. Even small progress still counts.
"""
    },
    {
        "slug": "letting-go-of-perfect-art",
        "title": "Letting Go of Perfect Art",
        "category": "Should You Be Perfect?",
        "image": "img/images/project6.png",
        "preview": "A short reflection on why progress matters more than perfection.",
        "body": """
Perfect art can become a trap. Growth happens when you allow yourself to make
things, learn from them, and keep moving.

A finished imperfect piece can teach more than an idea that never leaves your head.
Progress gives you something real to build from.
"""
    },
]

def blog_view(request):

    paginator = Paginator(BLOG_POSTS, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/blog.html", {"page_obj": page_obj})

def blog_detail(request, slug):
    post = next((post for post in BLOG_POSTS if post["slug"] == slug), None)

    if post is None:
        return render(request, "blog/blog_404.html", status=404)

    return render(request, "blog/blog_detail.html", {"post": post})