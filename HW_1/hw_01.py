from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index_shop.html')


@app.route('/clothes/')
def clothes():
    clothes_list = [
        {'title': 'Верхняя одежда',
         'description': 'описание01',
         },
        {'title': 'Спортивная одежда',
         'description': 'описание02',
         },
        {'title': 'Детская одежда',
         'description': 'описание03',
         }
    ]
    return render_template('clothes.html', clothes_list=clothes_list)

@app.route('/clothes/jacket/')
def jacket():
    return render_template('jacket.html')


@app.route('/shoes/')
def shoes():
    shoes_list = [
        {'title': 'Спортивная',
         'description': 'описание01',
         },
        {'title': 'Зимняя обувь',
         'description': 'описание02',
         },
        {'title': 'Летняя обувь',
         'description': 'описание03',
         }
    ]

    return render_template('shoes.html', shoes_list=shoes_list)


if __name__ == '__main__':
    app.run(debug=True)
