## Django瘦身  
Django项目默认的settings.py中会默认给我们install很多  
我们可能用不到的内置app  
```python
INSTALLED_APPS = [
    'django.contrib.admin',  #后台管理功能可以对创建的数据表进行增删改查
    'django.contrib.auth',  #权限功能,和admin一样都很鸡肋
    'django.contrib.contenttypes', #为复杂的表结构设计提供的，前后端分离会用到
    'django.contrib.sessions', #记录用户状态的,前后端分离倒是用不到
    'django.contrib.messages', #页面a与页面b之间的通信
    'django.contrib.staticfiles', #支持静态文件
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware', #对应上面的message的中间件
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',#当我们注释掉auth的app之后这个当然也要注释掉
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```  
对于这些我们其实并不都是需要的,那么我们就可以通过注释掉其中不需要的来达到给django瘦身的效果  
注意,只要上边的installed_apps注释掉了,下面对应的也要注释掉,否则可能会发生报错
