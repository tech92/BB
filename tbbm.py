import os
import sys
from firebase import firebase
import requests
import json
import doctest
import datetime

fb = firebase.FirebaseApplication('https://the-bb-manager.firebaseio.com')
conflag = 1
try:
    check = fb.get('/', 'isLoggedIn')
except:
    print("No internet connection")
    conflag = None

logflag = 1
if len(sys.argv) > 1 and conflag:
    if sys.argv[1] != '-h' and sys.argv[1] != '--help' and sys.argv[1] != '-li' and sys.argv[1] != '--login' and \
                    sys.argv[1] != '-cp' and sys.argv[1] != '--changePassword' and sys.argv[1] != '-ut' and sys.argv[
        1] != '--unitTests':
        if not check:  # in not logged in
            print("You must first login")
            logflag = None


# ----------main:
def main():
    id = None  # default values
    name = None
    sourceType = None
    projectIDs = None
    title = None
    firstName = None
    lastName = None
    categoryIDs = None
    isFinal = None
    note = None
    state = None
    pageStart = None
    pageEnd = None
    url = None
    day = None
    month = None
    year = None
    secondaryAuthors = None
    publisher = None
    password = None
    newPassword = None

    pos = 2  # 0 is the name of the file , 1 is the option , 2+ are the arguments
    if 'sfn:' in sys.argv:
        secondaryAuthors = list()
    while pos < len(sys.argv):  # arguments parsing

        if sys.argv[pos] == 'st:':
            pos += 1
            sourceType = sys.argv[pos]

        elif sys.argv[pos] == 'id:':
            pos += 1
            id = int(sys.argv[pos])
        elif sys.argv[pos] == 'pass:':
            pos += 1
            password = sys.argv[pos]
        elif sys.argv[pos] == 'np:':
            pos += 1
            newPassword = sys.argv[pos]
        elif sys.argv[pos] == 'pid:':
            pos += 1
            projectIDs = list(
                sys.argv[pos].replace(' ', ',').split(','))  # converting to a list, in case of more than one id
        elif sys.argv[pos] == 't:':
            pos += 1
            title = sys.argv[pos]
        elif sys.argv[pos] == 'fn:':
            pos += 1
            firstName = sys.argv[pos]
        elif sys.argv[pos] == 'ln:':
            pos += 1
            lastName = sys.argv[pos]
        elif sys.argv[pos] == 'cid:':
            pos += 1
            categoryIDs = list(
                sys.argv[pos].replace(' ', ',').split(','))  # converting to a list, in case of more than one id
        elif sys.argv[pos] == 'f:':
            pos += 1
            if sys.argv[pos] == 'yes' or sys.argv[pos] == 'Yes' or sys.argv[pos] == 'YES' or sys.argv[pos] == 'true' or \
                            sys.argv[pos] == 'True':
                isFinal = True
            else:
                isFinal = False
        elif sys.argv[pos] == 'no:':
            pos += 1
            note = sys.argv[pos]
        elif sys.argv[pos] == 'n:':
            pos += 1
            name = sys.argv[pos]
        elif sys.argv[pos] == 'pub:':
            pos += 1
            publisher = sys.argv[pos]
        elif sys.argv[pos] == 's:':
            pos += 1
            state = sys.argv[pos]
        elif sys.argv[pos] == 'ps:':
            pos += 1
            pageStart = sys.argv[pos]
        elif sys.argv[pos] == 'pe:':
            pos += 1
            pageEnd = sys.argv[pos]
        elif sys.argv[pos] == 'u:':
            pos += 1
            url = sys.argv[pos]
        elif sys.argv[pos] == 'd:':
            pos += 1
            day = sys.argv[pos]
        elif sys.argv[pos] == 'm:':
            pos += 1
            month = sys.argv[pos]
        elif sys.argv[pos] == 'y:':
            pos += 1
            year = sys.argv[pos]
        elif sys.argv[pos] == 'sfn:':
            pos += 1
            secondaryAuthors.append(sys.argv[pos])
            if sys.argv[pos + 1] != 'sln:':
                print("A last name should come after secondary author's first name")
                secondaryAuthors += str()
            else:
                pos += 2
                secondaryAuthors.append(sys.argv[pos])
        pos += 1
    if len(sys.argv) > 1:
        case = sys.argv[1]
        if case == '-h':
            print(getHelp())
        elif case == '--help':
            print(getHelp())
        elif case == '-li':
            login(password)
        elif case == '--login':
            login(password)
        elif case == '-lo':
            logout()
        elif case == '--logout':
            logout()
        elif case == '-cp':
            changePassword(password, newPassword)
        elif case == '--changePassword':
            changePassword(password, newPassword)
        elif case == '-ut':
            print("Running tests,this may take while")
            print(doctest.testmod())
        elif case == '--unitTests':
            print("Running tests,this may take while")
            print(doctest.testmod())
        elif case == '-ap':
            addProject(name)
        elif case == '--addProject':
            addProject(name)
        elif case == '-ep':
            editProject(id, name, state)
        elif case == '--editProject':
            editProject(id, name, state)
        elif case == '-dp':
            deleteProject(id)
        elif case == '--deleteProject':
            deleteProject(id)
        elif case == '-acat':
            addCategory(name)
        elif case == '--addCategory':
            addCategory(name)
        elif case == '-ecat':
            editCategory(id, name)
        elif case == '--editCategory':
            editCategory(id, name)
        elif case == '-dcat':
            deleteCategory(id)
        elif case == '--deleteCategory':
            deleteCategory(id)
        elif case == '-ac':
            addCitation(sourceType, projectIDs, title, firstName, lastName, categoryIDs, isFinal, note, year, month,
                        day, pageStart, pageEnd, url, secondaryAuthors, publisher)
        elif case == '--addCitation':
            addCitation(sourceType, projectIDs, title, firstName, lastName, categoryIDs, isFinal, note, year, month,
                        day, pageStart, pageEnd, url, secondaryAuthors, publisher)
        elif case == '-ec':
            editCitation(id, sourceType, projectIDs, title, firstName, lastName, categoryIDs, isFinal, note, year,
                         month, day, pageStart, pageEnd, url, secondaryAuthors, publisher)
        elif case == '--editCitation':
            editCitation(id, sourceType, projectIDs, title, firstName, lastName, categoryIDs, isFinal, note, year,
                         month, day, pageStart, pageEnd, url, secondaryAuthors, publisher)
        elif case == '-dc':
            deleteCitation(id)
        elif case == '--deleteCitation':
            deleteCitation(id)
        elif case == '-pap':
            printAllProjects()
        elif case == '--printAllProjects':
            printAllProjects()
        elif case == '-paca':
            printAllCategories()
        elif case == '--printAllCategories':
            printAllCategories()
        elif case == '-paci':
            printAllCitations()
        elif case == '--printAllCitations':
            printAllCitations()
        elif case == '-ppc':
            printProjectCitations(id)
        elif case == '--PrintProjectCitations':
            printProjectCitations(id)
        elif case == '-pcc':
            printCategoryCitations(id)
        elif case == '--printCategoryCitations':
            printCategoryCitations(id)
        elif case == '-eieee':
            export(id, 'ieee')
        elif case == '--exportIEEE':
            export(id, 'ieee')
        elif case == '-emla':
            export(id, 'mla')
        elif case == '--exportMLA':
            export(id, 'mla')
        elif case == '-eh':
            export(id, 'harvard')
        elif case == '--exportHarvard':
            export(id, 'harvard')
        elif case == '-eapa':
            export(id, 'apa')
        elif case == '--exportAPA':
            export(id, 'apa')
        else:
            print("Wrong input")
            return


