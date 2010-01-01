{% extends "html.tpl" %}
{% block content %}
<p>Record saved with key = {{ key }}.</p>
<p><a href="/record?key={{ key }}">Show options</a></p>
{% endblock %}