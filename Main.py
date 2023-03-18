def Style(var):
    if(var == "erro"):
        return "QLineEdit{color: rgb(184, 184, 184);\nbackgroud:none;\npadding: 5px;\nborder: 2px solid rgb(255, 0, 0);\nborder-radius: 6px;\n}\nQLineEdit:hover{\nborder: 2px solid rgb(255, 0, 255)\n}\nQLineEdit:focus{\ncolor: rgb(255, 255, 255);\nborder: 2px solid rgb(255, 0, 255)\n}"
    else:
        return "QLineEdit{color: rgb(184, 184, 184);\nbackgroud:none;\npadding: 5px;\nborder: 2px solid rgb(83, 0, 226);\nborder-radius: 6px;\n}\nQLineEdit:hover{\nborder: 2px solid rgb(255, 0, 255)\n}\nQLineEdit:focus{\ncolor: rgb(255, 255, 255);\nborder: 2px solid rgb(255, 0, 255)\n}"

def Peso(pes):
    try:
        peso = float(pes)
        if (peso <= 0):
            QMessageBox.about(tela_new_main, "Erro!", "Peso invalido!")
            return
        return peso
    except:
        QMessageBox.about(tela_new_main, "Erro!", "Digite apenas numeros e utilize o ponto flutuante!")
def Altura(alt):
    try:
        altura = float(alt)
        if (altura <= 0 or altura > 2.5):
            QMessageBox.about(tela_new_main, "Erro!", "Altura até 2.5m!")
            return
        return altura
    except:
        QMessageBox.about(tela_new_main, "Erro!", "Digite apenas numeros e utilize o ponto flutuante!")
def CalcularImc():
    if(tela_new_main.tb_main_imc_peso.text() == "" or tela_new_main.tb_main_imc_altura.text() == ""):
        if(tela_new_main.tb_main_imc_peso.text() == ""):
            tela_new_main.tb_main_imc_peso.setStyleSheet(Style("erro"))
        else:
            tela_new_main.tb_main_imc_peso.setStyleSheet(Style(""))
        if (tela_new_main.tb_main_imc_altura.text() == ""):
            tela_new_main.tb_main_imc_altura.setStyleSheet(Style("erro"))
        else:
            tela_new_main.tb_main_imc_altura.setStyleSheet(Style(""))
    else:
        tela_new_main.tb_main_imc_peso.setStyleSheet(Style(""))
        tela_new_main.tb_main_imc_altura.setStyleSheet(Style(""))
        try:
            peso = Peso(tela_new_main.tb_main_imc_peso.text())
            altura = Altura(tela_new_main.tb_main_imc_altura.text())
            imc = peso / pow(altura, 2)
            tela_new_main.lbl_imc_resultado.setText(str(round(imc, 2)))
            tela_new_main.tb_main_calc_peso.setText(tela_new_main.tb_main_imc_peso.text())
            tela_new_main.tb_main_calc_altura.setText(tela_new_main.tb_main_imc_altura.text())
        except:
            print()
