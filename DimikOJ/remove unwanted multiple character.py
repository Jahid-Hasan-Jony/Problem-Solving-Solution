bad_chars = [';', ':', '!', "*",".",","] 
  
name = input()

name = ''.join(i for i in name if not i in bad_chars) 

print (str(name))