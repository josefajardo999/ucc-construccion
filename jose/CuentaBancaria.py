__author__ = "Jose David Fajardo Martinez"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "jose.fajardom@campusucc.edu.co"

class CuentaBancaraia:
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    
    __saldo = 0
    
    #----------------------------------------------------------------
    # Metodos
    #---------------------------------------------------------------- 

    __method__='Ahorro'
    __params__='monto'
    __returns__='ninguno'
    __descriptions__='retirar el monto de la cuenta corriente y lo deposito en la cuenta corriente'
    def Ahorro(self, monto):
        self.__cuentaCorriente=RetirarValor(monto)
        self.__cuentaAhorros=ConsignarValor(monto) 

    __method__='RetirarAhorro'
    __params__='Monto'
    __returns__='Nada'
    __descriptions__='Este metodo retira el monto del ahorro'
    def RetirarAhorro(self, monto):
        self.__cuentaAhorro=self.__cuentaAhorro.retirar(monto)  
    
    __method__='DarSaldoCorriente'
    __params__='Ninguno'
    __returns__='Saldo'
    __descriptions__='Este metodo retorna el saldo'
    def DarSaldoCorriente(self):
        return self.__cuentaCorriente.DarSaldo()

    __method__='DuplicarAhorro'
    __params__='Monto'
    __returns__='Nada'
    __descriptions__='Este metodo duplica el monto del ahorro'
    def DuplicarAhorro(self, monto): 
        self.__cuentaAhorros.ConsignarValor(self.__cuentaAhorro.DarSaldo())
    
    __method__='RetirarTodo'
    __params__='Monto'
    __returns__='cantidad retirada'
    __descriptions__='Este metodo retira el monto de la cuenta'
    def RetirarTodo(self):
        total=self.__cuentaCorriente.DarSaldo() +self.__cuentaAhorro.DarSaldo()
        self.__cuentaCorriente.retirarValor(self.__cuentaCorriente.DarSaldo()) 
        self.__cuentaAhorros.retirarValor(self.__cuentaAhorro.DarSaldo()) 
        return 'usted acaba de retirar '+total 