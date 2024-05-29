from os import *
from math import *
from datetime import *
import os
import time
from tabulate import tabulate
import schedule

class Médico:
    medicos_cadastrados = [

    ]
    def __init__(self, nome_med, idade_med, sexo_med, crm, uf_crm, especialidade_med):
        self.nome_med = nome_med
        self.idade_med = idade_med
        self.sexo_med = sexo_med
        self.crm = crm
        self.uf_crm = uf_crm
        self.especialidade_med = especialidade_med

    @classmethod
    def cadastrarMedico(cls, nome_med, idade_med, sexo_med, crm, uf_crm, especialidade_med):
        novo_medico = Médico(nome_med, idade_med, sexo_med, crm, uf_crm, especialidade_med)
        Médico.medicos_cadastrados.append(novo_medico)
        return novo_medico

    def __str__(self):
        return f'Nome: {self.nome_med}, Idade: {self.idade_med}, Sexo: {self.sexo_med}, CRM: {self.crm}, UF(CRM): {self.uf_crm}, Especialidade: {self.especialidade_med}'


class Enfermeiro:
    enfermeiros_cadastrados = [

    ]
    def __init__(self, nome_enf, idade_enf, coren, sexo_enf):
        self.nome_enf = nome_enf
        self.coren = coren
        self.idade_enf = idade_enf
        self.sexo_enf = sexo_enf

    @classmethod
    def cadastrarEnfermeiro(cls, nome_enf, idade_enf, coren, sexo_enf):
        novo_enfermeiro = Enfermeiro(nome_enf, coren, idade_enf, sexo_enf)
        Enfermeiro.enfermeiros_cadastrados.append(novo_enfermeiro)
        return novo_enfermeiro


class Paciente:
    pacientes_cadastrados = [

    ]
    def __init__(self, nome_pac, rg, cpf, idade_pac: int, sexo_paciente, convenio):
        self.nome_pac = nome_pac
        self.rg = rg
        self.cpf = cpf
        self.idade_pac = idade_pac
        self.sexo_paciente = sexo_paciente
        self.convenio = convenio

    @classmethod
    def cadastrarPaciente(cls, nome_pac, rg, cpf, idade_pac: int, sexo_paciente, convenio):
        novo_paciente = Paciente(nome_pac, rg, cpf, idade_pac, sexo_paciente, convenio)
        Paciente.pacientes_cadastrados.append(novo_paciente)
        return novo_paciente
    
    def __str__(self):
        return f'Nome: {self.nome_pac}, RG: {self.rg}, CPF: {self.cpf}, Idade: {self.idade_pac}, Sexo: {self.sexo_paciente}, Convênio: {self.convenio}'

        
class Consulta:
    consultas_marcadas = [

    ]
    def __init__(self, dia, horario, motivo, medico_disponivel):
        self.dia = dia
        self.horario = horario
        self.motivo = motivo
        self.medico_disponivel = medico_disponivel
    
    @classmethod
    def agendarConsulta(cls, dia, horario, motivo, medico_disponivel):
        nova_consulta = Consulta(dia, horario, motivo, medico_disponivel)
        return nova_consulta
    
class Acessorio:
    acessorios_cadastrados = []

    def __init__(self, nome_acs, marca, quantidade, valor_total, valor_unitario):
        self.nome_acs = nome_acs
        self.marca = marca
        self.quantidade = quantidade
        self.valor_total = valor_total
        self.valor_unitario = valor_unitario


    @classmethod
    def cadastrarAcessorio(cls, nome_acs, marca, quantidade, valor_total, valor_unitario):
        novo_acessorio = Acessorio(marca, nome_acs, quantidade, valor_total, valor_unitario)
        Acessorio.acessorios_cadastrados.append(novo_acessorio)

def agendarConsulta():
    os.system('cls')
    #Nome do paciente (deve estar na lista de pacientes cadastrados)
    #Motivo da consulta
    #Médico (deve ser um medico existente)
    #Dia da consulta (dia disponivel)
    #Hora da consulta (horario disponivel)       
    
