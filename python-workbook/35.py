dog_year = int(input("How old is your dog?: "))
if(dog_year <= 2):
  print("Your Dog is", dog_year * 10.5, "Years Old")
if(dog_year > 2):
  print("Your dog is", 2*10.5 + (dog_year - 2) * 4, "Years Old")
