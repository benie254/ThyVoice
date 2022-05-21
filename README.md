# ThyVoice

A CRUD (Create,Read,Update,Delete) blog app, generated with [Python](https://www.python.org/) version 3.8.13 && [Flask](https://flask.palletsprojects.com/en/2.1.x/) version 1.1.4 

# ThyVoice
#### This repo creates a blogging app for content creators and reading enthusiasts, utilizing a database for data storage, retrieval, and manipulation.
## Author
[Benson Langat](https://github.com/benie254)

## Description

ThyVoice is a blogging app for people who love to write and those who enjoy reading. The app is built on a database, which stores user data & information, retrieves data for user requests, such as accessing blogs and comments && finally, our database enables user data manipulation, in cases such as deleting comments, or updating user posts and/or profile. Users have the initial option to view all blogs. To create a pitch, bloggers must log in or sign up. Once logged in, bloggers can share blog posts, comment on posted blogs, or update their profiles and/or posts. Bloggers can also delete comments they find insulting. 
      
    ThyVoice consumes a quotes api.

## Screenshot

<img src="https://user-images.githubusercontent.com/99865051/168407909-9fe76430-7b5c-442f-b76e-f75d1ba6af1e.png" >

## Screenshot #2

<img src="https://user-images.githubusercontent.com/99865051/168407922-023079e5-1e2e-4d51-b66a-079099abfe22.png">

## Behavior Driven Development--BDD

**1. Home Page**
   - OUTPUT: 'Navbar, Home page content'
   
**2. User Action:** 
   - INPUT:  Click : Navbar : 'ThyVoice', 'HOME'
   - OUTPUT: Home page
   - OUTPUT: All Blogs
   - OUTPUT: Random Quote
   
**4. User Action:**
   - INPUT:  Click : Navbar : 'Sign in'
   - OUTPUT: Login page
   - OUTPUT: Login form + option to 'Sign up'
   
**5. User Action:**
   - INPUT:  Click : option : 'Sign up'
   - OUTPUT: Sign up page
   - OUTPUT: Sign up form: 'Your email address...:','Your username...','Your password...:','Confirm your password'
   - INPUT:  user's details, click/ENTER: Submit
   - OUTPUT: Redirect to 'Login' page.
   
**6. Login Form:**
   - OUTPUT: 'Email...:','Password...:'
   - INPUT:  user's details, click/ENTER: Sign In
   - OUTPUT: Redirect to 'Home' page

**7. Home Page:**
   - OUTPUT: Random quote
   - OUTPUT: All blog posts
   - INPUT:  Click : 'Read more'
   - OUTPUT: Blog page
   - OUTPUT: The selected blog posts
   - OUTPUT: Blog content, All comments accordion, Comment accordion
   - INPUT:  Click: Comment
   - OUTPUT: Create comment form--on submit, blog page refreshes
   - INPUT:  Click: All comments
   - OUTPUT: All blog post comments

**8. User Action:**
   - INPUT:  Click : Navbar : 'ThyVoice', 'Home'
   - OUTPUT: Random quote
   - OUTPUT: All blog posts

**9. User Action:**
   - INPUT:  Click : Navbar : 'Create post'
   - OUTPUT: Create blog page
   - OUTPUT: Create blog form--on submit, redirects to home page

**10. User Action:**
   - INPUT:  Click : Navbar : 'Blogger Profile'
   - OUTPUT: Blogger profile page
   - OUTPUT: User bio section
   - OUTPUT: User's blog posts

**11. User Action:**
   - INPUT:  Click : 'Edit bio' 
   - OUTPUT: Profile update page
   - OUTPUT: profile update form--on submit, redirects to profile page
   
**12. User Action:**
   - INPUT:  Click : 'Update post' 
   - OUTPUT: Blog update page
   - OUTPUT: Blog update form--on submit, redirects to profile page

**13. User Action:**
   - INPUT:  Click : 'Delete post' 
   - OUTPUT: Blog delete page
   - OUTPUT: Blog delete confirmation--on submit, redirects to profile page

**14. User Action:**
   - INPUT:  Click : Navbar : 'ThyVoice','Home'
   - INPUT:  Click : 'Subscribe' 
   - OUTPUT: Subscribe page
   - OUTPUT: Subscribe user form--on submit, redirects to home page

**15. User Action:**
   - INPUT:  Click : Browser Page : Close
   - Exits


## Setup/Installation Requirements

* To use this open-source repo, clone it; to contribute, fork it. 
* Open your Terminal (CTRL + ALT + T on Ubuntu/Linux). 
* Make a destination directory in your preferred path (where you would like to clone the repo into.)
* Run the command ``` cd yourDestinationDirectory ```
* Run the command ``` git clone https://github.com/benie254/thyvoice.git ``` to clone the repo into your destination directory. 
* Run the command ``` cd ThyVoice ``` to move you into this repo's directory.
* Run the command ``` atom . ``` for Atom or ``` code . ``` for VSCode --opens the directory in your preferred code editor. (it is okay if you use something different.)
* Happy coding!

## Known Bugs

No known bugs. Please report any issues or encountered bugs! 

## Technologies Used

* [Python](https://www.python.org/) 
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)

## Other Resources 

* [Bootstrap](https://getbootstrap.com/) -- page designs
* [Adobe Color Wheel](https://color.adobe.com/) -- color palette 
* [Coolors](https://coolors.co/) -- color palette
* [Google Fonts](https://fonts.google.com) -- stylized fonts


## Support and contact details

Reach out with any issues, concerns, or contributions to [Benie-throughMail](davinci.monalissa@gmail.com)

### License

*Copyright (c) 2022* ***Benson Langat***

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*

###
Copyright (c) 2022 **Benson Langat**

[Python](https://www.python.org/) version 3.8.13
