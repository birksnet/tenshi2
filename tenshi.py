#CLASS TENSHI 
#Uma class para construir interface grafica para codigos em python
#Essa Class e baseada na interface TKINTER do python
# Autor: Felipe M A B Huinka

from tkinter import Tk, Frame, scrolledtext, Button, Label, Checkbutton
from os import system,listdir

class tenshi:
    modelo = {}
    esquema = {}
    tk = None
    params = {}
 
    def __init__(self,_params={}):
        self.params = _params
        self.criaJanela()

        self.montaEsquema()

        self.chamaJanela()
    
    def existe(self,_chave,_dicionary):
        for k,v in _dicionary.items():
            if k == _chave:
                return True
        return False

    def criaJanela(self):
        ins = Tk()
        self.tk = ins
        self.iniciando()

    def iniciando(self):
        _params = self.params
        self.params.update({"APP":self.tk})
        if len(_params) > 1:
            if self.existe("titulo",self.params):
                self.tk.title(_params['titulo'])
            else:
                self.tk.title('Janela Padrão Tenshi')
            if self.existe("esquema",self.params):
                self.modelo = self.params['esquema']
            if self.existe("minsize",self.params):
                if len(self.params['minsize']) == 2:
                    self.tk.minsize(self.params['minsize'][0],self.params['minsize'][1] )
    
    def getParam(self,_nomeParam):
        return self.params[_nomeParam]
    def getEsquema(self,_nomeEsquema):
        return self.esquema[_nomeEsquema]
    def chamaJanela(self):
        self.tk.mainloop()

    def montaEsquema(self):
        if len(self.modelo) > 0:
            for k,v in self.modelo.items():
                if self.existe("tipo",v):
                    if self.existe(v['nome'],self.esquema):
                        pass
                    else:
                        self.criaComponente(v)

    def criaComponente(self,_previa = {}):
        novo = None
        pai  = None
        tipo = _previa['tipo']
        if _previa['pai'] == "APP":
            pai = self.tk
        else:
            pai = self.getEsquema(_previa['pai'])
        
        _previa = self.padrao(_previa)
        _previa = self.comando(_previa)

        #tipos de componentes
        if tipo == 'bloco' or tipo == 'frame' or tipo == 'blc':
            novo = Frame(pai)
        if tipo == 'buttom' or tipo == 'botao' or tipo == 'btn':
            novo = Button(pai)
        if tipo =='chb' or tipo == "checkbox" or tipo == 'CheckBox':
            novo = Checkbutton(pai)
        if tipo == 'label' or tipo == 'titulo' or tipo == 'h1' or tipo == 'span':
            novo = Label(pai)

        #setando pack
        if _previa['status']:
            self.fim(novo,_previa['fim'])

        #se o componente foi criado
        if novo != None:      
            self.addAparencia(novo,_previa)
            self.esquema.update({_previa['nome']:novo})

    def addAparencia(self,_componente,_aparencia):
        cp = _componente
        for k,v in _aparencia.items():
            if k == "width" or k == 'largura' or k == 'x':
                cp['width'] = v
            if k == "height" or k == "altura" or k == 'y':
                cp['height'] = v
            if k == "background" or k == 'corFundo' or k == 'bg':
                cp['background'] = v
            if k == "foreground" or k == "cor" or k == "fg" or k == "corTexto":
                cp['foreground'] == 'grey'
            if k == "texto" or k == "txt" or k == "text":
                cp['text'] = v
            if k == 'fonte' or k == 'F':
                cp['font'] = v
            if k == 'fg' or k == 'foreground' or k == 'corTexto':
                cp['foreground'] = v
            if k == 'var' or k == 'variable' or k == 'variavel':
                cp['variable'] = v
                cp['onvalue'] = 1
                cp['offvalue'] = 0
            if k == 'command':
                if isinstance(v,str):
                    cp['command'] = (lambda: self.getRetorna(v))
                else:
                    cp['command'] = (lambda: self.execute(v))

    def execute(self,_funcao):
        ins = _funcao()
        if self.existe('status',ins.params):
            if ins.params['status']:
                if ins.params['pegaComponente'] != '' or ins.params['pegaComponente'] != None:
                     
                    ins.execute({'pegaComponente':self.getEsquema(ins.params['pegaComponente'])})
            

    def getRetorna(self,_cond:str):
        spl = _cond.split("-")
        if spl[0] == 'mostra':
           return self.mostra(spl[1],spl[2])

    def padrao(self,_previa):
        if self.existe('fim',_previa):
            pass
        else: 
            _previa.update({"fim":0})
        if self.existe('status',_previa):
            pass
        else:
            _previa.update({'status':True})
        
        return _previa

    def mostra(self,_nome,_grupo):
        consulta = self.modelo[_nome]
        pg = self.getEsquema(_nome)

        if consulta['status']:
            pass
        else:
            self.statusOff(_grupo)
            consulta['status'] = True
            self.fim(pg,consulta['fim'])


    def comando(self,_conjunto={}):
        if self.existe('exe',_conjunto):
            _conjunto.update({'command':_conjunto['exe']})
        if self.existe('comando',_conjunto):
            _conjunto.update({'command':_conjunto['comando']})
        if self.existe('run',_conjunto): 
            _conjunto.update({'command':_conjunto['run']})
        return _conjunto

    def statusOff(self,_grupo):
        for ki , vi in self.modelo.items():
            if self.existe('grupo',vi):
                if vi['status'] == True and vi['grupo'] == _grupo:
                    alt = self.getEsquema(vi['nome'])
                    alt.pack_forget()
                    vi['status'] = False

    def fim(self,_instancia,_opcao=0):
        if _opcao == 1:
            _instancia.pack(fill="both", side='left')
        if _opcao == 2:
            _instancia.pack( )
        if _opcao == 3:
            _instancia.pack(fill="x")
        if _opcao == 4:
            _instancia.pack(fill="y")
        if _opcao == 0:
            _instancia.pack( expand=True, fill='both', side='left' )

    def escreve():
        print('Isso mesmo')

