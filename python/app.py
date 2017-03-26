import web
import model

urls = (
    '/', 'Index',
    '/view/(\d+)', 'View',
    '/new', 'New',
    '/delete/(\d+)', 'Delete',
    '/edit/(\d+)', 'Edit',
    '/borrar/(\d+)','Borrar'
    
)


t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates', base='base', globals=t_globals)


class Index:

    def GET(self):
        posts = model.get_posts()
        return render.index(posts)


class View:

    def GET(self, id):
        post = model.get_post(int(id))
        return render.view(post)


class New:

    form = web.form.Form(
        web.form.Textbox('producto', web.form.notnull, 
            size=30,
            description="Producto:"),
        web.form.Textarea('descripcion', web.form.notnull, 
            rows=8, cols=32,
            description="Descipcion:"),
        web.form.Textbox('existencias', web.form.notnull, 
            size=30,
            description="Existencias:"),
        web.form.Textbox('precio_compra', web.form.notnull, 
            size=30,
            description="Precio Compra:"),
        web.form.Textbox('precio_venta', web.form.notnull, 
            size=30,
            description="Precio Venta:"),
        web.form.File('imagen_producto', web.form.notnull,
            size=30,
            description="Imagen del producto:"),
        web.form.Button('Registrar'),
    )
    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        imagen = web.input(imagen_producto={})
        filedir = 'static/images'
        filepath = imagen.imagen_producto.filename.replace('\\','/')
        filename = filepath.split('/')[-1]
#copiar archivo al servidor
        fout= open(filedir+'/'+filename,'w')
        fout.write(imagen.imagen_producto.file.read())
        fout.close()
        imagen_producto = filename
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.producto, form.d.descripcion,form.d.existencias, form.d.precio_compra, form.d.precio_venta, imagen_producto)
        raise web.seeother('/')

class Borrar:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.borrar(post)
    
    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/')
               

class Delete:

    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/')


class Edit:

    def GET(self, id):
        post = model.get_post(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)


    def POST(self, id):
        form = New.form()
        imagen = web.input(imagen_producto={})
        filedir = 'static/images'
        filepath = imagen.imagen_producto.filename.replace('\\','/')
        filename = filepath.split('/')[-1]
        fout= open(filedir+'/'+filename,'w')
        fout.write(imagen.imagen_producto.file.read())
        fout.close()
        imagen_producto = filename
        post = model.get_post(int(id))
        if not form.validates():
            return render.edit(post, form)
        model.update_post(int(id), form.d.producto, form.d.descripcion, form.d.existencias, form.d.precio_compra, form.d.precio_venta, imagen_producto)
        raise web.seeother('/')

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
