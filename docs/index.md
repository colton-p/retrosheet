---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

### retrosheet diversions

<ul>
{% for page in site.pages %}
<li>
<a href="{{page.url | relative_url}}">
{{page.title}}
</a>
</li>
{% endfor %}
</ul>
