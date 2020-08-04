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


tweet_dict = {
              '101':'Hi, I am a tweet! My ID is 101!',
              '102':'Hi, I am also a tweet! My ID is 102!',
              '103':'I think therefore I am - Rene Descartes. (103)!'
              }

@app.route('/show_tweet/<string:tweet_id>', methods=['GET'])
def get_tweet_via_tweet_id(tweet_id='0'):
    """
    To fetch tweet from the server based on tweet ID and display if ID exists.

    Params:
      tweet_id: Agent Email ID that will be enabled.

    Return:
      <HTML Response of Tweet>
    """

    if tweet_id in tweet_dict:
        tweet = tweet_dict[tweet_id]
    else:
        tweet = "This tweet has been deleted!"

    return f"<h1>{tweet}</h1>"


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
