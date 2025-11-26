from django.shortcuts import render
import datetime
# Create your views here.
class Stu(object):
    def __init__(self,name,age,gender,address):
        self.name = name
        self.age =age
        self.gender = gender
        self.address = address

def gen_r():
    yield 111
    yield 222
    yield 333
#也可以传入函数
def fetch_data():
    return '我是一个函数,我被调用执行了'

def index(request):
    if request.method == 'GET':
        a1 = '你好'
        lst=[i for i in range(10)]
        dic={
            'name':'jakson',
            'age':24,
            'gender':'male',
            'address':'queen_s'
        }
        infodic_lst=[
            {
                'name': 'fjaafeson',
                'age': 24,
                'gender': 'mfeale',
                'address': 'afqaefen_s'
            },
            {
                'name': 'zdfson',
                'age': 21,
                'gender': 'male',
                'address': 'queen_s'
            },
            {
                'name': 'dxfzvaefon',
                'age': 23,
                'gender': 'female',
                'address': 'aauaedfan_s'
            },
            {
                'name': 'aaaw1son',
                'age': 21,
                'gender': 'male',
                'address': 'qfn_s'
            },
            {
                'name': 'jakson',
                'age': 22,
                'gender': 'female',
                'address': 'qefn_s'
            }
        ]

        content={
            'a1':a1,
            'lst':lst,
            'dic':dic,
            'infodic_lst':infodic_lst,
            'obj':Stu('nikofox',28,'male','hawaii'),
            'func':fetch_data,
            'gen_er_obj':gen_r(),#这样传入的就是一个生成器对象
            'gen_er_func':gen_r, #这样传入的就是一个生成器函数
            'datetime':datetime.datetime.now()
        }

        return render(request,'api/index.html', content)
