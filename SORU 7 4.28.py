girdi = raw_input("Lütfen sayıları virgülle ayırarak girin: ") 
my_list = [eleman.strip() for eleman in girdi.split(",")]

for index, eleman in enumerate(my_list):
    print "my_list[{}] = {}".format(index, eleman)
