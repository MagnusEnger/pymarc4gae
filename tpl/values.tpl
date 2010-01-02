{% extends "html.tpl" %}
{% block content %}
<p>title: {{ title }}</p>
<p>uniformtitle: {{ uniformtitle }}</p>
<p>author: {{ author }}</p>
<p>isbn: {{ isbn }}</p>
<p>subjects: {{ subjects }}</p>
<p>addedentries: {{ addedentries }}</p>
<p>location: {{ location }}</p>
<p>notes: {{ notes }}</p>
<p>physicaldescription: {{ physicaldescription }}</p>
<p>publisher: {{ publisher }}</p>
<p>pubyear: {{ pubyear }}</p>
{% endblock %}