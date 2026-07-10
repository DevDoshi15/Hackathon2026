# Cruise Itinerary

**Path:** Cruise Itinerary > Cruise Itinerary

---

## Request Details

**Method:** `GET`

**URL:** `{{BaseUrl}}/v2/cruise/Itinerary/336475`

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
Date: Wed, 01 Feb 2023 09:25:01 GMT
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
    "id": 336475,
    "nodes": [
      {
        "port": {
          "code": "FAI",
          "type": "CruisePort",
          "internalCode": "FAI"
        },
        "description": "Fairbanks - Alaska (PRE-CRUISE TOUR)"
      },
      {
        "port": {
          "code": "FAI",
          "type": "CruisePort",
          "internalCode": "FAI"
        },
        "dayOffSet": 1,
        "description": "Fairbanks - Alaska (PRE-CRUISE TOUR)"
      },
      {
        "port": {
          "code": "DNL",
          "type": "CruisePort",
          "internalCode": "DNLI"
        },
        "dayOffSet": 1,
        "description": "Denali - Alaska (PRE-CRUISE TOUR)"
      },
      {
        "port": {
          "code": "DNL",
          "type": "CruisePort",
          "internalCode": "DNLI"
        },
        "dayOffSet": 2,
        "description": "Denali - Alaska (PRE-CRUISE TOUR)"
      },
      {
        "port": {
          "code": "DNL",
          "type": "CruisePort",
          "internalCode": "DNLI"
        },
        "dayOffSet": 3,
        "description": "Denali - Alaska (PRE-CRUISE TOUR)"
      },
      {
        "port": {
          "code": "TLK",
          "type": "CruisePort",
          "internalCode": "TKA"
        },
        "dayOffSet": 3,
        "description": "Talkeetna - Alaska (PRE-CRUISE TOUR)"
      },
      {
        "port": {
          "code": "TLK",
          "type": "CruisePort",
          "internalCode": "TKA"
        },
        "dayOffSet": 4,
        "description": "Talkeetna - Alaska (PRE-CRUISE TOUR)"
      },
      {
        "port": {
          "code": "ANC",
          "type": "CruisePort",
          "internalCode": "ANC"
        },
        "dayOffSet": 4,
        "description": "Anchorage - Alaska (PRE-CRUISE TOUR)"
      },
      {
        "port": {
          "code": "ANC",
          "type": "CruisePort",
          "internalCode": "ANC"
        },
        "dayOffSet": 5,
        "description": "Anchorage - Alaska (PRE-CRUISE TOUR)"
      },
      {
        "port": {
          "code": "SWD",
          "type": "CruisePort",
          "internalCode": "SWD"
        },
        "dayOffSet": 5,
        "description": "Seward - Alaska (PRE-CRUISE TOUR)"
      },
      {
        "port": {
          "code": "SWD",
          "type": "CruisePort",
          "internalCode": "SWD"
        },
        "dayOffSet": 6,
        "description": "Seward - Alaska (PRE-CRUISE TOUR)"
      },
      {
        "port": {
          "code": "SWD",
          "type": "CruisePort",
          "internalCode": "SWD"
        },
        "departureTime": "19:00:00",
        "dayOffSet": 6,
        "description": "Seward -  Alaska"
      },
      {
        "port": {
          "code": "YAK",
          "type": "CruisePort"
        },
        "departureTime": "18:00:00",
        "arrivalTime": "15:00:00",
        "dayOffSet": 7,
        "description": "Hubbard Glacier (Cruising)"
      },
      {
        "port": {
          "code": "JNU",
          "type": "CruisePort",
          "internalCode": "JNU"
        },
        "departureTime": "21:00:00",
        "arrivalTime": "11:30:00",
        "dayOffSet": 8,
        "description": "Juneau -  Alaska"
      },
      {
        "port": {
          "code": "SGY",
          "type": "CruisePort",
          "internalCode": "SGY"
        },
        "departureTime": "17:00:00",
        "arrivalTime": "07:00:00",
        "dayOffSet": 9,
        "description": "Skagway -  Alaska"
      },
      {
        "port": {
          "code": "HNS",
          "type": "CruisePort",
          "internalCode": "HNS"
        },
        "departureTime": "23:00:00",
        "arrivalTime": "19:00:00",
        "dayOffSet": 9,
        "description": "Haines -  Alaska"
      },
      {
        "port": {
          "code": "PSO",
          "type": "CruisePort",
          "internalCode": "ICYS"
        },
        "departureTime": "15:00:00",
        "arrivalTime": "06:30:00",
        "dayOffSet": 10,
        "description": "Icy Strait Point -  Alaska"
      },
      {
        "port": {
          "code": "KTN",
          "type": "CruisePort",
          "internalCode": "KTN"
        },
        "departureTime": "19:00:00",
        "arrivalTime": "10:00:00",
        "dayOffSet": 11,
        "description": "Ketchikan -  Alaska"
      },
      {
        "port": {
          "code": "ISP",
          "type": "CruisePort"
        },
        "dayOffSet": 12,
        "description": "Inside Passage (Cruising)"
      },
      {
        "port": {
          "code": "YVR",
          "type": "CruisePort",
          "internalCode": "YVR"
        },
        "arrivalTime": "07:00:00",
        "dayOffSet": 13,
        "description": "Vancouver -  British Columbia"
      }
    ],
    "portsOfCalls": "Fairbanks - Alaska (PRE-CRUISE TOUR)|Fairbanks - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Talkeetna - Alaska (PRE-CRUISE TOUR)|Talkeetna - Alaska (PRE-CRUISE TOUR)|Anchorage - Alaska (PRE-CRUISE TOUR)|Anchorage - Alaska (PRE-CRUISE TOUR)|Seward - Alaska (PRE-CRUISE TOUR)|Seward - Alaska (PRE-CRUISE TOUR)|Seward -  Alaska|Juneau -  Alaska|Skagway -  Alaska|Haines -  Alaska|Icy Strait Point -  Alaska|Ketchikan -  Alaska|Vancouver -  British Columbia",
    "normalizedPortsOfCall": "FAI|DNLI|TKA|ANC|SWD|JNU|SGY|HNS|ICYS|KTN|YVR"
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