def CalcularCal():
    if(tela_new_main.tb_main_calc_peso.text() == "" or tela_new_main.tb_main_calc_altura.text() == "" or tela_new_main.tb_main_calc_idade.text() == "" or (tela_new_main.rb_masculino.isChecked() == False and tela_new_main.rb_feminino.isChecked() == False) or (tela_new_main.rb_leve.isChecked() == False and tela_new_main.rb_moderada.isChecked() == False and tela_new_main.rb_intensa.isChecked() == False)):
        if(tela_new_main.tb_main_calc_peso.text() == ""):
            tela_new_main.tb_main_calc_peso.setStyleSheet(Style("erro"))
        else:
            tela_new_main.tb_main_calc_peso.setStyleSheet(Style(""))
        if(tela_new_main.tb_main_calc_altura.text() == ""):
            tela_new_main.tb_main_calc_altura.setStyleSheet(Style("erro"))
        else:
            tela_new_main.tb_main_calc_altura.setStyleSheet(Style(""))
        if(tela_new_main.tb_main_calc_idade.text() == ""):
            tela_new_main.tb_main_calc_idade.setStyleSheet(Style("erro"))
        else:
            tela_new_main.tb_main_calc_idade.setStyleSheet(Style(""))
        if(tela_new_main.rb_masculino.isChecked() == False and tela_new_main.rb_feminino.isChecked() == False):
            QMessageBox.about(tela_new_main, "Erro!", "Escolha dentre as opções de Sexo!")
        if(tela_new_main.rb_leve.isChecked() == False and tela_new_main.rb_moderada.isChecked() == False and tela_new_main.rb_intensa.isChecked() == False):
            QMessageBox.about(tela_new_main, "Erro!", "Escolha dentre as opções de Fator Atividade!")
    else:
        tela_new_main.tb_main_calc_idade.setStyleSheet(Style(""))
        tela_new_main.tb_main_calc_peso.setStyleSheet(Style(""))
        tela_new_main.tb_main_calc_altura.setStyleSheet(Style(""))
        try:
            altura = peso = 0
            peso = Peso(tela_new_main.tb_main_calc_peso.text())
            altura = Altura(tela_new_main.tb_main_calc_altura.text())
            gastoBasal = sexoCaloria = valorFatorAtividade = 0
            if (tela_new_main.rb_masculino.isChecked() == True):
                sexoCaloria = 1
            elif (tela_new_main.rb_feminino.isChecked() == True):
                sexoCaloria = 2
            idadeCaloria = int(tela_new_main.tb_main_calc_idade.text())
            if (idadeCaloria < 3):
                if (sexoCaloria == 2):
                    gastoBasal = (58.317 * peso) - 31.1
                else:
                    gastoBasal = (59.512 * peso) - 30.4
            elif (idadeCaloria < 10):
                if (sexoCaloria == 2):
                    gastoBasal = (20.315 * peso) + 485.9
                else:
                    gastoBasal = (22.706 * peso) + 504.3
            elif (idadeCaloria < 18):
                if (sexoCaloria == 2):
                    gastoBasal = (13.384 * peso) + 692.6
                else:
                    gastoBasal = (17.686 * peso) + 658.2
            elif (idadeCaloria < 30):
                if (sexoCaloria == 2):
                    gastoBasal = (14.818 * peso) + 486.6
                else:
                    gastoBasal = (15.057 * peso) + 692.2
            elif (idadeCaloria < 60):
                if (sexoCaloria == 2):
                    gastoBasal = (8.126 * peso) + 845.6
                else:
                    gastoBasal = (11.472 * peso) + 873.1
            else:
                if (sexoCaloria == 2):
                    gastoBasal = (9.082 * peso) + 658.5
                else:
                    gastoBasal = (11.711 * peso) + 587.7
            if(tela_new_main.rb_leve.isChecked() == True):
                valorFatorAtividade = 1.55
            elif(tela_new_main.rb_moderada.isChecked() == True):
                valorFatorAtividade = 1.84
            elif(tela_new_main.rb_intensa.isChecked() == True):
                valorFatorAtividade = 2.2
            gastoTotal = round(gastoBasal * valorFatorAtividade, 2)
            tela_new_main.lbl_result_manterpeso.setText(f"{gastoTotal}")
            tela_new_main.lbl_result_perderpeso.setText(f"{gastoTotal - 250}")
            tela_new_main.lbl_result_ganharpeso.setText(f"{gastoTotal + 500}")
        except:
            QMessageBox.about(tela_new_main, "Erro!", "Digite apenas numeros e utilize o ponto flutuante!")

