#LUIS ENRIQUE GUZMAN NIÑO S14120070
x=[5,15,20,25]
y=[375,487,450,500]
producto=[]
cuadrados=[]
index=0
index2=0
print ('| x  |  y  |')
print ('| 5  | 375 |')
print ('| 15 | 487 |')
print ('| 20 | 450 |')
print ('| 25 | 500 |')

for a in x:
    #print x[index]*y[index]
    producto.append(x[index] * y[index])
    index=index+1

        #print (x[a])*(y[a])
for b in x:
    #print x[index2]**2
    cuadrados.append(x[index2]**2)
    index2=index2+1

sumx= sum(x)
sumy= sum(y)
sump= sum(producto)
sumc= sum(cuadrados)

despejem1=(sump-((sumx*sumy)/len(x)))
despejem2=sumc-((sumx)**2/len(x))

pendiente= despejem1/despejem2
print ('___________')
print ('')
print ('PENDIENTE: ',pendiente)

despejeb=sumy/len(x)-(pendiente)*sumx/len(x)
print ('INTERSECCION:',despejeb)

pronostico=despejeb+(pendiente*35)
print ('PRONOSTICO PARA UNA CASA DE 35 METROS: ',pronostico)
