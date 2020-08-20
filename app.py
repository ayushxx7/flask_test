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


@app.route('/about', methods=['POST'])
def about_me():
  '''
  Since our form's action is set to trigger '/about' endpoint,
  this function will be triggered on form submission.

  To access the form data we use the request module imported from Flask.
  The format is:
  element_name = request.form['name_attribute_of_the_element_in_the_form']
  '''
  name = request.form['my_name']
  choice = request.form['dd']
  reason = request.form['reason']
  first_number = request.form['first_number']
  second_number = request.form['second_number']
  sum_first_second = int(first_number)+int(second_number)

  sentence = f'My name is {name} and I would rather have {choice} because {reason}. The machine says, that the sum of the numbers entered is: {sum_first_second} and I certainly agree with it.'
  return sentence

if __name__ == "__main__":
    print('starting server')
    app.run(debug=True)
