from collections import Counter

key = raw_input()
decrypted_text = raw_input()


i = 0
a = [10]
b = [10]
j = 0
while (i<30):
    a = Counter(decrypted_text).most_common(i+1)[i]
    print(a)
    #print(a[0])

    # if(j<10):
    #  if (j == 0):
    #   print (decrypted_text.replace(a[0], 'e'))
    #  if (j == 1):
    #   print (decrypted_text.replace(a[0], 't'))
    #  if (j == 2):
    #   print (decrypted_text.replace(a[0], 'a'))
    #  if (j == 3):
    #   print (decrypted_text.replace(a[0], 'o'))
    #  if (j == 4):
    #   print (decrypted_text.replace(a[0], 'i'))
    #  if (j == 5):
    #   print (decrypted_text.replace(a[0], 'n'))
    #  if (j == 6):
    #   print (decrypted_text.replace(a[0], 'r'))
    #  if (j == 7):
    #   print (decrypted_text.replace(a[0], 's'))
    #  if (j == 8):
    #   print (decrypted_text.replace(a[0], 'h'))
    #
    #  j = j + 1

    i = i+1



#print (decrypted_text.replace(' ', 'e'))

#print(a[0])
