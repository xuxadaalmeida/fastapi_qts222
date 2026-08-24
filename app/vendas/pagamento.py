import time

def processar_pagamento(valor: float) -> bool:
    if valor <= 0:
        return False

    # Simula a latência de rede ou comunicação com API externa
    time.sleep(0.05)
    return True
    
