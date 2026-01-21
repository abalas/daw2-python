def divisoresComunes(n,n2):
    divisores = list()
    divisores2 = list()
    if(n==0 or n2 ==0):
        print("No puedo calcular los  divisores comunes de estos números")
    else:
        for i in range(1, int(n // 2 + 1)):
            if (n % i == 0):
                divisores.append(str(i))
            divisores.append(str(n))
        for i in range(1, int(n2 / 2 + 1)):
            if (n % i == 0):
                divisores2.append(str(i))
            divisores2.append(str(n2))
        divisoresTotales = set(divisores) & set(divisores2)
        divisoresOrdenados = sorted(list(divisoresTotales))

        print("Los divisores comunes de ", n, " y ", n2, " son :", ",".join(divisoresOrdenados))


divisores= divisoresComunes(22,16)
