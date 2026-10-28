# Sprint 2 - Implement Database and Display of Test Data


## Sprint Goals

Implement the database, populated with test data. Create queries that retrieve test data, and display this on web pages as needed. Test and refine the queries and data display, so that it stands as the basis of the next sprint.

### Specific Goals

**Edit these goals as needed**

- Implement the database
- Add test data to the database
- Create the following web pages:
    - Home pages showing the two options shown in my test UI flow. 
    - Successfully display a page where the user can import student names. 
    - Etc.
- Develop SQL database queries to:
    - Retrieve all data nessacery for the report to be generated.
    - Retrieve specific information such as student names.
    - Etc.


## Test 1 - Displaying Seed Data of Student Info

I am testing whether the seed data I added into the data bases were accessable and displaying on the front end. I did this by creating a page that shows some information from these data bases, such as student id, ratings for subjects and overall rating. I was able to display some test data hich proved that the connection is working.

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

![report-preview-test](image-4.png)

### Changes / Improvements

After a discussion with my stakeholder, he asked the question "How will I be able to pick a student from the class list to view there report?" - Gareth 
This made me realise that there is a massive flaw in the system, the user cannot look back on reports or students in general which destroys the point of saving student data in a database. 

"Could you have a page where all of my students are showed, so I can select which student I want to create a report for?" - Gareth
Further discussion with my stakeholder revealed that it would be a much better idea to have a class list page with a list of students that show their name and student ID

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**

Here is the UI mock up:
![class-room-page-penpot](image-5.png)


## Test 2 - Class Room Page

I will be testing whether the class room page displays the student name and student ID as it should in the desired order.

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

![class-room-page](<Screenshot 2026-10-27 144131.png>)
### Changes / Improvements

"Can the students be ordered in Alphabetical order?" - Gareth 
I will sort the students names A to Z and display them in this order.

![names-alphabetical-order](image-6.png)

"What term does the plus button bring you to?" - Gareth 
The plus button was the original link to the term selection page, for clearity I will remove the plus button and replace it by making the student's container a link itself.

![student-info-link](image-7.png)

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**


## Testing Student Info 

I will be testing whether the info of the student can be displayed using seed data when selecting someone from the list.

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**


### Changes / Improvements

Replace this text with notes any improvements you made as a result of the testing.

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**


## ETC...


## Sprint Review

Replace this text with a statement about how the sprint has moved the project forward - key success point, any things that didn't go so well, etc.

