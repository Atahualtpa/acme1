import web

db = web.database(dbn='mysql',host='jnc6n3xpbgc3kek2.chr7pe7iynqr.eu-west-1.rds.amazonaws.com', db='gaa3ikw2m8jp29p9', user='tls6apgwcf9f8z0g', pw='cbio915ps7tg27jj')

def get_posts():
    return db.select('productos', order='id_producto')

def get_post(id):
    try:
        return db.select('productos', where='id_producto=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(producto,descripcion,existencias,precio_compra,precio_venta,imagen_producto):
    db.insert('productos',
              producto=producto,
              descripcion= descripcion,
              existencias = existencias, 
              precio_compra= precio_compra,
              precio_venta= precio_venta, 
              imagen_producto= imagen_producto)

def del_post(id):
    db.delete('productos', where="id_producto=$id", vars=locals())

def update_post(id, producto, descripcion, existencias, precio_compra, precio_venta,imagen_producto):
    db.update('productos', where="id_producto=$id", vars=locals(),
        producto=producto, descripcion=descripcion, existencias = existencias, precio_compra=precio_compra, precio_venta=precio_venta, imagen_producto = imagen_producto)

    
def insertar(producto,descripcion,existencias,precio_compra,precio_venta,imagen_producto):
	db.insert('productos',
		producto=producto,
		descripcion= descripcion,
		existencias = existencias, 
		precio_compra= precio_compra,
		precio_venta= precio_venta, 
             imagen_producto= imagen_producto)
