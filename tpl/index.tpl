{% extends "html.tpl" %}
{% block content %}
<p>Paste in some MARC in ISO2709 format and click the button to save it and show options for what you can do with it.</p>
<form action="/saverecord" method="post">
<div><textarea name="marc" rows="20" cols="120"></textarea></div>
<div><input type="submit" value="Save MARC and show options"></div>
<div> - or - </div>
<div><select name="action">
<option value="">Select action...</option>
<option value="values">Values</option>
</select></div>
<div><select name="format">
<option value="">Select format...</option>
<option value="">HTML</option>
<option value="json">JSON</option>
<option value="pickle">pickle</option>
</select></div>
<div><input type="submit" value="and perform action without saving"></div>
</form>
{% endblock %}