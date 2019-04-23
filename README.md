# The BB Manager
An educational cli based project.

=========================================

Welcome to The BB Manager!

* Please notice that the first argument after the filename must be an option,         *
* while the order of the rest doesn't matter                                          *
* (except for secondary names,where last name must come after first name).            *
* Also please separate the argument marks and the values with a blank space.          *
* In addition you can use " " to mark few words as one argument(notes for example).   *
* "<" and ">" are used to demonstrate the syntax,using them is not necessary.         *

Here are your options:

==========================================================================================================
"-h" or "--help" to print this message
==========================================================================================================
"-li" or "--login" to log into The BB Manager:

Please use the following format:
'python tbbm.py -li pass: <password> '
Please note that you won't be asked to login again until you log out.
==========================================================================================================
"-lo" or "--logout" to log out The BB Manager
==========================================================================================================
"-cp" or "--changePassword" to change the current password:

Please use the following format:
'python tbbm.py -cp (or --changePassword) pass: <old_password> np: <new_password>
==========================================================================================================
"-ut" or "--unitTests" to run the unit tests.
==========================================================================================================
"-ap" or "--addProject" to add a new project:

Please use the following format:
'python tbbm.py -ap (or --addProject) n: "Project Name"  '
while "n:" is used to mark the name of the project
==========================================================================================================
"-ep" or "--editProject" to edit an existing project:

Please use the following format:
'python tbbm.py -ep (or --editProject) id: <id> pn: "Updated Name" '
while "<id>" is the id of the project you want to update
or
'python tbbm.py -ep (or --editProject) id: <id> s: "Updated State" '
while "s:" is to mark the state of your project (Active/Projected/Archived)
==========================================================================================================
"-dp" or "--deleteProject" to delete a project:

Please use the following format:
'python tbbm.py -dp (or --deleteProject) id: <id> '
while "<id>" is the id of the project you want to delete
==========================================================================================================
"-acat" or "--addCategory" to add a new category:

Please use the following format:
'python tbbm.py -acat (or --addCategory) n: "Category Name"  '
while "n:" is used to mark the name of the category
==========================================================================================================
"-ecat" or "--editCategory" to edit an existing category:

Please use the following format:
'python tbbm.py -ecat (or --editCategory) id: <id> n: "Updated Name" '
while "<id>" is the id of the Category you want to update
==========================================================================================================
"-dcat" or "--deleteCategory" to delete a category:

Please use the following format:
'python tbbm.py -dcat (or --deleteCategory) id: <id> '
while "<id>" is the id of the category you want to delete
==========================================================================================================
"-ac" or "--addCitation" to add a new citation:

Please use the following format:
'python tbbm.py -ac (or --addCitation) <mark1>: <value1> <mark2>: <value2> ... '
Here is the list of the marks you can use ( part of them are mandatory ):
"st:"   - source type (Available source types are: Book, Journal, Newspaper, Online, Magazine)
"pid:" - the ID(s) of the project(s) that the citation is related to (for example pid: "1 2 3 4")
"t:"   - title
"fn:"  - main author's first name
"ln:"  - main author's last name
"cid:" - the ID(s) of the category(ies) that the citation is relevant to
"f:"   - will the file appear in the final version (yes/no )
"no:"   - a note
"y:"   - publishing year
"pub:" - publisher      ( please note that it should be one of the publishers in the list )                          
"m:"   - publishing month                         
"d:"   - publishing day                           
"ps:"  - from page __                             
"pe:"  - to page __                               
"u:"   - URL                                      
"sfn:" - secondary author's first name            
"sln:" - secondary author's last name             
==========================================================================================================
"-ec" or "--editCitation" to edit an existing citation:

Please use the following format:
'python tbbm.py -ec (or --editCitation) id: <id> <mark1>: <new_value1> <mark2>: <new_value2> ... '
while "<id>" is the id of the citation you want to update
and   "<mark>" is the mark of the field you want to update
==========================================================================================================
"-dc" or "--deleteCitation" to delete an existing citation:

Please use the following format:
'python tbbm.py -dc (or --deleteCitation) id: <id> '
while "<id>" is the id of the citation you would like to delete
==========================================================================================================
"-pap" or "--printAllProjects" to print all the projects
==========================================================================================================
"-paca" or "--printAllCategories" to print all the categories
==========================================================================================================
"-paci" or "--printAllCitations" to print all the citations
==========================================================================================================
"-ppc" or "--printProjectCitations" to print all the citations that are related to a particular project:

Please use the following format:
'python tbbm.py -ppc (or --printProjectCitations) id: <id> '
while "<id>" is the id of the project you are intrested in
==========================================================================================================
"-pcc" or "--printCategoryCitations" to print all the citations that are related to a particular category:

Please use the following format:
'python tbbm.py -pcc (or --printCategoryCitations) id: <cid> '
while "<cid>" is the id of the category you are intrested in
==========================================================================================================
"-eieee" or "--exportIEEE" to export a bibliography in IEEE format to a textfile:

Please use the following format:
'python tbbm.py -eieee (or --exportIEEE) id: <id> '
while <id> is the id of the project you would like to export in IEEE format
Please note that only the citations that are marked as "Will be exported" will be exported.
==========================================================================================================
"-emla" or "--exportMLA" to export a bibliography in MLA format to a textfile:

Please use the following format:
'python tbbm.py -emla (or --exportMLA) id: <id> '
while <id> is the id of the project you would like to export in MLA format
Please note that only the citations that are marked as "Will be exported" will be exported.
==========================================================================================================
"-eh" or "--exportHarvard" to export a bibliography in Harvard format to a textfile:

Please use the following format:
'python tbbm.py -eieee (or --exportHarvard) id: <id> '
while <id> is the id of the project you would like to export in Harvard format
Please note that only the citations that are marked as "Will be exported" will be exported.
==========================================================================================================
"-eapa" or "--exportAPA" to export a bibliography in APA format to a textfile:

Please use the following format:
'python tbbm.py -eieee (or --exportAPA) id: <id> '
while <id> is the id of the project you would like to export in APA format
Please note that only the citations that are marked as "Will be exported" will be exported.
==========================================================================================================
For more information please contact the developers.
Thank you for using The BB Manager :)

=========================================
