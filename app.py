from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/html_to_flask')
def form_data_to_flask_app():
    return render_template('content_to_flask.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dynamic_content')
def passing_content_to_html():
    """
    To test passing info from Backend to Front End
    """

    name = "Slim Shady"
    return f"Hi, My name is what? My name is who? My name is chika-chika {name}"


@app.route('/run', methods=['POST', 'GET']) # specificying POST is important, else you will get 'Method not allowed' error.
def run_suite_util():

  suite_name = request.form['suite'] # accessing variables from your form elements.
  build_url = request.form['build_url'] # notice, we are using the "name" attribute to access the values.
  host_url = request.form['host_url']

  print('The Suite that is going to be triggered is:',suite_name)
  print('The Suite that is going to be triggered is:',build_url)
  print('The Suite that is going to be triggered is:',host_url)

  example = [suite_name, build_url, host_url]
  return render_template('jinja_to_html.html', example=example)


if __name__ == "__main__":

    print('starting server')
    app.run(debug=True)
