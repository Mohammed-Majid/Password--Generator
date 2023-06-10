from flask import Flask, render_template, request
import secrets
import string


app = Flask(__name__)

def create_graph():
    nodes = list(string.ascii_lowercase + string.digits + "!@#$%&~")
    adj_list = {}
    for node in nodes:
        adj_list[node] = []
        for adj in nodes:
            if adj != node and adj not in adj_list[node]:
                adj_list[node].append(adj)
    return adj_list

def get_neighbors(adj_list, v):
    return adj_list[v]

def get_random_neighbor(adj_list, v):
    return secrets.choice(get_neighbors(adj_list, v))

def random_walk(adj_list, start, num_steps):
    walk = [start]
    for _ in range(num_steps - 1):
        walk.append(get_random_neighbor(adj_list, walk[-1]))
    return ''.join(walk)

@app.route('/', methods=['GET', 'POST'])
def generate_password():
    length = 12
    if request.method == 'POST':
        length = request.form.get('length', 12)
        try:
            length = int(length)
        except ValueError:
            length = 12
        length = min(max(8, length), 20)  # Constrain length between 8 and 20
        adj_list = create_graph()
        start_node = secrets.choice(list(adj_list.keys()))
        password = random_walk(adj_list, start_node, length)
        final_password = []
        for char in password:
            if secrets.randbelow(2):  # 0 or 1
                final_password.append(char.upper())
            else:
                final_password.append(char)
        password = ''.join(final_password)
    else:
        password = None
    return render_template('index.html', password=password, length=length)

if __name__ == '__main__':
    app.run(debug=True)

