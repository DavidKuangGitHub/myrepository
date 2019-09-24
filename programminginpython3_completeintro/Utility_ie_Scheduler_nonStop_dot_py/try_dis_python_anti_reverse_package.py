import dis
#try_dis_python_anti_reverse_package.py

def dead_loop():
    while True:
        print('HW')
        
def normal_loop():
    for i in range(10):
        print("Here i = %s " %i)
        
#dis.dis(dead_loop)
dis.dis(normal_loop)

