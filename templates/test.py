from flask import Flask, render_template

app = Flask(__name__)


@app.route('/dynamic_content')
def passing_content_to_html():
    """
    To test passing info from Backend to Front End
    """
    name = "Slim Shady"
    return f'Hi, My name is what? My name is who? My name is chika-chika {name}'

@app.route('/html_to_flask')
def form_data_to_flask_app():
    return render_template('content_to_flask.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":

    print('starting server')
    app.run()
