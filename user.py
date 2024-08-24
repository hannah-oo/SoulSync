import json

class User:
        
    def __init__(self, username, location):
        self.location = location
        self.username = username
        
        with open('user.json', 'r') as f:
            data = json.load(f)
        
        with open('user.json', 'w') as f:
            data[username] = {'location': self.location,
                              'posts': []}
            json.dump(data, f, indent=4)