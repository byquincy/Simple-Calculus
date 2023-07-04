from calculusCore import printFunction, disintegrate, integrate, getValue
import math

print("[Python을 활용한 좌표 계산기]")
print("x⁴ + 5x + 2를 입력하려면: 1 0 0 5 2")
userInput = input("속력 함수를 입력하세요: ").split()

inputTime = int( input("좌표가 필요한 시간을 입력하세요: ") )
radian = math.radians(
    int( input("각도를 입력하세요: ") )
)
sin = math.sin(radian)
cosin = math.cos(radian)

function = []
for i in userInput:
    try: function.insert(0, int(i))
    except: raise ValueError
print("\n--입력한 함수--")
printFunction(function)
print("-----")

function = integrate(function)
print("적분 결과: ", end='')
printFunction(function)

definiteIntegral = getValue(function, inputTime, c=0) - getValue(function, 0, c=0)
print("부정적분 결과:", definiteIntegral)
print("x좌표:", definiteIntegral*sin)
print("y좌표:", definiteIntegral*cosin)

exit()
