import argparse
import sys

def get_options():   
    
    parser = argparse.ArgumentParser(description='Python Primer')    
    parser.add_argument('-in_file', action="store", default='infile.txt',
                        dest="in_file", type=str)    
    parser.add_argument('-out_file', action="store", default='outfile.txt', dest="out_file", type=str)
    opts = parser.parse_args(sys.argv[1:])    
        

    return opts