# Shehraan Hafiz
# July 5, 2023
# Mr. Manyanga
# This program will find the BMI of the user

#Input - Takes the weight of the user (in kilograms), as well as the height of the user (in meters)
symbols = ["`","~","!","@","$","%","^","&","*","(",")","_","+","-","=","/","{","}","|",":",",","<",">","?","'",'"',"[","]"]
numbers = ["1","2","3","4","4","5","6","7","8","9","0"]

#Symbolchecker
def symbol(word):
    for letters in word:
        if (letters in symbols)==True:
            return True
    return False

#Numberchecker
def number(word):
    for letters in word:
        if (letters in numbers)==True:
            return True
    return False
while True:
    massUnit = (input("Choose your desired units to enter your weight.\nEnter 'kg' for kilograms\nEnter 'lb' for pounds\n")).lower()
    while massUnit!="kg" and massUnit!="lb":
        print("Error, please enter one of the given options")
        massUnit = (input("Choose your desired units to enter your weight.\nEnter 'kg' for kilograms\nEnter 'lb' for pounds\n")).lower()
    mass = input("Enter your weight in your chosen units: ")
    while symbol(mass)==True or any(i.isalpha() for i in mass)==True or number(mass)==True:
        symbols = ["`","~","!","@","$","%","^","&","*","(",")","_","+","=","/","{","}","|",":",",","<",">","?","'",'"',"[","]"]
        if symbol(mass)==True:
            print("Error, you entered a symbol which is an invalid input. Please only enter a positive number.")
            mass = input("Enter your weight in your chosen units: ")
        if any(i.isalpha() for i in mass)==True:
            print("Error, you entered a letter which is an invalid input. Please only enter a positive number.")
            mass = input("Enter your weight in your chosen units: ")
        if number(mass)==True:
            if float(mass)<0:
                print("Error, you have entered a negative weight which is impossible. Please enter a positive number.")
                mass = input("Enter your weight in your chosen units: ")
            mass = float(mass)
            if massUnit=="lb":
                mass = mass/2.205
            #Enter real number above minimum weight and below max weight
            if float(mass)<2.1:
                print("Error, you have entered a weight that is likely false as it is less than that of the lightest person recorded. If this is your real weight, please contact the Guinness Book of World Records instead.")
                mass = input("Enter your weight in your chosen units: ")
            elif float(mass)>635:
                print("Error, you have entered a weight that is likely false as it is higher than that of the heaviest person recorded. If this is your real weight, please contact the Guinness Book of World Records instead.")
                mass = input("Enter your weight in your chosen units: ")
            else:
                break

    heightUnit = (input("Choose your desired units to enter your height.\nEnter 'm' for meters\nEnter 'cm' for centimeters\nEnter 'in' for inches\nEnter 'ft' for feet\nEnter 'ftin' for both feet and inches\n")).lower()
    while heightUnit!="m" and heightUnit!="in" and heightUnit!="ft" and heightUnit!="cm" and heightUnit!="ftin":
        print("Error, please enter one of the given options")
        heightUnit = (input("Choose your desired units to enter your height.\nEnter 'm' for meters\nEnter 'cm' for centimeters\nEnter 'in' for inches\nEnter 'ft' for feet\nEnter 'ftin' for both feet and inches\n")).lower()

    if heightUnit!="ftin":
        height = input("Enter your height in your desired units: ")
    else:
        height = input("Please enter your height in feet first (the remainder will be entered later in inches): ")
        
    while symbol(height)==True or any(i.isalpha() for i in height)==True or number(height)==True or massUnit=="ftin":
        if symbol(height)==True:
            print("Error, you entered a symbol which is an invalid input. Please only enter a positive number.")
            if heightUnit=="remainderInches":
                height = input("Please enter the rest of your height in inches: ")
            elif heightUnit=="ftin":
                height = input("Please enter your height in feet first (the remainder will be entered later in inches): ")
            else:
                height = input("Enter your height in your desired units: ")
        if any(i.isalpha() for i in height)==True:
            print("Error, you entered a letter which is an invalid input. Please only enter a positive number.")
            if heightUnit=="remainderInches":
                height = input("Please enter the rest of your height in inches: ")
            elif heightUnit=="ftin":
                height = input("Please enter your height in feet first (the remainder will be entered later in inches): ")
            else:
                height = input("Enter your height in your desired units: ")
        if float(height)<0:
            print("Error, you have entered a negative height which is impossible. Please enter a positive number.")
            height = input("Enter your height in your desired units: ")
            
        if number(height)==True:
            height = float(height)
            if heightUnit=="cm":
                height = height/100
            elif heightUnit=="ft":
                height = height/3.281
            elif heightUnit=="remainderInches":
                height = height + heightinches
                height = height/39.37
                print(height)
                heightUnit="finished"
            elif heightUnit=="ftin":
                heightinches = height*12
                height = input("Please enter the rest of your height in inches: ")
                heightUnit = "remainderInches"
            elif heightUnit=="in":
                height = height/39.37
            if float(height)<0:
                print("Error, you have entered a negative height which is impossible. Please enter a positive number.")
                height = input("Enter your height in your desired units: ")
            if float(height)<0.24 and heightUnit!="remainderInches":
                print("Error, please enter your real height. The height you entered is lower than that of the shortest recorded person. If this is your real height, please contact the Guinness Book of World Records instead.")
                height = input("Enter your height in your desired units: ")
            elif float(height)>2.72 and heightUnit!="remainderInches":
                print("Error, please enter your real height. The height you entered is higher than that of the tallest recorded person. If this is your real height, please contact the Guinness Book of World Records instead.")
                height = input("Enter your height in your desired units: ")
            elif heightUnit!="remainderInches":
                break

    #PROCESS - Calculating the BMI of the user, using their height and mass
    mass = float(mass)
    height = float(height)
    BMI = round(mass/height**2,1)
    
    #Output - Printing the user's BMI score, as well as their resulting classification
    print("Your BMI is: "+str(BMI))
    if BMI<18.5:
        print("You are underweight.\nIn order to bring your weight to a normal level, here is what you can do: \n1. Eat more often\n2. Choose foods with many nutrients\n3. Add extra ingredients to your foods such as sauces and cheese\n4. Drink less before a meal as they can make you feel full and therefore, eat less than you should\n5. Drink heavy beverages such as smoothies and shakes\n6. Exercise, as it can stimulate your appetite and help you increase your weight")
    elif BMI>=18.5 and BMI<25:
        print("Congratulations, you are normal weight! Continue maintaining your healthy weight levels and you shall go on to live a long and fulfilling life.")
    elif BMI>=25 and BMI<30:
        print("You are overweight. \nIn order to bring your weight to a normal level, here is what you can do: \n1. Exercise more\n2. Eat more healthy foods such as fruits and vegetables\n3. Eat less high-calorie foods\n4. Take on a weight-management program\n5. Use weight loss devices.")
    elif BMI>=30 and BMI<35:
        print("You are obese (Class 1) \nIn order to bring your weight to a normal level, here is what you can do:\n1. EXERCISE MORE! This is a recommendation for nearly everyone. Exercising helps stabilize your weight level and even gain muscles!\n2. Use weight-loss medicines (ask your doctor for a prescription first)\n3. Use special diets such as a calorie-restricted diet.\n4. Use intermittent fasting\n4. Eat less salty foods as they can raise your blood pressure which may be dangerous.")
    elif BMI>=35 and BMI<40:
        print("You are obese (Class 2) \nIn order to bring your weight to a normal level, here is what you can do:\n1. EXERCISE MORE! This is a recommendation for nearly everyone. Exercising helps stabilize your weight level and even gain muscles!\n2. Use weight-loss medicines (ask your doctor for a prescription first)\n3. Use special diets such as a calorie-restricted diet.\n4. Use intermittent fasting\n4. Eat less salty foods as they can raise your blood pressure which may be dangerous.")
    else:
        print("You are extremely obese (Class 3)\nUnfortunately, due to your level of obesity, your options to quickly lose weight may be extremely limited. Nonetheless, here they are:\n1. Seek help from your doctor and obtain weight-loss pills\n2. Batriatric surgery which helps you lose weight by altering your digestive system\n3. Get a liposuction, which removes fat from certain areas of the body.\n4. Strictly avoid salty foods as they can raise your blood pressure which may be dangerous.")
    
    redo = (input("If you would like to use this program again, please enter 'y' \nIf you would like to exit the program, please enter 'n': ")).lower()
    while redo!="y" and redo!="n":
        print("Error, please enter one of the given options")
        redo = (input("If you would like to use this program again, please enter 'y' \nIf you would like to exit the program, please enter 'n': ")).lower()
    if redo=="n":
        break
    else:
        print("\nRestarting program\n")
