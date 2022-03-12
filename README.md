# Pantry Application

<h1>The Pantry</h1>
<p>Contributors: Derek Li & Lukas Nam</p>
<ul>Stack:
<li>HTML</li>
<li>CSS/Bootstrap</li>
<li>Javascript/JQuery</li>
<li>Django</li>
</ul>
<p>We developed a web application that lets users store ingredients provided to us by spoonacular's API into a "pantry" and will let the user and other users see what your pantry has. Selecting items in the pantry will fetch 2 recipes (hard-coded in fetch) and ingredients missing.</p>

<br>
<p>Since we are using an internal database to start off our ingredients database, I have provided the uncleaned .csv file and a csvtosql.py file which uses the SQLAlchemy module to export the cleaned data onto SQL. This poses a new problem, as you will likely get a foreign key relation error afterwards. What you need to do in this situation is:</p>

```
python manage.py syncdata
```

<p>This will sync our django's database to our server-side database. This poses the next issue, which revolved around the fact that the "cleaned data" is split with ingredient name and ingredient id where the ingredient id column imported is not the <b>primary key</p>, which affects the foreign key from my pantry models. A quick solve would be to go to the ingredient table in your database GUI and change the ID field to be a unique primary key. After this your ingredients table should be set and you can run:</p>

<p>PS: If you have previously messed with the models, you might want to consider deleting thepantry's migration files first before you makemigrations</p>

```
python manage.py makemigrations thepantry
python manage.py migrate
```

