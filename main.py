#!/usr/bin/env python
__author__ = "Christopher Phillips, chris@tcp-networking.com"

# This script is used to generate random flags for a capture the flag hackathon.
# The user can change the length of the key, the number of keys generated, and the name of the key

from random import choice


# Create the list that stores and checks all the keys
def randomKeyGen(numberOfKeys, keyLength, keyName):
    # store new keys in this array
    keyList = []
    newKey = createNewKey(keyLength)

    # numberOfKeysCounter tracks how many keys have been added to the array
    numberOfKeysCounter = 0

    # Until the keyList reaches the specified number of keys, this loop will play.
    while numberOfKeysCounter < numberOfKeys:

        # If keyList is empty, add the 1st key without checking if it is matching any other keys (since there are none).
        if len(keyList) > 0:

            # Check for a new key
            for i in range(len(keyList)):

                # If the newKey matches another one in the list, regenerate newKey and try again.
                if newKey == keyList[i]:
                    newKey = createNewKey(keyLength)
                    break

                # If the newKey reaches the end of the list and did not match any of the keys
                if i+1 == len(keyList):
                    # Add the new key to the list and generate another key
                    keyList.append(newKey)
                    newKey = createNewKey(keyLength)
                    # Increase the count for number of keys in the list.
                    numberOfKeysCounter = numberOfKeysCounter + 1

        # Else this is the first key in the list
        else:
            # Add the first key to the list and generate another key
            keyList.append(newKey)
            newKey = createNewKey(keyLength)
            # Increase the count for number of keys in the list.
            numberOfKeysCounter = numberOfKeysCounter + 1

    printKeys(keyList, keyName)


# Generate a random key from a set of all possible hexadecimal characters in a hexadecimal number
def createNewKey(keyLength):
    newKey = ""
    # Every possible hexadecimal character that can appear in a hexadecimal number
    hexStringValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    # Pick a random character from hexStringValues and add it to newKey for the length of keyLength
    for i in range(keyLength):
        newKey = newKey + choice(hexStringValues)

    return newKey


# Print the keys
def printKeys(keyList, keyName):
    # Print all the keys inside keyList
    # Keys appear like keyName_01{ABCD1234}
    for i in range(len(keyList)):
        print(keyName + "_" + str(str(i).zfill(2)) + "{" + keyList[i] + "}")


# Example use of this function to make 10, 16 digit keys all called "Key"
randomKeyGen(10, 16, "Key")