# --------definitions:                             ------third hackathon,publisher field updated:
def getHelp():
    """ returns the help string """
    str = '=========================================\n\nWelcome to The BB Manager!\n\n* Please notice that the first argument after the filename must be an option,         *\n* while the order of the rest doesn\'t matter                                          *\n* (except for secondary names,where last name must come after first name).            *\n* Also please separate the argument marks and the values with a blank space.          *\n* In addition you can use " " to mark few words as one argument(notes for example).   *\n* "<" and ">" are used to demonstrate the syntax,using them is not necessary.         *\n\nHere are your options:\n\n==========================================================================================================\n"-h" or "--help" to print this message\n==========================================================================================================\n"-li" or "--login" to log into The BB Manager:\n\nPlease use the following format:\n\'python tbbm.py -li pass: <password> \'\nPlease note that you won\'t be asked to login again until you log out.\n==========================================================================================================\n"-lo" or "--logout" to log out The BB Manager\n==========================================================================================================\n"-cp" or "--changePassword" to change the current password:\n\nPlease use the following format:\n\'python tbbm.py -cp (or --changePassword) pass: <old_password> np: <new_password> \n==========================================================================================================\n"-ut" or "--unitTests" to run the tests.\n==========================================================================================================\n"-ap" or "--addProject" to add a new project:\n\nPlease use the following format:\n\'python tbbm.py -ap (or --addProject) n: "Project Name"  \' \nwhile "n:" is used to mark the name of the project\n==========================================================================================================\n"-ep" or "--editProject" to edit an existing project:\n\nPlease use the following format:\n\'python tbbm.py -ep (or --editProject) id: <id> pn: "Updated Name" \'\nwhile "<id>" is the id of the project you want to update \nor\n\'python tbbm.py -ep (or --editProject) id: <id> s: "Updated State" \'\nwhile "s:" is to mark the state of your project (Active/Projected/Archived) \n==========================================================================================================\n"-dp" or "--deleteProject" to delete a project:\n\nPlease use the following format:\n\'python tbbm.py -dp (or --deleteProject) id: <id> \'\nwhile "<id>" is the id of the project you want to delete \n==========================================================================================================\n"-acat" or "--addCategory" to add a new category:\n\nPlease use the following format:\n\'python tbbm.py -acat (or --addCategory) n: "Category Name"  \' \nwhile "n:" is used to mark the name of the category\n==========================================================================================================\n"-ecat" or "--editCategory" to edit an existing category:\n\nPlease use the following format:\n\'python tbbm.py -ecat (or --editCategory) id: <id> n: "Updated Name" \'\nwhile "<id>" is the id of the Category you want to update \n==========================================================================================================\n"-dcat" or "--deleteCategory" to delete a category:\n\nPlease use the following format:\n\'python tbbm.py -dcat (or --deleteCategory) id: <id> \'\nwhile "<id>" is the id of the category you want to delete \n==========================================================================================================\n"-ac" or "--addCitation" to add a new citation:\n\nPlease use the following format:\n\'python tbbm.py -ac (or --addCitation) <mark1>: <value1> <mark2>: <value2> ... \' \nHere is the list of the marks you can use ( part of them are mandatory ):\n"st:"  - source type (Available source types are: Book, Journal, Newspaper, Online, Magazine)\n"pid:" - the ID(s) of the project(s) that the citation is related to (for example pid: "1 2 3 4")\n"t:"   - title \n"fn:"  - main author\'s first name\n"ln:"  - main author\'s last name\n"cid:" - the ID(s) of the category(ies) that the citation is relevant to \n"f:"   - will the file appear in the final version (yes/no )\n"no:"  - a note\n"y:"   - publishing year \n"pub:" - publisher ( please note that it should be one of the publishers in the list )		                   \n"m:"   - publishing month 		           \n"d:"   - publishing day  			   \n"ps:"  - from page __     			   \n"pe:"  - to page __       			   \n"u:"   - URL              			   \n"sfn:" - secondary author\'s first name            \n"sln:" - secondary author\'s last name             \n==========================================================================================================\n"-ec" or "--editCitation" to edit an existing citation:\n\nPlease use the following format:\n\'python tbbm.py -ec (or --editCitation) id: <id> <mark1>: <new_value1> <mark2>: <new_value2> ... \'\nwhile "<id>" is the id of the citation you want to update \nand   "<mark>" is the mark of the field you want to update \n==========================================================================================================\n"-dc" or "--deleteCitation" to delete an existing citation:\n\nPlease use the following format:\n\'python tbbm.py -dc (or --deleteCitation) id: <id> \'\nwhile "<id>" is the id of the citation you would like to delete\n==========================================================================================================\n"-pap" or "--printAllProjects" to print all the projects\n==========================================================================================================\n"-paca" or "--printAllCategories" to print all the categories\n==========================================================================================================\n"-paci" or "--printAllCitations" to print all the citations\n==========================================================================================================\n"-ppc" or "--printProjectCitations" to print all the citations that are related to a particular project:\n\nPlease use the following format:\n\'python tbbm.py -ppc (or --printProjectCitations) id: <id> \' \nwhile "<id>" is the id of the project you are intrested in\n==========================================================================================================\n"-pcc" or "--printCategoryCitations" to print all the citations that are related to a particular category:\n\nPlease use the following format:\n\'python tbbm.py -pcc (or --printCategoryCitations) id: <cid> \' \nwhile "<cid>" is the id of the category you are intrested in\n==========================================================================================================\n"-eieee" or "--exportIEEE" to export a bibliography in IEEE format to a textfile:\n\nPlease use the following format:\n\'python tbbm.py -eieee (or --exportIEEE) <id> \' \nwhile <id> is the id of the project you would like to export in IEEE format\nPlease note that only the citations that are marked as "Will be exported" will be exported.\n==========================================================================================================\n"-emla" or "--exportMLA" to export a bibliography in MLA format to a textfile:\n\nPlease use the following format:\n\'python tbbm.py -emla (or --exportMLA) <id> \' \nwhile <id> is the id of the project you would like to export in MLA format\nPlease note that only the citations that are marked as "Will be exported" will be exported.\n==========================================================================================================\n"-eh" or "--exportHarvard" to export a bibliography in Harvard format to a textfile:\n\nPlease use the following format:\n\'python tbbm.py -eieee (or --exportHarvard) <id> \' \nwhile <id> is the id of the project you would like to export in Harvard format\nPlease note that only the citations that are marked as "Will be exported" will be exported.\n==========================================================================================================\n"-eapa" or "--exportAPA" to export a bibliography in APA format to a textfile:\n\nPlease use the following format:\n\'python tbbm.py -eieee (or --exportAPA) <id> \' \nwhile <id> is the id of the project you would like to export in APA format\nPlease note that only the citations that are marked as "Will be exported" will be exported.\n==========================================================================================================\nFor more information please contact the developers.\nThank you for using The BB Manager :) \n\n=========================================\n'
    return str


