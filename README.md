
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/tylertaewook/kentschool-emailbot">
    <img src="./logo.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Kent School Email Bot</h3>

  <p align="center">
    Email bot to automate Peertutor & Wrting Lab scheduling for Kent School
  <p align="center">
      October 2020
    <br />
    <a href="https://github.com/tylertaewook/kentschool-emailbot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/tylertaewook/kentschool-emailbot">View Demo</a>
    ·
    <a href="https://github.com/tylertaewook/kentschool-emailbot/issues">Report Bug</a>
    ·
    <a href="https://github.com/tylertaewook/kentschool-emailbot/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [About the Project]
  * [Modules & API]
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

This emailBot is a demonstration project used in my automation proposal made to Kent School Library in November 2020.
The main idea in this proposal was to change ARC(Writing Lab)'s sign-up system from handwriting on whiteboard to simple google forms/sheets.

Instead of students having to travel across the campus to write their name on library's whiteboard, using simple python scripts and google forms can make ARC reservation as easy as click of a button.
Of course, when they want to make a reservation, they will have to check what timeslot/tutor/teacher are available.
Rather than tediously visiting library several times a day to check the whiteboard, students can check the real-time timetable anywhere anytime using their phone.
This google sheet can only be editted by scripts to prevent others from changing schedules to their advantage. (Trust me, it happened a lot)
![Google Sheets](/images/sheets.png)

ARC-checker.py runs every five minutes to check for any new form submissions.
If a new submission is found, the script will simply compare with google sheets to check if a desired timeslot is available, and send a confirmation/rejection email to both students and tutor/teacher.

![Email](/images/email.png)

For demonstration purposes, I used my personal emailbot *tylerkim.bot@gmail.com*. 

<!-- CONTACT -->
## Contact

Tyler Kim - taewook.kim@columbia.edu

Project Link: [https://github.com/tylertaewook/kentschool-emailbot](https://github.com/tylertaewook/peertutor-emailbot)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/tylertaewook/repo.svg?style=flat-square
[contributors-url]: https://github.com/tylertaewook/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tylertaewook/repo.svg?style=flat-square
[forks-url]: https://github.com/tylertaewook/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/tylertaewook/repo.svg?style=flat-square
[stars-url]: https://github.com/tylertaewook/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/tylertaewook/repo.svg?style=flat-square
[issues-url]: https://github.com/tylertaewook/repo/issues
[license-shield]: https://img.shields.io/github/license/tylertaewook/repo.svg?style=flat-square
[license-url]: https://github.com/tylertaewook/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/tylertaewook
[product-screenshot]: images/screenshot.png
