from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    context = {
        'title': 'Главная',
        'heading': 'Добро пожаловать на главную страницу',
        'content': 'Это главная страница нашего Flask-приложения.'
    }
    return render_template('home.html', **context)

@app.route('/about')
def about():
    context = {
        'title': 'О нас',
        'heading': 'О нас',
        'content': 'Это страница "О нас" нашего Flask-приложения.'
    }
    return render_template('about.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
