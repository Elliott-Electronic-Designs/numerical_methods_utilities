#this file was made to fill out a template for fortran code
#this should remove some of the tedious work and silly errors that come up when starting new fortran projects
#created by: Forrest Elliott on 04/20/25
#updated: n/a

#functions
def fileNameChecker(fileName):
    allowedChars = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0','_']

    #check for null
    if fileName == [] or fileName == None or fileName == '':
        return False

    #check for special characters
    for char in fileName:
        if char not in allowedChars:
            return False
    
    #check that first character is a letter
    if fileName[0].isalpha() == False:
        return False

    return True

acceptedVersionNums = ['77','90','95','03','08','18']

#get the version number
while True:
    print('Please enter the version of Fortran you want this to be in. Supported Fortran versions by this program are: 77, 90, 95, 03, 08, and 18')

    versionNum = str(input())
    if versionNum not in acceptedVersionNums:
        print('That version is not supported or you did not use the correct format. Please type the last two numbers in the file format you desire--e.g. if you want Fortran90 type in 90 so this program can generate a .f90 file')
        versionNum = str(input())
    else:
        break

#get the program name
#sanitize the input--do not let them put spaces in the file name!
print('Type the name of the prgram you want to create. Please dinnae do anything stupid with it. I suggest using camelCase for readability. Fortran is not case senstiive so if you are going to have multiple simillarly named cases you might want to put some _ in there.')
programName = input()
programNameChecksOut = fileNameChecker(programName)
while programNameChecksOut == False:
    print('WTF Bro. I said dinnae so wack shit. Put in a real program name that follows both fortran and linux naming rules. No special characters except _ and start the file name with a letter for the love of Satan! Try again.')
    programName = input()
    programNameChecksOut = fileNameChecker(programName)


#get intro and optional note
print('Please type in a short introduction to you program to be put in the header. As long or as short as you want.')
intro = input()

optionalNote = None
print('Would you like to add an additional note into the header comments? y/n')
noteExistence = input()
if noteExistence == 'y':
    print('Please enter the note you want to add then.')
    optionalNote = input()

#get author and creation details
print('Please enter your name')
authorName = input()
print('Please enter the date')
date = input()

#actually print out the general structure of the program
bigSectionChar = '='
littleSectionChar = '-'
numSectionChars = 80

#file stuff
fileType = '.f' + versionNum
fileName = programName + fileType
print('file type = ' + fileType)
print('file name = ' + fileName)

try:
    #create/open file
    file = open(fileName, 'x')
    
    #header
    file.write('!' + (numSectionChars * bigSectionChar) + '\n')
    file.write('! ' + fileName + '\n')
    file.write('! ' + intro + '\n')
    if optionalNote != None:
        file.write('! ' + optionalNote + '\n')
    file.write('! Created by ' + authorName + ' on ' + date + '\n')
    file.write('!' + (numSectionChars * bigSectionChar) + '\n')
    file.write('\n\n')
    
    #start
    file.write('!' + (numSectionChars * bigSectionChar) + '\n')
    file.write('PROGRAM ' + programName + '\n')
    file.write('!' + (numSectionChars * bigSectionChar) + '\n')
    file.write('\n\n\n\n\n')
    
    #variables, paramters, and arrays
    file.write('!' + (numSectionChars * bigSectionChar) + '\n')
    file.write('!!! variable decleration !!!' + '\n')
    file.write('! declare parameters here' + '\n')
    file.write('!' + (numSectionChars * littleSectionChar) + '\n')
    file.write('! normal variables go here' + '\n')
    file.write('\n\n\n\n\n')
    
    #executable code
    file.write('!' + (numSectionChars * bigSectionChar) + '\n')
    file.write('!!! executabe code !!!' + '\n')
    file.write('!' + (numSectionChars * littleSectionChar) + '\n')
    file.write('\n\n\n\n\n')
    
    #contains
    file.write('!' + (numSectionChars * bigSectionChar) + '\n')
    file.write('!!! contains section !!!' + '\n')
    file.write('!' + (numSectionChars * littleSectionChar) + '\n')
    file.write('\n\n\n\n\n')
    
    #subroutines
    file.write('!' + (numSectionChars * bigSectionChar) + '\n')
    file.write('!!! subroutines !!!' + '\n')
    file.write('!' + (numSectionChars * littleSectionChar) + '\n')
    file.write('\n\n\n\n\n')
    
    #end program
    file.write('!' + (numSectionChars * bigSectionChar) + '\n')
    file.write('END PROGRAM ' + programName + '\n') 
    file.write('!' + (numSectionChars * bigSectionChar) + '\n')
    
    #close file
    file.close()
except FileExistsError:
    print("File already exists.")


##header
#print('!' + (numSectionChars * bigSectionChar))
#print('! ' + fileName)
#print('! ' + intro)
#if optionalNote != None:
#    print('! ' + optionalNote)
#print('! Created by ' + authorName + ' on ' + date)
#print('!' + (numSectionChars * bigSectionChar))
#print('\n\n')
#
##start
#print('!' + (numSectionChars * bigSectionChar))
#print('PROGRAM ' + programName)
#print('!' + (numSectionChars * bigSectionChar))
#print('\n\n\n\n\n')
#
##variables, paramters, and arrays
#print('!' + (numSectionChars * bigSectionChar))
#print('!!! variable decleration !!!')
#print('! declare parameters here')
#print('!' + (numSectionChars * littleSectionChar))
#print('! normal variables go here')
#print('\n\n\n\n\n')
#
##executable code
#print('!' + (numSectionChars * bigSectionChar))
#print('!!! executabe code !!!')
#print('!' + (numSectionChars * littleSectionChar))
#print('\n\n\n\n\n')
#
##contains
#print('!' + (numSectionChars * bigSectionChar))
#print('!!! contains section !!!')
#print('!' + (numSectionChars * littleSectionChar))
#print('\n\n\n\n\n')
#
##subroutines
#print('!' + (numSectionChars * bigSectionChar))
#print('!!! subroutines !!!')
#print('!' + (numSectionChars * littleSectionChar))
#print('\n\n\n\n\n')
#
##close
#print('!' + (numSectionChars * bigSectionChar))
#print('END PROGRAM ' + programName) 
#print('!' + (numSectionChars * bigSectionChar))

