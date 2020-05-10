## Wireframes
Purpose / Notes
![Purpose / Notes](https://i.imgur.com/iiANu6z.jpg)

Login / Register
![Login / Register](https://i.imgur.com/RQL9jm0.jpg)

Add / Edit Dog
![Add / Edit Dog](https://i.imgur.com/Okj4R33.jpg)

All Dogs
![All Dogs](https://i.imgur.com/6nr1w42.jpg)

Map / Home
![Map / Home](https://i.imgur.com/SjRDyt7.jpg)

OR

MapShowPage / Home(UserPage) (better version)
![MapShowPage / Home(UserPage) (better version)](https://i.imgur.com/vhpRonQ.jpg)

Add / Edit Profile / Preferences
![Add / Edit Profile / Preferences](https://i.imgur.com/vhpRonQ.jpg)

Models chicken scratch
![Models chicken scratch](https://i.imgur.com/dJt1Us0.jpg)

User Preferences / Dog Profile (version 1)
![User Preferences / Dog Profile (version 1)](https://i.imgur.com/l3Ukqb0.jpg)


## User Stories

- User can REGISTER, LOGIN, LOGOUT
- User can CREATE their dog
- User can EDIT/UPDATE/DELETE their dog
- User can DELETE their dog
- User can VIEW all dogs
- User can VIEW the map
- User can CREATE a profile (preferences)
- User can EDIT/UPDATE/DELETE their profile (preferences)
- User can VIEW all parks ??
- User can see which parks are Green, Yellow, or Red light
- User can select park to see that park's details:
	- including name, location, clean, big, fenced, busy
- User can CRUD Parks

## Models

- Dog
	- name
	- owner (FK)
	- breed
	- image

- User
	- username
	- email
	- password
	- ? current location ? (Geospatial)

- Park
	- name
	- location (Geospatial)
	- isClean (bool)
	- isFenced (bool)
	- isBusy (bool)
	- isBig (bool)

- UserPref (or maybe call it Profile, or UserProfile)
	- clean
	- fenced
	- busy
	- big

## Routes (-- all /api/v1 --)

- /users/register (register) POST
- /users/login (login) POST
- /users/edit (edit/update) PUT
- /users/delete (delete/destroy) DELETE
- /users/all (show/index) GET

- /dogs (show/index user's dogs) GET
- /dogs/all (show/index all dogs) GET
- /dogs/ (create) POST
- /dogs/id (delete) DELETE
- /dogs/id (edit/update) PUT

- /parks (show/index) GET
- /parks/ (create) POST
- /parks/id (delete) DELETE
- /parks/id (edit/update) PUT


## Tech Used

- React front
- Flask back
- SQL DB
- Google Maps / Mapbox API ??


## Other Notes
- Can the User add comments / posts to the park

- Does the park data (related to User Preferences) revert to Default at 12AM daily? (user is going to cruyd the parks)

- Should the home page be the Map, or the list of parks with the User's profile side by side?
	- where the User could select a park, or edit/update their profile/preferences
- Can Users chat? (socket.io)

- Can user "check-in" to say they are currently at a park?

- Is there any social element whatsoever?
- 

## Questions for TS, RA or DB
- How can I assign values to the importance of each preference a User selects from the options? (later 5.10)
- Am I setting up models correctly? (good)

- Route for creating user profile?  dog profile?  or should those fields be a part of the models?

- registering (sign up here to register) -- 

		Warning: Failed prop type: Invalid prop `children` supplied to `Form`, expected a ReactNode.
    in Form (at LoginRegisterForm/index.js:44)
    in LoginRegisterForm (at App.js:95)
    in div (at App.js:86)
    in App (at src/index.js:9)
// dont worry about this for now //

# NEED TO UPDATE THIS ( THE NEW USER MODEL INFO (PREFS) ) IN THE USER STUFF!!!!

- FOR scoring system (preferences) use 1, 2, and 3
- Get mapbox token
- integerfield for perferences
- making both parks and user pref's integers, 


NEW Q for TS -- 
if i DONT wanna create multiple user_prefs... need help with conditional (if already have user prefs created, dont create, etc... )

-- what to do for the User Profile Show / addform / edit/update? all messed up



TODO's
- set up parks container, parks list, addpark form, edit park modal







