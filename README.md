# Workshop-Flask

## Environement Virtuel
on ouvre un terminal:  
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

(Pour le désactiver, simplement: deactivate)  
  
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

Pour que cela fonctionne, dans le fichier "todo.py", nous se dirige dans render_template qui se trouve dans la route et nous allons remplacer le "layout.html" par "index.html".  

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
mais d'où vient se tasks ? eh bien pour le moment il ne le sait pas (vous avez sûrement eu un message d'erreur !) pour que render_template ai accès à la lise que l'on à déclarer il y a deux minutes, il faudra simplement le lui spécifier comme ceci:  

```python
@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html', tasks=tasks)
```  

il vous faudra peut-être redémarer votre serveur suite à votre message d'erreur (dans le terminal ctrl+c et ensuite on retape python3 todo.py) mais on peut déjà voir à quoi vas ressembler le projet final. Le problème c'est que pour le moment, notre appliquation n'est pas du tout utilisable car il nous manque le plus important !

## Aussi léger qu'une base de données

Vous vous souvenez de la partie goûte à goûte ? c'est ici qu'elle prend son sens. Pour pouvoir utiliser facilement une base de donnée avec flask, surtout en phase de production, il existe un add-on super efficace: SQL Alchemy !

vous l'avez déjà installer dans votre environement virtuel tout à l'heure, maintenant il ne nous reste plus qu'à l'importer pour pouvoir l'utiliser.

Tout au dessus de notre fichier "todo.py" on vas ajouter :

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
```  

Maintenant qu'il est importer on vas l'initialiser et lui dire où elle se trouve en ajoutant juste en dessous de notre app: 

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)
```

vous devriez donc avoir un code qui ressemble à ceci:

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


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


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
```

Maintenant on vas donner forme à la table de notre base de donnée en ajoutant ce bout de code en dessous de l'initialisation de notre base de donnée:

```python 
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    text = db.Column(db.String(200))
```

Ensuite, on se rend dans la console à la racine de notre projet et on indique:

`sqlite3 todo.db`

une fois dans la base de donnée, pour pouvoir la "créer" on indique:

`.tables`

à ce niveau rien ne se passe dans le terminal, mais si on regarde dans notre dossier, un nouveau fichier nommé todo.db vient d'apparaitre. Pour sortir de sqlite3 on indique:

`.exit`

c'est bien, il y a une base de donnée, mais ce n'est pas encore la notre à proprement parler. Pour ca, toujours dans le terminal, on entre dans la console python 

`python3`

et ensuite:

`from todo import db`

et enfin:

`db.create_all()`

et on sors de la console.

`exit()`

Pour l'instant rien ne nous indique que notre base de donnée soit bien faite, alors allons vérifier par nous même ! toujours dans le terminal:

`sqlite3 todo.db`

une fois dans la base de donnée, lorsque l'on fais

`.tables`

la console doit normalement nous retourner le nom de la table que nous avons créer plus tôt: Todo

une fois vérifier, on peux simplement quitter la base de donnée en faisant un simple

`.exit`


## on a une base de donnée et un formulaire ....

Dans le code que l'on à copier dans le fichier "index.html" se trouve un formulaire. Pour l'instant celui ci ne redirige vers rien, mais nous allons nous en charger !

Tout d'abords nous allons ajouter à notre flask trois modules qui vont nous être très utile: redirect, request, url_for. Leurs nom sont assez explicite non ? 

on vas donc les ajouter tout au dessus de votre fichier "todo.py", comme ceci:

```python
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
```

Comme tout bon dev, nous allons traiter les information de manières invisible. pour celà nous allons devoir rediriger notre formulaire vers une autre page. Et pour créer une autre page avec flask, il suffit simplement de créer une autre route !

en dessous du notre première route, nous allons donc ajouter ceci:

```python 
@app.route('/add')
def add():
    
```

Simple, n'est-ce pas ?

La prochaine étape consiste à rediriger vers cette page lorsque l'on clique sur le bouton du formulaire. pour ce faire, on vas cette fois sur le fichier "index.html" et dans l'attribut href de notre formulaire on indique:

`href="{{ url_for('add') }}"`

ca suffira à faire rediriger vers notre page "add". A notter qu'ici l'argument que l'on passe dans la fonction url_for() est le nom de la fonction de nottre route et non pas la route elle même !

Pour l'instant, c'est bien beau on redirige vers la page, mais il ne se passe rien ! Pour remédier à ca on se redirige vers notre fichier "todo.py" et on vas y ajouter deux trois petite choses. 

Premièrement, il faut indiquer à notre route qu'elle peut accepter les requêtes de type POST (celle que l'on utilise avec notre formulaire).

sur la route de notre page "add" on vas indiquer:

```python
@app.route('/add', methods=['POST'])
def add():
```

Maintenant que ca c'est fait, il faut traiter les données que l'on récupère avec ce formulaire. Pour ce faire on vas étoffé notre fonction:

```python
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        task = Todo(title=request.form['title'], text=request.form['text'])
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
```

si ce bout de code vous fait peur, pas de panique, je vais vous l'expliquer:

Quand on est redirigé vers la page add à l'aide du formulaire:

- On vérifie qu'on est bien arrivé là par une requête POST (on ne sais jamais)
- On assigne dans une variable les données du formulaire spécialement formatée pour notre base de donnée
- On ajoute ces données à notre base de donnée 
- Et on commit 

Sinon on redirige vers la page index


C'est plutôt pas mal pour le moment, si on oublie le fait qu'on affiche pas les bonnes données dans la page ! 

Pour réglé le problème il vas faloir d'abord passer les données de notre base de donnée dans notre route:

```python
@app.route('/')
@app.route('/home')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)
```

une fois que ca c'est fait, on retourne vers notre fichier "index.html" et on remplace le code que l'on y avait ajouter par:

```html
% for todo in todos %}
                <div class="card">
                    <div class="card-body text-left">
                        <h3 class="card-title font-weight-bold">{{todo.title}}</h3>
                        <p class="card-text">{{todo.text}}</p>
                        <a href="#" class="text-small font-weight-light text-muted"">delete this task</a>
                    </div>
                </div>
            {% endfor %}
```

Ce qui fait que l'on devrait avoir ceci comme code: [pour todo](todo.py) et [pour index](index-2.html)


## Supprimer des éléments de la base de donnée.



