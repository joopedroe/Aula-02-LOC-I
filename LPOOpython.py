class Pessoa:
    def __init__(self,nome,data_nascimento):
        self.nome=nome
        self.data_nascimento=data_nascimento
    def __str__(self):
        return "Pessoa:"+self.nome+"data: "+self.data_nascimento
        
class Projeto:
    def __init__(self,nome,data_inicio,data_fim):
        self.nome=nome
        self.data_inicio=data_inicio
        self.data_fim=data_fim
        

class Atividade:
    def __init__(self,nome,prioridade,pessoa,projeto):
        self.nome=nome
        self.prioridade=prioridade
        self.pessoa=pessoa
    def __str__(self):
        return "Atividade : nome :"+ self.nome +"   Prioridade: "+str(self.prioridade)
class AtividadeProjeto:
    def __init__(self,projeto,atividade):
        self.atividade=atividade
        self.projeto=projeto

class Endereco:
    pass
p=Pessoa("João","03-09-98")
pro=Projeto("Projeto 1","03-02-2019","20-10-2019")
ati=Atividade("Atividade 1",1,p,pro)
print(ati.pessoa.nome,'\n')
print(ati)
pa=AtividadeProjeto(pro,ati)
print(pa.atividade.nome)



        
