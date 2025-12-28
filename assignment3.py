try:
  file_o=open("sample.txt",'rt')
  linenum=1
  lines=file_o.readlines()
  for line in lines:
   if line.strip()=="":
    continue
   print(f"Line{linenum}:{line.strip()}")
   linenum+=1
except FileNotFoundError:
  print("Error:The file sample.txt not found")
finally:
  file_o.close()
  
  

 #task2
file_obj=open("output.txt",'wt')
cont=input("Enter text to write to the file:")
file_obj.write(cont)
print("Data succesfully written to output.txt")
file_obj.close()
print(" ")

file_obj=open("output.txt",'at')
cont_app=input("Enter additional text to append:")
file_obj.write(f"\n{cont_app}")
print("Data succesfully appended")
file_obj.close()
print(" ")

file_ob=open("output.txt",'rt')
print("Final content of output.txt\n")
fi_r=file_ob.readlines()
for line in fi_r:
 print(line.strip())

file_obj.close()



 
