

import os, math, sys
import matplotlib.pyplot as plt

# A function to plot the data and save it to a file

def makeplot(data,p):
    fts = 14
    fig = plt.figure(figsize=(8, 6))
    ax = plt.gca()
    # plot each data point with a symbol:
    for pt in data:
        ax.plot(pt[0], pt[1], 'o', color='blue')
    for i,txt in enumerate(p):
        pass
        #ax.annotate(txt,(data[i][0], data[i][1]))

    # label axes and put title:
    plt.ylabel('Distance to center', fontsize=fts)
    plt.xlabel('Microtubule length', fontsize=fts)
    plt.title('Simulations', fontsize=fts+4)
    fig.tight_layout()
    
# A function to read the files from the directory files
def process(path):
    """ 
        This extracts the data in one simulation directory
        Assuming the current directory has already been adjusted
    """
    # get parameter value:
    config_file = os.path.join(path,'config.cym')
    aster_file = os.path.join(path,'aster.txt')
    with open(config_file, 'r') as f:
        line = f.readline()
        #print(line)
        pam = float(line[1:])
        f.close()
    # get position of aster:
    with open(aster_file, 'r') as f:
        for line in f:
            if len(line)>3 and not line[0]=='%':
                #print(line)
                val = line.split()
                x = float(val[2])
                y = float(val[3])
                z = float(val[4])
                pos = math.sqrt(x*x+y*y+z*z)
        f.close()
    return (pam, pos)

## Settings
# The folder where the subfolders with the simulations are
parent_folder = 'scan'
# A logical variable indicating wether you want the output to be written into a file
print_file = True
# The name of the file where we want to print the data
file_name = "data.txt"

paths = os.listdir(parent_folder)
paths2 = list()
for i in paths:
    if i[0:3]=='run':
        paths2.append(os.path.join(parent_folder,i))
res = list()
if print_file:
    oldstdout = sys.stdout
    sys.stdout = open(file_name,'w')
for p in paths2:
    val = process(p)
    print("%s %f %f" % (p, val[0], val[1]) )
    res.append(val)
if print_file:
    sys.stdout = oldstdout

print('DONE')
makeplot(res,paths)
plt.savefig('plot', dpi=300)
plt.show()
plt.close()

