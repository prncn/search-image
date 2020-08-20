from flask import Flask, render_template, request, session, make_response, json
import requests
import image_api
import time

app = Flask(__name__)
app.secret_key = '14082020'


@app.route('/', methods=['GET', 'POST'])
def index():
    default_query = "edo art"
    default_color = False
    session['query'] = request.args.get('query', default_query)
    session['color'] = request.args.get('color', default_color)
    return render_template('index.html')


@app.route("/load")
def load():
    query = session['query']
    color = session['color']

    if request.args:
        counter = int(request.args.get('page'))
        if counter > 5:
            data = []
        else:
            data = image_api.get_images(query, color, counter)
            # data = [{'url': 'https://images.unsplash.com/photo-1511360823-5c672a170787?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1596534193399-1018035478c6?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1596534194341-63f1ccbfb5ac?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1596534193170-fcfe3a2cff82?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1596534194505-0fc344ed7303?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1596534634180-843843895549?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1596534193126-bc6477d2a79f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1596534634517-6c760550e832?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1596713200266-32353f9f554e?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1551913902-c92207136625?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1553519495-a6384546a328?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1561084746-f360502e5abe?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1559740983-b9c5ffbac1ff?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1579963823690-4593d0ea2814?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1562574480-fd97d35cee6c?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1553523292-1140e57d4f87?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/flagged/photo-1572392640988-ba48d1a74457?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1567693016361-8be252b3848d?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1584654600747-3b18033abee8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1579541814924-49fef17c5be5?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/flagged/photo-1569154707792-459d556b4bc3?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1572450732467-5eb1311e7bc8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1567466061910-46fdb3bc18b0?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1578926288207-a90a5366759d?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1597142140602-bc1ddf323e87?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1588106986459-db99895705c4?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1594977862439-0654305d2b6d?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1551807305-baa15a10803f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1548262016-9bf97ff61020?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}, {'url': 'https://images.unsplash.com/photo-1579541591970-e5780dc6b31f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjE1NzA2OH0'}]
        print(counter)
        response = make_response(json.dumps(data), 200)
        data.clear()

    return response


if __name__ == '__main__':
    app.run()
