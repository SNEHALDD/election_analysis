#Add out dependencies
import csv
import os

#file_to_load = "/Users/snehalborhade/Desktop/UT_Austin_BootCamp/Challeneges/Challenge_3/Resources/election_results.csv"

#Read data from a file
# direct way(1)-Open the election results and read the file
#election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()

# direct way(2) - Second method using "with" function - Open the election results and read the file
#with open(file_to_load) as election_data:

#    print(election_data)

 #Indirect way    
#file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
# os.chdir("/Users/snehalborhade/Desktop/UT_Austin_BootCamp/Challeneges/Challenge_3")
# file_to_save = os.path.join("election_analysis/analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file, set outfile variable
#outfile = open(file_to_save, "w")

# Write some data to the file.
#outfile.write("Hello World")

#close the file
#outfile.close()

#Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

  # Write some data to the file.
  #txt_file.write("Hello World!")

 # Write three counties to the file.
  #txt_file.write("\nArapahoe, Denver, Jefferson")
os.chdir("/Users/snehalborhade/Desktop/UT_Austin_BootCamp/Challeneges/Challenge_3")

  # Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

  # Assign a variable to save the file to a path
file_to_save = os.path.join("election_analysis/analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
  
# Read the file object with the reader function
  file_reader = csv.reader(election_data)

   # Print each row in the CSV file.
   #for row in file_reader:
   # print(row)

  # Print the header row.
  headers = next(file_reader)
  print(headers)