def CalcularCalTotal():
    if(tela_new_main.tb_main_calc_cafemanha.text() == "" or tela_new_main.tb_main_calc_cafetarde.text() == "" or
    tela_new_main.tb_main_calc_almoco.text() == "" or tela_new_main.tb_main_calc_jantar.text() == "" or
    tela_new_main.tb_main_calc_ceia.text() == ""):
        if(tela_new_main.tb_main_calc_cafemanha.text() == ""):
            tela_new_main.tb_main_calc_cafemanha.setStyleSheet(Style("erro"))
        else:
            tela_new_main.tb_main_calc_cafemanha.setStyleSheet(Style(""))
        if(tela_new_main.tb_main_calc_cafetarde.text() == ""):
            tela_new_main.tb_main_calc_cafetarde.setStyleSheet(Style("erro"))
        else:
            tela_new_main.tb_main_calc_cafetarde.setStyleSheet(Style(""))
        if(tela_new_main.tb_main_calc_almoco.text() == ""):
            tela_new_main.tb_main_calc_almoco.setStyleSheet(Style("erro"))
        else:
            tela_new_main.tb_main_calc_almoco.setStyleSheet(Style(""))
        if(tela_new_main.tb_main_calc_jantar.text() == ""):
            tela_new_main.tb_main_calc_jantar.setStyleSheet(Style("erro"))
        else:
            tela_new_main.tb_main_calc_jantar.setStyleSheet(Style(""))
        if(tela_new_main.tb_main_calc_ceia.text() == ""):
            tela_new_main.tb_main_calc_ceia.setStyleSheet(Style("erro"))
        else:
            tela_new_main.tb_main_calc_ceia.setStyleSheet(Style(""))
    else:
        tela_new_main.tb_main_calc_cafemanha.setStyleSheet(Style(""))
        tela_new_main.tb_main_calc_cafetarde.setStyleSheet(Style(""))
        tela_new_main.tb_main_calc_almoco.setStyleSheet(Style(""))
        tela_new_main.tb_main_calc_jantar.setStyleSheet(Style(""))
        tela_new_main.tb_main_calc_ceia.setStyleSheet(Style(""))
        try:
            cafemanha = float(tela_new_main.tb_main_calc_cafemanha.text())
            cafetarde = float(tela_new_main.tb_main_calc_cafetarde.text())
            almoco = float(tela_new_main.tb_main_calc_almoco.text())
            jantar = float(tela_new_main.tb_main_calc_jantar.text())
            ceia = float(tela_new_main.tb_main_calc_ceia.text())
            tela_new_main.lbl_result_cal_total.setText(f"{round(cafemanha + cafetarde + almoco + jantar + ceia, 2)}")
            if(tela_new_main.lbl_result_manterpeso.text() != "..."):
                if (tela_new_main.lbl_result_manterpeso.text() == tela_new_main.lbl_result_cal_total.text()):
                    tela_new_main.lbl_comp.setText("Quantidade ingerida IGUAL a recomendada!")
                elif(tela_new_main.lbl_result_manterpeso.text() > tela_new_main.lbl_result_cal_total.text()):
                    tela_new_main.lbl_comp.setText("Quantidade ingerida MENOR do que recomendada!")
                elif(tela_new_main.lbl_result_manterpeso.text() < tela_new_main.lbl_result_cal_total.text()):
                    tela_new_main.lbl_comp.setText("Quantidade ingerida MAIOR do que recomendada!")
        except:
            QMessageBox.about(tela_new_main, "Erro!", "Digite apenas numeros e utilize o ponto flutuante!")
def Login(list):
    i = 0
    formatuser = formatsenha = False
    while (i < len(list)):
        if (tela_login.tb_user.text() == list[i].user):
            formatuser = True
            if (tela_login.t_password.text() == list[i].senha):
                formatsenha = True
                break
        elif (tela_login.tb_user.text() == list[i].email):
            formatuser = True
            if (tela_login.t_password.text() == list[i].senha):
                formatsenha = True
                break
        i += 1
    if (formatuser == formatsenha == True):
        Mostrar()
    else:
        if (formatuser == False):
            Mostra_Erro("user")
        elif (formatuser == True and formatsenha == False):
            Mostra_Erro("senha")

