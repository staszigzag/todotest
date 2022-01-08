from flask import Flask
import random
app = Flask(__name__)

to_do = []

@app.route('/create/<item>')
def hello_world(item):
    to_do.append(item+str(random.randint(1, 10)))
    print(to_do)
    return 'create success'

@app.route('/get')
def hello_world2():
    return str(to_do)

@app.route('/delete/<position>')
def delete(position):
    to_do.pop(int(position))
    return f'deleting position {position} succesful'

if __name__ == '__main__':
    app.run( port=2222)
