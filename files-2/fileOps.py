# READING A TEXT FILE
# rainbowFile = open('files/rainbow.txt',"r")
# out = rainbowFile.read(4)
# # print(out)
# outAll=rainbowFile.read()
# # print(outAll)
# rainbowFile.seek(0)
# out_all_again = rainbowFile.read()
# # print(out_all_again)
# rainbowFile.seek(0)
# # oneLine = rainbowFile.readline()
# # print(oneLine)
# allLines = rainbowFile.readlines()
# print(allLines)

sampleFile = open("files/sample_text_rev.text", "w")
# for i in range(3): 
#     a_name = input("Enter the name of the animal: ") 
#     sampleFile.write(a_name) 
#     sampleFile.write("\n") 
# sampleFile.close() #the resources given away will not update properly if not closed
# print("Data is written into the file.") 
# if ran again, it will not append, it will overwrite

colorList = [] 
for i in range(3): 
    a_name = input("Enter the name of a color: ") 
    colorList.append(a_name + '\n') 
    #writing > line
sampleFile.writelines(colorList) 
sampleFile.close() 
print("Data is written into the file.") 


