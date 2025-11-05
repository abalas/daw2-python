profesoresPrimero= {"Natalia", "José María", "Pedro", "Yago"}
profesoresSegundo = {"José María", "Agustín", "Puche", "Pedro"}

print(profesoresPrimero & profesoresSegundo)
print(profesoresPrimero - profesoresSegundo)
print(profesoresSegundo - profesoresPrimero)
print(profesoresPrimero | profesoresSegundo)


print(profesoresPrimero.intersection((profesoresSegundo)))
print(profesoresPrimero.union(profesoresSegundo))
print(profesoresPrimero.difference(profesoresSegundo))
print(profesoresSegundo.difference(profesoresPrimero))