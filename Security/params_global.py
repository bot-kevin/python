import argparse

class Parameters:
    """Parametros globales"""
    def __init__(self, **kwargs):
        self.param1 = kwargs.get("param1")
        self.param2 = kwargs.get("param2")
    def view_params(self, input_parameter):
        print (input_parameter.param1)
        print (input_parameter.param2)
parser = argparse.ArgumentParser(description='Para de parametros')
parser.add_argument("-p1", dest="param1", help="parameter1", type="int")
parser.add_argument("-p2", dest="param2", help="parameter2", type="int")

params = parser.parse_args()
input_parameter = Parameters(param1=params.param1, param2=params.param2)
input_parameter.view_params(input_parameter)
