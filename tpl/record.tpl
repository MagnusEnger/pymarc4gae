{% extends "html.tpl" %}
{% block content %}
<ul>
<li><a href="/marcxml?key={{ key }}">MARCXML</a></li>
<li><a href="/mnem?key={{ key }}">Mnemonic format</a></li>
</ul>

<!-- key: {{ key }} -->
<!-- {{ marc }} -->

{% endblock %}