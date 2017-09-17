
with open('swimmers.csv','r') as ins:
    for line in ins:
        l = line.split(';')
        print(';'.join(l[:-1])+';'+l[-1].split()[-1] )
        