def cadastrarpaciente():
    os.system('cls')
    nome_pac = input('| Nome do Paciente: ')
    rg0 = input('| RG do Paciente: ')
    rg = '{}.{}.{}-{}'.format(rg0[:2], rg0[2:5], rg0[5:8], rg0[8:])
    cpf0 = input('| CPF do Paciente: ')
    cpf = '{}.{}.{}-{}'.format(cpf0[:3], cpf0[3:6], cpf0[6:9], cpf0[9:])
    idade_pac = int(input('| Idade do Paciente: '))
    sexo_paciente = input('| Sexo (M/H): ')
    convenio = input('| Convênio Médico: ')
    Paciente.cadastrarPaciente(nome_pac, rg, cpf, idade_pac, sexo_paciente, convenio)  
    time.sleep(0.6)
    print('| Paciente cadastrado com sucesso!')
    time.sleep(0.6)
    print('| Retornando ao menu principal')

def pacientesOpcoes():
  os.system('cls')
  print('MENU PACIENTES')
  print('')
  print('A | Exibir Pacientes Cadastrados')
  print('B | Cadastrar Paciente')
  print('')
  escolha_paciente = input('ESCOLHA A OPÇÃO DESEJADA: ')
  escolha_paciente = escolha_paciente.lower()
  if escolha_paciente == 'a':
      os.system('cls')
      pacientes_table = []
      for paciente in Paciente.pacientes_cadastrados:
          paciente_info = [paciente.nome_pac, paciente.rg, paciente.cpf, paciente.idade_pac, paciente.sexo_paciente, paciente.convenio]
          pacientes_table.append(paciente_info)

      headers = ["Nome", "RG", "CPF", "Idade", "Sexo", "Convênio"]
      print(tabulate(pacientes_table, headers=headers, tablefmt="grid"))      
      volta = input('Digite ENTER para voltar.')


  elif escolha_paciente == 'b':
      cadastrarpaciente()
      time.sleep(1.6)
      menuOpcoesSimples()
      
def cadastrarMédico():
    os.system('cls')
    nome_med = input('| Nome do Médico: ')
    idade_med = int(input('| Idade do Médico: '))
    sexo_med = input('| Sexo (M/H): ')
    crm = input('| CRM : ')
    uf_crm = input('| UF (CRM): ')
    especialidade_med = input('| Especialidade: ')
    Médico.cadastrarMedico(nome_med,idade_med, sexo_med, crm, uf_crm, especialidade_med)
    print('| Médico cadastrado com sucesso!')
    time.sleep(0.6)
    print('| Retornando ao menu principal')

def medicosOpcoes():
     os.system('cls')
     print('MENU MÉDICOS')
     print('')
     print('A | Exibir Médicos Cadastrados')
     print('B | Cadastrar Médico')
     print('')
     escolha_medico = input('ESCOLHA A OPÇÃO DESEJADA: ')
     escolha_medico = escolha_medico.lower()
     if escolha_medico == 'a':
         os.system('cls')
         medicos_table = []
         for medico in Médico.medicos_cadastrados:
             medico_info = [medico.nome_med, medico.idade_med, medico.sexo_med, medico.crm, medico.uf_crm, medico.especialidade_med]
             medicos_table.append(medico_info)
         headers = ["Nome", "Idade", "Sexo", "CRM", "UF CRM", "Especialidade"]
         print(tabulate(medicos_table, headers=headers, tablefmt="grid"))
         volta = input('Digite ENTER para voltar.')


     elif escolha_medico == 'b':
         cadastrarMédico()
         time.sleep(1.6)
         menuOpcoesSimples()


def cadastrarEnfermeiro():
    os.system('cls')
    nome_enf = input('| Nome do Enfermeiro: ')
    idade_enf = int(input('| Idade do Enfermeiro: '))
    sexo_enf = input('| Sexo (M/H): ')
    coren = input('| COREN : ')
    Enfermeiro.cadastrarEnfermeiro(nome_enf, idade_enf, coren, sexo_enf)
    print('| Enfermeiro cadastrado com sucesso!')
    time.sleep(0.6)
    print('| Retornando ao menu principal')


