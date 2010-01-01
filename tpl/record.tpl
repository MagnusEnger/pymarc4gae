{% extends "html.tpl" %}
{% block content %}
<p>Full record</p>
<ul>
<li><a href="/marcxml?key={{ key }}">MARCXML</a></li>
<li><a href="/mnem?key={{ key }}">Mnemonic format</a> (plain text)</li>
<li><a href="/iso?key={{ key }}">ISO2709</a> (plain text)</li>
</ul>
<p>Bits and pieces</p>
<ul>
<li><a href="/author?key={{ key }}">Author</a> <a href="/author?format=json&key={{ key }}">JSON</a></li>
</ul>

<!-- key: {{ key }} -->
<!-- {{ marc }} -->

{% endblock %}