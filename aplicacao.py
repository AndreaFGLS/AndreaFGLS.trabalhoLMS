from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
        return render_template ('index.html')

@app.route('/detalhescurso')
def detalhescurso():
        return render_template ('detalhescurso.html')
        
app.run()