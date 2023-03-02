##
#  Read a database of per capita income by country and allow the user to
#  query it.
#

# Load the data into a dictionary.
incomes = {}
inf = open("rawdata_2004.txt", "r")
for line in inf:
   parts = line.split("\t")

   # Remove the dollar sign and comma.
   parts[2] = parts[2].replace("$", "")
   parts[2] = parts[2].replace(",", "")

   # Add the country to the dictionary.
   #incomes[parts[1].upper()] = float(parts[2])
   
   country = parts[1].upper()
   if country[0] in incomes :
       incomes[country[0]].append(country)
   else :
        incomes[country[0]] = [country]
       

# Read queries from the user and respond to them.
letter = input("Enter a letter (or type quit to quit): ").upper()
while letter != "QUIT" :
   if letter in incomes :
      print("Countries starting with", letter, ":")
      for country in incomes[letter] :
          print(country)
   else :
      print("No countries starting with", letter)
   print()
   letter = input("Enter a letter (or type quit to quit): ").upper()

   # Read the next country from the user.
   #country = input("Enter a country name (or type quit to quit): ").upper()

