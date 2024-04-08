## About SpamMarker: 
SpamMarker is a backend module that creates  REST Api to be consumed by application similar to various popular applications which tell if a phone number is spam or not and allow 
a registered user to find person's name by searching for their phone number and vice versa.

A registered user can have multiple contacts in contact list and all contacts in the contact list may not be registered. Hence two different custom models were used- one for storing 
credentials such as phone number, name, email, password of a registered user and another is for storing details of others who are in contact list of registered users.

If I make a summary of what are the features that SpamMarker has-
   1. JWT based authentication system,
   2. Registered users can have their own contact list and may have multiple registered or non-registered users or phone numbers,
   3. Registered users have access to global database of contacts,
   4. Searching functionality is there to search phone number through name and vice versa,
   5. Registered users can mark a potential spam contact as spam.

Visit this link to see the [Approach](https://drive.google.com/file/d/1lK2sMg5BA04s-ye0qvq-GEMvlHqrYfHR/view?usp=sharing) 

Last Edit: 8th April, 2024