def isLoggedIn():
    """ checks if you're logged in """
    return fb.get('/isLoggedIn', None)


def login(pswrd):
    """ tries to log in """
    if not isLoggedIn():
        if pswrd == fb.get('/password', None):
            fb.put('/', 'isLoggedIn', True)
            print("Logged in")
        else:
            print("Wrong password")
    else:
        print("Already logged in")


def logout():
    """ logs out """
    fb.put('/', 'isLoggedIn', False)
    print("Logged out")


def changePassword(oldpass, newpass):
    """ changes the old password to a new one """
    if oldpass != fb.get('/password', None):
        print("Wrong current password")
        return
    if not newpass:
        print("You must enter a new password")
        return
    fb.put('/', 'password', newpass)
    print("The password was changed")


def addProject(pname):
    """ adds a new project to the DB """
    if not pname:
        print("You must enter a project name")
        return
    id = fb.get('/nextProjectID', None)
    fb.put('/', 'nextProjectID', id + 1)
    sid = str(id)
    fb.put('/DB/Projects/Project' + sid, 'ID', id)
    fb.put('/DB/Projects/Project' + sid, 'Name', pname)
    fb.put('/DB/Projects/Project' + sid, 'State', 'Active')
    fb.put('/DB/Projects/Project' + sid, 'last_date_changed', datetime.datetime.now().date())
    fb.put('/DB/Projects/Project' + sid, 'last_time_changed', "{}:{}:{}".format(datetime.datetime.now().hour,datetime.datetime.now().minute,datetime.datetime.now().second))
    print("Project #" + sid + " was added")


