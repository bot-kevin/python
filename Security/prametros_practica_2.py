import argparse
class Parametros:
    #El parametro **kwargs indica que podemos paras parametros dinamicos
    def __init__(self, **kwargs):
        self.param1 = kwargs.get('parametro1')
        self.param2 = kwargs.get('parametro2')
    def mostrar_parametros(self, parametro):        
        print([parametro.param2,parametro.param1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Params mine")        
    parser.add_argument("-p1", dest="param1", help="parametro1" )
    parser.add_argument("-p2", dest="param2", help="parametro2")

    parametros = parser.parse_args()
    my_parametro = Parametros(parametro1= parametros.param1, parametro2 = parametros.param2)
    my_parametro.mostrar_parametros(my_parametro)
