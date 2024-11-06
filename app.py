from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

#base de datos
USER_DB = 'root'
PASS_DB = ''
URL_DB = 'localhost'
NAME_DB = 'progo'
FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Configuración de la migración

migrate = Migrate()
migrate.init_app(app, db)

class Proveedor(db.Model):  
    provee_id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(128))
    nombre = db.Column(db.String(128))
    celular = db.Column(db.String(250))

    def __init__(self,provee_id, correo, nombre, celular ):
        self.provee_id = provee_id
        self.correo = correo
        self.nombre = nombre
        self.celular = celular

    def json(self):
        return {'provee_id': self.provee_id, 'correo': self.correo, 'nombre': self.nombre,'celular': self.celular}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
  
  
class Categoria(db.Model):  
    cate_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    
    def __init__(self,cate_id, nombre, descripcion ):
        self.cate_id = cate_id
        self.nombre = nombre
        self.descripcion = descripcion

    def json(self):
        return {'cate_id': self.cate_id, 'nombre': self.nombre,'descripcion': self.descripcion}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
class Cliente(db.Model):  
    Cedula_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    celular = db.Column(db.String(128))

    def __init__(self, Cedula_id, nombre, celular ):
        self.Cedula_id = Cedula_id
        self.nombre = nombre
        self.celular = celular

    def json(self):
        return {'Cedula_id': self.Cedula_id, 'nombre': self.nombre,'celular': self.celular}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
class detalleproductos(db.Model):  
    TP_id = db.Column(db.Integer, primary_key=True)
    PrecioUnitario = db.Column(db.String(128))
    Presentacion = db.Column(db.String(128))
    Lote = db.Column(db.String(128))
    CantidadTotal = db.Column(db.String(128))

    def __init__(self, TP_id, PrecioUnitario, Presentacion, Lote, CantidadTotal):
        self.TP_id= TP_id
        self.PrecioUnitario = PrecioUnitario
        self.Presentacion = Presentacion
        self.Lote = Lote
        self.CantidadTotal = CantidadTotal

    def json(self):
        return {'TP_id': self.TP_id, 'PrecioUnitario': self.PrecioUnitario,'Presentacion': self.Presentacion, 'Lote': self.Lote, 'CantidadTotal': self.CantidadTotal}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class Usuarios(db.Model):  
    usu_id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(128))
    Celular = db.Column(db.String(128))
    Correo = db.Column(db.String(128))
    TipoUsuario = db.Column(db.String(128))

    def __init__(self, usu_id, Nombre, Celular, Correo, TipoUsuario):
        self.usu_id = usu_id
        self.Nombre = Nombre
        self.Celular = Celular
        self.Correo = Correo
        self.TipoUsuario = TipoUsuario

    def json(self):
        return {'usu_id': self.usu_id, 'Nombre': self.Nombre,'Celular': self.Celular, 'Correo': self.Correo, 'TipoUsuario': self.TipoUsuario}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
class detallepedidos(db.Model):  
    DPid = db.Column(db.String(30), primary_key=True)
    Presentacion = db.Column(db.String(128))
    PrecioTotal = db.Column(db.String(128))
    MontoTotal = db.Column(db.String(128))

    def __init__(self, DPid, Presentacion, PrecioTotal, MontoTotal):
        self.DPid = DPid
        self.Presentacion = Presentacion
        self.PrecioTotal = PrecioTotal
        self.MontoTotal = MontoTotal

    def json(self):
        return {'DPid': self.DPid, 'Presentacion': self.Presentacion,'PrecioTotal': self.PrecioTotal, 'MontoTotal': self.MontoTotal}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
class Pedidos(db.Model):  
    pedidos_id = db.Column(db.Integer, primary_key=True)
    CantidadUnitaria = db.Column(db.String(128))
    NombreProducto = db.Column(db.String(128))
    usuarios = db.Column(db.Integer, db.ForeignKey('usuarios.usu_id'))
    detallepedidos = db.Column(db.Integer, db.ForeignKey('detallepedidos.DPid'))


    def __init__(self, pedidos_id, CantidadUnitaria, NombreProducto):
        self.pedidos_id = pedidos_id
        self.CantidadUnitaria = CantidadUnitaria
        self.NombreProducto = NombreProducto

    def json(self):
        return {'pedidos_id': self.pedidos_id, 'CantidadUnitaria': self.CantidadUnitaria,'NombreProducto': self.NombreProducto}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
