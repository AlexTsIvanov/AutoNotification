# AutoNotification
Automatic Notification(Email/SMS) Web Application for Vehicle Inspections

## Reason Behind the Project
While doing the yearly technical inspection for my car I noticed that at the end of my check the employee asked for my name and telephone number and put it in a physical book. After a year they take out the book from last year and manually go through the list and notify the customers that their inspection is due. I realised that software can be used to automate this process and even extend it to be able to notify customers through email. 

## Development Process
Created a PostgreSQL database containing all the needed values.  
Created a simple HTML page to visualize the database entries.  
Implemented a filter that the user can filter the values based on different criteria.  
Created a data entry form.  
All the newly created entries get a status value of "Inspection Period Not Over".  
Created a script that executes once every day. It takes all the database entries whose inpection is due in 7 days and sends an email.  
Once the email request goes through the status value is updated to "Customer Notified Successfully".  
The user can filter by status to see if all the customers are notified successfully.

## Future Work
Implement SMS notifications.    
Create a way for users to be able to resend notifications in cases where there is an error during notification process.