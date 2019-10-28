from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
        return render_template ('index.html')

@app.route('/detalhescurso')
def detalhescurso():
        return render_template ('detalhescurso.html')

@app.route('/disciplina')
def disciplina():
        return render_template ('disciplina.html')

@app.route('/listacurso')
def listacurso():
        return render_template ('listacurso.html')

@app.route('/noticias')
def noticias():
        return render_template ('noticias.html')

app.run()
