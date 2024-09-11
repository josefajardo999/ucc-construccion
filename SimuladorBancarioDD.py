__author__ = "Jose David Fajardo Martinez"
__license__ = "GPL"
__version__ = "1.0.0"
+__email__ = "jose.fajardom@campusucc.edu.co"

'''----------------------------------------------------------------
# Importaciones
----------------------------------------------------------------'''
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    
    __cedula=''
    __nombre=''
    
    __cuentaCorriente = CuentaCorriente()
    __cuentaAhorros = CuentaAhorros()
    __cdt = CDT()
    
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    
    __method__='ConsignarCuentaCorriente'
    __params__='Monto'
    __returns__='Nada'
    __descriptions__='Este metodo consignar un monto a la cuenta corriente'
    def ConsignarCuentaCorriente(self, monto):
        # Aqui inicia el metodo
        # self.__cuentaCorriente.saldo = self.__cuentaCorriente.saldo+monto # modo no recomendable
        self.__cuentaCorriente.ConsignarValor(monto)
        
    __method__='CalcularSaldoTotal'
    __params__='Ninguno'
    __returns__='Saldo Total'
    __descriptions__='Este metodo sumo el saldo de todas las cuentas'
    def CalcularSaldoTotal(self):
        # Aqui inicia el metodo
        # forma 1
        total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        return total
    
    __method__='PasarAhorrosACorriente'
    __params__='Ninguno'
    __returns__='Ninguno'
    __descriptions__='Este metodo transfiere el saldo de ahorros a corriente'
    def PasarAhorrosACorriente(self):
        saldoTemporal = self.DarSaldo()
        self.__cuentaAhorros.RetirarValor(saldoTemporal)
        self.__cuentaCorriente.ConsignarValor(saldoTemporal)

    