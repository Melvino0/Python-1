mil2 = int(input('Mätarställning i dag'))
mil1 = int(input('Mätarställning för ett år sedan? '))
print('antal körda mil:', mil2 - mil1)
liter = float(input('a§ntal liter bensin? '))
print(f'förbrukning per mil: {liter/(mil2-mil1):.2f}')