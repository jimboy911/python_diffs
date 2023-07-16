# diff.py
#compares the diffs between two files and then returns the output
#no special modules need to be imported

# importing the required modules  
import difflib #native to python install
from difflib import unified_diff #i have to import this specific thing for some reason
  
# importing file data
f1 = open("file1.txt", "r")
file_1 = f1.readlines()

f2 = open("file2.txt", "r")
file_2 = f2.readlines()

#comparing the two files
diffs = (unified_diff(file_1, file_2)) #this returns an object that an be iterated through with a for loop

w = open("results.txt", "a") #open my file in "append" mode
w.writelines("\n---" + "\nfile_1.txt" + " vs " + "file_2.txt\n") #give this part a header / title

#i can use as for loop to show all my results and save it to a file
#remember that it will keep appending to the file the more i run it
for line in diffs:
    w.writelines(line)

w.close() #gotta close the file after i'm done with it

print("All done!")

#- is everything that was removed from the previous string
#+ is everything that was added
# no + or - means it stayed the same