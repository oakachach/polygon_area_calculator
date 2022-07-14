import shape_calculator

rect = shape_calculator.Rectangle(10, 5)
print(rect.getArea())
rect.setHeight(3)
print(rect.getPerimeter())
print(rect)
print(rect.getPicture())

sq = shape_calculator.Square(9)
print(sq.getArea())
sq.setSide(4)
print(sq.getDiagonal())
print(sq)
print(sq.getPicture())

rect.setHeight(8)
rect.setWidth(16)
print(rect.getAmountInside(sq))