class Rectangle :
    def __init__(self, _width, _height) :
        self.width = _width
        self.height = _height

    def setWidth(self, _width) :
        self.width = _width

    def setHeight(self, _height) :
        self.height = _height

    def getArea(self) :
        return self.width * self.height

    def getPerimeter(self) :
        return (2 * self.width + 2 * self.height)

    def getDiagonal(self) :
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def getPicture(self) :
        pictureString = ""
        if self.width > 50 or self.height > 50 :
            return "Too big for picture."
        
        for i in range(0, self.height) :
            for j in range(0, self.width - 1) :
                pictureString += "*"
            pictureString += "*\n"
        
        return pictureString


    def getAmountInside(self, _shape) :
        parentArea = self.getArea()
        sonArea = _shape.getArea()
        return int(parentArea / sonArea)

    def __str__(self) :
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"


class Square(Rectangle) :
    def __init__(self, _sideLength) :
        self.width = _sideLength
        self.height = _sideLength
    
    def setSide(self, _sideLength) :
        self.width = _sideLength
        self.height = _sideLength
    
    def __str__(self) :
        return "Square(side=" + str(self.width) + ")"
        