from flask import Flask, render_template, jsonify, request, abort, url_for, redirect
from flask_socketio import SocketIO
import json

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
def welcome():
    return render_template('welcome.html')

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
    
    with open('user.json', 'r') as f:
        data = json.load(f)
    if username in data:
        return redirect(url_for('home', username=username))
    return "Username doesn't exist. Please try again or sign up."

@app.route('/signup')
def signup():
    return render_template('signup.html')

# process signup when user clicks the signup button -> trigger this function
@app.route('/signup/user', methods=['POST'])
def signup_user():
    if not request.is_json:
        abort(404)
    
    username = request.json.get("username")
    country = request.json.get("country")
    with open('data.json', 'r') as f:
        data = json.load(f)

    if username not in data:
        with open('user.json', 'r') as f:
            data = json.load(f)
        
        with open('user.json', 'w') as f:
            data[username] = {'country': country,
                              'posts': []}
            json.dump(data, f, indent=4)
        return redirect(url_for('home', username=username))
    
    return "Username already exists"

@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')

# @app.route('/read_data', methods=['POST'])
# def read_data():
#     file_path = 'SoulSync/posts.json'
#     with open(file_path, 'r') as json_file:
#         data_dict = json.load(json_file)
#     # print(data_dict)
#     return redirect(url_for('home', data_dict))

# @app.route('/coordinates')
# def get_coordinates():
#     return jsonify(coordinates)

# get all posts with the chosen hashtag
# @app.route('/get_posts_by_hashtag', methods=['POST'])
# def get_posts_by_hashtag():
#     if not request.is_json:
#         abort(404)
        
#     hashtag = request.json.get("hashtag")
#     with open('posts.json', 'r') as f:
#         data = json.load(f)
#         posts = data[hashtag]['posts']
#     return redirect(url_for('/home', posts=posts))

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
# when user clicks on the button to create a new post or filter posts by hashtag
# @app.route('/create_post')
# def create_post():
#     return render_template('post.html', username='Anna')

# handle when users click on "input" button in the thoughts input page
# add the post to both the json files
# @app.route('/add_post', methods=['POST'])
# def add_post():
#     if not request.is_json:
#         abort(404)
        
#     username = request.json.get('username')
#     post_content = request.json.get('post_content')
#     hashtag = request.json.get('hashtag')
#     emotion = request.json.get('emotion')
        
    # add to the user's history
    # with open('user.json', 'r') as f:
    #     data = json.load(f)
    #     new_post = {'content': post_content,
    #                 'hashtag': hashtag,
    #                 'emotion': emotion}
    #     print(data)
    #     data[username]['posts'].append(new_post)
        
    # with open('user.json', 'w') as f:
    #     json.dump(data, f, indent=4)
    
    # add to the posts list
    # with open('posts.json', 'r') as f:
    #     data = json.load(f)
    #     new_post = {'content': post_content,
    #                 'hashtag': hashtag}
    #     data[hashtag]["posts"].append(new_post)
        
    # with open('posts.json', 'w') as f:
    #     json.dump(data, f, indent=4)
    
    # return redirect(url_for('home', username=username))

if __name__ == '__main__':
    socketio.run(app, debug=True)
    
    
# user clicks on a hashtag -> triggers this function to display the suggested hashtags
# @app.route('/suggesting', methods=['POST'])
# def suggesting():
#     if not request.is_json:
#         abort(404)

#     hashtag = request.json.get('hashtag')
#     suggested_hashtags = groups[hashtags[hashtag]]
#     return url_for('/', suggested_hashtags=suggested_hashtags)