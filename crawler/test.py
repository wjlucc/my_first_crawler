file_object = open('name.txt','w+')
file_object.write("hello")
file_object.write("\n")
file_object.write('jdlfjlkdjfs')
file_object.close()



try:
    a = int('8[')
    print a
except ValueError:
    print '000000'





