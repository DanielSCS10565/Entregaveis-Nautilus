#           ============ Parte 1==============
def pf_iguais(lista):#Função para verificar se primeiro e ultimo item de uma lista são igual
    if lista[0] == lista[-1]:
        print("são iguais")
    else:
        print("há diferenças")

def fat_primos(numero,param = False): #Função que retorna fatoração em numeros primos
    fatoracao = [1]
    contador = 2
    val = numero
    if param == True:
        fatoracao = [1]
        contador = 2
        val = numero
        while val != 1:
           if val%contador == 0:
              val = val/contador
              fatoracao.append(contador)
           else:
              contador +=1
        return fatoracao
    else:
        numero = int(input("Escolha um numero que tenha menos de 100 algarismos:"))
        fatoracao = [1]
        contador = 2
        val = numero
        while val != 1:
            if val%contador == 0:
               val = val/contador
               fatoracao.append(contador)
            else:
               contador +=1
            return fatoracao

def mdp(): # Funao que retorna o maior primo dentro da fatoracao de um numero
    fatoracao = fat_primos()
    return max(fatoracao)
            
def ide_palindromos(objeto_possivel_de_percorrer):
    objeto_possivel_de_percorrer_inv = str(objeto_possivel_de_percorrer)[::-1]
    if str(objeto_possivel_de_percorrer) == objeto_possivel_de_percorrer_inv:
        print("palindromo")
    else:
        print("não é um palindromo")
    

def ide_primo(numero):
    fat = fat_primos(numero,True)
    if fat[-1]==numero:
        return "primo"
    else:
        return "não é primo"

def numera_primos(numero):
    primos = [1]
    for i in range(2,numero):
        if ide_primo(i) == "primo":
            primos.append(i)

    return primos
        

def soma_primos_menores(n):
    return sum(numera_primos(n))


#       ==================== Parte 2 =======================



class Drone():

    def __init__(self,n_motores,n_cameras,anoConstrucao,nome,cor = "Preto",solicitacao_voo = "VLOS"):
        self.n_motores = n_motores
        self.n_cameras = n_cameras
        self.anoConstrucao = anoConstrucao
        self.nome = nome
        self.cor = cor
        self.Tipo_de_voo = solicitacao_voo
        self.cordenada = (0,0,0)#origem
        self.altorizacao_de_voo = ""

    def altorizavoo(self):
        self.altorizacao_de_voo = input("voo altorizado? ")
        return None

    def mododevoo(self):
        self.altorizavoo()
        if self.altorizado_de_voo == "sim":
            print("drone esta apto a voar")
            return "drone esta apto a voar"
        else:
            print("drone não esta apto a voar")
            return "drone não esta apto a voar"

    def controle(self): #uma forma completamente simbolica do que seria o controle do drone
        if mododevoo(self,self.altorizacao_de_voo) == "drone esta apto a voar":
            altura = input(" subindo à qual altura? ")
            esquerda = input( " esquerda: ")
            direita = input("direita: ")
            self.coordenada = (int(altura),int(esquerda),int(direita))
            print("localização do drone é" + str(self.coordenada))
        else:
            return None
    def __str__(self):

        table = f" {'numero de motores'}: | {self.n_motores} \n"
        table += f" {'numero de cameras'}: | {self.n_cameras}  \n"
        table += f" {'ano de construção'}: | {self.anoConstrucao}  \n"
        table += f" {'nome':} | {self.nome}  \n"
        table += f" {'cor do Vant':} | {self.cor}  \n"
        
        
        return table



        
class Drones():
    drones = {}

    def cria_drones(self):
        drones_iniciados = int(input("quantos drones vc quer inserir? "))
        for i in range(drones_iniciados):
            n_motores = int(input("quantos motores vc quer inserir? "))
            n_cameras= int(input("quantas cameras vc quer inserir? "))
            anoConstrucao = int(input("data de construcao? "))
            idd = input(" nome do Vant? ")
            cor = input(" cor do Vant? ")
            self.drones[idd] = Drone(n_motores,n_cameras,anoConstrucao,idd,cor)

    # a ideia era para quando chamasse o DataFrame do pandas
    #ele desse uma tabela com os atributos como
    #colunas e as linhas sendo as "chaves" que no caso são os nomes dos drones
    def exibir_drones(self): 
        df = pd.DataFrame.from_dict(self.drones, orient='index')
        return df

    def exibir_drone(self,drone):
        print(self.drones[drone])

    def rankea(self):
        print(self.drones)
        rank= sorted(self.drones.values(), key=lambda x: x.anoConstrucao)
        for i in range(len(rank)):
            print("i: " + rank[i].nome)
            

    def delet_drone(self,nome):
        del.self.drones[nome]

    def limpar(self):

        clear.self.drones()
        
        













    
        
