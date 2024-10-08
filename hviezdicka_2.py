import time

start=time.perf_counter()

hviezdicka = "*"
#vyska = int(input( "Vyska hviezdicky?" ))
vyska = 6
pocitadlo = vyska

if vyska % 2 == 0:
    vyska += 1

for riadok in range(0, vyska):       
    for i in range(0, vyska):
        print(hviezdicka if (riadok == vyska/2-0.5 or riadok == i or i == vyska/2-0.5 or i == pocitadlo) else(' '), end=' ')
    pocitadlo -= 1      
    print()
    
    
end = time.perf_counter()

print(end - start)
