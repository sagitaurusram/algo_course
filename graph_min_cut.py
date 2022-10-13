print('welcome to graph min cut')
fpath = '/Users/srirammadavswamy/Downloads/prog_assign_txt_scc.txt'
file = open(fpath, mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()
my_dict = {}
my_list = []
for line in lines:
    line = line.split(' ')
    line = [i.strip() for i in line]
    line = line[0:2]
    my_list.append(line)

print(my_list)