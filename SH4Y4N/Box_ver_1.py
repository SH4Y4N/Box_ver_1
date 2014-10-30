# Programmed By SH4Y4N
# Ashiyane Digital Security Team

import base64 as box

ban1='--|| Ashiyane Hash Box ver.1 ||--'

ban2='--|| By SH4Y4N ||--'

print '\n\n'

print ban1.center(90, ' ')
print ban2.center(90, ' ')

choise = raw_input('''

For Base64 Encode /Decode    Enter : B64

For Box    Encode /Decode    Enter : BOX

''')

if choise.upper() == 'BOX' :

 whaten = raw_input('''

 If You Want To Create New Box Hash   Enter : EN

 If You Want To Crack Box Hash        Enter : DE \n\n''')

 if whaten.upper() == 'EN' :
   whato = raw_input("\n\n Enter your Text Please :\n")
   elmon=""
   for i in whato :
     elmon += hex(ord(i)).split("x")[1]
     elmin = box.b64encode(box.b64encode(elmon))
   finone = elmin + 'b0x'
   print 'Your BOX Hash Is :: '+finone

 if whaten.upper() == 'DE' :
   wsti = raw_input("Enter Your Hex Please : \n")
   wait = wsti.replace("b0x" , "")
   wol = box.b64decode(box.b64decode(wait))  
   nitro = wol.decode('hex')
   print nitro

if choise.upper() == 'B64' :
 elem = raw_input('''
 
 If You Want To Create New Base64 hash   Enter : A
 
 If You want To Crack Base64 Hash        Enter : B
 
 ''')
 if elem.upper() == 'A' :
  new_b = raw_input("\nEnter Your Text First : \n\n")
  new_hash = box.b64encode(new_b)
  print '\n Your Base64 Hash Is ::   '+new_hash
 if elem.upper() == 'B' :
  crack_b = raw_input("\nEnter Your base64 Hash  : \n\n")
  crack_hash = box.b64decode(crack_b)
  print 'The Result Is ::  ' + crack_hash
  

raw_input('')
