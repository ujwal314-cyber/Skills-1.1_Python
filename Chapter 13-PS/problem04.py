l=[2,45,6,730,80,20,76,56,34,24,56,87,95]
def div(n):
    if n%5==0:
        return True
    return False # Here there is no need of else because if if statement is not executed then there is only one statement after it which will be executed and however after return nothing will be executed

five=list(filter(div,l))
print(five)