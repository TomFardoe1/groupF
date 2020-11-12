import time #by importing time it means time.sleep(n) can be used to make the command line UI easier to understand 
givenDevice = {
    "Siri" : {
        "Generation": "First Gen",
        "UI" : "Whole Screen",
        "Voice" : "1 Male, low level natural Lang",
        "Activation" : "Hold button, Raise to wake"
},
    "Maps" : {
        "Generation" : "First Gen Apple maps",
        "Travel Options" : "Car, Walking"
},
    "Car Options" : {
        "Generation" : "N/A"
},
    "Interaction" : {
        "Secondary Press" : "3D touch"
},
    "Battery" : {
        "Degradation" : "N/A"
}
}
#updates dict [FeatureName][Attribute]="UPDATED FEATURE"
def updateSiri():
    '''updates the siri element of the nested dictionary to the latest software'''
    givenDevice["Siri"]["Generation"]="7th Generation"
    givenDevice["Siri"]["UI"]="Compact User Interface"
    givenDevice["Siri"]["Voice"]="Male/Female, 6 different accents"
def updateMaps():
    '''updates the maps element of the nested dictionary with more travel options, and changes the generation'''
    givenDevice["Maps"]["Generation"]="7th Generation"
    givenDevice["Maps"]["Travel Options"]="Driving, Walking, Cycling, Public Transit, Electric"
def updateCar():
    ''' adds new features and updates existing features of the softwars car intergration capibilities '''
    givenDevice["Car Options"]["Generation"]="5th Generation Car Play"
    givenDevice["Car Options"]["Keys"]="Digital Car keys"
    givenDevice["Car Options"]["Navigation"]="Apple Maps, Google Maps, Waze"
def updateBattery():
    '''adds new features into the battery element of nested deict, for managing battery degradation'''
    givenDevice["Battery"]["Degradation"]="Smart Charging, Battery health info"
def addFeatures():
    '''after checking if new features need to be added this func adds both facetime screenshare and multitasking to givenDevice'''
    givenDevice["Facetime"] = {"Sharing" : "Screen/media sharing over Facetime"}
    givenDevice["Misc"] = {"Multitasking" : "Split Screen view for multiple apps"}
def removeFeatures():
    '''after checking if features need to be removed this function uses .pop() to remove the whole interaction element and del() to remove siri, activation  '''
    givenDevice.pop("Interaction")
    del(givenDevice["Siri"]["Activation"])
def updateFeatures():
    '''this function brings together the above functions and creates an updated nested dictionary with the added features'''
    updateCar()
    updateMaps()
    updateSiri()
    updateBattery()

#Start with an input of the given device
print("GIVEN DEVICE: iphone 5")
print("")
time.sleep(1)

def showDevice(dictionary):
    '''this function can be used easily to output a nested dictionary using two for loops to iterate through'''
    for p_id, p_info in dictionary.items():
        print("")
        time.sleep(0.2)
        print(p_id+":")
        for key in p_info:
            print(key + ':', p_info[key])
showDevice(givenDevice)
time.sleep(1)
print("")
time.sleep(1)
inupdate = raw_input("Would you like to update device?: ")
if inupdate == 'yes':
    updateFeatures()
#List/Add new features to the device
print("Features to be updated: Siri, Maps, Battery, CarPlay, Airdrop")

time.sleep(1)
print("")
print("Updated Device:")
print("")

showDevice(givenDevice)
        

#Check if you need to remove any outdated features
removedUserInp = raw_input("Are there any features to be removed? ")
if removedUserInp == "Yes" or removedUserInp == "yes":
    removeFeatures()
    print("Raise to wake and 3D touch have been removed from current device.")
else:
    print("No features removed")

#Check if you need to add any new features
newFeatUserInp = raw_input("Are there any new features to add? ")
if newFeatUserInp == "Yes" or newFeatUserInp == "yes":
    addFeatures()
    print("New Features added: Screensharing, Split Screen")
else:
    print("No new features added.")

showDevice(givenDevice)
