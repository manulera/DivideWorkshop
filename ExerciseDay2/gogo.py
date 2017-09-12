#!/usr/bin/env python
# Copyright F. Nedelec, Sept. 2017

"""
    Collect data from given run directories, and make a plot

Syntax:

    gogo.py DIRECTORIES
    
Example:

    gogo.py run???? > data.txt

Description:

    This script is used to analyze Cytosim's simulations

F. Nedelec, 8 Sep 2017
"""

import sys, os, subprocess, math
import matplotlib.pyplot as plt

#------------------------------------------------------------------------

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
    
#------------------------------------------------------------------------

def process(path):
    """ 
        This extracts the data in one simulation directory
        Assuming the current directory has already been adjusted
    """
    # get parameter value:
    with open('config.cym', 'r') as f:
        line = f.readline()
        #print(line)
        pam = float(line[1:])
        f.close()
    # get position of aster:
    with open('aster.txt', 'r') as f:
        for line in f:
            if len(line)>3 and not line[0]=='%':
                #print(line)
                val = line.split()
                x = float(val[2])
                y = float(val[3])
                #z = float(val[4])
                #pos = math.sqrt(x*x+y*y+z*z)
                pos = math.sqrt(x*x+y*y)

        f.close()
    return (pam, pos)

#------------------------------------------------------------------------

def main(args):
    curdir = os.getcwd()
    paths = []
    res = []
    for arg in args:
        if os.path.isdir(arg):
            paths.append(arg)
        else:
            sys.stderr.write("  Error: unexpected argument `%s'\n" % arg)
            sys.exit()
    
    if not paths:
        sys.stderr.write("  Error: you must specify directories\n")
        sys.exit()
    
    for p in paths:
        os.chdir(p)
        val = process(p)
        print("%s %f %f" % (p, val[0], val[1]) )
        res.append(val)
        os.chdir(curdir)
    
    makeplot(res,paths)
    plt.savefig('plot', dpi=300)
    plt.show()
    plt.close()

#------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1]=='help':
        print(__doc__)
    else:
        main(sys.argv[1:])