def Cadastra(list):
    if(tela_cadastro.tb_email_cadastro.text() == "" or tela_cadastro.tb_nome_cadastro.text() == "" or tela_cadastro.tb_username_cadastro.text() == "" or tela_cadastro.tb_senha_cadastro.text() == ""):
        Mostra_Erro2("vazio")
    elif(tela_cadastro.tb_senha_cadastro.text() == tela_cadastro.tb_confirmasenha_cadastro.text()):
        i = 0
        format = False
        while (i < len(list)):
            if (tela_cadastro.tb_username_cadastro.text() == list[i].user):
                Mostra_Erro2("username")
                format = True
                break
            if(tela_cadastro.tb_email_cadastro.text() == list[i].email):
                Mostra_Erro2("email")
                format = True
                break
            i+=1
        if (format == False):
            Cadastrar(list)
            Mostrar()
            tela_cadastro.hide()
    else:
        Mostra_Erro2("senha")

def Limpar():
    tela_new_main.tb_main_usuario.setText("")
    tela_new_main.tb_main_imc_peso.setText("")
    tela_new_main.tb_main_imc_altura.setText("")
    tela_new_main.lbl_imc_resultado.setText("...")


    tela_new_main.tb_main_calc_peso.setText("")
    tela_new_main.tb_main_calc_altura.setText("")
    tela_new_main.tb_main_calc_idade.setText("")
    tela_new_main.lbl_result_manterpeso.setText("...")
    tela_new_main.lbl_result_ganharpeso.setText("...")
    tela_new_main.lbl_result_perderpeso.setText("...")


    tela_new_main.tb_main_calc_cafemanha.setText("")
    tela_new_main.tb_main_calc_cafetarde.setText("")
    tela_new_main.tb_main_calc_almoco.setText("")
    tela_new_main.tb_main_calc_jantar.setText("")
    tela_new_main.tb_main_calc_ceia.setText("")
    tela_new_main.lbl_result_cal_total.setText("...")
def Fecha_Erro():
    tela_login.lbl_erro_login_existe.hide()
    tela_login.lbl_erro_senha.hide()
    tela_login.lbl_erro_login.hide()
    tela_login.btn_lbl_erro_usuario.hide()
    tela_login.btn_lbl_erro_senha.hide()
    tela_login.btn_lbl_erro_login_existe.hide()
    tela_login.label.hide()
    tela_login.label_2.hide()
    tela_login.label_3.hide()

def Fecha_Erro2():
    tela_cadastro.lbl_erro_registro.hide()
    tela_cadastro.btn_lbl_erro_registro.hide()
    tela_cadastro.label_3.hide()

def Fecha_main():
    tela_new_main.close()

def Mostra_Erro(erro):
    if(erro == "existe"):
        tela_login.lbl_erro_login_existe.show()
        tela_login.btn_lbl_erro_usuario.show()
        tela_login.label.show()
    elif (erro == "user"):
        tela_login.lbl_erro_login.show()
        tela_login.btn_lbl_erro_usuario.show()
        tela_login.label_3.show()
    elif (erro == "senha"):
        tela_login.lbl_erro_senha.show()
        tela_login.btn_lbl_erro_senha.show()
        tela_login.label_2.show()

def Mostra_Erro2(erro):
    if(erro == "email"):
        tela_cadastro.lbl_erro_registro.setText("Email Already Exists")
    elif(erro == "username"):
        tela_cadastro.lbl_erro_registro.setText("Username Already Exists")
    elif(erro == "senha"):
        tela_cadastro.lbl_erro_registro.setText("Password Not Confirmed")
    elif(erro == "vazio"):
        tela_cadastro.lbl_erro_registro.setText("Empty Fields")
    tela_cadastro.lbl_erro_registro.show()
    tela_cadastro.label_3.show()
    tela_cadastro.btn_lbl_erro_registro.show()

