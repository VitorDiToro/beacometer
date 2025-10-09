import math


class DistanceCalculator:
    def __init__(self, tx_power: int = -59, path_loss_exponent: float = 2.0):
        self.tx_power = tx_power
        self.path_loss_exponent = path_loss_exponent
    
    def calculate(self, rssi: int) -> float:
        if rssi == 0:
            return -1.0
        
        ratio = (self.tx_power - rssi) / (10 * self.path_loss_exponent)
        distance = math.pow(10, ratio)
        
        return round(distance, 2)