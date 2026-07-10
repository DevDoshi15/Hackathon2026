# Custom Package Details

**Path:** Custom Package Details > Custom Package Details

---

## Request Details

**Method:** `GET`

**URL:** `{{BaseUrl}}/v2/packageDetails/36228`

### Headers

```
SiteItemId: {{Nitro.Sandbox.SiteItemId}}
```

### Authentication

**Type:** basic

```
password: {{Nitro.Sandbox.ClientSecret}}
username: {{Nitro.Sandbox.ClientId}}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Tue, 18 Mar 2025 11:59:01 GMT
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
X-Served-From: 208.64.67.225
X-Powered-By: ASP.NET
X-Server-Ip: 192.168.214.15
Content-Encoding: gzip
```

### Response Body

```json
{
  "isSucceed": true,
  "data": {
    "siteItemId": 130385,
    "languageId": 7,
    "entityId": "-1_36228",
    "contentInfo": {
      "name": "HISTORY TO HIGH FASHION",
      "shortDescription": "Set sail on a 7-night Mediterranean cruise from Athens to Rome, with enchanting stops in the picturesque town of Sorrento, the vibrant city of Catania and the historic port of Chania. Discover stunning coastal landscapes, rich cultural heritage and captivating local traditions as you journey through these exquisite destinations before continuing on to experience the grandeur of Italy by rail from Rome to Milan, exploring Florence&#39;s artistic history along the way. ",
      "longDescription": ""
    },
    "media": {
      "files": [
        {
          "path": "/Site/Images/custompackage/1120x480_Florence_City.jpg",
          "name": "ShowcaseImage",
          "type": "Image",
          "imageType": "Other"
        }
      ]
    },
    "inclusion": "<ul><li>1 Nights, 4-Star Accommodation in Athens+, breakfast included</li><li>7 night cruise aboard&nbsp;<strong><em>Azamara Pursuit</em></strong><strong><em>&nbsp;</em></strong>from Athens (Piraeus) to Rome (Civitavecchia)</li><li>Main meals~ and entertainment onboard</li><li>2 nights 4-star accommodation in Rome+, breakfast included</li><li><strong>Sightseeing</strong>: Imperial Tour of Rome</li><li>2 nights at 4-star accommodation in Florence+, breakfast included</li><li><strong>Sightseeing</strong>: Half-day guided walking tour of Florence</li><li>2 nights at 4-star accommodation in Venice+, breakfast included</li><li><strong>Sightseeing</strong>: 30-minute gondola ride in Venice</li><li>1 night at 4-star accommodation in Milan+, breakfast included</li><li><strong>Sightseeing</strong>: 1 Day Hop-on, Hop-off ticket in Milan</li><li>2nd Class rail travel from Rome to Florence, Florence to Venice and Venice to Milan</li><li>Private transfers between airport and hotel pre and post</li><li>Port charges, government fees, onboard gratuities and most taxes</li></ul><strong>BONUS OFFERS</strong><ul><li><strong>AIR CREDIT</strong> of&nbsp;<strong>$1,500^</strong> per person</li><li><strong>SAVE&nbsp;</strong>up to&nbsp;<strong>$600</strong> per stateroom twin share</li></ul>Use this as inspiration for your holiday as similar cruises are available. Why not extend with other arrangements, speak with your Travel Advisor for options.&nbsp;",
    "travelNotes": "",
    "policies": {
      "generic": "Cancellation penalties and conditions apply. Prices correct as of 17 Sep 2024 and are per adult in AUD<strong>.&nbsp;</strong>Prices are subject to change due to fluctuations in charges, taxes and currency even after the deposit is paid. Offer subject to availability. Agents may charge service fees or fees for card payments which vary. Cancellation penalties and conditions apply. ^Air Credit is $1,500 per person and included in the package price. Air Credit may be used toward any airfare booked with your Travel Advisor or the value may be deducted from the package if you prefer to book this component independently. Cruise fares also cover certain shipboard services including stateroom accommodations, onboard main meals and entertainment. ~Meals are included in selected restaurants onboard; specialty restaurants may incur a surcharge. Pricing and savings are based on the difference between the exclusive package cruise fare and the best available equivalent fare for veranda category V3, twin occupancy. The 7-night land tour is an independent tour package and does not include gratuities, meals unless noted, or porterage and has a limit of one (1) piece of luggage. +Local city tax and resort fees to be collected on arrival at each hotel in Athens, Rome, Florence and Milan. Transfers to/from train stations are not included. Please note any dietary of mobility needs at time of booking. This offer is valid until 11 Nov 2024,<strong>&nbsp;</strong>unless sold out prior. Offers may be withdrawn without notice and are not combinable with any other offers unless stated. Please check all prices, availability and other information before booking. For full terms and conditions please refer to Viva Holidays and Azamara Cruises respective websites and https://www.creativecruising.com.au/terms-conditions/ REF AZA089. "
    },
    "packageTourId": 36228,
    "pdfPath": "",
    "templateName": "Template1",
    "isActive": true,
    "status": "Publish",
    "validFrom": "03-Oct-2024",
    "validTill": "01-Sep-2025",
    "itineraryDetails": [
      {
        "description": "Air Credit",
        "priority": 1,
        "type": "Air",
        "position": "PreCruise",
        "longDescription": "Air Credit ",
        "id": 120919,
        "isDefault": true,
        "optionalNodes": []
      },
      {
        "description": "Private Transfer: Airport to Hotel",
        "priority": 2,
        "type": "Transfer",
        "position": "PreCruise",
        "longDescription": "Private standard car transfer from airport to hotel<br><em>Note: Guest flight details and emergency contact number are required to confirm the transfer.</em>&nbsp;",
        "id": 120920,
        "isDefault": true,
        "optionalNodes": []
      },
      {
        "description": "1 Night Accommodation in Athens",
        "priority": 3,
        "type": "Hotel",
        "position": "PreCruise",
        "durationInMinutes": 1440,
        "longDescription": "1 nights, 4-star accommodation in Athens, breakfast included ",
        "id": 120921,
        "isDefault": true,
        "optionalNodes": []
      },
      {
        "dayOffSet": 1,
        "description": "Private Transfer: Hotel to Port",
        "priority": 4,
        "type": "Transfer",
        "position": "PreCruise",
        "longDescription": "Private standard car transfer from hotel to port ",
        "id": 120922,
        "isDefault": true,
        "optionalNodes": []
      },
      {
        "dayOffSet": 8,
        "description": "Private Transfer: Port to Hotel",
        "priority": 6,
        "type": "Transfer",
        "position": "PostCruise",
        "durationInMinutes": 1440,
        "longDescription": "Private standard car transfer from port to hotel ",
        "id": 120923,
        "isDefault": true,
        "optionalNodes": []
      },
      {
        "dayOffSet": 8,
        "description": "7 Night Art & Fashion - 4* - Standard Tour / Independent Rail",
        "priority": 7,
        "type": "Activity",
        "position": "PostCruise",
        "durationInMinutes": 10080,
        "longDescription": "<strong>7 nights Art &amp; Fashion Cities of Italy Tour</strong><br><br><strong>DAY 1 - ROME</strong><br>You can explore the city on your own to discover the most famous symbols of Rome, such as Piazza Navona, the Trevi Fountain, the Pantheon, Spain Square. We recommend a guided tour of the Vatican Museums, to admire Michelangelo&#39;s famous Sistine Chapel and other masterpieces of the Italian Renaissance more closely. It is also possible to participate in a series of other optional activities, such as a cooking lesson to learn how to make pizza or pasta and ice cream. For dinner we suggest trying a typical Roman restaurant. Overnight stay at the hotel in Rome.<br>Accommodation: Hotel Gambrinus or similar.<br><br><strong>DAY 2 - ROME (B)</strong><br>Breakfast at the hotel, then another day dedicated to discovering the city. Today you join our Imperial Tour of Rome (included in the rates), to closely admire the monuments of the Roman Forum, enter the Colosseum and listen to our guide&#39;s presentation of the evocative history of ancient Rome and the gladiators&#39; fights that took place there. In the afternoon, free time to continue exploring the Eternal City. You can join an excursion to visit Rome Catacombs. For the sporty people, there is also the option of an electric bike tour, to discover the historic center with its symbols or even a more secret and unusual Rome. For the evening, we recommend a nice walk in the Trastevere district, full of typical restaurants. Overnight stay at the hotel in Rome.<strong>&nbsp;</strong><br>Accommodation: Hotel Gambrinus or similar.<br><br><strong>DAY 3 - ROME - FLORENCE (B)</strong><br>After breakfast at the hotel, you will reach Rome Termini station to board the high-speed train to Florence; the journey takes about 1h 30&rsquo;. After arriving, hotel accommodation and free time available for an independent visit of the city, the &#39;cradle of the Renaissance&#39;. We would suggest a guided tour of one of the main museums: the Uffizi Galleries, with the masterpieces of the masters of the Italian Renaissance (Leonardo, Caravaggio, Raffaello, Tiziano, Botticelli and many others), or the Accademia Gallery, which houses the original of Michelangelo&#39;s famous statue of David, or an half day visit to Pisa and its famous leaning tower. Overnight stay at the hotel.<br>Accommodation: Hotel Executive or similar.<br><br><strong>DAY 4 - FLORENCE (B)</strong><br>Breakfast at the hotel. Today you will discover two thousand years of history of the cradle of the Renaissance through the eyes of an expert local guide, who will take you in an unforgettable journey to discover the most beautiful squares and monuments of Florence. With this half day tour, you will admire with your own eyes the sites and monuments that have made Florence one of the most visited destinations in the world. Rest of the day at disposal to visit the monuments and/or the museums or Florence or organize an excursion to the surrounding areas. Overnight stay at the hotel.<br>Accommodation: Hotel Executive or similar.<br><br><strong>DAY 5 - FLORENCE - VENICE (B)</strong><br>After breakfast at the hotel, we board the high-speed train to Venice S. Lucia. The journey takes about 2h 15&#39;. After arriving, hotel accommodation, so in the afternoon there will be a 30-minute &ldquo;gondola ride&rdquo; with commentary via app on your mobile phone. Before dinner in Venice, it is traditional to have an aperitif based on &ldquo;cich&eacute;ti&rdquo; (small snacks) in one of the many &ldquo;bacari&rdquo; (taverns) scattered along the &ldquo;calli&rdquo; (that is what the Venetian streets are called): a must experience to try, absolutely! Overnight stay at the hotel.<br>Accommodation: Hotel Carlton on the Gran Canal/ Hotel Principe&nbsp;or similar.<br><br><strong>DAY 6 - VENICE (B)</strong><br>Breakfast at the hotel, then full day dedicated to the discovery of Venice or its lagoon. You can take a guided walking tour through the most famous places in the city (Piazza San Marco with the Basilica and the Clock Tower, the Rialto Bridge, Campo Santa Maria Formosa) and others less known; or a skip-the-line guided tour of the Doge&#39;s Palace, with the Doge&#39;s luxurious apartments and the famous Bridge of Sighs. Alternatively, you can go on a boat trip to the islands of the Venice lagoon: Murano, known all over the world for its famous glass craftmanship; Burano, famous not only for its lace, but also for the picturesque fishermen&#39;s houses all painted in bright colours; and Torcello, the first settlement centre in the lagoon. Overnight stay at the hotel.<br>Accommodation: Hotel Carlton on the Gran Canal/Hotel Principe or similar.<br><br><strong>DAY 7 - VENICE - MILAN (B)</strong><br>After breakfast at the hotel, we board the high-speed train to Milan. The journey takes about 2h 30 &#39;. After arriving, hotel accommodation and free time for all to visit the city on one&rsquo;s own. A one-day ticket for the hop-on / hop-off tourist bus (with multilingual audio guide) is included, which can also be used to get around the city, ideal for those who want to go sightseeing on their own to discover the most famous symbols of Milan, such as the Duomo, the Castello Sforzesco, the Basilica of Sant&#39;Ambrogio and the Navigli, the famous canals, the very hub of the Milanese nightlife. You can continue your visit to the city with an internal visit of the Teatro alla Scala and its museum, a unique experience to visit one of the most famous theatre houses in the world. For the sports enthusiasts, a bike tour Tour is also available. Alternatively, you can choose a day of shopping at the Serravalle outlet. Overnight stay at Hotel.<br>Accommodation: NYX Hotel Milan or similar.<br><br><strong>DAY 8 - MILAN (B)</strong><br>Breakfast at the hotel, check-out and end of the tour.<br>Possibility to book a private transfer to the airport as an additional service, or to continue the journey by joining another tour of ours. ",
        "id": 120924,
        "isDefault": true,
        "optionalNodes": []
      },
      {
        "dayOffSet": 15,
        "description": "Private Transfer: Hotel to Airport",
        "priority": 8,
        "type": "Transfer",
        "position": "PostCruise",
        "longDescription": "",
        "id": 120925,
        "isDefault": true,
        "optionalNodes": []
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
