#pimport datetime

#print(dir(datetime))
#print(datetime.MAXYEAR)
#pdata = datetime.datetime(2019, 4, 4, 21, 19, 6)
#print(data - datetime.datetime.now())
#today = data + datetime.timedelta(days=367)
#print(today)
#print(today.weekday())
#print(today.strftime("%d/%m/%Y %H:%M:%S"))
#print(datetime.timedelta(days=367))
#print(datetime.datetime.strptime(today.strftime("%d/%m/%Y"), "%d/%m/%Y"))
#print(today.time())

#record = "c ".join(map(str, ["A",2,3,4,5,6,7,8,9,10,"J","Q","K",""])).split(" ")[0:13]
#print(record)

# def soma(a,b):
#     """soma os numeros a e b
#     
#     >>> soma(1 ,2)
#     3
#     """
#     return a + b

class Viver:

    def __init__(self):
        self.comida = None
        self.eh_saudavel = None

    def comer(self, comida, eh_saudavel):
        self.comida = comida
        self.eh_saudavel = eh_saudavel
        return f"comer {comida}" if eh_saudavel else f"nao comer {comida}"

    def dormir(self, num_horas):
        pass
    
    @property
    def comida(self):
        return self._comida
    
    @comida.setter
    def comida(self, valor):
        self._comida = valor

import unittest

class AtividadesTestes(unittest.TestCase):
    
    def setUp(self):
        self.vida = Viver()
    
    def test_comer(self):
        self.assertEqual(self.vida.comer("a", True), "comer a")
        self.assertEqual(self.vida.comer("a", False), "nao comer a")
        self.assertEqual(self.vida.comer("b", True), "comer b")
        self.assertEqual(self.vida.comer("b", False), "nao comer b")
        self.assertNotEqual(self.vida.comer("b", True), "comer c")

    def tearDown(self):
        del self.vida

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AtividadesTestes)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    pass
    #runTests()
else:
    pass
    #unittest.main()

from functools import wraps


def valida_tipo(fn):
    @wraps(fn)
    def converte(valor):
        return int(valor)
    return converte

def formatada(fn):
    @valida_tipo
    def formata(valor):
        """funtion formata"""
        return fn(f"O valor digitado foi: {valor}")
    return formata

@formatada
def imprime_valor(valor):
    """funtion imprime valor"""
    return valor

#print(imprime_valor(23))
#print(imprime_valor("2"))
#print(imprime_valor.__name__)
#print(imprime_valor.__doc__)

import sys
a = []
b = a
#print(sys.getrefcount(a))

if __name__ != '__main__':
    def contagem_regressiva(n):
        while n > 0:
            n -= 1

    def processa(process):
        import time
        contador = 50000000
        inicio = time.time()
        if process == 0:
            from threading import Thread
            t1 = Thread(target=contagem_regressiva, args=(contador//2,))
            t2 = Thread(target=contagem_regressiva, args=(contador//2,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif process == 1:
            contagem_regressiva(contador)
        elif process == 2:
            from multiprocessing import Pool
            pool = Pool(processes=2)
            r1 = pool.apply_async(contagem_regressiva, [contador//2])
            r2 = pool.apply_async(contagem_regressiva, [contador//2])
            pool.close()
            pool.join()
        fim = time.time()
        print(f"tempo em segundos {fim - inicio} para o process: {process}")

    for process_ in range(3):
        processa(process_)


def inteiro(valor: int) -> int:
    return valor * 2
#print(inteiro(2))
#print(inteiro("string"))

class Tipada:

    def __init__(self, valor: str) -> None:
        self.__valor = valor
    
    """
    def __init__(self, valor):
        # type: (str) -> None
        self.__valor = valor
    """

    def valor(self) -> str:
        return self.__valor

t: Tipada = Tipada("valor")
#print(t.__init__.__annotations__)
#print(t.valor.__annotations__)


from functools import reduce


dados = [
    {"id": 1, "valor": 20},
    {"id": 2, "valor": 50},
    {"id": 3, "valor": 150},
    ]

total = reduce(lambda v1, v2 : v1+v2, map(lambda v : v["valor"], dados))
print(total)
print(sum(map(lambda v : v["valor"], dados)))






















