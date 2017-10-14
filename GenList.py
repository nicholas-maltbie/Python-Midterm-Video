"""

Makes a list of random numbers of size n
random numbers are of range [0, n*2)

The program will output a file where the first line is the size of the list and 
the next n lines will contain ranodm numbers.

run program with following format -- 

python3 GenList.py [size] [output_file_name]

"""

if __name__ == "__main__":
    import random
    import sys
    
    if len(sys.argv) == 3:
        try:
            size = int(sys.argv[1])
        except:
            print("Size must be an integer")
            sys.exit(1)
        output = sys.argv[2]
        
        with open(output, 'w') as file_out:
            file_out.write(str(size) + "\n")
            for _ in range(size):
                file_out.write(str(random.randrange(size * 2)) + "\n")
            file_out.close()
    else:
        print("Must specify file and size")
        print("Use format")
        print("  python3 GenList.py [size] [output_file_name]")

