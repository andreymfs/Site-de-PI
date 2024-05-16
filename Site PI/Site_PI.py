from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():

    # Suponha que você tenha uma lista de imagens para exibir no carrossel
    images = [
        'img1.jpg',
        'img2.jpg',
        'img3.jpg'
    ]
    return render_template('index.html', images=images)

# Rota para a página "Sobre nós"
@app.route('/about')
def about():
    return render_template('about.html')

# Rota para a página de adoção de animais
@app.route('/adopt')
def adopt():
    return render_template('adopt.html')

# Rota para a página de doação
@app.route('/donate')
def donate():
    return render_template('donate.html')

if __name__ == '__main__':
    app.run(debug=True)
