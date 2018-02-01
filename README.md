# RunDo
capstone
#RUNdo Your Cravings

Overview: I'm sitting on the couch and looked down and just realized I ate and entire 'sleeve' of Oreos. Has this ever happened to you? Do you immediately feel guilty and want to do undo what you just ate? With this app, just add in a few personal fitness details and find out how far you need to run to get back to zero!

Features- help people stay fit when they have cheat meals

use api to access a food/exercise database so users will have ability to input branded food products or standard foods to obtain accurate nutritional information
pre-set calculations will provide accurate workout information to user
link to fitness app/tracker like Myfitnesspal to input food and run data to profile (major milestone)
Libraries/frameworks- Django

Functionality-

the homepage will prompt you to login or create account
the profile page will prompt you to input the food you ate, physical stats (age, sex, height, weight), fitness level (how fast you are in mph), and a calculate function
the user's individual results page will include confirmation of their food, a results table (shows how far they will need to run to burn off food eaten), and a recalculate function that will redirect to their profile page for new input
Models-

User profile

age
sex
height
weight
fitness level (running- mph; other activities- newbie/novice, average, athletic/buff)
Food data

serving size
number of servings
total calories
Schedule

Milestone 1
create profile to store user data
food data tables
figure out how to pull calorie info from a food api
running/exercise calculations (function)
Milestone 2
add additional types of exercises (swimming, tennis, ultimate frisbee)
link and push data to Myfitnesspal or similar app tracker