def enfermeiroOpcoes():
    os.system('cls')
    print('MENU ENFERMEIROS')
    print('')
    print('A | Exibir Enfermeiros Cadastrados')
    print('B | Cadastrar Enfermeiro')
    print('')
    escolha_enfermeiro = input('ESCOLHA A OPÇÃO DESEJADA: ')
    escolha_enfermeiro = escolha_enfermeiro.lower()
    if escolha_enfermeiro == 'a':
        os.system('cls')
        enfermeiros_table = []
        # nome_enf, coren, idade_enf: int, sexo_enf
        for enfermeiro in Enfermeiro.enfermeiros_cadastrados:
            enfermeiro_info = [enfermeiro.nome_enf, enfermeiro.idade_enf, enfermeiro.coren, enfermeiro.sexo_enf]
            enfermeiros_table.append(enfermeiro_info)
        headers = ["Nome", "Idade", "COREN", "Sexo" ]
        print(tabulate(enfermeiros_table, headers=headers, tablefmt="grid"))
        volta = input('Digite ENTER para voltar.')

    elif escolha_enfermeiro == 'b':
        cadastrarEnfermeiro()
        time.sleep(1.6)
        menuOpcoesSimples()



def cadastrarAcessorios():
    os.system('cls')
    nome_acs = input('| Nome do Acessório: ')
    marca_acs = input('| Marca do Acessório: ')
    quantidade_acs = int(input('| Quantidade comprada: '))
    valor_total = float(input('| Valor total da compra: R$'))
    valor_unitario = valor_total / quantidade_acs if quantidade_acs != 0 else 0
    valor_total_formatado = "R${:,.2f}".format(valor_total)
    valor_unitario_formatado = "R${:,.2f}".format(valor_unitario)
    Acessorio.cadastrarAcessorio(nome_acs ,marca_acs, quantidade_acs, valor_total_formatado, valor_unitario_formatado)
    print('| Acessório cadastrado com sucesso!')
    time.sleep(0.6)
    print('| Retornando ao menu principal')



def acessoriosOpcoes():
    os.system('cls')
    print('MENU ACESSÓRIOS')
    print('')
    print('A | Exibir Acessórios Cadastrados')
    print('B | Cadastrar Acessório')
    print('')
    escolha_acessorio = input('DIGITE A OPÇÃO DESEJADA: ')
    escolha_acessorio = escolha_acessorio.lower()
    if escolha_acessorio == 'a':
        os.system('cls')
        acessorios_table = []
        for acessorio in Acessorio.acessorios_cadastrados:
            acessorio_info = [acessorio.nome_acs ,acessorio.marca, acessorio.quantidade, acessorio.valor_unitario]
            acessorios_table.append(acessorio_info)
        headers = ["Nome" ,"Marca", "Quantidade", "Valor Unitário"]
        print(tabulate(acessorios_table, headers=headers, tablefmt="grid"))
        volta = input('Digite ENTER para voltar ao menu principal.')
        menuOpcoesSimples()

    elif escolha_acessorio == 'b':
        cadastrarAcessorios()
        time.sleep(1.6)
        menuOpcoesSimples()

def remedioOpcoes():
    pass
          
def menuOpcoesSimples():
    os.system('cls')
    print('𝐀𝐌𝐑𝐌 𝐒𝐘𝐒𝐓𝐄𝐌')
    print('')
    print('1 - Pacientes')
    print('2 - Médicos')
    print('3 - Enfermeiros')
    print('4 - Medicamentos')
    print('5 - Acessórios Hospitalares')
    print('')
    escolha1 = input('DIGITE A OPÇÃO ESCOLHIDA: ')
    if escolha1 == '1':
        time.sleep(1)
        pacientesOpcoes()
    elif escolha1 == '2':
        time.sleep(1)
        medicosOpcoes()
    elif escolha1 == '3':
        time.sleep(1)
        enfermeiroOpcoes()
    elif escolha1 == '4':
        time.sleep(1)
        remedioOpcoes()
    elif escolha1 == '5':
        time.sleep(1)
        acessoriosOpcoes()
    else:
        time.sleep(1)
        print('Opção inválida! Selecione uma opção existente.')
        time.sleep(1.2)
        print('')
        print('Voltando ao menu principal ...')
        menuOpcoesSimples()

menuOpcoesSimples()