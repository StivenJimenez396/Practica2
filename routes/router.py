from flask import Blueprint, jsonify, abort , request, render_template, redirect, make_response
from flask import flash
from controls.facturaDaoControl import FacturaDaoControl
from controls.personaDaoControl import PersonaDaoControl
from controls.tda.linked.metodosBusqueda.binary import Binary
from controls.tda.linked.metodosBusqueda.binarySecuencial import BinarySecuencial
from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedEmpty import LinkedEmpty

import time
router = Blueprint('router', __name__)

@router.route('/')
def home():
    return render_template("template.html")

# Ver Interfaz----------------------------------------
@router.route('/personas')
def crear_persona():
    return render_template("interfaz/persona.html")

@router.route('/lista')
def ver_lista():
    pd = PersonaDaoControl()
    lista = pd._list()
    
    atributo = request.args.get('sort_by', '_apellido')
    order = request.args.get('order', 'asc')
    metodo = request.args.get('metodo', 'quicksort')

    tipo = 1 if order == 'asc' else 2

    lista.sort_models(atributo, tipo, metodo)
    
    return render_template("interfaz/listaPersonas.html", lista=pd.to_dic_lista(lista))

#@router.route('/lista')
#def ver_lista():
#    pd = PersonaDaoControl()
#    list = pd._list()
#    list.sort_models('_nombre',1)
#    return render_template("interfaz/listaPersonas.html", lista=pd.to_dic_lista(list))

@router.route('/historial')
def ver_historial():
    fd = FacturaDaoControl()
    return render_template("interfaz/historial.html", lista=fd.to_dic())



#Acciones que tiene la interfaz-----------------------

@router.route('/personas/guardar', methods=['POST'])
def guardar_personas():
    pd = PersonaDaoControl()
    data = request.form
    if not "apellido" in data.keys():
        abort(400)            
    pd._persona._apellido = data['apellido']
    pd._persona._nombre = data['nombre']
    pd._persona._cedula = data['cedula']
    pd._persona._tipoRuc = data['tipoRuc']
    pd._persona._numRuc = data['numRuc']
    pd.save
    return redirect("/lista", code=302)

@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._list().get(int(pos)-1)
    return render_template("interfaz/emitirFactura.html", data=nene)

@router.route('/factura/guardar', methods=['POST'])
def guardar_factura():
    fd = FacturaDaoControl()
    data = request.form
    if not "apellido" in data.keys():
        abort(400)            
    fd._factura._apellido = data['apellido']
    fd._factura._nombre = data['nombre']
    fd._factura._cedula = data['cedula']
    fd._factura._tipoRuc = data['tipoRuc']
    fd._factura._numRuc = data['numRuc']
    fd._factura._dniEmisor = data['dniEmisor']
    fd._factura._valor = float(data['valor'])
    fd.calcularRetencion()
    fd.totalPago()
    fd.save
    return redirect("/historial", code=302)

@router.route('/buscar', methods=['GET', 'POST'])
def buscar():
    pd = PersonaDaoControl()

    if request.method == 'POST':
        attribute = request.form.get('attribute')
        value = request.form.get('value')
        method = request.form.get('method')

        lista = pd._list()
        if method == 'binary':
            index = lista.search_binary(value)
            results = [lista.get(index)] if index != -1 else []
        elif method == 'binarySecuencial':
            indices = lista.search_binarySecuencial_models(value, attribute)
            results = [lista.get(index) for index in indices]
        else:
            results = lista.search_equals(value)
        
        return render_template("interfaz/search.html", results=results)

    return render_template("interfaz/search.html")