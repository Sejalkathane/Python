python app.py
       │
       ▼
Create Flask App
       │
       ▼
Register Route "/"
       │
       ▼
Start Flask Server
       │
       ▼
Browser requests:
http://127.0.0.1:5000/
       │
       ▼
@app.route('/')
       │
       ▼
index()
       │
       ▼
render_template('index.html')
       │
       ▼
Browser displays index.html



# some imp in html
* The code in your index.html is Jinja2 Template syntax. Jinja2 is the template engine used by Flask to generate dynamic HTML.

* 
Normally, HTML is static.
<h1>Hello World</h1>
-----------------------------------
* <h1>Hello {{ name }}</h1> => html
* name = "Sejal"  => python
* The browser displays == Hello Sejal


<!-- ========================================================= -->


#  {{ }}  Used to display data (variables).
* <h1>{{ name }}</h1>
* return render_template("index.html" , name="Sejal")
* Output: <h1>Sejal</h1>

# {% %} : Used for logic or instructions, not for printing.
* {% if %}  :::: Used to check a condition and display HTML only if the condition is true.
Syntax
{% if condition %}
    HTML code
{% endif %}


* {% for %} :::  Used to loop through a list, tuple, dictionary, etc.
Syntax
{% for item in items %}
    HTML
{% endfor %}


* {% extends %} ::: Used for template inheritance. It tells Flask that the current HTML file should inherit from another template (usually base.html).
Syntax
{% extends "base.html" %}


* {% block %} ::: Defines a section that child templates can replace or fill.
Syntax
{% block body %}
{% endblock %}


<!-- ========================================================= -->



