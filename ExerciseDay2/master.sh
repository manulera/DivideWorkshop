#!/usr/bin/env bash


## Basically a script to run the whole exercise and check that it works properly

# Destroy any previous data

rm -rf ./scan

# Make the folder where all the simulation folders will be

mkdir scan

# Use preconfig.py to make a bunch of config files

./preconfig.py 300 ./config.cym.tpl scan

# Use collect to put all the config files in subfolders with formatted names

./collect.py ./scan/run%04i/config.cym scan/config????.cym

# Run simulations in parallel (This will take a while)

./scan.py ./sim nproc=8 scan/run????

# Include the result files in svn so that they are sent to github

cd ..
git add ExerciseDay2/scan/run0*/aster.txt

# This is the step where the students have to make their own python script and analyse the data

