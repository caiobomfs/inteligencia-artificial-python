from linear_algebra import dot 

def step_function(x) :
    return 1 if x >= 2 else 0 
#P_O is perceptron output # 
    def P_O(weights, bias, x) :
        calculation = dot(weights, x) + bias
        return step_function(calculation)

x0 = [0,0]
x1 = [0.1]
x2 = [1,0]
x3 = [1,1]

weights = [1,1]
bias = 0

saida0 =  P_O (weights, bias, x0)
saida1 =  P_O(weights, bias, x1)
saida2 =  P_O (weights, bias, x2)
saida3 =  P_O (weights, bias, x3)

print ("perceptron boolean and")
print("0 AND 0 =", saida0)
print("0 AND 1 =", saida1)
print("1 AND 0 =", saida2)
print("1 AND 1 =", saida3)