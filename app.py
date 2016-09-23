import web
from web import form

render = web.template.render('views/',cache=False)
        
urls = (
    '/', 'index',
    '/about','about',
    '/variables/(.*)','variables',
    '/login','login',
    '/saludo','script'
)

class script:
    def GET(self):
        return render.script()

class index:        
    def GET(self):
       return render.index()

class about:
    def GET(self):
        i = web.input(name=None)
        return render.dos(i.name)

class variables:
    def GET(self, name):
        return render.dos(name)

class login:
    def GET(self):
        login = form.Form(
            form.Textbox('username'),
            form.Password('password'),
            form.Button('Login')
        )
        f = login()
        return render.login(f)

    def POST(self):
        i = web.input()
        f=form()
        f.username
        if i.username == 'sax' and i.passwords=='123':
            return 'Usuario valido'
        else:
            return 'Verifique usuario y clave'

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = False
    app.run()