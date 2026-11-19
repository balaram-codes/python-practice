# write a function that replaces all occurance of "java" with "python" in the above file .
def replace_java():
     with open ("practice.txt","r") as f:
         data = f.read()

     new_data = data.replace("java","python")

     with open ("practice.txt","w") as f:
      f.write(new_data)

replace_java()
with open ("practice.txt", "r") as f:
     print (f.read())


