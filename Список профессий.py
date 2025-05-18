from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/index/<title>')
def index(title='заготовка'):
    return render_template('base.html', title=title)

@app.route('/list_prof/<list>')
def list_prof(list):
    professions = [
        "Инженер-исследователь",
        "Пилот",
        "Строитель",
        "Экзобиолог",
        "Врач",
        "Инженер по терраформированию",
        "Климатолог",
        "Специалист по радиационной зашите",
        "Астрогеолог",
        "Гляциолог",
        "Инженер жизнеобеспечения",
        "Метеоролог",
        "Оператор марсохода",
        "Киберинженер",
        "Штурман",
        "Пилот дронов"
    ]
    return render_template(
        'prof_list.html',
        list=list,
        prof_list=professions
    )


if __name__ == '__main__':
    app.run(debug=True)
