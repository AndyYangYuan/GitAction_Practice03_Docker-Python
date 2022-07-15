import boto3
import pandas
import pytz
import sys
import getopt

def process_exit(code):
    print(f'Extraction process finished with code: {code}')
    exit(code)

def main():
    source_name = ''
    # Get source_name from input parameter
    try:
        if(len(sys.argv)!=3):
            print("Usage: %s -s source_name" % sys.argv[0])
            process_exit(101)
        opts,args = getopt.getopt(sys.argv[1:],"s:")
        for opt, arg in opts:
            if opt == "-s":
                source_name = arg
    except getopt.GetoptError:
        print("Usage: %s -s source_name" % sys.argv[0])
        process_exit(201)
    
    # Main Process
    # TODO:

if __name__ == "__main__":
    main()