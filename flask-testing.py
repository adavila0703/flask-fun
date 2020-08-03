from flask import Flask, render_template, request
import connexion
import people

app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
