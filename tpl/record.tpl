{% extends "html.tpl" %}
{% block content %}
<ul>
<li><a href="/marcxml?marc={{ marc|urlencode }}">MARCXML</a></li>
</ul>
{% endblock %}