def Cadastrar(list):
    list.append(Cadastro(0, tela_cadastro.tb_nome_cadastro.text(), tela_cadastro.tb_username_cadastro.text(), tela_cadastro.tb_email_cadastro.text(), tela_cadastro.tb_senha_cadastro.text()))
    sql_insert_Definition = f"INSERT INTO Usuario VALUES (null, '{listaCadastro[len(listaCadastro) - 1].nome.strip().lower()}', '{listaCadastro[len(listaCadastro) - 1].user.strip()}', '{listaCadastro[len(listaCadastro) - 1].email.strip()}', '{listaCadastro[len(listaCadastro) - 1].senha.strip()}');"
    cursor.execute(sql_insert_Definition)
    connection.commit()

def Mostrar():
    tela_cadastro.hide()
    tela_login.hide()
    tela_new_main.showMaximized()

def Salvar(list):
    list.append(Usuario(0, tela_new_main.tb_main_usuario.text(), tela_new_main.tb_main_imc_peso.text(), tela_new_main.tb_main_imc_altura.text()))
    sql_insert_Definition = f"INSERT INTO Paciente VALUES (null, '{listaUsuario[len(listaUsuario) - 1].nome.strip().lower()}', '{listaUsuario[len(listaUsuario) - 1].peso.strip()}', '{listaUsuario[len(listaUsuario) - 1].altura.strip()}');"
    cursor.execute(sql_insert_Definition)
    connection.commit()

import sys
from usuario import Usuario
import os
os.system("pip install pyqt5")
os.system("pip install mysql.connector")
import mysql.connector
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
from design4 import *
from cadastro import Cadastro

listaCadastro = []
connection = mysql.connector.connect(host = 'sql10.freemysqlhosting.net',
                                             database = 'sql10498561',
                                             user = 'sql10498561',
                                             password = 'MYja3qiJQ1')

cursor = connection.cursor()
sql_select_Query = "select * from Usuario"
cursor.execute(sql_select_Query)
records = cursor.fetchall()
#print(cursor.rowcount)
for row in records:
    listaCadastro.append(Cadastro(row[0], row[1], row[2], row[3], row[4]))
listaUsuario = []
app = QtWidgets.QApplication([])
tela_login = uic.loadUi("design4.ui")
tela_cadastro = uic.loadUi("design_cadastro.ui")
tela_new_main = uic.loadUi("nova_main.ui")
tela_login.show()

Fecha_Erro()
Fecha_Erro2()

tela_login.btn_cadastrar.clicked.connect(tela_cadastro.show)
tela_login.btn_lbl_erro_usuario.clicked.connect(Fecha_Erro)
tela_login.btn_lbl_erro_senha.clicked.connect(Fecha_Erro)
tela_login.btn_lbl_erro_login_existe.clicked.connect(Fecha_Erro)
tela_login.btn_enviar.clicked.connect(lambda: Login(listaCadastro))
tela_cadastro.btn_enviar_cadastro.clicked.connect(lambda: Cadastra(listaCadastro))
tela_cadastro.btn_lbl_erro_registro.clicked.connect(Fecha_Erro2)

tela_new_main.btn_calculo_imc_calcular.clicked.connect(CalcularImc)
tela_new_main.btn_main_sair.clicked.connect(tela_new_main.close)

tela_new_main.btn_calculo_caltotal_calcular.clicked.connect(CalcularCalTotal)
tela_new_main.btn_calculo_cal_calcular.clicked.connect(CalcularCal)
tela_new_main.btn_limpar.clicked.connect(Limpar)

tela_new_main.btn_salvar.clicked.connect(lambda: Salvar(listaUsuario))
app.exec()

if connection.is_connected():
    connection.close()
    cursor.close()