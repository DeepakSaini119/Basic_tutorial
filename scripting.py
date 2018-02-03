#Useful as a convenient replacement for bash scripts.
import os

#use os.system(command) to run a command
os.system('python primer.py output.csv')

#Loops for multiple commands. Variables are readily usable by combining them with the command string
for i in xrange(5):
  os.system('python primer.py output'+str(i)+'.csv')

