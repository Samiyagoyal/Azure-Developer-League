# Azure-Developer-League

## Contents

- [ABOUT](#about)
- [PROJECT FEATURES](#project-features)
  - [SOCIAL NETWORK](#social-network)
  - [VOLUNTEERING OPPORTUNITIES](#volunteering-opportunities)
  - [RECOMMENDATION SYSTEM FOR THE ORGANIZATIONS](#recommendation-system-for-the-organizations)
  - [RECOMMENDING NGOs TO COLLABORATE IN EVENTS](#recommending-ngos-to-collaborate-in-events)
  - [CUSTOMER ENGAGEMENT](#customer-engagement)
  - [EMLOYEE MANAGEMENT SYSTEM](#employee-management-system)
  - [CALENDAR](#calendar)
- [TECHNOLOGIES USED IN THE PROJECT](#technologies-used-in-the-project)
- [PACKAGES USED](#packages-used)
- [PROPOSED PLAN](#proposed-plan)
  
## ABOUT

This repository provides code for machine learning based recommendation system  algorithms which recommends events and partnerships for non-profit organizations.

SocieTree is aimed at becoming a SaaS integrated networking platform to empower nonprofits while redefining the way the social sector functions. The platform would allow nonprofits to hire skilled volunteers, collaborate with similar organizations, manage their employees, and engage with their audiences, thus proving to be a one-stop destination for all their requirements.

On visiting the [website], click on Nonprofit Login in the header. The homepage offers the basic details about the platform and the features they will have access to after onboarding. The organizations can use the non-profit login to acquire the Dashroot controls. The platform addresses the management and networking issues of non-profit organizations by setting up a social network for them to maintain their web presence, hire skilled volunteers, form partnerships with organizations having similar interests and much more.

## PROJECT FEATURES

### SOCIAL NETWORK
It will act as a social networking platform for non-profit organizations. It is customised just for them to socialise with their fellow organizations and prospective partners. It would help initiate collaborations and expand their networking circle.  

After logging in, the users are displayed with their feed i.e they will be able to interact/socialise with their network. The organizations will be able to:
1. Add new posts, sharing with all their partner organizations their work and progress, and delete posts
2. Save other organizations’ posts for reference, 
3. Share posts they find informative and valuable, 
4. Like and comment on the posts they find worthy.

<img src="Images/Main page 1.png"
     style="width:100%; height:auto; padding-right:55px; margin-left:25px;" />

### VOLUNTEERING OPPORTUNITIES
It acts as an aggregation platform where organizations can add positions under any vertical for which they want volunteers. These positions/vacancies are then offered to the volunteers where they can apply as suitable to them.

Features that can be used are: 
1. Adding new positions - New positions can be created by filling out a simple form stating the work requirements from the volunteer such as their expected time commitments, their work responsibilities, the domain of work and mode of volunteering etc.
2. Edit the added positions - Positions can be edited as per the revised requirements of the organizations.
3. Deleting completed positions - Once the number of applicants fills the vacancies available, the organization can delete the position.
4. Archiving positions - For positions they would like to reopen later, an archive feature is also available. This would facilitate easy handling of constant demanding positions.

<img src="Images/Volunteering Opportunity 1.png"
     style="width:100%; height:auto; padding-right:55px; margin-left:25px;" />

### RECOMMENDATION SYSTEM FOR THE ORGANIZATIONS
It recommends opportunities to partner organizations with similar nonprofits to hold collaborative events to leverage the use of shared resources.

A recommender system is established over a dataset, collected and pre-processed from a Government recognized repository by using the TF-IDF (term frequency-inverse document frequency) Vectorizer and Cosine Similarity functions made available in Scikit-Learn.

Core technologies used model construction and deployment:
- Azure Machine Learning Studio
- Azure cloud services
- Bubble.io, a low-code platform for developing SaaS applications.

### RECOMMENDING NGOs TO COLLABORATE IN EVENTS
- Data pertaining to events organized by the NGOs is collected
- The collected dataset is preprocessed and reduced such that it contains only the key features of every NGOs event. 
- TF-IDF Vectorizer and calculated Cosine similarity are implemented which explains the amount of correlation within the data with respect to every entry in the data. The major focus is on the ‘Organizational Activities ’ conducted by the NGO so as to prioritize the accurate recommendation to NGOs 
- Cosine similarity matrix is deployed as a model by converting it into a pickle file and retrieving the data later through joblib function. 
- The model is deployed using a scoring script. The deployed model is used as a REST Endpoint which gets generated when the model is deployed. 
- We then recommend the NGOs to participate in various events from our Website which is made using Bubble platform, to facilitate the users to communicate/collaborate with other similar NGOs regarding the event taking place.

<img src="Images/ML Recommendation.png"
     style="width:100%; height:auto; padding-right:55px; margin-left:25px;" />


### CUSTOMER ENGAGEMENT
Email campaigns play a major role for the organizations to roll out important information about new initiatives or maybe weekly newsletters. 

The portal allows users to schedule marketing campaigns such as email marketing. The organizations can upload all their contacts onto the portal in a CSV file and send out custom designed emails at once to all their contacts. The user just has to fill out a simple form mentioning information like subject, the body of the mail, any images to be included, other attachments etc and then choose from a variety of predesigned templates. The mass mailing can be automated to be sent at a particular time at which the user wants it to be delivered. This feature can help organizations to enhance content marketing and establish their continuous presence.

<img src="Images/Customer Engagement 1.png"
     style="width:100%; height:auto; padding-right:55px; margin-left:25px;" />
     
### EMPLOYEE MANAGEMENT SYSTEM
A systematic approach for managing the work at organisations is made available to the organisations under the “Employees” tab. These features allow efficient agile functionality to get a proper working system for communication between various sub-teams at the same time.

The employees can be added with the help of the “Add Employee” button, where the organisation can add a CSV file having the details of the employees to be added. Upon uploading the file, instantly a list of employees will be displayed there. 

The employee details added are linked to the Projects Tab where the organisations can manage and assign tasks to the employee.

Functionality:

- The user can add sub-tasks under a project and choose the employees to whom the task is to be assigned. 
- The files and any other attachments related to the task can also be provided to the employees then and there, which on clicking will open on a separate tab, eliminating the need to download the files. Hence, the employees don’t need to use their own storage space for the files.  
- Any other details or instructions can also be added as comments in the project so that they can easily be noted by the employees. 
- The employees can submit their work by adding their respective files under the Files Tab under Projects.  
- The project can then be deleted after it’s done successfully.

The projects can also be added to the calendar to keep track of deadlines and progress.

<img src="Images/Employee Management 1.png"
     style="width:100%; height:auto; padding-right:55px; margin-left:25px;" />

### CALENDAR
The portal has an integrated calendar that can help users manage their personal schedules, time and activities. Users can schedule and keep track of their events and upcoming programs. The calendar is colour coded for different categories of work events and can be sort based on the type of event as well as based on time (upcoming or past events).

---

## TECHNOLOGIES USED IN THE PROJECT
- Figma
- Bubble
- Rest API
- Python
- Azure - ML Studio
- SendGrid API

---

## PACKAGES USED

- `numpy==1.20.1`
- `scikit-learn==0.24.1`
- `Flask==1.1.2`

---

## PROPOSED PLAN

FOR EXISTING FEATURES
- Login options and a customized dashboard for volunteers
- NGO recommendation system to be optimized for real-time recommendations taking into account new organizations
- Unifying social media platforms, post scheduling

ADDITIONAL FEATURES AS PER SOLUTIONS
- Volunteering position recommendation system
- WhatsApp integration (simpler method for nonprofits to receive regular updates - push notifications)     
     
