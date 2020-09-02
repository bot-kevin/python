import argparse
parser = argparse.ArgumentParser(description="Paso de parametros y escaneo de puertos")

parser.add_argument("-t", dest="target", help="target 2", required=True)
parser.add_argument("-p", "--port", dest="port", type=int, default=80, help="port to scam defaul:80")
parser.add_argument("-v", dest="verbosity", help="verbosity level",type=int, default=0 )
parser.add_argument("--open", dest="only_open", action="store_true", help="only display open port", default=False)

parameter = parser.parse_args()
print ("Target: ", parameter.target)
print ("Port: ", parameter.port)
print ("Vebosity: ", parameter.verbosity)
print ("Only open: ", parameter.only_open)

