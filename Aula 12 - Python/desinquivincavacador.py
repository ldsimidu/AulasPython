desinq = "O desinquivincavacador, das caravelarias desinquivincavacaria as cavidades que deveriam ser desinquivincavacadas."
desinq = desinq.lower()
desinq = desinq.replace('.','')
for char in '.,:;?!':
    desinq = desinq.replace(char,'')
print(desinq)
frequencias = {}
for palavra in desinq:
    if palavra in frequencias.keys():
        frequencias[palavra] += 1
    else:
        frequencias[palavra] = 1
    print(frequencias)