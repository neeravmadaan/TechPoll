# QuickPoll | A fullstack online polling application 

## Features:
- User Login & Signup System
- Poll Creation: Registered users can create public/private polls 
- Time Limits & Poll Scheduling: Users can set time limits and schedule their polls
- Poll History: Users can view polls created by them via their profile. Users can also views the polls on which they voted.
- Deleting polls: Users can also delete the polls created by them
- Public Polls: Anyone can vote and view results
- Private Polls: Anyone can view the results. Only registered users can vote on them.
- Expired Polls: Anyone can view the results. No one can vote.
- Options: Polls can have any number of options.
- Data: Polls along with questions/options also display Start Time, End Time & Created By.
- Limits: Users are limited to 1 vote per poll
- Responsivness: The site is full responsive across all devices
- SEO: Relevant meta tags have been used. Further Google Lighthouse has been used to test SEO of the website.  

## Pages/Components:

### Header 
- Home Page, Login, Signup, Logout buttons 
### Home
- Header
- Active Polls (Public/Private)
- Inactive Polls 
### Login  
- Login Form 
### Signup 
- Signup Form
### Profile 
- Polls created by users
- Button to create new polls
- Button to delete polls
### Poll Creation Page
- Button to view poll creation guidelines
- Form to create poll

## Database Structure 
QuickPoll
<br>
|_ _ _ Polls
       <br>&nbsp;&nbsp;&nbsp;
       |_ _ _ Poll ID
       <br>&nbsp;&nbsp;&nbsp;
       |_ _ _ Question
       <br>&nbsp;&nbsp;&nbsp;
       |_ _ _ Options
       <br>&nbsp;&nbsp;&nbsp;
       |_ _ _ Start Time
       <br>&nbsp;&nbsp;&nbsp;
       |_ _ _ End Time
       <br>&nbsp;&nbsp;&nbsp;
       |_ _ _ Type (Public/Private)
       <br>&nbsp;&nbsp;&nbsp;
       |_ _ _ Created By 
<br>
|_ _ _ Users
       <br>&nbsp;&nbsp;&nbsp;
       |_ _ _ User ID
              <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              |_ _ _ Username 
              <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              |_ _ _ Created Polls: Poll ID
              <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              |_ _ _ Voted Polls: Poll ID

## Tech Stack
- Django: Main framework, Server Side Scripting 
- HTML5, CSS3: Website structing, Website Design 
- JavaScript: DOM Manipulation, Client Side Scripting 
- Google Firebase: User authentication, Database
- Heroku: Website deployment 