def projectExists(pid):
    """" checks if the project exists """
    if pid == None:
        print("No id was entered")
        return False
    if pid >= fb.get('/nextProjectID', None) or pid < 0:  # project id is out of range
        print("Wrong project ID")
        return False
    if fb.get('/DB/Projects/Project' + str(pid), None) == None:  # if the project was deleted
        print("Wrong project ID")
        return False
    return True


def editProject(pid, pname, pstate):
    """ edits an existing project """
    if not projectExists(pid):
        return
    if not pname and not pstate:
        print("No data was entered")
        return
    flag = 1
    if pname:
        fb.put('/DB/Projects/Project' + str(pid), 'Name', pname)
    if pstate:
        if pstate != 'Active' and pstate != 'active' and pstate != 'Projected' and pstate != 'projected' and pstate != 'Archived' and pstate != 'archived':
            print("Wrong state")
            flag = None
        else:
            fb.put('/DB/Projects/Project' + str(pid), 'State', pstate)
    if flag or pname:
        print("Project #" + str(pid) + " was updated")
        fb.put('/DB/Projects/Project' + str(pid), 'last_date_changed', datetime.datetime.now().date())
        fb.put('/DB/Projects/Project' + str(pid), 'last_time_changed',
               "{}:{}:{}".format(datetime.datetime.now().hour, datetime.datetime.now().minute,
                                 datetime.datetime.now().second))


def deleteProject(pid):
    """ deletes an existing project """
    fb.delete('/DB/Projects', 'Project' + str(pid))
    print("Project #" + str(pid) + " was deleted (if existed)")


def addCategory(catname):
    """ adds a new category to the DB """
    if not catname:
        print("You must enter a category name")
        return
    id = fb.get('/nextCategoryID', None)
    fb.put('/', 'nextCategoryID', id + 1)
    sid = str(id)
    fb.put('/DB/Categories/Category' + sid, 'ID', id)
    fb.put('/DB/Categories/Category' + sid, 'Name', catname)
    fb.put('/DB/Categories/Category' + sid, 'last_date_changed', datetime.datetime.now().date())
    fb.put('/DB/Categories/Category' + sid, 'last_time_changed', "{}:{}:{}".format(datetime.datetime.now().hour,datetime.datetime.now().minute,datetime.datetime.now().second))
    print("Category #" + sid + " was added")


def categoryExists(catid):
    """" checks if the category exists """
    if catid == None:
        print("No id was entered")
        return False
    if catid >= fb.get('/nextCategoryID', None) or catid < 0:  # category id is out of range
        print("Wrong category ID")
        return False
    if fb.get('/DB/Categories/Category' + str(catid), None) == None:  # if the category was deleted
        print("Wrong category ID")
        return False
    return True


def editCategory(catid, catname):
    if not categoryExists(catid):
        return
    if not catname:
        print("No data was entered")
        return
    fb.put('/DB/Categories/Category' + str(catid), 'Name', catname)
    print("Category #" + str(catid) + " was edited")
    fb.put('/DB/Categories/Category' + str(catid), 'last_date_changed', datetime.datetime.now().date())
    fb.put('/DB/Categories/Category' + str(catid), 'last_time_changed', "{}:{}:{}".format(datetime.datetime.now().hour,datetime.datetime.now().minute,datetime.datetime.now().second))



def deleteCategory(catid):
    """ deletes an existing category """
    fb.delete('/DB/Categories', 'Category' + str(catid))
    print("Category #" + str(catid) + " was deleted (if existed)")


# ----------third hackathon:

def publisherInList(publisher):
    publist = list(fb.get('/', 'Publishers List'))
    return publisher in publist


# ------------------------------

