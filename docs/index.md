---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<ul>
{% for page in site.pages %}
    <li>
        <a href="{{page.url}}">{{page.title}}</a>
    </li>
{% endfor %}
</ul>
