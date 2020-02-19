# Workshop-Flask

## Environement Virtuel
` ctrl + alt + t `  
Vérifier la version de python:  
` python3 -V`  
Installer le seteur d'environement:  
`sudo apt install python3-venv `  
Créer le dossier de votre projet:  
` mkdir flask-todo`  
Dans le dossier du projet:  
` python3 -m venv todo-env`  
Activation de l'environement virtuel Python:  
` source todo-env/bin/activate `  
(Pour le désactiver: deactivate)  
  
## Autre installations recquises  
Installation SQLite  
` sudo apt install sqlite3`  
Installation Flask:  
` pip install flask`  
Installation SQLAlchemy:    
` pip install flask_sqlalchemy`  

## Une application en 7 lignes  
Création du fichier todo.py:  
` touch todo.py`  
Ouvrez le dossier dans VsCode.
Copiez/collez ce code dans le fichier todo.py:  
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run() 
```  
Une fois dans le dossier du projet dans le terminal :  
` python3 todo.py`  

## Début du projet, les templates  

Pour pouvoir utiliser render_template, il faut l'importer.  
Tout au dessus de todo.py, notez :  
```python
from flask import Flask, render_template
```  
Dans la route, changez le nom de la fonction et appelez la "index". Ensuite, au lieu de return une string on va return "render_template("layout.html).  
Vous devriez avoir ce code la :  
```python
@app.route("/")
@app.route("/home")
def index():
    return render_template("layout.html")
```  
Pour le moment on essaye d'utiliser quelque chose qui n'existe pas... du coup, créons le !  

Création d'un dossier "templates" dans lequel on va créer un fichier "layout.html".  
Dans le fichier "layout.html" écrivez :  
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
<title>Todo</title>
</head>
<body>

<!-- __________ HEADER _________________ -->

<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="{{ url_for('index') }}">Todo</a>
</nav>


<!-- __________ CONTENT _________________ -->

{% block content %} {% endblock %}



<!-- __________ FOOTER _________________ -->


<footer class="page-footer font-small blue bg-light ">
  <div class="footer-copyright text-center py-3">
    <p>made with love by <a href='https://github.com/Louis-vd'><strong>Louis Van Driessche</strong></a> and <a href='https://github.com/MickyCompanie'><strong>Micky Companie</strong></a> for our workshop at <a href='https://becode.org/webdev/'><strong>Becode</strong></a></p>
  </div>
</footer>

<!-- __________ SCRIPTS _________________ -->

<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" 
integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" 
integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" 
integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

</body>
</html>
```
Pour le moment, nous n'avons qu'un header et un footer. Mais grace à render_template, nous allons pouvoir rendre ca beaucoup plus intéressant.  
Dans le dossier template, nous allons créer un fichier "index.html". Dans lequel nous allons écrire :  
```html
{% extends 'layout.html' %}
{% block content %}
<div class="container my-5 py-5">

    <!-- card things to do  -->

        <div class="card text-center">
            <!-- card-header  -->
            <div class="card-header">
            Things To Do
            </div>

    <!-- Block à ajouter ensuite -->

      
        </div>
    

    <!-- formulaire pour ajouter des tâches -->

    <div class="card text-center">
    <div class="card-body">
        <p class="card-text">add your own task!</p>
        <form action="" method="POST">
            <div class="my-1">
            <input class="form-control form-control-lg" required="true" type="text" placeholder="Task's title" name="title">
            </div>
            <div class="my-1">
            <input class="form-control form-control-lg" required="true" type="text-area" placeholder="Task's text" name="text"> 
            </div>
            <div class="mt-3">
            <input type="submit" value="submit" class="btn btn-primary">
            </div>
        </form>
    </div>
    <!-- footer de la carte  -->
    <div class="card-footer">
    </div>
    </div>
</div>
{% endblock content %}

```
Pour que cela fonctionne, dans le fichier "todo.py", nous allons dans render_template qui se trouve dans la route et nous allons remplacer le "layout.html" par "index.html".  

## Afficher des données  

Pour afficher des données dans notre page c'est très simple. On va tout d'abord créer ces données dans notre page "todo.py" :  
```python
tasks = [
{
'title' : 'bonjour',
'text' : 'ca vas ?'
},
{
'title' : 'oui',
'text' : 'et toi ?'
}
]
```
Pour les afficher dans notre page, nous allons ajouter au fichier "index.html", sous le commentaire "Block à ajouter ensuite" :  
```html
            {% for task in tasks %}
                <div class="card">
                    <div class="card-body text-left">
                        <h3 class="card-title font-weight-bold">{{task.title}}</h3>
                        <p class="card-text">{{task.text}}</p>
                        <a href="#" class="text-small font-weight-light text-muted"">delete this task</a>
                    </div>
                </div>
            {% endfor %}
```










