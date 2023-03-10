from flask import Flask, render_template, url_for, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('data.db', check_same_thread=False)

conn.execute('''CREATE TABLE IF NOT EXISTS dados
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            x INTEGER,
            y INTEGER,
            z INTEGER,
            r INTEGER)''')

@app.route('/')
def index():
    cursor = conn.cursor()
    cursor.execute('SELECT id, x, y, z, r FROM dados ORDER BY id DESC LIMIT 1')
    ultima_linha = cursor.fetchone()
    x = ultima_linha[1]
    y = ultima_linha[2]
    z = ultima_linha[3]
    r = ultima_linha[4]
    return render_template('index.html', x=x, y=y, z=z, r=r)

@app.route('/rota', methods=['POST'])
def rota():
    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    r = request.form['r']
    conn.execute('INSERT INTO dados (x, y, z, r) VALUES (?, ?, ?, ?)', (x, y, z, r))
    conn.commit()
    return "Dados inseridos com sucesso"

# @app.teardown_appcontext
# def encerrar_conexao(exception):
#     conn.close()

if __name__ == '__main__':
    app.run(debug=True)
