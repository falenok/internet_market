class Cup:
    def __init__(self, type, color, surface, size):
        #print("Выберите тип кружки")
        self.type = type
        self.color = color
        self.surface = surface
        self.size = size

cup1 = Cup(1,'белый','гладкая','большой')
print(cup1.size,cup1.type,cup1.surface,cup1.color)

