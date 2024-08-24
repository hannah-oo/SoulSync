from flask import Flask, render_template, request, abort, url_for
from flask_socketio import SocketIO
import json

from user import User

app = Flask(__name__)
socketio = SocketIO(app)

hashtags = {'depression', 'toxic', 'relationship', 'gay', 'bisexual',
            'breakup', 'breakdown', 'gender',
            'empty', 'failure', 'bodyshaming', 'domestic violence', 'anxiety', 'lonely', 'family', 'stressed'}

# groups = {1 : ['depressed', 'empty', 'breakdown', 'failure'],
#             2: ['boyfriend', 'relationship', 'girlfriend', 'breakup', 'ex'],
#             3: ['gender', 'gay', 'lesbian', 'bisexual'],
#             4: ['fat', 'bodyshaming']}


# index.html contains the first page pop up when users visit the website
# contains the options to login, register or be a guest
@app.route('/')
def index():
    return render_template('index.html')

# the main page with the map
@app.route('/home')
def home():
    return render_template('home.html', username=request.args.get('username'))

# login page
@app.route('/login')
def login():
    return render_template('login.html')

# process login when user clicks the login button -> trigger this function
@app.route('/login/user', methods=['POST'])
def login_user():
    if not request.is_json:
        abort(404)
    
    username = request.json.get("username")
    
    with open('data.json', 'r') as f:
        data = json.load(f)

    if username in data:
        return url_for('home', username=username)
    return "Username doesn't exist. Please try again or sign up."

# sign up page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# process signup when user clicks the signup button -> trigger this function
@app.route('/signup/user', methods=['POST'])
def signup_user():
    if not request.is_json:
        abort(404)
    
    username = request.json.get("username")
    location = request.json.get("location")
    
    with open('data.json', 'r') as f:
        data = json.load(f)

    if username not in data:
        user = User(username, location)
        return url_for('home', username=username)
    
    return "Username already exists"

# get all posts with the chosen hashtag
@app.route('/get_posts_by_hashtag', methods=['POST'])
def get_posts_by_hashtag():
    if not request.is_json:
        abort(404)
        
    hashtag = request.json.get("hashtag")
    with open('posts.json', 'r') as f:
        data = json.load(f)
        posts = data[hashtag]['posts']
    return url_for('/home', posts=posts)

# get the number of posts in each country
# @app.route('/get_posts_in_country', methods=['POST'])
# def get_posts_in_country():
#     if not request.is_json:
#         abort(404)
    
    

# see post made by yourself
# @app.route('/profile')
# def user_profile():
#     return render_template('user_profile')

# @app.route('/see_post_history', methods=['POST'])
# def see_post_history():
#     if not request.is_json:
#         abort(404)
        
#     username = request.json.get("username")
#     with open('user.json', 'r') as f:
#         data = json.load(f)
#         posts = data[username]['posts']
#     return url_for('/profile', posts=posts)

# redirect to the page for user to input their thoughts
@app.route('/input_thoughts')
def input_thoughts():
    return render_template('input_thoughts.html')

# handle when users click on "input" button in the thoughts input page
# add the post to both the json files
@app.route('/add_post', methods=['POST'])
def add_post():
    if not request.is_json:
        abort(404)
        
    username = request.json.get('username')
    post_content = request.json.get('post_content')
    hashtag = request.json.get('hashtag')
        
    # add to the user's history
    with open('user.json', 'r') as f:
        data = json.load(f)
        data[username]['posts'].append(post_content)
        
    with open('user.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    # add to the posts list
    with open('posts.json', 'r') as f:
        data = json.load(f)
        data[hashtag].append([username, post_content])
        
    with open('posts.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    return url_for('home', username=username)

if __name__ == '__main__':
    socketio.run(app)
    
    
# user clicks on a hashtag -> triggers this function to display the suggested hashtags
# @app.route('/suggesting', methods=['POST'])
# def suggesting():
#     if not request.is_json:
#         abort(404)

#     hashtag = request.json.get('hashtag')
#     suggested_hashtags = groups[hashtags[hashtag]]
#     return url_for('/', suggested_hashtags=suggested_hashtags)