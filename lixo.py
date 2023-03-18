Fecha_erro3()


def Fecha_nome_usuario():
    format = True
    addlista = True
    if(tela_calculo_imc.tb_nome_usuario.text() == ""):
        Mostra_erro3("vazio")
        format = False
    if(tela_calculo_imc.cb_nome_usuario.isChecked()):
        i = 0
        while(i < len(listaUsuario)):
            if (tela_calculo_imc.tb_nome_usuario.text() == listaUsuario[i].nome):
                Mostra_erro3("existe")
                format = False
                addlista = False
                break
            i+=1
        if(addlista == True and tela_calculo_imc.tb_nome_usuario.text() != ""):
            listaUsuario.append(Usuario(tela_calculo_imc.tb_nome_usuario.text()))
    if (format == True):
        tela_calculo_imc.lbl_imc_usuario.setText(tela_calculo_imc.tb_nome_usuario.text().title())
        tela_calculo_imc.lbl_nome_usuario.hide()
        tela_calculo_imc.btn_nome_usuario_enviar.hide()
        tela_calculo_imc.tb_nome_usuario.hide()
        tela_calculo_imc.cb_nome_usuario.hide()
        tela_calculo_imc.cb_nome_usuario.setChecked(False)



tela_calculo_imc.btn_imc_erro.clicked.connect(Fecha_erro3)
tela_calculo_imc.btn_nome_usuario_enviar.clicked.connect(Fecha_nome_usuario)
tela_calculo_imc.btn_calculo_imc_calcular.clicked.connect(CalcularImc)
tela_calculo_imc.btn_calculo_imc_voltar.clicked.connect(Fecha_calculadora)
tela_main.btn_main_imc.clicked.connect(Abre_calculadora)
tela_main.btn_main_sair.clicked.connect(Fecha_main)

def Mostra_erro3(erro):
    if(erro == "vazio"):
        tela_calculo_imc.lbl_imc_erro.setText("Campo vazio!")
    elif(erro == "formatacao"):
        tela_calculo_imc.lbl_imc_erro.setText("Digite apenas numeros e utilize o ponto flutuante!")
    elif(erro == "existe"):
        tela_calculo_imc.lbl_imc_erro.setText("Usuário ja está salvo!")
    elif(erro == "peso"):
        tela_calculo_imc.lbl_imc_erro.setText("Digite um peso maior que 0!")
    elif(erro == "altura"):
        tela_calculo_imc.lbl_imc_erro.setText("Digite uma altura positiva até 2.5m!")
    tela_calculo_imc.lbl_imc_erro.show()
    tela_calculo_imc.btn_imc_erro.show()


def Abre_calculadora():
    tela_calculo_imc.show()
    tela_calculo_imc.lbl_nome_usuario.show()
    tela_calculo_imc.tb_nome_usuario.show()
    tela_calculo_imc.cb_nome_usuario.show()
    tela_calculo_imc.btn_nome_usuario_enviar.show()
    tela_calculo_imc.lbl_imc_usuario.setText("")
    tela_calculo_imc.tb_main_imc_altura.setText("")
    tela_calculo_imc.tb_main_imc_peso.setText("")
    tela_calculo_imc.tb_nome_usuario.setText("")
    tela_calculo_imc.lbl_imc_resultado.setText("...")


def Fecha_calculadora():
    tela_calculo_imc.hide()


def Fecha_erro3():
    tela_calculo_imc.lbl_imc_erro.hide()
    tela_calculo_imc.btn_imc_erro.hide()