class Inventario(db.Model):  
    iven_id = db.Column(db.Integer, primary_key=True)
    Stock = db.Column(db.String(128))
    Fecha = db.Column(db.DateTime(128))

    def __init__(self, iven_id, Stock, Fecha):
        self.iven_id = iven_id
        self.Stock = Stock
        self.Fecha = Fecha

    def json(self):
        return {'iven_id': self.iven_id, 'Stock': self.Stock,'Fecha': self.Fecha}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
class Movimientos(db.Model):  
    movi_id = db.Column(db.Integer, primary_key=True)
    Fecha = db.Column(db.DateTime(128))
    Descripcion = db.Column(db.String(128))
    inventario = db.Column(db.Integer, db.ForeignKey('inventario.iven_id'))
    

    def __init__(self, movi_id, Fecha, Descripcion):
        self.movi_id = movi_id
        self.Fecha = Fecha
        self.Descripcion = Descripcion

    def json(self):
        return {'movi_id': self.movi_id, 'Fecha': self.Fecha,'Descripcion': self.Descripcion}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
class detallefactura(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    Productos = db.Column(db.String(128))
    Precio = db.Column(db.String(128))
    Cantidad = db.Column(db.String(128))

    def __init__(self, id, Productos, Precio, Cantidad):
        self.id = id
        self.Productos = Productos
        self.Precio = Precio
        self.Cantidad = Cantidad

    def json(self):
        return {'id': self.id, 'Productos': self.Productos,'Precio': self.Precio,'Cantidad': self.Cantidad}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class Factura(db.Model):  
    ft_id = db.Column(db.Integer, primary_key=True)
    Fecha = db.Column(db.DateTime(128))
    MontoTotal = db.Column(db.String(128))
    PrecioTotal = db.Column(db.String(128))
    inventario = db.Column(db.Integer, db.ForeignKey('inventario.iven_id'))
    cliente = db.Column(db.Integer, db.ForeignKey('cliente.Cedula_id'))
    detallefactura = db.Column(db.Integer, db.ForeignKey('detallefactura.id'))


    def __init__(self, ft_id, Fecha, MontoTotal, PrecioTotal):
        self.ft_id = ft_id
        self.Fecha = Fecha
        self.MontoTotal = MontoTotal
        self.PrecioTotal = PrecioTotal

    def json(self):
        return {'ft_id': self.ft_id, 'Fecha': self.Fecha,'MontoTotal': self.MontoTotal,'PrecioTotal': self.PrecioTotal}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    

class Productos(db.Model):
    pt_id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(128))
    FechaVence = db.Column(db.DateTime(128))
    Estado = db.Column(db.String(128))
    FechaEntrada = db.Column(db.DateTime(128))
    PrecioSalida = db.Column(db.String(128))

    pedidos = db.Column(db.Integer, db.ForeignKey('pedidos.pedidos_id'))
    categoria = db.Column(db.Integer, db.ForeignKey('categoria.cate_id'))
    detalleproductos = db.Column(db.Integer, db.ForeignKey('detalleproductos.TP_id'))
    proveedor = db.Column(db.Integer, db.ForeignKey('proveedor.provee_id'))
    inventario = db.Column(db.Integer, db.ForeignKey('inventario.iven_id'))

    def __init__(self, pt_id, FechaVence, MontoTotal, PrecioTotal):
        self.pt_id = pt_id
        self.FechaVence = FechaVence
        self.MontoTotal = MontoTotal
        self.PrecioTotal = PrecioTotal

    def json(self):
        return {'pt_id': self.pt_id, 'FechaVence': self.FechaVence, 'MontoTotal': self.MontoTotal, 'PrecioTotal': self.PrecioTotal}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


