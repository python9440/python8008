try:
    file=open("myfile.txt","r")
except IOError:
    print("error:unable to read the file!")
finally:
    file.close()