class teste:
    params = { 'status':True, 'pegaComponente':'Comandos'}
    def execute(self,_params={}):
        cp = _params['pegaComponente']
        cp['text'] = 'Teste'
    

cpp = {
        "Tudo":     {"nome":"Tudo", "pai":"APP" ,"tipo":"bloco"},
        "Menu":     {"nome":"Menu", "pai":"Tudo", "tipo":"bloco", 'bg':'grey', 'largura':200,'fim':1},
        "PG":       {"nome":"PG", "pai":"Tudo" ,"tipo":"bloco", "bg":"#ccc","x":400,'y':200 },
        "Tdo":      {"nome":"Tdo", "pai":"PG" ,"tipo":"bloco", "bg":"#CFCFCF","x":400,'y':200,"fim":3,'grupo':'menu'},
        "Titulo":   {"nome":"Titulo", "pai":"Tdo","tipo":"h1", "fg":'grey', "x":30, "txt":"Sobre a Class Tenshi","fim":3,"F":['Arial',22]},
        "Tdo2":     {"nome":"Tdo2","pai":"PG","tipo":"blc","x":400,"y":400,"bg":"#ccc",'fim':3,'status':False,'grupo':'menu'},
        "btn1":     {"nome":"btn1","pai":"Menu","tipo":"botao","x":20,"fim":2, "txt":"INICIO","comando":'mostra-Tdo-menu'},
        "btn2":     {"nome":"btn2","pai":"Menu","tipo":"btn","fim":2,"txt":"Comandos Servidores","x":20,"exe":'mostra-Tdo2-menu'},
        "Comandos": {"nome":"Comandos","pai":"Tdo2","tipo":"h1",'x':30,'fim':3,"txt":"Comandos para Servidores",'F':['Arial',22]},
        "ComandosPg":{"nome":"ComandosPg",'pai':'Tdo2','tipo':'blc','x':350,'y':300,'bg':'red'},
        "ComandosMn":{"nome":"ComandosMn",'pai':'Tdo2','tipo':'blc','x':150,'y':200,'bg':'grey','fim':1},
        "btnC1":    {"nome":'btnC1','pai':'ComandosMn','tipo':'btn','txt':'Abrir SSH','fim':2,'exe':teste},
        "check":    {'nome':"check",'pai':'ComandosPg','tipo':'chb','txt':'Teste CheckBox','var':'teste','fim':1}
    } 



cll = tenshi({'titulo':'Resumo Tenshi Interface','esquema':cpp,'minsize':[500,400]})

