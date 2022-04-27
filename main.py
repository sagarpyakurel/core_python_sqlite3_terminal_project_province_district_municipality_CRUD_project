from dbhelper import DBHelper


def main():
    db = DBHelper()

    while True:
        print("\n ")
        print("*********    WELCOME     *********")
        print("press 1 to for Province operation")
        print("press 2 for District operation")
        print("press 3 for  Municipality operation")
        print("press 4 for get district in the province")
        print("press 5 for get municipality in the district")
        print("press 6 for exit")

        try:
            choice = int(input())
            if(choice == 1):
                print("\n ########### Province Choice #############")
                print("press a for CREATE province")
                print("press b for UPDATE province")
                print("press c for DELETE province")
                print("press d for Return Main Menu")
                innerchoice = str(input())
                if(innerchoice == 'a'):
                    province_name = str(input("provide province name:"))
                    db.insert_province(province_name)
                    print(f'province with name: {province_name} created')

                elif(innerchoice == 'b'):
                    print("list of province:")
                    db.fetchallprovince()
                    inputprovince = str(input("provide old province name:"))
                    oldprovincelist = db.getallprovince()

                    if inputprovince in oldprovincelist:
                        newname = str(input("provide new province name:"))
                        db.update_province(inputprovince, newname)
                    else:
                        print('provided province name is not valid')

                elif(innerchoice == 'c'):
                    print("\nlist of province:")
                    db.fetchallprovince()
                    inputprovince = str(
                        input("\n provide province name you want to delete: "))
                    oldprovincelist = db.getallprovince()
                    if inputprovince in oldprovincelist:
                        confirm = str(
                            input("\nDo you really want to delete the province? y/n : "))
                        if confirm == 'y':
                            db.delete_province(inputprovince)
                        elif confirm == 'n':
                            break
                        else:
                            print(
                                '\n only accept y or n for the delete conformation')
                    else:
                        print(" \n Invalid province name ")

                elif(innerchoice == 'd'):
                    main()

                else:
                    print("invalid input!! Try again")

            elif(choice == 2):
                print("\n ########### District Choice #############")
                print("press a for CREATE district")
                print("press b for UPDATE district")
                print("press c for DELETE district")
                print("press d for Return Main Menu")
                innerchoice = str(input())
                if(innerchoice == 'a'):
                    db.fetchallprovince()
                    # all province is printed
                    inputprovince = str(
                        input(" Provide the associated province name:"))
                    # name inputed
                    provincelist = db.getallprovince()
                    if inputprovince in provincelist:
                        # dictionaryofprovince=db.getprovincedictionary()
                        inputdistrict = str(
                            input("Provide the district name:"))
                        db.fetchprovince_insertdistrict(
                            inputdistrict, inputprovince)

                    else:
                        print('your provided district is not valid')

                elif(innerchoice == 'b'):
                    print("list of district")
                    db.fetchalldistrict()
                    inputdistrict = str(input("provide old district name:"))
                    olddistrictlist = db.getalldistrict()

                    if inputdistrict in olddistrictlist:
                        newname = str(input("provide new district name:"))
                        db.update_district(inputdistrict, newname)
                    else:
                        print('provided district name is not valid')

                elif(innerchoice == 'c'):
                    print("\nlist of district:")
                    db.fetchalldistrict()
                    inputdistrict = str(
                        input("\n provide district name you want to delete: "))
                    olddistrictlist = db.getalldistrict()
                    if inputdistrict in olddistrictlist:
                        confirm = str(
                            input(f"\nDo you really want to delete the district:{inputdistrict}? y/n : "))
                        if confirm == 'y':
                            db.delete_district(inputdistrict)
                        elif confirm == 'n':
                            break
                        else:
                            print(
                                '\n only accept y or n ')
                    else:
                        print(" \n Invalid district name ")

                elif(innerchoice == 'd'):
                    main()

                else:
                    print("invalid input!! Try again")

            elif(choice == 3):
                print("\n ########### Municipality Choice #############")
                print("press a for CREATE municipality")
                print("press b for UPDATE municipality")
                print("press c for DELETE municipality")
                print("press d for Return Main Menu")
                innerchoice = str(input())
                if(innerchoice == 'a'):
                    db.fetchalldistrict()
                    # all province is printed
                    inputdistrict = str(
                        input(" Provide the associated district:"))
                    # name inputed
                    districtlist = db.getalldistrict()
                    if inputdistrict in districtlist:
                        # dictionaryofprovince=db.getprovincedictionary()
                        inputmunicipality = str(
                            input("Provide the municipality name:"))
                        db.fetchdistrict_insertmunicipality(
                            inputmunicipality, inputdistrict)

                    else:
                        print('your provided district is not valid')

                elif(innerchoice == 'b'):
                    print("list of municipality:")
                    db.fetchallmunicipality()
                    inputmunicipality = str(
                        input("provide old municipality name from the list:>"))
                    oldmunicipalitylist = db.getallmunicipality()

                    if inputmunicipality in oldmunicipalitylist:
                        newname = str(input("provide new municipality name:"))
                        db.update_municipality(inputmunicipality, newname)
                    else:
                        print('provided municipality 3is not valid')

                elif(innerchoice == 'c'):
                    print("\nlist of municipality:")
                    db.fetchallmunicipality()
                    inputmunicipality = str(
                        input("\n provide municipality name you want to delete: "))
                    oldmunicipalitylist = db.getallmunicipality()
                    if inputmunicipality in oldmunicipalitylist:
                        confirm = str(
                            input(f"\nDo you really want to delete the municipality:{inputmunicipality}? y/n : "))
                        if confirm == 'y':
                            db.delete_municipality(inputmunicipality)
                        elif confirm == 'n':
                            break
                        else:
                            print('\n only accept y or n ')
                    else:
                        print(" \n Invalid municipality name ")
                    pass

                elif(innerchoice == 'd'):
                    main()

                else:
                    print("invalid input!! Try again")

            elif(choice == 4):
                print("which province do you want to select?")
                db.fetchallprovince()
                inputprovince = str(input(" Provide the name of province whose district are to be listed: "))
                provincelist = db.getallprovince()
                if inputprovince in provincelist:
                    db.listdistrict_by_province(inputprovince)

                else:
                    print('no province name match the list')

            elif(choice == 5):
                print("which district do you want to select?")
                db.fetchalldistrict()
                inputdistrict = str(input(" Provide the name of district whose municipality are to be listed: "))
                districtlist = db.getalldistrict()
                if inputdistrict in districtlist:
                    db.listmunicipality_by_district(inputdistrict)

                else:
                    print('no district name match the list')

            elif(choice == 6):
                break

            else:
                print("\n invalid input!! Try again\n")
        except Exception as e:
            print(e)
            print("\n invalid input!! Try again\n")


if __name__ == "__main__":
    main()
