from dbhelper import DBHelper


def main():
    db = DBHelper()

    while True:
        print("\n ")
        print("*********    WELCOME     *********")
        print("press 1 >> Province operation:")
        print("press 2 >> District operation:")
        print("press 3 >> Municipality operation:")
        print("press 4 >> getting district in the province:")
        print("press 5 >> getting municipality in the district:")
        print("press 6 >> exit:")

        try:
            choice = int(input())
            if(choice == 1):
                print("\n ########### Province Choice #############")
                print("press a >> CREATE province")
                print("press b >> UPDATE province")
                print("press c >> DELETE province")
                print("press d >> Return Main Menu")
                innerchoice = str(input())
                if(innerchoice == 'a'):
                    
                    province_name = str(input("provide new province name:"))
                    db.insert_province(province_name)
                    print(f'province with name: {province_name} created')

                elif(innerchoice == 'b'):
                    print("Type the name of provinceyou want to update from the list?")
                    db.fetchallprovince()
                    inputprovince = str(input("provide old province name:"))
                    oldprovincelist = db.getallprovince()

                    if inputprovince in oldprovincelist:
                        newname = str(input("provide new province name:"))
                        db.update_province(inputprovince, newname)
                    else:
                        print('provided province name is not valid')

                elif(innerchoice == 'c'):
                    print("\n From the list type province name you want to delete?")
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
                print("press a >> CREATE district")
                print("press b >> UPDATE district")
                print("press c >> DELETE district")
                print("press d >> Return Main Menu")
                innerchoice = str(input())
                if(innerchoice == 'a'):
                    print("you can create new district here:")
                    print("select any province from here?")
                    db.fetchallprovince()
                    # all province is printed
                    inputprovince = str(
                        input(" Type the province name first:"))
                    # name inputed
                    provincelist = db.getallprovince()
                    if inputprovince in provincelist:
                        # dictionaryofprovince=db.getprovincedictionary()
                        inputdistrict = str(
                            input("Type the district name:"))
                        db.fetchprovince_insertdistrict(
                            inputdistrict, inputprovince)

                    else:
                        print('your provided district is not valid')

                elif(innerchoice == 'b'):
                    print("list of district for updating:")
                    db.fetchalldistrict()
                    inputdistrict = str(input("provide old district name:"))
                    olddistrictlist = db.getalldistrict()

                    if inputdistrict in olddistrictlist:
                        newname = str(input("provide new district name:"))
                        db.update_district(inputdistrict, newname)
                    else:
                        print('provided district name is not valid')

                elif(innerchoice == 'c'):
                    print("\nlist of district for delete purpose:")
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
                print("press a >> CREATE municipality")
                print("press b >> UPDATE municipality")
                print("press c >> DELETE municipality")
                print("press d >> Return Main Menu")
                innerchoice = str(input())
                if(innerchoice == 'a'):
                    print("you can create new municipality here:")
                    db.fetchalldistrict()
                    # all province is printed
                    inputdistrict = str(
                        input(" Type district name first:"))
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
                    print("list of municipality for updating:")
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
                    print("\nlist of municipality for deleting:")
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
                inputprovince = str(input(" Type province name first: "))
                provincelist = db.getallprovince()
                if inputprovince in provincelist:
                    db.listdistrict_by_province(inputprovince)

                else:
                    print('no province name match the list')

            elif(choice == 5):
                print("which district do you want to select?")
                db.fetchalldistrict()
                inputdistrict = str(input(" type any district first:"))
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
