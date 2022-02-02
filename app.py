from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def todo_create():
    """Создание листа"""
    global task_i
    global to_do_list
    global completed_tasks
    to_do_list = []
    task_i = 0
    completed_tasks = []
    print('Your ToDo list was created!')
    return str(to_do_list)


@app.route('/add')
def todo_add():
    """Создание новой задачи
    реализовал через словарь
    пока в нем номер позиции (индекс, начиная с 1) и название"""
#    here we want to get the value of user (i.e. ?task=some-value)
    task = request.args.get('task')
    note = {'pos': len(to_do_list)+1, 'title': task}
    to_do_list.append(note)
    print(to_do_list)
    return f'Task "{task}" was added to your ToDo list'


@app.route('/read')
def todo_read():
    return str(to_do_list)


@app.route('/update')
def todo_update():
    """Передается не индекс, а номер позиции ТуДуЛиста
     (начинается не с 0, а с 1)"""
    new_task = request.args.get('new_task')
    position = request.args.get('position')
    to_do_list[int(position)-1]['title'] = new_task
    return str(to_do_list)


@app.route('/delete')
def delete():
    """Передается не индекс, а номер позиции ТуДуЛиста
    (начинается не с 0, а с 1)"""
    position = request.args.get('position')
    not_finished = to_do_list.pop(int(position)-1)
    for i in range(int(position)-1, len(to_do_list)):
        to_do_list[i]['pos'] = i+1
    return f'Deleting position {position} "{not_finished["title"]}" complete successful'


if __name__ == '__main__':
    app.run()

