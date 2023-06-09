from flask.views import MethodView
from flask import request,render_template, redirect
from src.db import mysql


class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("select * from veiculos inner join encontro on veiculos.id_encontro = encontro.id_encontro")
            data = cur.fetchall()
        return render_template('public/index.html', data=data)
    
    
    def post(self):
        codigo = request.form['codigo']
        placa = request.form['placa']
        modelo = request.form['modelo']
        responsavel = request.form['responsavel']
        id_encontro = request.form['id_encontro']
        
        with mysql.cursor()as cur:
            cur.execute("insert into veiculos values(%s,%s,%s,%s,%s)",(codigo,placa,modelo,responsavel,id_encontro))
            cur.connection.commit()
            return redirect('/')
            
class DeleteVeiculoController(MethodView):
    def post(self, codigo):
        with mysql.cursor()as cur:
            cur.execute("delete from veiculos where codigo = (%s)",(codigo,))
            cur.connection.commit()
            return redirect('/')
        
class UpdateVeiculoController(MethodView):
    def get(self, codigo):
        with mysql.cursor()as cur:
            cur.execute("select * from veiculos where codigo = (%s)",(codigo,))
            veiculo = cur.fetchone()
            return render_template('public/update.html',veiculo=veiculo)
        
    def post(self, codigo):
        veiculocodigo = request.form['codigo']
        placa = request.form['placa']
        modelo = request.form['modelo']
        responsavel = request.form['responsavel']
        id_encontro = request.form['id_encontro']
        
        with mysql.cursor()as cur:
            cur.execute("update veiculos set codigo = %s, placa = %s, modelo = %s, responsavel = %s, id_encontro = %s where codigo = %s",(codigo,placa,modelo,responsavel,id_encontro,veiculocodigo))
            cur.connection.commit()
            return redirect('/')

class EncontroController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("select * from encontro")
            data = cur.fetchall()
        return render_template('public/encontros.html', data=data)
    
    
    def post(self):
        codigo = request.form['codigo']
        nome = request.form['nome']
        descricao = request.form['descricao']
        data = request.form['data']

        
        with mysql.cursor()as cur:
            cur.execute("insert into encontro values(%s,%s,%s,%s)",(codigo,nome,descricao,data))
            cur.connection.commit()
            return redirect('/encontro')

class DeleteEncontroController(MethodView):
    def post(self, codigo):
        with mysql.cursor()as cur:
            cur.execute("delete from encontro where id_encontro = (%s)",(codigo,))
            cur.connection.commit()
            return redirect('/encontro')
