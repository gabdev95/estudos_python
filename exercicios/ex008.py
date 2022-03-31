# Escreva um programa que leia um valor em metros e exiba convertido em cm e mm.
# Extra: leia uma medida em metros e converter em km, hm, dam e dm também (km, hm, dam, m, dm, cm, mm)
medida = float(int(input('Digite a medida em metros: ')))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida dada foi: {}m. Isso equivale a:'.format(medida))
print('Quilômetros: {}km;'.format(km))
print('Hectômetros: {}hm;'.format(hm))
print('Decâmetros: {}dam;'.format(dam))
print('Decímetros: {}dm;'.format(dm))
print('Centímetros: {}cm;'.format(cm))
print('Milímetros: {}mm'.format(mm))
