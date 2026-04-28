#import pigAge module and call pigAge_converter()
#one pig year is equivalent to five human years
#solution accepts integer input representing a pig's age
#solution outputs the human-equivalent age for a pig

#import pigAge module and call pigAge_converter()
import pigAge

#accept integer input
print("Enter the age of the pig in years:")
input_pigAge = int(input()) 

#call module function pigAge_converter with user input parameter to calculate human equivalent age

human_years = pigAge.pigAge_converter(input_pigAge)

print(f"{input_pigAge} pig years is equivalent to {human_years} in human years")