Django project School app (Students HUB)  
Clement JONGLAS  
  
|-----------------------------------------------------------|  
|----------------------|CA 1 CREATION|----------------------|  
|-----------------------------------------------------------|  
  
------------------------------------------------------------- schools uses  
  
this app is made of 2 object:  
  
-> School:    
    -id(auto_genrated)  int     private key  
    -name               String        
    -location           String  
    -nb_stutens         int  
  
-> Student:  
    -id(auto_genrated)  int     private key  
    -name               String  
    -school             School  foreignkey  
    -year               String    
    -already_graduated  Boolean  
  
the app allow the user to see the list of schools  
-Main page-
by cliking on a school you can see school's information   
  
    SCHOOL INFORMATION PAGE
        here you can see the name, the location, the number of students attending classes in this school and the list of those students
        on the same page you can delete a school(Delete a school will delete every students attending courses in this school)

you can also add an other school to the list

    SCHOOL ADD PAGE
        here you can ener all information needed for the creation of a new school

fianly you can also see the list of every students, order by schoolby clicking the last link

    STUDENTS LIST PAGE

        here you can see the list of student order by school, even those who don't have one
        by cliking on a student you can access the student page

            STUDENT PAGE
                here you can find all informations about the student : name,school...
                from here you can delete and update the profile of the student
        there is also a link to create students profile


|-----------------------------------------------------------|  
|-----------------------|CA 2 UPDATE|-----------------------|  
|-----------------------------------------------------------|  
  
  
New addition :   
  
-> Accounts system :  
	Now you need a accounts to access Students HUB.  
	To do so, you will be able on the main page to log you/ create a account.  
	Once done, you will be able to access the aplication Home page.  
	An other button apear on the main page, cliking it will browse you to the account settings.  
	there you can log out and change reset your password  
  
-> Front-end interface :   
	A brand new inteface as been intergrated at the aplication. Main colors are red/white/black  
	All pages have been modified.  
	All images used are from mine own création, rendered on Blender software(this is why there is no mention/credits on images)  
  
Few fixes :   
  
-> corection of a little bug find in the number of staudent of schools:  
	when a students was created with a school link, or when a student was delete the atribute {nb_students} was updated, but not when a student's profile was modified.  
	
	




