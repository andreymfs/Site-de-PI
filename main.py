from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configuração da URL de conexão com o banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definição do modelo de dados para animais para adoção
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Animal {self.name}>'

# Rota para a página de adoção
@app.route('/adopt')
def adopt():
    animals = Animal.query.all()
    return render_template('adopt.html', animals=animals)

# Rota para adicionar um novo animal
@app.route('/add_animal', methods=['GET', 'POST'])
def add_animal():
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        age = request.form['age']
        description = request.form['description']

        new_animal = Animal(name=name, species=species, age=age, description=description)
        db.session.add(new_animal)
        db.session.commit()

        return redirect(url_for('adopt'))

    return render_template('add_animal.html')

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/user>")
def guest():
    return render_template('user.html')


if __name__ == "__main__":
    app.run(debug=True)