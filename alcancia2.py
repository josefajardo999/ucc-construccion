__author__ = "jose david fajardo martinezo"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "jose.fajardom@campusucc.edu.co"

class Alcancia:
    
    totalAhorrado=0
    monedas50=0
    monedas100=0
    monedas200=0
    monedas500=0
    monedas1000=0 
    
    '''---------------------------------------------------------------
    # methods 
    ------------------------------------------------------------------'''
    
    __method__='AgregarMoneda50'
    __params__='nada'
    __returns__='Nada'
    __descriptions__='Agregar una moneda de $50 al saldo de la alcancia'
    def AgregarMoneda50(self):
        self.moneda50 += 1  
        
    __method__='AgregarMoneda500'
    __params__='nada'
    __returns__='Nada'
    __descriptions__='Agregar una moneda de $500 al saldo de la alcancia'   
    
    def AgregarMoneda500(self): 
        self.moneda500 += 1 
        
    __method__='darTotalDinero'
    __params__='nada'
    __returns__='un numero enetro representa el total de la alcancia '
    __descriptions__='duelve el total del dinero ahorrado en la alcancia'    
    
    def darTotalDinero(self):
        TotalDinero = self.moneda50+self 