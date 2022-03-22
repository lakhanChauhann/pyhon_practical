from string import digits
from unicodedata import digit


spell=""
final_word=""
words=("zero","one","two","three","four","five","six","seven","eight","nine")
num=int(input("Enter a number:"))
if(num==0):
    final_word=""
while(num!=0):
    digit=num%10
    num=int(num/10)
    spell+=words[digit]+" "
spell=spell.split(" ")[::-1]
for word in spell:
    final_word+=word+" "
print(final_word)
