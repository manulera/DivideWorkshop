#### Tutorial 8.09.2017

cp cytosim/cym/aster.cym config.cym
cp cytosim/bin/sim sim

#### check that sim runs:
./sim

#### check results visually:
./play

#### save result into new directory

mkdir run
mv *.cmo run
cp config.cym run

examine again:
./play run

#### edit config and change parameters


#### vary parameters automatically

#get Preconfig from github
#get collect.py from github
#get scan.py from github

# make config file:
cp config.cym config.cym.tpl

#edit config.cym.tpl:

add text on first line:
[[length=random.uniform(5, 15)]]% [[length]]

replace 
    length=10
by
    length=[[length]]

#generate files:

preconfig config.cym.tpl 64

# prepare directories

collect.py run%04i/config.cym config????.cym

# run simulations

scan.py ../sim nproc=4 run????

# examine some result

./play run0003

# run python script to plot things

./gogo.py




