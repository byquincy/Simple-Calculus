from calculusCore import printFunction, disintegrate, integrate, getValue

print("[Python을 활용한 부정적분 계산기]")
print("x⁴ + 5x + 2를 입력하려면: 1 0 0 5 2")
userInput = input("함수를 입력하세요: ").split()

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

exit()