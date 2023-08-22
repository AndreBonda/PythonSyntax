# Vengono create due variabili 'var_name' nel Global Namespace e nel
# function Namespace della funzione demo.

def demo():
    var_name = 5
    print("var_name IN the function is", var_name)

var_name = 1
print("var_name OUTSIDE the function is", var_name)
demo()
print("var_name OUTSIDE the function is", var_name)

# var_name OUTSIDE the function is 1
# var_name IN the function is 5
# var_name OUTSIDE the function is 1

# ------------------
def demo_bis():
    print(x) # 1
    # x+=1 -> error
    print(dir()) # [] 

x = 1
demo_bis()

# ---------

def demo_global():
    global y # viene dichiarata nel Global Namespace
    y = 7

demo_global()
y+=1
print(y) # 8