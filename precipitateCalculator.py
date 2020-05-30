"""
title: precipitate calculator
author: Chelsea Chen
date created: 2020-05-27
"""
# --- Variables/Arrays --- #
ionName = (("Li",1), ("Mg",2), ("Ca",2), ("Sr",2),("Ba",2),("Fe",2),("Hg2",2), ("Pb",2), ("F",1), ("Cl",1), ("Br",1), ("I",1), ("Cu",1), ("Ag",1), ("Tl",1), ("SO4",2), ("Ra",2), ("NH4",1), ("NO3",1), ("ClO4",1), ("CH3COO",1), ("RbClO4",1), ("CsClO4",1), ("AgCH3COO",1), ("Hg2(CH3COO)2",1),("H",1),("Na",1), ("K",1), ("Rb",1), ("Cs",1), ("Fr",1))
ionMass =(6.94, 24.31, 40.08, 87.62, 137.33, 55.85, 401.18, 207.2, 19.0, 35.45,79.90,126.90,63.55,107.87,204.38,96.06,226, 18.039, 62.0049,99.451,59.05, 184.918, 232.36,167.03,519.28, 1.01, 22.99, 39.1, 85.47, 132.91, 223)
again = True
# --- Inputs --- #
def intro():
    """
    Display options for exiting or for calculating
    :return: valid option within the menu
    """
    print("Welcome to the precipitate calculator. Find the limiting reagent and mass of the precipitate.")
    start = str(input("Press s/S to start. Press e/E to exit: "))
    if start == "s" or start =="S":
        return start
    elif start == "e" or start == "E":
        exit()
    else:
        print("Please enter a valid option")
        return intro()

def valuesPos():
    """
    asks for name, volume, and concentration for positive ion
    :return: positiveReacting, positiveVolume, positiveConcentration
    """
    positiveReacting = input("Please enter the positive reacting ion. (no charges)")
    positiveVolume = checkNumberFloat(input("What is the volume of the positive solution? (L)"))
    positiveConcentration = checkNumberFloat(input("What is the concentration of the positive solution? (mol/L) "))
    return positiveReacting, positiveVolume, positiveConcentration

def valuesNeg():
    """
    asks for name, volume, and concentration for negative ion
    :return: negReacting, negVolume, negConcentration
    """
    negReacting = input("Please enter the negative reacting ion. (no charges)")
    negVolume = float(input("What is the volume of the negative solution? (L)"))
    negConcentration = float(input("What is the concentration of the postive solution? (mol/L)"))
    return negReacting, negVolume, negConcentration

def calculateAgain():
    global again
    """
    asks if want to calculate again
    :return: again
    """
    again = str(input("Would you like to calculate again? y/N"))
    if again == "y" or again == "Y":
        again = True
    else:
        exit()
    return again

# --- Processing --- #
def checkNumberFloat(value):
    """
    checks if value is a float and will typecast to a float
    :param value: string value to check
    :return: float value
    """
    try:
        value = float(value)
        return value
    except ValueError:
        print("You did not enter a number")
        newNum = input("Please enter a number")
        return checkNumberFloat(newNum)
# --- Main --- #
# --- Inputs --- #
startIntro = intro()
while again == True:
# input values for positive ion name, volume, concentration
    positiveReacting, positiveVolume, positiveConcentration = valuesPos()
    postiveVolume = checkNumberFloat(positiveVolume)
    postiveConcentration = checkNumberFloat(positiveConcentration)

    positiveSolution = ["name","volume","concentration"]
    positiveSolution[0] = positiveReacting
    positiveSolution[1] = float(positiveVolume)
    positiveSolution[2] = float(positiveConcentration)

# input values for negative ion name, volume, concentration
    negReacting, negVolume, negConcentration = valuesNeg()
    negSolution = ["name","volume","concentration"]
    negSolution[0] = negReacting
    negSolution[1] = negVolume
    negSolution[2] = negConcentration

# --- Processing --- #
# balencing chemical equations
    # positive ion (reactant)
    reactIon1= []
    for i in range(len(ionName)):
        if positiveSolution[0] == ionName[i][0]:
            reactIon1.append(ionName[i][0])
            reactIon1.append(ionName[i][1])

    # negative ion (reactant)
    reactIon2= []
    for i in range(len(ionName)):
        if negSolution[0] == ionName[i][0]:
            reactIon2.append(ionName[i][0])
            reactIon2.append(ionName[i][1])

    # number of positive ion
    productIon1 = []
    productIon1.append(reactIon1[0]) #switch charges
    productIon1.append(reactIon2[1])

    # number of negative ion
    productIon2 = []
    productIon2.append(reactIon2[0]) #switch charges
    productIon2.append(reactIon1[1])
    productMoles = 1


# find mass of product
    massOfProduct = []
    for i in range(len(ionName)):
        if productIon1[0] == ionName[i][0]:
            massOfProduct.append(ionName[i][0])
            massOfProduct.append(ionMass[i])

        if productIon2[0] == ionName[i][0]:
            massOfProduct.append(ionName[i][0])
            massOfProduct.append(ionMass[i])
    mass1 = massOfProduct[1]*reactIon2[1]
    mass2 = massOfProduct[3]*reactIon1[1]
    mass = mass1 + mass2
    massOfProduct.append(mass)

# find moles from concentration and volume
    molesPosReacting = positiveSolution[1] * positiveSolution[2] # find out how to do with arrays
    positiveSolution.append(molesPosReacting)

    molesNegReacting = negSolution[1] * negSolution[2] # find out how to do with arrays
    negSolution.append(molesNegReacting)

#find limiting reagent
    # moles of positive ion needed to fully react moles of negative ion
    molesNegReagent = positiveSolution[3] * (productIon2[1]/productIon1[1])
    negSolution.append(molesNegReagent)

    # moles of negative ion needed to fully react moles of positive ion
    molesPosReagent = negSolution[3] * (productIon1[1]/productIon2[1])
    positiveSolution.append(molesPosReagent)

#--- Outputs --- #
    # find limiting reagent if positive solution
    if positiveSolution[4] > positiveSolution[3]:
        print("The limiting reagent is" + " " + positiveSolution[0])
    #calculate mass of limiting reagent if the positive ion is the limiting reagent
        productMoles = 1
        molarRatio = float(productMoles) / float(productIon2[1])
        mass = float(positiveSolution[3]) * float(molarRatio) * float(massOfProduct[4])  # fix for moles of overall product
        print("The mass of " + str(positiveSolution[0]) + str(negSolution[0]) + " " + str(round(mass, 2)) + "grams")

    # find limiting reagent if negative solution
    elif negSolution[4] > negSolution[3]:
        print("The limiting reagent is" + " " + negSolution[0])
    # calculate mass of limiting reagent if the negative ion is the limiting reagent
        productMoles = 1
        molarRatio = float(productMoles)/ float(productIon2[1])
        mass = float(negSolution[3]) * float(molarRatio) * float(massOfProduct[4]) # fix for moles of overall product
        print("The mass of " + str(positiveSolution[0]) + str(negSolution[0]) + " " + str(round(mass,2)) + "grams")
    # no limiting reagent
    elif (negSolution[4] == negSolution[3]) and (positiveSolution[4] == positiveSolution[3]):
        print("There is no limiting reagent")


    #play again
    again = calculateAgain()