from django.shortcuts import render
import markdown

def md_to_html(request):
    with open('/home/naga/djangogirls/templates/blog/a.md') as f:
        a = f.read()
        md = markdown.Markdown()
        b = md.convert(a)
    with open('/home/naga/djangogirls/templates/blog/a.html', 'w') as f:
        f.write(b)
    return render(request, 'blog/a.html', {})


def html(request):
    return render(request, 'blog/post_list.html')
