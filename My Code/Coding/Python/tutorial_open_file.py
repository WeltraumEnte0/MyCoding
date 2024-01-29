


if __name__ == "__main__":


    with open("text") as myfile:
     data = open('text', 'r+')
     total_lines = sum(1 for line in myfile)
    total_lines = total_lines + 1

    data.write(str(total_lines))
    data.close()


"""     data = open('text', 'r+')
    i = len(data.readline(1)) #len(data)
    data.write("\nnummer" + str(i))
    data.close() """






""" 
'''
    file = open('text', 'a')
    file.write("\n3. Zeile")



    file = open('text', 'r') #hier wird gespeichert was in der Datei steht
    for line in file: 
        #print(file.read()) #gesamte Datei lesen
        #print(file.read(3))
        #print(line)
        #print(file.readline())
        #print(line)
''' """


    