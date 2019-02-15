class Pessoa():
    def __init__(self,nome,data_nascimento):
        self.nome=nome
        self.data_nascimento=data_nascimento
    def mudarNome(self,nome):
        self.nome=nome
        
class Projeto():
    def __init__(self,nome,data_inicio,data_fim):
        self.nome=nome
        self.data_inicio=data_inicio
        self.data_fim=data_fim
        

class Atividade():
    def __init__(self,nome,prioridade,nomePessoa,nasci,nomePro,inicio,fim):
        self.nome=nome
        self.prioridade=prioridade
        self.pessoa=Pessoa(nomePessoa,nasci)
        self.projeto=Projeto(nomePro,inicio,fim)

p=Atividade("Troca de gerência","Máxima","João","03/09/98","Mudança de cargo","2018","2019")
print(p.pessoa.nome,'\n')
p.pessoa.mudarNome("Pedro")
print(p.pessoa.nome)



        
