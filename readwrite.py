f = open("c:\\code\\hello.txt", "r")
f_out = open("c:\\code\\hello_wc.txt", "w")
for line in f:
    tokens = line.split(' ')
    f_out.write("wordcount:"+str(len(tokens))+line)

f.close()
f_out.close()
