
## Import statements
import os, math, sys
import matplotlib.pyplot as plt

## Defining functions

def makeplot(data,p):
    """
    A function to plot the data and save it to a file
    :param data: data is a list of tuples of the format [(length_1,dist_1),(length_2,dist_2),(length_n,dist_n)]
    :param p: list of strings with the names of the folders containing the simulations
    :return: None
    """
    fts = 14
    fig = plt.figure(figsize=(8, 6))
    ax = plt.gca()
    # plot each data point with a symbol:
    for pt in data:
        ax.plot(pt[0], pt[1], 'o', color='blue')

    # You would activate this if you want the names of the simulations plotted along with the points
    for i,txt in enumerate(p):
        pass
        #ax.annotate(txt,(data[i][0], data[i][1]))

    # label axes and put title:
    plt.ylabel('Distance to center', fontsize=fts)
    plt.xlabel('Microtubule length', fontsize=fts)
    plt.title('Simulations', fontsize=fts+4)
    fig.tight_layout()
    return


def process(path):
    """
    A function to read the files from the simulation folders and return the length and the position of the center of the
     aster as a tuple
    :param path: string containing the path to the simulation folder
    :return: a tuple (length,dist)
    """
    # Path of the files
    config_file = os.path.join(path,'config.cym')
    aster_file = os.path.join(path,'aster.txt')

    ## Get the length of the filaments
    with open(config_file, 'r') as f:
        # We only need the first line to get the value of the length
        line = f.readline()
        # The first character of the line is the % symbol
        pam = float(line[1:])
        f.close()

    ## Get position of aster:
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

## Parameters
# The folder where the subfolders with the simulations are
parent_folder = 'scan'
# A logical variable indicating wether you want the output to be written into a file
print_file = True
# The name of the file where we want to print the data
file_name = "data.txt"
# Paths is a list of strings with all the subfolders in the parent folder ("scan" in this example)
paths = os.listdir(parent_folder)

# We should only keep those folders that are simulation runs, so we create the list path2 which contains only those
# subfolders of which names start with run
paths2 = list()
for i in paths:
    if i[0:3]=='run':
        paths2.append(os.path.join(parent_folder,i))
res = list()

# If we are using print to either print on the console or in a file we can redirect the standard output to a file. We
# keep the original at oldstdout to restore it after, and print DONE to double check
if print_file:
    oldstdout = sys.stdout
    sys.stdout = open(file_name,'w')

# Print formatted values either in the console or in the text file
for p in paths2:
    val = process(p)
    print("%s %f %f" % (p, val[0], val[1]) )
    res.append(val)
# Close file and restore standard output
if print_file:
    sys.stdout.close()
    sys.stdout = oldstdout

print('DONE')
makeplot(res,paths)
# Save the figure to a document
plt.savefig('plot', dpi=300)
plt.show()
plt.close()

