from calculusCore import printFunction, disintegrate, integrate, getValue

print("[Python을 활용한 정적분 계산기]")
print("x⁴ + 5x + 2를 입력하려면: 1 0 0 5 2")
userInput = input("함수를 입력하세요: ").split()

a = int( input("첫 번째 값을 입력하세요: ") )
b = int( input("두 번째 값을 입력하세요: ") )

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

definiteIntegral = getValue(function, a, c=0) - getValue(function, b, c=0)
print("부정적분 결과:", definiteIntegral)

exit()