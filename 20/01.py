string = "cats dog CAT DOGGY monkey"
lst = string.split()
sorted_string = ' '.join(sorted(lst,key=str.lower))
print(sorted_string)