def addCitation(source, projectIDs, title, firstName, lastName, categoryIDs, isFinal, note, year, month, day, pageStart,
                pageEnd, url, secondaryAuthors, publisher):
    """ adds a new citation """
    if source != 'Journal' and source != 'journal' and source != 'Book' and source != 'book' and source != 'Newspaper' and source != 'newspaper' and source != 'Online' and source != 'online' and source != 'Magazine' and source != 'magazine':
        print("Wrong source type")
        return
    # -------------third hackathon:
    if publisher:
        if not publisherInList(publisher):
            print('Publisher is not in the list,no publisher field were added')
            publisher = None
    # ------------------------------
    id = fb.get('/nextCitationID', None)
    fb.put('/', 'nextCitationID', id + 1)
    sid = str(id)
    fb.put('/DB/Citations/Citation' + sid, 'ID', id)
    if source:
        fb.put('/DB/Citations/Citation' + sid, 'Source', source)
    if projectIDs:
        fb.put('/DB/Citations/Citation' + sid, 'Project IDs', projectIDs)
    if title:
        fb.put('/DB/Citations/Citation' + sid, 'Title', title)
    if firstName:
        fb.put('/DB/Citations/Citation' + sid + '/Author', 'First Name', firstName)
    if lastName:
        fb.put('/DB/Citations/Citation' + sid + '/Author', 'Last Name', lastName)
    if categoryIDs:
        fb.put('/DB/Citations/Citation' + sid, 'Category IDs', categoryIDs)
    if isFinal:
        fb.put('/DB/Citations/Citation' + sid, 'Will be exported', isFinal)
    else:
        fb.put('/DB/Citations/Citation' + sid, 'Will be exported', False)
    if note:
        fb.put('/DB/Citations/Citation' + sid, 'Note', note)
    if year:
        fb.put('/DB/Citations/Citation' + sid + '/Date', 'Year', year)
    if month:
        fb.put('/DB/Citations/Citation' + sid + '/Date', 'Month', month)
    if day:
        fb.put('/DB/Citations/Citation' + sid + '/Date', 'Day', day)
    if pageStart:
        fb.put('/DB/Citations/Citation' + sid + '/Pages', 'From', pageStart)
    if pageEnd:
        fb.put('/DB/Citations/Citation' + sid + '/Pages', 'To', pageEnd)
    if url:
        fb.put('/DB/Citations/Citation' + sid, 'URL', url)
    if publisher:
        fb.put('/DB/Citations/Citation' + sid, 'Publisher', publisher)
    if secondaryAuthors:
        i = 0
        while i < len(secondaryAuthors):
            fb.put('/DB/Citations/Citation' + sid + '/Secondary Authors/Author' + str(i // 2), 'First Name',
                   secondaryAuthors[i])
            fb.put('/DB/Citations/Citation' + sid + '/Secondary Authors/Author' + str(i // 2), 'Last Name',
                   secondaryAuthors[i + 1])
            i += 2
    print("Citation #" + sid + " was added")
    fb.put('/DB/Citations/Citation' + sid, 'last_date_changed', datetime.datetime.now().date())
    fb.put('/DB/Citations/Citation' + sid, 'last_time_changed',
           "{}:{}:{}".format(datetime.datetime.now().hour, datetime.datetime.now().minute,
                             datetime.datetime.now().second))


def citationExists(cid):
    """" checks if the citation exists """
    if cid == None:
        print("No id was entered")
        return False
    if cid >= fb.get('/nextCitationID', None) or cid < 0:  # citation id is out of range
        print("Wrong citation ID")
        return False
    if fb.get('/DB/Citations/Citation' + str(cid), None) == None:  # if the citation was deleted
        print("Wrong citation ID")
        return False
    return True


def editCitation(citationID, source, projectIDs, title, firstName, lastName, categoryIDs, isFinal, note, year, month,
                 day, pageStart, pageEnd, url, secondaryAuthors, publisher):
    """" edits an existing citation """
    if not citationExists(citationID):
        return
    if not source and not projectIDs and not title and not firstName and not lastName and not categoryIDs and not isFinal and not note and not year and not month and not day and not pageStart and not pageEnd and not url and not secondaryAuthors and not publisher:
        print("No data was entered")
        return
    # -----------third hackathon:
    if publisher:
        if not publisherInList(publisher):
            print('Publisher is not in the list,no publisher field were added')
            publisher = None
    # ----------------------------
    sid = str(citationID)
    if source:
        if source != 'Journal' and source != 'journal' and source != 'Book' and source != 'book' and source != 'Newspaper' and source != 'newspaper' and source != 'Online' and source != 'online' and source != 'Magazine' and source != 'magazine':
            print("Wrong source name")
        else:
            fb.put('/DB/Citations/Citation' + sid, 'Source', source)
    if projectIDs:
        fb.put('/DB/Citations/Citation' + sid, 'Project IDs', projectIDs)
    if title:
        fb.put('/DB/Citations/Citation' + sid, 'Title', title)
    if firstName:
        fb.put('/DB/Citations/Citation' + sid + '/Author', 'First Name', firstName)
    if lastName:
        fb.put('/DB/Citations/Citation' + sid + '/Author', 'Last Name', lastName)
    if categoryIDs:
        fb.put('/DB/Citations/Citation' + sid, 'Category IDs', categoryIDs)
    if isFinal != None:
        fb.put('/DB/Citations/Citation' + sid, 'Will be exported', isFinal)
    if note:
        fb.put('/DB/Citations/Citation' + sid, 'Note', note)
    if year:
        fb.put('/DB/Citations/Citation' + sid + '/Date', 'Year', year)
    if month:
        fb.put('/DB/Citations/Citation' + sid + '/Date', 'Month', month)
    if day:
        fb.put('/DB/Citations/Citation' + sid + '/Date', 'Day', day)
    if pageStart:
        fb.put('/DB/Citations/Citation' + sid + '/Pages', 'From', pageStart)
    if pageEnd:
        fb.put('/DB/Citations/Citation' + sid + '/Pages', 'To', pageEnd)
    if url:
        fb.put('/DB/Citations/Citation' + sid, 'URL', url)
    if publisher:
        fb.put('/DB/Citations/Citation' + sid, 'Publisher', publisher)
    if secondaryAuthors:
        i = 0
        while i < len(secondaryAuthors):
            fb.put('/DB/Citations/Citation' + sid + '/Secondary Authors/Author' + str(i // 2), 'First Name',
                   secondaryAuthors[i])
            fb.put('/DB/Citations/Citation' + sid + '/Secondary Authors/Author' + str(i // 2), 'Last Name',
                   secondaryAuthors[i + 1])
            i += 2
    print("Citation #" + sid + " was edited")
    fb.put('/DB/Citations/Citation' + sid, 'last_date_changed', datetime.datetime.now().date())
    fb.put('/DB/Citations/Citation' + sid, 'last_time_changed',
           "{}:{}:{}".format(datetime.datetime.now().hour, datetime.datetime.now().minute,
                             datetime.datetime.now().second))


def deleteCitation(citationID):
    """" deletes a citation if it exists """
    fb.delete('/DB/Citations', 'Citation' + str(citationID))
    print("Citation #" + str(citationID) + " was deleted (if existed)")


def printAllProjects():
    """" prints all the projects """
    data = fb.get('/DB', 'Projects')
    if data:
        print('Those are all your projects:')
    for project in data:
        print('===============================')
        print('Project ID: ', data[project]['ID'])
        print('Project Name: ', data[project]['Name'])
        print('Project State: ', data[project]['State'])
        print('Last date updated: ', data[project]['last_date_changed'])
        print('Last time updated: ', data[project]['last_time_changed'])


def printAllCategories():
    """" prints all the categories """
    data = fb.get('/DB', 'Categories')
    if data:
        print('Those are all your projects:')
    for category in data:
        print('===============================')
        print('Category ID: ', data[category]['ID'])
        print('Category Name: ', data[category]['Name'])
        print('Last date updated: ', data[category]['last_date_changed'])
        print('Last time updated: ', data[category]['last_time_changed'])


def printCitation(citation):
    """" prints a specific citation """
    print('Citation ID: ', citation['ID'])
    if 'Source' in citation:
        print('Source Type: ', citation['Source'])
    if 'Project IDs' in citation:
        print('Relevant to projects: ', end='')
        for i in list(citation['Project IDs']):
            print(i, end=' ')
        print('')
    if 'Title' in citation:
        print('Title: ', citation['Title'])
    if 'Author' in citation:
        print('Author: ', end='')
        if 'First Name' in citation['Author']:
            print(citation['Author']['First Name'], end=' ')
        if 'Last Name' in citation['Author']:
            print(citation['Author']['Last Name'], end='')
        print('')
    if 'Category IDs' in citation:
        print('Relevant to categories: ', end='')
        for i in list(citation['Category IDs']):
            print(i, end=' ')
        print('')
    if 'Pages' in citation:
        print('Pages: ', end='')
        if 'From' in citation['Pages']:
            print(citation['Pages']['From'], end='')
        else:
            print('0 ', end='')
        print(' - ', end='')
        if 'To' in citation['Pages']:
            print(citation['Pages']['To'], end='')
        else:
            print('end', end='')
        print('')
    if 'Publisher' in citation:
        print('Publisher: ', citation['Publisher'])
    if 'URL' in citation:
        print('URL: ', citation['URL'])
    if 'Secondary Authors' in citation:
        print('Secondary Authors:')
        for author in citation['Secondary Authors']:
            print("    ", end='')
            print(citation['Secondary Authors'][author]['First Name'], end=' ')
            print(citation['Secondary Authors'][author]['Last Name'])
    if 'Date' in citation:
        print('Date: ')
        if 'Day' in citation['Date']:
            print('    Day:', citation['Date']['Day'])
        if 'Month' in citation['Date']:
            print('    Month:', citation['Date']['Month'])
        if 'Year' in citation['Date']:
            print('    Year:', citation['Date']['Year'])
    if 'Note' in citation:
        print('Note: ', citation['Note'])
    if 'Will be exported' in citation:
        print('Will be exported: ', end='')
        if citation['Will be exported']:
            print('Yes')
        else:
            print('No')
    print('Last date updated: ', citation['last_date_changed'])
    print('Last time updated: ', citation['last_time_changed'])


def printAllCitations():
    """" prints all the citations """
    data = fb.get('/DB', 'Citations')
    if data:
        print('Those are all your citations:')
    for citation in data:
        print('===============================')
        printCitation(data[citation])


def printProjectCitations(pid):
    """" prints all the citations that are relevant to a specific project """
    if not projectExists(pid):
        return
    data = fb.get('/DB', 'Citations')
    flag = 1
    print("The citations that are relevant to project #" + str(pid) + " are:")
    for citation in data:
        if str(pid) in list(data[citation]['Project IDs']):
            print('===============================')
            printCitation(data[citation])
            flag = None
    if flag:
        print("None")


def printCategoryCitations(catid):
    """" prints all the citations that are relevant to a specific category"""
    if not categoryExists(catid):
        return
    data = fb.get('/DB', 'Citations')
    flag = 1
    print("The citations that are relevant to category #" + str(catid) + " are:")
    for citation in data:
        if str(catid) in list(data[citation]['Category IDs']):
            print('===============================')
            printCitation(data[citation])
            flag = None
    if flag:
        print("None")


def ExportToFile(msg, fileName):
    newFile = open(fileName, 'a')
    newFile.write(msg + "\n")
    newFile.close()


def IsExist(dic, str):
    """function that checks if str field exist in the dictionary"""
    if str in dic:
        return dic[str]
    else:
        return None


def export(pid, style):
    if not projectExists(pid):
        return
    Check = fb.get("/DB/Citations/", None)
    ExportToFile("Project " + str(pid) + " : " + style.upper() + " \n", "Project" + str(pid) + ".txt")

    for i in Check:
        lpid = list(Check[i]["Project IDs"])
        year = ''
        month = ''
        day = ''
        if 'Date' in Check[i]:
            if 'Year' in Check[i]['Date']:
                year = Check[i]['Date']['Year']
            if 'Month' in Check[i]['Date']:
                month = Check[i]['Date']['Month']
            if 'Day' in Check[i]['Date']:
                day = Check[i]['Date']['Day']
        start = ''
        end = ''
        if 'Pages' in Check[i]:
            if 'From' in Check[i]['Pages']:
                start = Check[i]['Pages']['From']
            if 'To' in Check[i]['Pages']:
                end = Check[i]['Pages']['To']
        first = ''
        last = ''
        if 'Author' in Check[i]:
            if 'First Name' in Check[i]['Author']:
                first = Check[i]['Author']['First Name']
            if 'Last Name' in Check[i]['Author']:
                last = Check[i]['Author']['Last Name']

        if Check[i]["Will be exported"] and str(pid) in lpid:
            if Check[i]["Source"] == "book":

                dic = {
                    "key": 'db692591e248f09b5cb1314d063dd00f',
                    "source": 'book',
                    "style": style,
                    "pubtype": {"main": 'pubnonperiodical'},
                    "pubnonperiodical": {
                        "title": IsExist(Check[i], 'Title'),
                        "publisher": IsExist(Check[i], 'Publisher'),
                        "year": year,
                        "start": start,
                        "end": end
                    },
                    "contributors": [
                        {
                            "function": 'author',
                            "first": first,
                            "last": last
                        }
                    ]
                }
            elif Check[i]["Source"] == "magazine":
                dic = {
                    "key": 'db692591e248f09b5cb1314d063dd00f',
                    "source": 'magazine',
                    "style": style,
                    "pubtype": {"main": 'pubmagazine'},
                    "pubmagazine": {
                        "title": IsExist(Check[i], 'Title'),
                        "vol": IsExist(Check[i], 'Volume'),  # update lust for that or asking
                        "day": day,
                        "month": month,
                        "year": year,
                        "start": start,
                        "end": end
                    },
                    "contributors": [
                        {
                            "function": 'author',
                            "first": first,
                            "last": last
                        }
                    ]
                }
            elif Check[i]["Source"] == "newspaper":
                dic = {
                    "key": 'db692591e248f09b5cb1314d063dd00f',
                    "source": 'magazine',
                    "style": style,
                    "pubtype": {"main": 'pubnewspaper'},
                    "pubnewspaper": {
                        "title": IsExist(Check[i], 'Title'),
                        "edition": IsExist(Check[i], 'Edition'),
                        "section": IsExist(Check[i], 'Section'),
                        "city": IsExist(Check[i], 'City'),
                        "day": day,
                        "month": month,
                        "year": year,
                        "start": start,
                        "end": end
                    },
                    "contributors": [
                        {
                            "function": 'author',
                            "first": first,
                            "last": last
                        }
                    ]
                }
            elif Check[i]["Source"] == "journal":
                dic = {
                    "key": 'db692591e248f09b5cb1314d063dd00f',
                    "source": 'journal',
                    "style": style,
                    "pubtype": {"main": 'pubjournal'},
                    "pubjournal": {
                        "title": IsExist(Check[i], 'Title'),
                        "issue": IsExist(Check[i], 'Issue'),
                        "volume": IsExist(Check[i], 'Volume'),
                        "series": IsExist(Check[i], 'Series'),
                        "year": year,
                        "start": start,
                        "end": end
                    },
                    "contributors": [
                        {
                            "function": 'author',
                            "first": first,
                            "last": last
                        }
                    ]
                }
            elif Check[i]["Source"] == "online":
                dic = {
                    "key": 'db692591e248f09b5cb1314d063dd00f',
                    "source": 'website',
                    "style": style,
                    "pubtype": {"main": 'pubonline'},
                    "pubonline": {
                        "title": IsExist(Check[i], 'Title'),
                        "inst": IsExist(Check[i], 'Institiution'),
                        "day": day,
                        "month": month,
                        "year": year,
                        "url": IsExist(Check[i], 'URL'),
                    },
                    "contributors": [
                        {
                            "function": 'author',
                            "first": first,
                            "last": last
                        }
                    ]
                }
            if IsExist(Check[i], 'Secondary Authors') != None:
                for j in Check[i]['Secondary Authors']:
                    dic["contributors"].append(
                        {"function": 'author', "first": Check[i]['Secondary Authors'][j]['First Name'],
                         "last": Check[i]['Secondary Authors'][j]['Last Name']})
            response = requests.put("https://api.citation-api.com/2.1/rest/cite", json.dumps(dic))
            data = response.json()
            text = str(data['data']).replace("<i>", "").replace("</i>", "").replace("<u>", "").replace("</u>", "")
            ExportToFile(text, "Project" + str(pid) + ".txt")
    ExportToFile("\n", "Project" + str(pid) + ".txt")
    print("Project" + str(pid) + " was successfully exported to Project" + str(pid) + ".txt")


# --------tests:
def test_exports():
    """
        >>> test_exports()
        Project #985123 was added
        Citation #985124 was added
        Project985123 was successfully exported to Project985123.txt
        Citation #985124 was deleted (if existed)
        Project #985123 was deleted (if existed)
    """
    id1 = fb.get('/', 'nextProjectID')
    fakeid1 = 985123
    fb.put('/', 'nextProjectID', fakeid1)
    addProject('test')
    id2 = fb.get('/', 'nextCitationID')
    fakeid2 = 985124
    fb.put('/', 'nextCitationID', fakeid2)
    addCitation("book", [985123, ], "aaaa", "bbbb", "cccc", 1, True, "dddd", 1990, 12, 12, 58, 96, "dfdsfsd", None,
                "fdgdf")
    export(985123, "harvard")
    doctest.testfile("Project" + str(fakeid1) + ".txt")
    deleteCitation(fakeid2)
    fb.put('/', 'nextCitationID', id2)
    deleteProject(fakeid1)
    fb.put('/', 'nextProjectID', id1)
    os.remove("Project985123.txt")


def test_addProject_editProject_deleteProject():
    """
        >>> test_addProject_editProject_deleteProject()
        You must enter a project name
        Project #985123 was added
        No id was entered
        No data was entered
        Project #985123 was updated
        Project #985123 was deleted (if existed)
    """
    id = fb.get('/', 'nextProjectID')
    fakeid = 985123
    fb.put('/', 'nextProjectID', fakeid)
    addProject(None)
    addProject('test')
    editProject(None, None, None)
    editProject(fakeid, None, None)
    editProject(fakeid, pname='newtest', pstate=None)
    deleteProject(fakeid)
    fb.put('/', 'nextProjectID', id)


def test_addCategory_editCategory_deleteCategory():
    """
        >>> test_addCategory_editCategory_deleteCategory()
        You must enter a category name
        Category #985123 was added
        No id was entered
        No data was entered
        Category #985123 was edited
        Category #985123 was deleted (if existed)
    """
    id = fb.get('/', 'nextCategoryID')
    fakeid = 985123
    fb.put('/', 'nextCategoryID', fakeid)
    addCategory(None)
    addCategory('test')
    editCategory(None, None)
    editCategory(fakeid, None)
    editCategory(fakeid, 'newtest')
    deleteCategory(fakeid)
    fb.put('/', 'nextCategoryID', id)


def test_addCitation_editCitation_deleteCitation():
    """
        >>> test_addCitation_editCitation_deleteCitation()
        Wrong source type
        Citation #985123 was added
        No id was entered
        No data was entered
        Citation #985123 was edited
        Citation #985123 was deleted (if existed)
    """
    id = fb.get('/', 'nextCitationID')
    fakeid = 985123
    fb.put('/', 'nextCitationID', fakeid)
    addCitation(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    addCitation('Book', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    editCitation(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    editCitation(fakeid, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    editCitation(fakeid, 'Online', None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                 None)
    deleteCitation(fakeid)
    fb.put('/', 'nextCitationID', id)


# -----------------------------------
if logflag and conflag:
    main()
