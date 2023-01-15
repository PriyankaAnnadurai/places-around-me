# Places Around Me
## AIM:
To develop a website to display details about the places around my house.

## Design Steps:

### Step 1:
Clone the github repository into Theia IDE.
### Step 2:
Create a new Django project
### Step 3:
Write the needed HTML code.
### Step 4:
Run the Django server and execute the HTML files.

## Code:
```
 map.html:

<!DOCTYPE html>
<html lang="en">
<head>
<title>My City</title>
</head>

<body style="background-color: black;">
    <img src="/static/images/map.png" usemap="#MyCity" alt="MyCity" height="877" width="1498">
<map name="MyCity">
    <area shape="RECT" coords="695,518,748,596" alt="Jawaharlal Nehru Stadium" title="Jawaharlal Nehru Stadium" href="/JawaharlalNehruStadium/">
    <area shape="RECT" coords="834,668,1019,741" alt="Central" title="Central" href="/Central/">
    <area shape="RECT" coords="1145,653,1254,731" alt="Museum" title="Museum" href="/Museum/">
    <area shape="RECT" coords="1198,202,1307,280" alt="Temple" title="Temple" href="/Temple/">
    <area shape="RECT" coords="1128,460,1249,546" alt="High Court" title="High Court" href="/HighCourt/">
</map>
</body>
</html>

 central.html:

<!DOCTYPE html>
<html lang="en">
<head>
<title>Central</title>
</head>
<body bgcolor="pink">
<h1 align="center">
<font color="black"><b>Chennai Central</b></font>
</h1>
<h2 align="center">
<font color="brown"><b>Railway Station</b></font>
</h2>
<hr size="3" color="black">
<p align="justify">
<font face="Times New Roman" size="5">
<b>
Puratchi Thalaivar Dr. M.G. Ramachandran Central Railway Station, commonly known as Chennai Central (station code: MAS), is the main railway terminus in the city of Chennai, Tamil Nadu, India. It is the busiest railway station in South India and one of the most important hubs in the country. It is connected to Moore Market Complex railway station, Puratchi Thalaivar Dr. M.G. Ramachandran Central metro station, Chennai Park railway station, Chennai Park Town railway station and is 2 km from Chennai Egmore railway station. The terminus connects the city to northern India, including Kolkata, Mumbai, New Delhi as well as to Bengaluru, Ahmedabad, Guwahati, Chandigarh, Kerala, Hyderabad and different parts of India.

The century-old building of the railway station, designed by architect George Harding, is one of the most prominent landmarks of Chennai.The station is also a main hub for the Chennai Suburban Railway system. It lies adjacent to the current headquarters of the Southern Railway and the Ripon Building. During the British Raj, the station served as the gateway to South India, and the station is still used as a landmark for the city and the state. 
</b>
</font>
</p>
</body>
</html>

 highcourt.html:

<!DOCTYPE html>
<html lang="en">
<head>
<title>Highcourt</title>
</head>
<body bgcolor="lightcyan">
<h1 align="center">
<font color="black"><b>Madras High Court</b></font>
</h1>
<h2 align="center">
<font color="purple">The third oldest high court of India<b></b></font>
</h2>
<hr size="3" color="black">
<p align="justify">
<font face="Times New Roman" size="5">
<b>
The Madras High Court is a High Court in India. It has appellate jurisdiction over the state of Tamil Nadu and the union territory of Puducherry. It is located in Chennai, and is the third oldest high court of India after the Calcutta High Court in Kolkata and Bombay High Court in Mumbai. The Madras High Court is one of three high courts of colonial India established in the three Presidency Towns of Madras, Bombay and Calcutta by letters patent granted by Queen Victoria, dated 26 June 1862. It exercises original jurisdiction over the city of Chennai, as well as extraordinary original jurisdiction, civil and criminal, under the letters patent and special original jurisdiction for the issue of writs under the Constitution of India. Covering 107 acres, the court complex is one of the largest in the world, second only to the Supreme Court of the United Kingdom.

The High Court consists of 74 judges and a chief justice.
</b>
</font>
</p>
</body>
</html>

 museum.html:

<!DOCTYPE html>
<html lang="en">
<head>
<title>Central</title>
</head>
<body bgcolor="lavender">
<h1 align="center">
<font color="black"><b>Fort St. George</b></font>
</h1>
<h2 align="center">
<font color="darkred"><b>Museum</b></font>
</h2>
<hr size="3" color="black">
<p align="justify">
<font face="Times New Roman" size="5">
<b>
The Fort Museum, which is the only ticketed institution of the Archaeological Survey of India in the complex, exhibits many items of the period of English and later British rule. This building was completed in 1795 and first housed the office of the Madras Bank. The hall upstairs was the Public Exchange Hall and served as a place for public meetings, lottery draws and occasional entertainment. These relics are reminders of British rule in India. The objects on display in the museum are the weapons, coins, medals, uniforms and other artefacts from England, Scotland, France and India dating back to the colonial period. Original letters written by Clive and Cornwallis make fascinating reading. One set of quaint period uniforms is displayed for viewing, as well. However, the pièce de resistance is a large statue of Lord Cornwallis.

The National Flag of India was designed by Pingali Venkayya and adopted in its present form during the meeting of the Constituent Assembly held on 22 July 1947, a few days before India's independence from Britain on 15 August 1947. The first ever flag flown after the independence is stored in the third floor of the museum. The public are allowed to see but not to touch or take photographs. 
</b>
</font>
</p>
</body>
</html>

 stadium.html:

<!DOCTYPE html>
<html lang="en">
<head>
<title>Stadium</title>
</head>
<body bgcolor="rosybrown">
<h1 align="center">
<font color="black"><b>Jawaharlal Nehru Stadium</b></font>
</h1>
<h2 align="center">
<font color="midnightblue"><b>Marina Arena</b></font>
</h2>
<hr size="3" color="black">
<p align="justify">
<font face="Times New Roman" size="5">
<b>
Jawaharlal Nehru Stadium (also known as the Marina Arena) is a multi-purpose stadium in Chennai, India. It has a capacity to seat 40,000 people. It hosts football matches and athletic competitions. The complex also houses a multipurpose indoor stadium with a seating capacity of 5,000 which hosts volleyball, basketball, table tennis games. The stadium is also used for functions and concerts. The stadium is named after Jawaharlal Nehru, India's first Prime Minister. The stadium earlier hosted cricket test matches between 1956 and 1965. As of 19 August 2017 it has hosted 9 tests.

The stadium is located at Sydenhams Road, Park Town behind the Chennai Central suburban railway station and the Ripon Building. Tamil Nadu football team, which plays in Santosh Trophy and Chennaiyin FC, the Indian Super League team representing the city, use the stadium as their home ground. 
</b>
</font>
</p>
</body>
</html>

 temple.html:

<!DOCTYPE html>
<html lang="en">
<head>
<title>Temple</title>
</head>
<body bgcolor="lightyellow">
<h1 align="center">
<font color="black"><b>Kalikambal Temple</b></font>
</h1>
<h2 align="center">
<font color="navy"><b>Georgetown</b></font>
</h2>
<hr size="3" color="maroon">
<p align="justify">
<font face="Times New Roman" size="5">
<b>
The Kālikāmbal Temple is a Hindu temple dedicated to Shri Kāligāmbāl (Kāmākshi) and Lord Kamadeswarar, located in Parry's corner (Old: George Town) locality of the city of Chennai, Tamil Nadu, India. The temple is located in Thambu Chetty Street, a prominent financial street at Georgetown, running parallel to Rajaji Salai. The temple was originally located closer to the sea shore at the site of the present-day Fort St. George. When the British East India Company built the fort, the temple was relocated to the current site on 1 March 1640 and the construction continued until 1678. Chhatrapati Shivaji, the 17th century Maratha warrior-king and the founder of Maratha Empire, had paid a visit in this temple on 3 October 1677.It is believed that a fierce form of Goddess was held in worship earlier and that this form was replaced with the shanta swaroopa (calm posture) form of Goddess Kamakshi by Adi Shankara. Tamil poet Subramaniya Bharathi was a regular visitor of the temple in the early 20th century
</b>
</font>
</p>
</body>
</html>
```
## Output:
![map](./images/map.png)
![central](./images/central.png)
![highcourt](./images/highcourt.png)
![museum](./images/museum.png)
![stadium](./images/stadium.png)
![temple](./images/temple.png)
![validator](./images/validatormap.png)

## Result:
The program for implementing image map is executed successfully.