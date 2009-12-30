{% extends "html.tpl" %}
{% block content %}
<p>Paste in some MARC in ISO2709 format and click the button to get back MARCXML.</p>
<form action="/record" method="get">
<div><textarea name="marc" rows="20" cols="120"></textarea></div>
<div><input type="submit" value="Create MARCXML"></div>
</form>
{% endblock %}