# Cruise Search Counters Only

**Path:** Cruise Search Counters only > Cruise Search Counters Only

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/cruise/Facets`

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

### Request Body

```json
// all search filters that work with /v2/Cruise, will work here as well
{
    "filters": [
        {
            "key": "departureDate",
            "ranges": [
                {
                    "from": "23-May-2023",
                    "to": "23-Nov-2023"
                }
            ]
        },
        {
            "key": "duration",
            "ranges": [
                {
                    "from": "",
                    "to": ""
                }
            ]
        },
        {
            "key": "destinationId",
            "values": []
        },
        {
            "key": "destinationType",
            "value": "All"
        },
        {
            "key": "cruiselineId",
            "values": []
        },
        {
            "key": "shipId",
            "values": []
        },
        {
            "key": "departurePortCode",
            "values": []
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Wed, 01 Feb 2023 09:23:43 GMT
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
X-Served-From: 208.64.67.223
X-Powered-By: ASP.NET
X-Server-Ip: 192.168.214.13
Content-Encoding: gzip
```

### Response Body

```json
{
  "isSucceed": true,
  "data": {
    "total": 15697,
    "pageStart": 0,
    "pageSize": 0,
    "list": [],
    "facets": [
      {
        "key": "duration",
        "isRangeFilter": true,
        "values": [
          {
            "count": 484,
            "from": 1,
            "to": 3
          },
          {
            "count": 1892,
            "from": 4,
            "to": 6
          },
          {
            "count": 6522,
            "from": 7,
            "to": 9
          },
          {
            "count": 3965,
            "from": 10,
            "to": 13
          },
          {
            "count": 2834,
            "from": 14
          }
        ]
      },
      {
        "key": "maxOccupancy",
        "isRangeFilter": true,
        "values": [
          {
            "count": 6723,
            "from": 2,
            "to": 2
          },
          {
            "count": 5025,
            "from": 4,
            "to": 4
          },
          {
            "count": 3949,
            "from": 5
          }
        ]
      },
      {
        "key": "packageTour",
        "values": [
          {
            "count": 15697,
            "value": "nonTourPackage"
          }
        ]
      },
      {
        "key": "StnExternalId",
        "values": [
          {
            "count": 9224
          }
        ]
      },
      {
        "key": "hasVrUrl",
        "values": [
          {
            "count": 6203
          }
        ]
      },
      {
        "key": "hasShipVideoUrl",
        "values": [
          {
            "count": 7957
          }
        ]
      },
      {
        "key": "isKidsFriendly",
        "values": [
          {
            "count": 6366
          }
        ]
      },
      {
        "key": "destinationId",
        "values": [
          {
            "count": 3928,
            "value": "15"
          },
          {
            "count": 1803,
            "value": "1"
          },
          {
            "count": 1122,
            "value": "51"
          },
          {
            "count": 827,
            "value": "41"
          },
          {
            "count": 775,
            "value": "9"
          },
          {
            "count": 737,
            "value": "16"
          },
          {
            "count": 685,
            "value": "39"
          },
          {
            "count": 664,
            "value": "19"
          },
          {
            "count": 648,
            "value": "7"
          },
          {
            "count": 599,
            "value": "18"
          },
          {
            "count": 542,
            "value": "2"
          },
          {
            "count": 383,
            "value": "10"
          },
          {
            "count": 261,
            "value": "38"
          },
          {
            "count": 251,
            "value": "57"
          },
          {
            "count": 225,
            "value": "32"
          },
          {
            "count": 200,
            "value": "60"
          },
          {
            "count": 174,
            "value": "29"
          },
          {
            "count": 139,
            "value": "75"
          },
          {
            "count": 138,
            "value": "48"
          },
          {
            "count": 132,
            "value": "14"
          },
          {
            "count": 123,
            "value": "55"
          },
          {
            "count": 118,
            "value": "26"
          },
          {
            "count": 111,
            "value": "8"
          },
          {
            "count": 101,
            "value": "67"
          },
          {
            "count": 99,
            "value": "44"
          },
          {
            "count": 86,
            "value": "65"
          },
          {
            "count": 80,
            "value": "36"
          },
          {
            "count": 78,
            "value": "56"
          },
          {
            "count": 77,
            "value": "104"
          },
          {
            "count": 72,
            "value": "13"
          },
          {
            "count": 69,
            "value": "40"
          },
          {
            "count": 61,
            "value": "73"
          },
          {
            "count": 58,
            "value": "112"
          },
          {
            "count": 53,
            "value": "31"
          },
          {
            "count": 43,
            "value": "49"
          },
          {
            "count": 35,
            "value": "34"
          },
          {
            "count": 31,
            "value": "42"
          },
          {
            "count": 23,
            "value": "74"
          },
          {
            "count": 22,
            "value": "58"
          },
          {
            "count": 20,
            "value": "45"
          },
          {
            "count": 17,
            "value": "68"
          },
          {
            "count": 16,
            "value": "47"
          },
          {
            "count": 16,
            "value": "52"
          },
          {
            "count": 11,
            "value": "121"
          },
          {
            "count": 10,
            "value": "21"
          },
          {
            "count": 10,
            "value": "61"
          },
          {
            "count": 7,
            "value": "24"
          },
          {
            "count": 4,
            "value": "105"
          },
          {
            "count": 4,
            "value": "124"
          },
          {
            "count": 3,
            "value": "63"
          },
          {
            "count": 3,
            "value": "171"
          },
          {
            "count": 1,
            "value": "50"
          },
          {
            "count": 1,
            "value": "53"
          },
          {
            "count": 1,
            "value": "142"
          }
        ]
      },
      {
        "key": "riverId",
        "values": [
          {
            "count": 1019,
            "value": "76"
          },
          {
            "count": 903,
            "value": "77"
          },
          {
            "count": 397,
            "value": "78"
          },
          {
            "count": 245,
            "value": "83"
          },
          {
            "count": 215,
            "value": "86"
          },
          {
            "count": 208,
            "value": "79"
          },
          {
            "count": 136,
            "value": "84"
          },
          {
            "count": 92,
            "value": "81"
          },
          {
            "count": 92,
            "value": "82"
          },
          {
            "count": 60,
            "value": "85"
          },
          {
            "count": 58,
            "value": "112"
          },
          {
            "count": 50,
            "value": "94"
          },
          {
            "count": 42,
            "value": "99"
          },
          {
            "count": 38,
            "value": "88"
          },
          {
            "count": 31,
            "value": "80"
          },
          {
            "count": 25,
            "value": "95"
          },
          {
            "count": 20,
            "value": "93"
          },
          {
            "count": 7,
            "value": "102"
          },
          {
            "count": 1,
            "value": "142"
          }
        ]
      },
      {
        "key": "cruiseType",
        "values": [
          {
            "count": 11604,
            "value": "CruiseOnly"
          },
          {
            "count": 4093,
            "value": "CruiseTour"
          }
        ]
      },
      {
        "key": "cruiselineId",
        "values": [
          {
            "count": 1619,
            "value": "8112"
          },
          {
            "count": 1410,
            "value": "8121"
          },
          {
            "count": 1283,
            "value": "982"
          },
          {
            "count": 1207,
            "value": "1"
          },
          {
            "count": 1198,
            "value": "9155"
          },
          {
            "count": 1165,
            "value": "8138"
          },
          {
            "count": 1069,
            "value": "7"
          },
          {
            "count": 810,
            "value": "5"
          },
          {
            "count": 785,
            "value": "8"
          },
          {
            "count": 737,
            "value": "6"
          },
          {
            "count": 544,
            "value": "2"
          },
          {
            "count": 515,
            "value": "8175"
          },
          {
            "count": 439,
            "value": "8149"
          },
          {
            "count": 365,
            "value": "9191"
          },
          {
            "count": 349,
            "value": "8115"
          },
          {
            "count": 302,
            "value": "11"
          },
          {
            "count": 251,
            "value": "12"
          },
          {
            "count": 249,
            "value": "8224"
          },
          {
            "count": 218,
            "value": "3"
          },
          {
            "count": 209,
            "value": "8146"
          },
          {
            "count": 172,
            "value": "8807"
          },
          {
            "count": 170,
            "value": "8116"
          },
          {
            "count": 153,
            "value": "8156"
          },
          {
            "count": 148,
            "value": "9"
          },
          {
            "count": 110,
            "value": "1043"
          },
          {
            "count": 101,
            "value": "4"
          },
          {
            "count": 61,
            "value": "9204"
          },
          {
            "count": 36,
            "value": "8829"
          },
          {
            "count": 22,
            "value": "8119"
          }
        ]
      },
      {
        "key": "shipId",
        "values": [
          {
            "count": 409,
            "value": "13762"
          },
          {
            "count": 402,
            "value": "62"
          },
          {
            "count": 265,
            "value": "36"
          },
          {
            "count": 265,
            "value": "13250"
          },
          {
            "count": 244,
            "value": "14086"
          },
          {
            "count": 164,
            "value": "14064"
          },
          {
            "count": 162,
            "value": "13708"
          },
          {
            "count": 131,
            "value": "13308"
          },
          {
            "count": 130,
            "value": "14304"
          },
          {
            "count": 128,
            "value": "14998"
          },
          {
            "count": 124,
            "value": "13393"
          },
          {
            "count": 119,
            "value": "13788"
          },
          {
            "count": 111,
            "value": "14964"
          },
          {
            "count": 110,
            "value": "14997"
          },
          {
            "count": 108,
            "value": "1109"
          },
          {
            "count": 108,
            "value": "14538"
          },
          {
            "count": 107,
            "value": "15044"
          },
          {
            "count": 102,
            "value": "13528"
          },
          {
            "count": 98,
            "value": "116"
          },
          {
            "count": 98,
            "value": "118"
          },
          {
            "count": 98,
            "value": "14383"
          },
          {
            "count": 95,
            "value": "13392"
          },
          {
            "count": 95,
            "value": "15045"
          },
          {
            "count": 93,
            "value": "1110"
          },
          {
            "count": 91,
            "value": "1"
          },
          {
            "count": 91,
            "value": "1108"
          },
          {
            "count": 88,
            "value": "14085"
          },
          {
            "count": 86,
            "value": "14060"
          },
          {
            "count": 85,
            "value": "14065"
          },
          {
            "count": 84,
            "value": "13670"
          },
          {
            "count": 84,
            "value": "14088"
          },
          {
            "count": 83,
            "value": "1116"
          },
          {
            "count": 83,
            "value": "13299"
          },
          {
            "count": 82,
            "value": "14090"
          },
          {
            "count": 82,
            "value": "15108"
          },
          {
            "count": 81,
            "value": "13231"
          },
          {
            "count": 80,
            "value": "14014"
          },
          {
            "count": 77,
            "value": "1093"
          },
          {
            "count": 77,
            "value": "13710"
          },
          {
            "count": 77,
            "value": "13786"
          },
          {
            "count": 77,
            "value": "14478"
          },
          {
            "count": 75,
            "value": "13714"
          },
          {
            "count": 75,
            "value": "13824"
          },
          {
            "count": 74,
            "value": "17"
          },
          {
            "count": 74,
            "value": "14047"
          },
          {
            "count": 73,
            "value": "71"
          },
          {
            "count": 73,
            "value": "13233"
          },
          {
            "count": 73,
            "value": "13307"
          },
          {
            "count": 73,
            "value": "13487"
          },
          {
            "count": 73,
            "value": "14270"
          },
          {
            "count": 72,
            "value": "14477"
          },
          {
            "count": 70,
            "value": "13496"
          },
          {
            "count": 70,
            "value": "13825"
          },
          {
            "count": 69,
            "value": "13309"
          },
          {
            "count": 68,
            "value": "13509"
          },
          {
            "count": 68,
            "value": "13867"
          },
          {
            "count": 68,
            "value": "14084"
          },
          {
            "count": 67,
            "value": "13237"
          },
          {
            "count": 67,
            "value": "13239"
          },
          {
            "count": 67,
            "value": "13306"
          },
          {
            "count": 66,
            "value": "1112"
          },
          {
            "count": 66,
            "value": "13649"
          },
          {
            "count": 66,
            "value": "13653"
          },
          {
            "count": 66,
            "value": "14535"
          },
          {
            "count": 65,
            "value": "13507"
          },
          {
            "count": 64,
            "value": "13669"
          },
          {
            "count": 63,
            "value": "135"
          },
          {
            "count": 63,
            "value": "1096"
          },
          {
            "count": 63,
            "value": "13696"
          },
          {
            "count": 63,
            "value": "13757"
          },
          {
            "count": 62,
            "value": "13627"
          },
          {
            "count": 61,
            "value": "15110"
          },
          {
            "count": 60,
            "value": "1181"
          },
          {
            "count": 60,
            "value": "14045"
          },
          {
            "count": 59,
            "value": "13490"
          },
          {
            "count": 58,
            "value": "13772"
          },
          {
            "count": 58,
            "value": "14533"
          },
          {
            "count": 58,
            "value": "14835"
          },
          {
            "count": 57,
            "value": "1163"
          },
          {
            "count": 56,
            "value": "13734"
          },
          {
            "count": 56,
            "value": "14006"
          },
          {
            "count": 56,
            "value": "15058"
          },
          {
            "count": 55,
            "value": "14512"
          },
          {
            "count": 54,
            "value": "13695"
          },
          {
            "count": 54,
            "value": "14740"
          },
          {
            "count": 54,
            "value": "15159"
          },
          {
            "count": 53,
            "value": "13500"
          },
          {
            "count": 53,
            "value": "13785"
          },
          {
            "count": 52,
            "value": "13697"
          },
          {
            "count": 52,
            "value": "14155"
          },
          {
            "count": 52,
            "value": "15087"
          },
          {
            "count": 51,
            "value": "5"
          },
          {
            "count": 51,
            "value": "1100"
          },
          {
            "count": 51,
            "value": "13256"
          },
          {
            "count": 50,
            "value": "14089"
          },
          {
            "count": 49,
            "value": "1191"
          },
          {
            "count": 49,
            "value": "13380"
          },
          {
            "count": 49,
            "value": "13522"
          },
          {
            "count": 49,
            "value": "13523"
          },
          {
            "count": 49,
            "value": "13712"
          },
          {
            "count": 49,
            "value": "13716"
          },
          {
            "count": 49,
            "value": "13797"
          },
          {
            "count": 49,
            "value": "14073"
          },
          {
            "count": 49,
            "value": "14471"
          },
          {
            "count": 49,
            "value": "14532"
          },
          {
            "count": 49,
            "value": "14965"
          },
          {
            "count": 48,
            "value": "3"
          },
          {
            "count": 48,
            "value": "13385"
          },
          {
            "count": 48,
            "value": "14046"
          },
          {
            "count": 48,
            "value": "14475"
          },
          {
            "count": 48,
            "value": "14719"
          },
          {
            "count": 47,
            "value": "1105"
          },
          {
            "count": 47,
            "value": "1182"
          },
          {
            "count": 47,
            "value": "14472"
          },
          {
            "count": 46,
            "value": "1104"
          },
          {
            "count": 46,
            "value": "13240"
          },
          {
            "count": 46,
            "value": "13731"
          },
          {
            "count": 46,
            "value": "14713"
          },
          {
            "count": 46,
            "value": "14714"
          },
          {
            "count": 46,
            "value": "14803"
          },
          {
            "count": 45,
            "value": "1097"
          },
          {
            "count": 45,
            "value": "13387"
          },
          {
            "count": 45,
            "value": "13608"
          },
          {
            "count": 44,
            "value": "4"
          },
          {
            "count": 44,
            "value": "6"
          },
          {
            "count": 44,
            "value": "13510"
          },
          {
            "count": 44,
            "value": "13711"
          },
          {
            "count": 44,
            "value": "15174"
          },
          {
            "count": 43,
            "value": "13236"
          },
          {
            "count": 43,
            "value": "13281"
          },
          {
            "count": 43,
            "value": "13645"
          },
          {
            "count": 43,
            "value": "13650"
          },
          {
            "count": 43,
            "value": "14087"
          },
          {
            "count": 43,
            "value": "14504"
          },
          {
            "count": 43,
            "value": "14698"
          },
          {
            "count": 43,
            "value": "15031"
          },
          {
            "count": 43,
            "value": "15127"
          },
          {
            "count": 43,
            "value": "15130"
          },
          {
            "count": 42,
            "value": "1179"
          },
          {
            "count": 42,
            "value": "13288"
          },
          {
            "count": 42,
            "value": "13386"
          },
          {
            "count": 42,
            "value": "13486"
          },
          {
            "count": 42,
            "value": "13773"
          },
          {
            "count": 42,
            "value": "14110"
          },
          {
            "count": 42,
            "value": "15014"
          },
          {
            "count": 42,
            "value": "15089"
          },
          {
            "count": 41,
            "value": "37"
          },
          {
            "count": 41,
            "value": "14109"
          },
          {
            "count": 41,
            "value": "14712"
          },
          {
            "count": 40,
            "value": "13717"
          },
          {
            "count": 40,
            "value": "13796"
          },
          {
            "count": 40,
            "value": "15020"
          },
          {
            "count": 39,
            "value": "13646"
          },
          {
            "count": 39,
            "value": "13761"
          },
          {
            "count": 39,
            "value": "14534"
          },
          {
            "count": 38,
            "value": "13232"
          },
          {
            "count": 38,
            "value": "13383"
          },
          {
            "count": 38,
            "value": "13658"
          },
          {
            "count": 38,
            "value": "13713"
          },
          {
            "count": 38,
            "value": "14106"
          },
          {
            "count": 38,
            "value": "14393"
          },
          {
            "count": 38,
            "value": "14476"
          },
          {
            "count": 38,
            "value": "15021"
          },
          {
            "count": 37,
            "value": "18"
          },
          {
            "count": 37,
            "value": "1159"
          },
          {
            "count": 37,
            "value": "14328"
          },
          {
            "count": 37,
            "value": "14717"
          },
          {
            "count": 37,
            "value": "15022"
          },
          {
            "count": 36,
            "value": "58"
          },
          {
            "count": 36,
            "value": "1176"
          },
          {
            "count": 36,
            "value": "13732"
          },
          {
            "count": 36,
            "value": "14492"
          },
          {
            "count": 36,
            "value": "15035"
          },
          {
            "count": 36,
            "value": "15065"
          },
          {
            "count": 36,
            "value": "15090"
          },
          {
            "count": 35,
            "value": "1117"
          },
          {
            "count": 35,
            "value": "13858"
          },
          {
            "count": 34,
            "value": "24"
          },
          {
            "count": 34,
            "value": "13289"
          },
          {
            "count": 34,
            "value": "13471"
          },
          {
            "count": 34,
            "value": "15026"
          },
          {
            "count": 33,
            "value": "21"
          },
          {
            "count": 33,
            "value": "1190"
          },
          {
            "count": 32,
            "value": "31"
          },
          {
            "count": 32,
            "value": "13472"
          },
          {
            "count": 32,
            "value": "13768"
          },
          {
            "count": 32,
            "value": "14948"
          },
          {
            "count": 32,
            "value": "15071"
          },
          {
            "count": 31,
            "value": "13437"
          },
          {
            "count": 31,
            "value": "13439"
          },
          {
            "count": 31,
            "value": "13440"
          },
          {
            "count": 31,
            "value": "13441"
          },
          {
            "count": 31,
            "value": "13633"
          },
          {
            "count": 31,
            "value": "13760"
          },
          {
            "count": 31,
            "value": "13766"
          },
          {
            "count": 31,
            "value": "14508"
          },
          {
            "count": 31,
            "value": "15041"
          },
          {
            "count": 31,
            "value": "15112"
          },
          {
            "count": 30,
            "value": "13449"
          },
          {
            "count": 30,
            "value": "13537"
          },
          {
            "count": 30,
            "value": "13539"
          },
          {
            "count": 30,
            "value": "13614"
          },
          {
            "count": 30,
            "value": "13660"
          },
          {
            "count": 30,
            "value": "13661"
          },
          {
            "count": 30,
            "value": "13672"
          },
          {
            "count": 30,
            "value": "13673"
          },
          {
            "count": 30,
            "value": "13719"
          },
          {
            "count": 30,
            "value": "13722"
          },
          {
            "count": 30,
            "value": "13765"
          },
          {
            "count": 30,
            "value": "14056"
          },
          {
            "count": 30,
            "value": "14058"
          },
          {
            "count": 30,
            "value": "15011"
          },
          {
            "count": 29,
            "value": "32"
          },
          {
            "count": 29,
            "value": "13442"
          },
          {
            "count": 29,
            "value": "13630"
          },
          {
            "count": 29,
            "value": "13682"
          },
          {
            "count": 29,
            "value": "13767"
          },
          {
            "count": 29,
            "value": "13993"
          },
          {
            "count": 29,
            "value": "14511"
          },
          {
            "count": 29,
            "value": "14723"
          },
          {
            "count": 28,
            "value": "13255"
          },
          {
            "count": 28,
            "value": "13444"
          },
          {
            "count": 28,
            "value": "13465"
          },
          {
            "count": 28,
            "value": "13616"
          },
          {
            "count": 28,
            "value": "13681"
          },
          {
            "count": 28,
            "value": "15008"
          },
          {
            "count": 28,
            "value": "15015"
          },
          {
            "count": 27,
            "value": "13443"
          },
          {
            "count": 27,
            "value": "14038"
          },
          {
            "count": 26,
            "value": "1098"
          },
          {
            "count": 26,
            "value": "1187"
          },
          {
            "count": 26,
            "value": "13295"
          },
          {
            "count": 26,
            "value": "13448"
          },
          {
            "count": 26,
            "value": "13615"
          },
          {
            "count": 26,
            "value": "13725"
          },
          {
            "count": 26,
            "value": "13758"
          },
          {
            "count": 26,
            "value": "13769"
          },
          {
            "count": 26,
            "value": "14072"
          },
          {
            "count": 26,
            "value": "15004"
          },
          {
            "count": 25,
            "value": "1188"
          },
          {
            "count": 25,
            "value": "13296"
          },
          {
            "count": 25,
            "value": "13538"
          },
          {
            "count": 25,
            "value": "13613"
          },
          {
            "count": 25,
            "value": "13622"
          },
          {
            "count": 25,
            "value": "13623"
          },
          {
            "count": 25,
            "value": "13624"
          },
          {
            "count": 25,
            "value": "13723"
          },
          {
            "count": 25,
            "value": "13736"
          },
          {
            "count": 25,
            "value": "13775"
          },
          {
            "count": 25,
            "value": "14059"
          },
          {
            "count": 25,
            "value": "15012"
          },
          {
            "count": 24,
            "value": "13286"
          },
          {
            "count": 24,
            "value": "13542"
          },
          {
            "count": 24,
            "value": "13543"
          },
          {
            "count": 24,
            "value": "13618"
          },
          {
            "count": 24,
            "value": "13621"
          },
          {
            "count": 24,
            "value": "13774"
          },
          {
            "count": 24,
            "value": "14055"
          },
          {
            "count": 24,
            "value": "14509"
          },
          {
            "count": 24,
            "value": "14510"
          },
          {
            "count": 24,
            "value": "15040"
          },
          {
            "count": 23,
            "value": "13287"
          },
          {
            "count": 23,
            "value": "13294"
          },
          {
            "count": 23,
            "value": "14516"
          },
          {
            "count": 23,
            "value": "14517"
          },
          {
            "count": 23,
            "value": "15029"
          },
          {
            "count": 23,
            "value": "15037"
          },
          {
            "count": 22,
            "value": "30"
          },
          {
            "count": 22,
            "value": "13297"
          },
          {
            "count": 22,
            "value": "13674"
          },
          {
            "count": 22,
            "value": "13721"
          },
          {
            "count": 22,
            "value": "13793"
          },
          {
            "count": 22,
            "value": "14949"
          },
          {
            "count": 22,
            "value": "15019"
          },
          {
            "count": 22,
            "value": "15024"
          },
          {
            "count": 21,
            "value": "13675"
          },
          {
            "count": 21,
            "value": "15141"
          },
          {
            "count": 20,
            "value": "15109"
          },
          {
            "count": 19,
            "value": "1161"
          },
          {
            "count": 19,
            "value": "13372"
          },
          {
            "count": 19,
            "value": "13469"
          },
          {
            "count": 19,
            "value": "13576"
          },
          {
            "count": 19,
            "value": "14053"
          },
          {
            "count": 19,
            "value": "14295"
          },
          {
            "count": 19,
            "value": "15043"
          },
          {
            "count": 18,
            "value": "13470"
          },
          {
            "count": 18,
            "value": "13617"
          },
          {
            "count": 18,
            "value": "14718"
          },
          {
            "count": 18,
            "value": "14829"
          },
          {
            "count": 18,
            "value": "15182"
          },
          {
            "count": 17,
            "value": "114"
          },
          {
            "count": 17,
            "value": "13577"
          },
          {
            "count": 17,
            "value": "15023"
          },
          {
            "count": 16,
            "value": "14091"
          },
          {
            "count": 16,
            "value": "14302"
          },
          {
            "count": 16,
            "value": "14514"
          },
          {
            "count": 16,
            "value": "15010"
          },
          {
            "count": 16,
            "value": "15027"
          },
          {
            "count": 15,
            "value": "33"
          },
          {
            "count": 15,
            "value": "52"
          },
          {
            "count": 15,
            "value": "1183"
          },
          {
            "count": 15,
            "value": "13536"
          },
          {
            "count": 15,
            "value": "14528"
          },
          {
            "count": 15,
            "value": "15002"
          },
          {
            "count": 14,
            "value": "13541"
          },
          {
            "count": 14,
            "value": "13575"
          },
          {
            "count": 14,
            "value": "14054"
          },
          {
            "count": 14,
            "value": "14057"
          },
          {
            "count": 14,
            "value": "15016"
          },
          {
            "count": 13,
            "value": "13290"
          },
          {
            "count": 13,
            "value": "13477"
          },
          {
            "count": 13,
            "value": "13540"
          },
          {
            "count": 13,
            "value": "13612"
          },
          {
            "count": 13,
            "value": "13619"
          },
          {
            "count": 13,
            "value": "13678"
          },
          {
            "count": 13,
            "value": "13679"
          },
          {
            "count": 13,
            "value": "13680"
          },
          {
            "count": 13,
            "value": "14435"
          },
          {
            "count": 13,
            "value": "15005"
          },
          {
            "count": 13,
            "value": "15030"
          },
          {
            "count": 13,
            "value": "15042"
          },
          {
            "count": 12,
            "value": "1162"
          },
          {
            "count": 12,
            "value": "13676"
          },
          {
            "count": 12,
            "value": "13720"
          },
          {
            "count": 12,
            "value": "14040"
          },
          {
            "count": 12,
            "value": "14043"
          },
          {
            "count": 12,
            "value": "14473"
          },
          {
            "count": 12,
            "value": "15017"
          },
          {
            "count": 11,
            "value": "13677"
          },
          {
            "count": 11,
            "value": "13685"
          },
          {
            "count": 10,
            "value": "13735"
          },
          {
            "count": 10,
            "value": "13822"
          },
          {
            "count": 10,
            "value": "13823"
          },
          {
            "count": 10,
            "value": "14479"
          },
          {
            "count": 10,
            "value": "15003"
          },
          {
            "count": 9,
            "value": "14275"
          },
          {
            "count": 9,
            "value": "15036"
          },
          {
            "count": 9,
            "value": "15168"
          },
          {
            "count": 8,
            "value": "15018"
          },
          {
            "count": 8,
            "value": "15032"
          },
          {
            "count": 8,
            "value": "15063"
          },
          {
            "count": 8,
            "value": "15126"
          },
          {
            "count": 7,
            "value": "14994"
          },
          {
            "count": 5,
            "value": "14759"
          },
          {
            "count": 3,
            "value": "15034"
          },
          {
            "count": 2,
            "value": "13259"
          },
          {
            "count": 2,
            "value": "15025"
          },
          {
            "count": 1,
            "value": "13447"
          },
          {
            "count": 1,
            "value": "15013"
          },
          {
            "count": 1,
            "value": "15038"
          },
          {
            "count": 1,
            "value": "15039"
          }
        ]
      },
      {
        "key": "departurePortCode",
        "values": [
          {
            "count": 842,
            "value": "MIA"
          },
          {
            "count": 788,
            "value": "AMS"
          },
          {
            "count": 786,
            "value": "YVR"
          },
          {
            "count": 595,
            "value": "BUD"
          },
          {
            "count": 436,
            "value": "PAR"
          },
          {
            "count": 430,
            "value": "XPC"
          },
          {
            "count": 394,
            "value": "BCN"
          },
          {
            "count": 379,
            "value": "SEA"
          },
          {
            "count": 376,
            "value": "BSL"
          },
          {
            "count": 353,
            "value": "FAI"
          },
          {
            "count": 329,
            "value": "CIV"
          },
          {
            "count": 324,
            "value": "GLS"
          },
          {
            "count": 304,
            "value": "ATH"
          },
          {
            "count": 296,
            "value": "CAI"
          },
          {
            "count": 295,
            "value": "FLL"
          },
          {
            "count": 275,
            "value": "VCE"
          },
          {
            "count": 260,
            "value": "BGO"
          },
          {
            "count": 248,
            "value": "ANC"
          },
          {
            "count": 248,
            "value": "PRG"
          },
          {
            "count": 239,
            "value": "LAX"
          },
          {
            "count": 224,
            "value": "SXB"
          },
          {
            "count": 210,
            "value": "SOU"
          },
          {
            "count": 207,
            "value": "LIS"
          },
          {
            "count": 197,
            "value": "REP"
          },
          {
            "count": 197,
            "value": "SYD"
          },
          {
            "count": 190,
            "value": "NYC"
          },
          {
            "count": 157,
            "value": "BA1"
          },
          {
            "count": 155,
            "value": "VIE"
          },
          {
            "count": 144,
            "value": "KUSA"
          },
          {
            "count": 141,
            "value": "SGN"
          },
          {
            "count": 139,
            "value": "CPT"
          },
          {
            "count": 138,
            "value": "BUH"
          },
          {
            "count": 136,
            "value": "OPO"
          },
          {
            "count": 130,
            "value": "GOA"
          },
          {
            "count": 129,
            "value": "HAN"
          },
          {
            "count": 125,
            "value": "BOD"
          },
          {
            "count": 125,
            "value": "TPA"
          },
          {
            "count": 122,
            "value": "REK"
          },
          {
            "count": 120,
            "value": "JNB"
          },
          {
            "count": 117,
            "value": "CPH"
          },
          {
            "count": 116,
            "value": "UIO"
          },
          {
            "count": 106,
            "value": "IST"
          },
          {
            "count": 100,
            "value": "LIM"
          },
          {
            "count": 99,
            "value": "HAM"
          },
          {
            "count": 93,
            "value": "MRS"
          },
          {
            "count": 91,
            "value": "MSY"
          },
          {
            "count": 89,
            "value": "PIRA"
          },
          {
            "count": 85,
            "value": "ZPM"
          },
          {
            "count": 79,
            "value": "AVN"
          },
          {
            "count": 76,
            "value": "VILS"
          },
          {
            "count": 74,
            "value": "NCE"
          },
          {
            "count": 72,
            "value": "EWR"
          },
          {
            "count": 69,
            "value": "BRI"
          },
          {
            "count": 68,
            "value": "CHS"
          },
          {
            "count": 68,
            "value": "ZRH"
          },
          {
            "count": 64,
            "value": "LYS"
          },
          {
            "count": 64,
            "value": "ZPF"
          },
          {
            "count": 62,
            "value": "NUE"
          },
          {
            "count": 60,
            "value": "LAVR"
          },
          {
            "count": 58,
            "value": "BGI"
          },
          {
            "count": 57,
            "value": "STO"
          },
          {
            "count": 56,
            "value": "BER"
          },
          {
            "count": 56,
            "value": "BUE"
          },
          {
            "count": 56,
            "value": "LYR"
          },
          {
            "count": 55,
            "value": "QQD"
          },
          {
            "count": 53,
            "value": "SJU"
          },
          {
            "count": 52,
            "value": "DEG"
          },
          {
            "count": 50,
            "value": "PSLR"
          },
          {
            "count": 49,
            "value": "MUC"
          },
          {
            "count": 47,
            "value": "BOS"
          },
          {
            "count": 47,
            "value": "BWI"
          },
          {
            "count": 47,
            "value": "PPT"
          },
          {
            "count": 45,
            "value": "AKL"
          },
          {
            "count": 45,
            "value": "SWD"
          },
          {
            "count": 43,
            "value": "PMO"
          },
          {
            "count": 43,
            "value": "SC1"
          },
          {
            "count": 42,
            "value": "NAP"
          },
          {
            "count": 41,
            "value": "MEL"
          },
          {
            "count": 40,
            "value": "BNE"
          },
          {
            "count": 40,
            "value": "HFA"
          },
          {
            "count": 38,
            "value": "BKK"
          },
          {
            "count": 38,
            "value": "TRS"
          },
          {
            "count": 37,
            "value": "FRA"
          },
          {
            "count": 37,
            "value": "SIN"
          },
          {
            "count": 35,
            "value": "KEL"
          },
          {
            "count": 35,
            "value": "MAD"
          },
          {
            "count": 35,
            "value": "SFO"
          },
          {
            "count": 34,
            "value": "WH1"
          },
          {
            "count": 33,
            "value": "QCM"
          },
          {
            "count": 33,
            "value": "TYO"
          },
          {
            "count": 31,
            "value": "HKG"
          },
          {
            "count": 31,
            "value": "LMAS"
          },
          {
            "count": 30,
            "value": "DEL"
          },
          {
            "count": 29,
            "value": "GIUR"
          },
          {
            "count": 29,
            "value": "USH"
          },
          {
            "count": 28,
            "value": "YQB"
          },
          {
            "count": 26,
            "value": "MOB"
          },
          {
            "count": 25,
            "value": "PMI"
          },
          {
            "count": 24,
            "value": "BIO"
          },
          {
            "count": 24,
            "value": "GNW"
          },
          {
            "count": 24,
            "value": "REM"
          },
          {
            "count": 23,
            "value": "LON"
          },
          {
            "count": 23,
            "value": "QME"
          },
          {
            "count": 23,
            "value": "SKG"
          },
          {
            "count": 22,
            "value": "AOI"
          },
          {
            "count": 22,
            "value": "DKR"
          },
          {
            "count": 22,
            "value": "NTS"
          },
          {
            "count": 22,
            "value": "SVQ"
          },
          {
            "count": 22,
            "value": "VLC"
          },
          {
            "count": 21,
            "value": "CEQ"
          },
          {
            "count": 21,
            "value": "SJDL"
          },
          {
            "count": 21,
            "value": "TAR"
          },
          {
            "count": 20,
            "value": "COK"
          },
          {
            "count": 20,
            "value": "DRW"
          },
          {
            "count": 20,
            "value": "MIL"
          },
          {
            "count": 20,
            "value": "PNH"
          },
          {
            "count": 19,
            "value": "AGP"
          },
          {
            "count": 19,
            "value": "SXM"
          },
          {
            "count": 18,
            "value": "BDS"
          },
          {
            "count": 18,
            "value": "LXR"
          },
          {
            "count": 17,
            "value": "LRM"
          },
          {
            "count": 17,
            "value": "RAN"
          },
          {
            "count": 17,
            "value": "YOK"
          },
          {
            "count": 17,
            "value": "ZAF"
          },
          {
            "count": 16,
            "value": "DXB"
          },
          {
            "count": 16,
            "value": "MEM"
          },
          {
            "count": 16,
            "value": "SYR1"
          },
          {
            "count": 16,
            "value": "WPU"
          },
          {
            "count": 16,
            "value": "YYC"
          },
          {
            "count": 15,
            "value": "DBV"
          },
          {
            "count": 15,
            "value": "ZWD"
          },
          {
            "count": 14,
            "value": "ALC"
          },
          {
            "count": 14,
            "value": "LEH"
          },
          {
            "count": 14,
            "value": "OLB"
          },
          {
            "count": 14,
            "value": "YMQ"
          },
          {
            "count": 13,
            "value": "LMK"
          },
          {
            "count": 13,
            "value": "LPA"
          },
          {
            "count": 12,
            "value": "BME"
          },
          {
            "count": 12,
            "value": "CHSS"
          },
          {
            "count": 11,
            "value": "DOJ"
          },
          {
            "count": 11,
            "value": "GVA"
          },
          {
            "count": 11,
            "value": "JFM"
          },
          {
            "count": 11,
            "value": "MYTH"
          },
          {
            "count": 11,
            "value": "SCL"
          },
          {
            "count": 11,
            "value": "VAP"
          },
          {
            "count": 11,
            "value": "ZQF"
          },
          {
            "count": 10,
            "value": "CCU"
          },
          {
            "count": 10,
            "value": "DPS"
          },
          {
            "count": 10,
            "value": "KZCH"
          },
          {
            "count": 10,
            "value": "LNZ"
          },
          {
            "count": 10,
            "value": "LUX"
          },
          {
            "count": 10,
            "value": "MSP"
          },
          {
            "count": 10,
            "value": "OLT"
          },
          {
            "count": 10,
            "value": "SFJ"
          },
          {
            "count": 10,
            "value": "VDT"
          },
          {
            "count": 9,
            "value": "ANR"
          },
          {
            "count": 9,
            "value": "DUB"
          },
          {
            "count": 9,
            "value": "MANT"
          },
          {
            "count": 9,
            "value": "ORF"
          },
          {
            "count": 9,
            "value": "OSL"
          },
          {
            "count": 9,
            "value": "TOS"
          },
          {
            "count": 8,
            "value": "AUA"
          },
          {
            "count": 8,
            "value": "BLB"
          },
          {
            "count": 8,
            "value": "RTM"
          },
          {
            "count": 7,
            "value": "CHC"
          },
          {
            "count": 7,
            "value": "JNU"
          },
          {
            "count": 7,
            "value": "KKN"
          },
          {
            "count": 7,
            "value": "MCM"
          },
          {
            "count": 7,
            "value": "MDL"
          },
          {
            "count": 7,
            "value": "SAN"
          },
          {
            "count": 7,
            "value": "TILB"
          },
          {
            "count": 7,
            "value": "YHZ"
          },
          {
            "count": 6,
            "value": "ADL"
          },
          {
            "count": 6,
            "value": "ASHD"
          },
          {
            "count": 6,
            "value": "BCON"
          },
          {
            "count": 6,
            "value": "BOM"
          },
          {
            "count": 6,
            "value": "KRK"
          },
          {
            "count": 6,
            "value": "STL"
          },
          {
            "count": 6,
            "value": "VLT"
          },
          {
            "count": 6,
            "value": "ZAG"
          },
          {
            "count": 6,
            "value": "ZCC"
          },
          {
            "count": 5,
            "value": "CNS"
          },
          {
            "count": 5,
            "value": "DUD"
          },
          {
            "count": 5,
            "value": "HNL"
          },
          {
            "count": 5,
            "value": "PTY"
          },
          {
            "count": 5,
            "value": "RAV"
          },
          {
            "count": 5,
            "value": "RIO"
          },
          {
            "count": 5,
            "value": "SIG"
          },
          {
            "count": 5,
            "value": "YBZ"
          },
          {
            "count": 4,
            "value": "CALL"
          },
          {
            "count": 4,
            "value": "EDI"
          },
          {
            "count": 4,
            "value": "FNC"
          },
          {
            "count": 4,
            "value": "KEEL"
          },
          {
            "count": 4,
            "value": "LACH"
          },
          {
            "count": 4,
            "value": "ONX"
          },
          {
            "count": 4,
            "value": "OSA"
          },
          {
            "count": 4,
            "value": "SAAN"
          },
          {
            "count": 4,
            "value": "SPND"
          },
          {
            "count": 4,
            "value": "TRI"
          },
          {
            "count": 3,
            "value": "AQJ"
          },
          {
            "count": 3,
            "value": "KGIA"
          },
          {
            "count": 3,
            "value": "MAO"
          },
          {
            "count": 3,
            "value": "MKE"
          },
          {
            "count": 3,
            "value": "OME"
          },
          {
            "count": 3,
            "value": "SZG"
          },
          {
            "count": 3,
            "value": "ZBR1"
          },
          {
            "count": 2,
            "value": "AMM"
          },
          {
            "count": 2,
            "value": "CGN"
          },
          {
            "count": 2,
            "value": "GLA"
          },
          {
            "count": 2,
            "value": "HEL"
          },
          {
            "count": 2,
            "value": "ORAN"
          },
          {
            "count": 2,
            "value": "PAS"
          },
          {
            "count": 2,
            "value": "RAI"
          },
          {
            "count": 2,
            "value": "SEZ"
          },
          {
            "count": 2,
            "value": "SHA"
          },
          {
            "count": 2,
            "value": "TCI"
          },
          {
            "count": 2,
            "value": "YUL"
          },
          {
            "count": 1,
            "value": "AMAD"
          },
          {
            "count": 1,
            "value": "AUH"
          },
          {
            "count": 1,
            "value": "AYT"
          },
          {
            "count": 1,
            "value": "CTG"
          },
          {
            "count": 1,
            "value": "DRS"
          },
          {
            "count": 1,
            "value": "DYR"
          },
          {
            "count": 1,
            "value": "ETHA"
          },
          {
            "count": 1,
            "value": "GREE"
          },
          {
            "count": 1,
            "value": "HAB"
          },
          {
            "count": 1,
            "value": "HBA"
          },
          {
            "count": 1,
            "value": "HOFL"
          },
          {
            "count": 1,
            "value": "JAP"
          },
          {
            "count": 1,
            "value": "MART"
          },
          {
            "count": 1,
            "value": "MMK"
          },
          {
            "count": 1,
            "value": "MVD"
          },
          {
            "count": 1,
            "value": "NAN"
          },
          {
            "count": 1,
            "value": "PME"
          },
          {
            "count": 1,
            "value": "PUQ"
          },
          {
            "count": 1,
            "value": "ROSY"
          },
          {
            "count": 1,
            "value": "SGT"
          },
          {
            "count": 1,
            "value": "SINA"
          },
          {
            "count": 1,
            "value": "SSZ"
          },
          {
            "count": 1,
            "value": "TOKY"
          },
          {
            "count": 1,
            "value": "UAK"
          },
          {
            "count": 1,
            "value": "UKB"
          },
          {
            "count": 1,
            "value": "URO"
          }
        ]
      },
      {
        "key": "arrivalPortCode",
        "values": [
          {
            "count": 935,
            "value": "YVR"
          },
          {
            "count": 846,
            "value": "MIA"
          },
          {
            "count": 676,
            "value": "AMS"
          },
          {
            "count": 632,
            "value": "BUD"
          },
          {
            "count": 447,
            "value": "PAR"
          },
          {
            "count": 433,
            "value": "BSL"
          },
          {
            "count": 430,
            "value": "XPC"
          },
          {
            "count": 397,
            "value": "BCN"
          },
          {
            "count": 347,
            "value": "CIV"
          },
          {
            "count": 325,
            "value": "GLS"
          },
          {
            "count": 314,
            "value": "FLL"
          },
          {
            "count": 310,
            "value": "SEA"
          },
          {
            "count": 309,
            "value": "ATH"
          },
          {
            "count": 280,
            "value": "FAI"
          },
          {
            "count": 269,
            "value": "CAI"
          },
          {
            "count": 265,
            "value": "VCE"
          },
          {
            "count": 260,
            "value": "PRG"
          },
          {
            "count": 256,
            "value": "BGO"
          },
          {
            "count": 241,
            "value": "OPO"
          },
          {
            "count": 238,
            "value": "VFA"
          },
          {
            "count": 233,
            "value": "ANC"
          },
          {
            "count": 233,
            "value": "LAX"
          },
          {
            "count": 217,
            "value": "SOU"
          },
          {
            "count": 214,
            "value": "SXB"
          },
          {
            "count": 199,
            "value": "SYD"
          },
          {
            "count": 191,
            "value": "NYC"
          },
          {
            "count": 171,
            "value": "SGN"
          },
          {
            "count": 157,
            "value": "BA1"
          },
          {
            "count": 154,
            "value": "VIE"
          },
          {
            "count": 141,
            "value": "GOA"
          },
          {
            "count": 128,
            "value": "REP"
          },
          {
            "count": 127,
            "value": "TPA"
          },
          {
            "count": 117,
            "value": "CPH"
          },
          {
            "count": 115,
            "value": "REK"
          },
          {
            "count": 110,
            "value": "LIS"
          },
          {
            "count": 107,
            "value": "IST"
          },
          {
            "count": 107,
            "value": "LAVR"
          },
          {
            "count": 105,
            "value": "BUH"
          },
          {
            "count": 101,
            "value": "BOD"
          },
          {
            "count": 98,
            "value": "HAN"
          },
          {
            "count": 97,
            "value": "KUSA"
          },
          {
            "count": 93,
            "value": "MSY"
          },
          {
            "count": 92,
            "value": "MRS"
          },
          {
            "count": 91,
            "value": "HAM"
          },
          {
            "count": 87,
            "value": "PIRA"
          },
          {
            "count": 86,
            "value": "ZRH"
          },
          {
            "count": 85,
            "value": "UIO"
          },
          {
            "count": 85,
            "value": "ZPM"
          },
          {
            "count": 82,
            "value": "GYE"
          },
          {
            "count": 81,
            "value": "AVN"
          },
          {
            "count": 77,
            "value": "VILS"
          },
          {
            "count": 76,
            "value": "NCE"
          },
          {
            "count": 73,
            "value": "BKK"
          },
          {
            "count": 73,
            "value": "EWR"
          },
          {
            "count": 71,
            "value": "LYS"
          },
          {
            "count": 68,
            "value": "BRI"
          },
          {
            "count": 68,
            "value": "CHS"
          },
          {
            "count": 67,
            "value": "NUE"
          },
          {
            "count": 63,
            "value": "BER"
          },
          {
            "count": 63,
            "value": "ZPF"
          },
          {
            "count": 62,
            "value": "HALO"
          },
          {
            "count": 61,
            "value": "BGI"
          },
          {
            "count": 59,
            "value": "BUE"
          },
          {
            "count": 59,
            "value": "QCM"
          },
          {
            "count": 57,
            "value": "QQD"
          },
          {
            "count": 56,
            "value": "LYR"
          },
          {
            "count": 53,
            "value": "DEG"
          },
          {
            "count": 52,
            "value": "STO"
          },
          {
            "count": 51,
            "value": "BOS"
          },
          {
            "count": 51,
            "value": "SJU"
          },
          {
            "count": 49,
            "value": "LIM"
          },
          {
            "count": 49,
            "value": "PSLR"
          },
          {
            "count": 48,
            "value": "WH1"
          },
          {
            "count": 47,
            "value": "BWI"
          },
          {
            "count": 45,
            "value": "MEL"
          },
          {
            "count": 44,
            "value": "LON"
          },
          {
            "count": 43,
            "value": "PMO"
          },
          {
            "count": 43,
            "value": "SC1"
          },
          {
            "count": 42,
            "value": "AKL"
          },
          {
            "count": 42,
            "value": "PPT"
          },
          {
            "count": 42,
            "value": "SWD"
          },
          {
            "count": 41,
            "value": "NAP"
          },
          {
            "count": 40,
            "value": "BNE"
          },
          {
            "count": 40,
            "value": "CCU"
          },
          {
            "count": 40,
            "value": "SIN"
          },
          {
            "count": 39,
            "value": "TRS"
          },
          {
            "count": 37,
            "value": "HFA"
          },
          {
            "count": 37,
            "value": "TYO"
          },
          {
            "count": 35,
            "value": "SFO"
          },
          {
            "count": 32,
            "value": "HKG"
          },
          {
            "count": 31,
            "value": "FRA"
          },
          {
            "count": 31,
            "value": "KEL"
          },
          {
            "count": 30,
            "value": "LMAS"
          },
          {
            "count": 29,
            "value": "USH"
          },
          {
            "count": 29,
            "value": "YQB"
          },
          {
            "count": 28,
            "value": "AMM"
          },
          {
            "count": 28,
            "value": "REM"
          },
          {
            "count": 26,
            "value": "BBU"
          },
          {
            "count": 26,
            "value": "GNW"
          },
          {
            "count": 26,
            "value": "MOB"
          },
          {
            "count": 25,
            "value": "PMI"
          },
          {
            "count": 24,
            "value": "GIUR"
          },
          {
            "count": 23,
            "value": "SKG"
          },
          {
            "count": 22,
            "value": "CPT"
          },
          {
            "count": 22,
            "value": "NTS"
          },
          {
            "count": 22,
            "value": "QME"
          },
          {
            "count": 22,
            "value": "SVQ"
          },
          {
            "count": 22,
            "value": "VLC"
          },
          {
            "count": 21,
            "value": "AOI"
          },
          {
            "count": 21,
            "value": "CEQ"
          },
          {
            "count": 21,
            "value": "DKR"
          },
          {
            "count": 20,
            "value": "KTM"
          },
          {
            "count": 20,
            "value": "SJDL"
          },
          {
            "count": 19,
            "value": "AGP"
          },
          {
            "count": 19,
            "value": "DXB"
          },
          {
            "count": 19,
            "value": "TAR"
          },
          {
            "count": 18,
            "value": "LXR"
          },
          {
            "count": 17,
            "value": "BDS"
          },
          {
            "count": 17,
            "value": "DRW"
          },
          {
            "count": 17,
            "value": "LEH"
          },
          {
            "count": 17,
            "value": "ZAF"
          },
          {
            "count": 16,
            "value": "DBV"
          },
          {
            "count": 16,
            "value": "LPA"
          },
          {
            "count": 16,
            "value": "LRM"
          },
          {
            "count": 16,
            "value": "MEM"
          },
          {
            "count": 16,
            "value": "RAN"
          },
          {
            "count": 16,
            "value": "SYR1"
          },
          {
            "count": 16,
            "value": "VAP"
          },
          {
            "count": 16,
            "value": "WPU"
          },
          {
            "count": 15,
            "value": "BME"
          },
          {
            "count": 15,
            "value": "DPS"
          },
          {
            "count": 15,
            "value": "VDT"
          },
          {
            "count": 14,
            "value": "ALC"
          },
          {
            "count": 14,
            "value": "OLB"
          },
          {
            "count": 14,
            "value": "PNH"
          },
          {
            "count": 14,
            "value": "SCL"
          },
          {
            "count": 14,
            "value": "SXM"
          },
          {
            "count": 14,
            "value": "YMQ"
          },
          {
            "count": 14,
            "value": "ZWD"
          },
          {
            "count": 13,
            "value": "JFM"
          },
          {
            "count": 12,
            "value": "LNZ"
          },
          {
            "count": 12,
            "value": "MAD"
          },
          {
            "count": 12,
            "value": "YOK"
          },
          {
            "count": 11,
            "value": "BCON"
          },
          {
            "count": 11,
            "value": "OLT"
          },
          {
            "count": 10,
            "value": "AUA"
          },
          {
            "count": 10,
            "value": "BLB"
          },
          {
            "count": 10,
            "value": "CHSS"
          },
          {
            "count": 10,
            "value": "CNS"
          },
          {
            "count": 10,
            "value": "HOFL"
          },
          {
            "count": 10,
            "value": "MSP"
          },
          {
            "count": 10,
            "value": "SFJ"
          },
          {
            "count": 10,
            "value": "TOS"
          },
          {
            "count": 9,
            "value": "ANR"
          },
          {
            "count": 9,
            "value": "GVA"
          },
          {
            "count": 9,
            "value": "MANT"
          },
          {
            "count": 9,
            "value": "ORF"
          },
          {
            "count": 8,
            "value": "DUB"
          },
          {
            "count": 8,
            "value": "OSL"
          },
          {
            "count": 7,
            "value": "ADL"
          },
          {
            "count": 7,
            "value": "BOM"
          },
          {
            "count": 7,
            "value": "CHC"
          },
          {
            "count": 7,
            "value": "JNU"
          },
          {
            "count": 7,
            "value": "LUX"
          },
          {
            "count": 7,
            "value": "MCM"
          },
          {
            "count": 7,
            "value": "QMZ"
          },
          {
            "count": 6,
            "value": "ASHD"
          },
          {
            "count": 6,
            "value": "BRIA"
          },
          {
            "count": 6,
            "value": "CALL"
          },
          {
            "count": 6,
            "value": "COCM"
          },
          {
            "count": 6,
            "value": "HNL"
          },
          {
            "count": 6,
            "value": "KKN"
          },
          {
            "count": 6,
            "value": "ONX"
          },
          {
            "count": 6,
            "value": "RIO"
          },
          {
            "count": 6,
            "value": "RTM"
          },
          {
            "count": 6,
            "value": "STL"
          },
          {
            "count": 6,
            "value": "VLT"
          },
          {
            "count": 6,
            "value": "ZAG"
          },
          {
            "count": 6,
            "value": "ZCC"
          },
          {
            "count": 6,
            "value": "ZQF"
          },
          {
            "count": 5,
            "value": "AQJ"
          },
          {
            "count": 5,
            "value": "DOJ"
          },
          {
            "count": 5,
            "value": "DUD"
          },
          {
            "count": 5,
            "value": "PTY"
          },
          {
            "count": 5,
            "value": "RAV"
          },
          {
            "count": 5,
            "value": "SPND"
          },
          {
            "count": 5,
            "value": "TILB"
          },
          {
            "count": 5,
            "value": "YBZ"
          },
          {
            "count": 4,
            "value": "EDI"
          },
          {
            "count": 4,
            "value": "KEEL"
          },
          {
            "count": 4,
            "value": "LACH"
          },
          {
            "count": 4,
            "value": "MDL"
          },
          {
            "count": 4,
            "value": "SAAN"
          },
          {
            "count": 4,
            "value": "SAN"
          },
          {
            "count": 4,
            "value": "SETE"
          },
          {
            "count": 4,
            "value": "SIG"
          },
          {
            "count": 4,
            "value": "SZG"
          },
          {
            "count": 3,
            "value": "BPE"
          },
          {
            "count": 3,
            "value": "GLA"
          },
          {
            "count": 3,
            "value": "KGIA"
          },
          {
            "count": 3,
            "value": "KRK"
          },
          {
            "count": 3,
            "value": "MAO"
          },
          {
            "count": 3,
            "value": "MART"
          },
          {
            "count": 3,
            "value": "MIL"
          },
          {
            "count": 3,
            "value": "MKE"
          },
          {
            "count": 3,
            "value": "PAS"
          },
          {
            "count": 3,
            "value": "RUDE"
          },
          {
            "count": 3,
            "value": "TRI"
          },
          {
            "count": 3,
            "value": "YHZ"
          },
          {
            "count": 3,
            "value": "ZBR1"
          },
          {
            "count": 2,
            "value": "BREI"
          },
          {
            "count": 2,
            "value": "CGN"
          },
          {
            "count": 2,
            "value": "FNC"
          },
          {
            "count": 2,
            "value": "GLC"
          },
          {
            "count": 2,
            "value": "HBA"
          },
          {
            "count": 2,
            "value": "MHG"
          },
          {
            "count": 2,
            "value": "NVS"
          },
          {
            "count": 2,
            "value": "OME"
          },
          {
            "count": 2,
            "value": "ORAN"
          },
          {
            "count": 2,
            "value": "OSA"
          },
          {
            "count": 2,
            "value": "ROSY"
          },
          {
            "count": 2,
            "value": "SEZ"
          },
          {
            "count": 2,
            "value": "SHA"
          },
          {
            "count": 2,
            "value": "SSZ"
          },
          {
            "count": 2,
            "value": "TCI"
          },
          {
            "count": 2,
            "value": "YUL"
          },
          {
            "count": 1,
            "value": "AUH"
          },
          {
            "count": 1,
            "value": "AVV"
          },
          {
            "count": 1,
            "value": "AYT"
          },
          {
            "count": 1,
            "value": "BBO"
          },
          {
            "count": 1,
            "value": "CTG"
          },
          {
            "count": 1,
            "value": "DRS"
          },
          {
            "count": 1,
            "value": "DYR"
          },
          {
            "count": 1,
            "value": "ETHA"
          },
          {
            "count": 1,
            "value": "HAB"
          },
          {
            "count": 1,
            "value": "HEL"
          },
          {
            "count": 1,
            "value": "IJM"
          },
          {
            "count": 1,
            "value": "JAP"
          },
          {
            "count": 1,
            "value": "LIV1"
          },
          {
            "count": 1,
            "value": "MMK"
          },
          {
            "count": 1,
            "value": "NAN"
          },
          {
            "count": 1,
            "value": "PUQ"
          },
          {
            "count": 1,
            "value": "PVR"
          },
          {
            "count": 1,
            "value": "SGT"
          },
          {
            "count": 1,
            "value": "SJO"
          },
          {
            "count": 1,
            "value": "SLSD"
          },
          {
            "count": 1,
            "value": "UAK"
          },
          {
            "count": 1,
            "value": "URO"
          }
        ]
      },
      {
        "key": "promoCode",
        "values": [
          {
            "count": 4925,
            "value": "DISCOUNT"
          },
          {
            "count": 1829,
            "value": "WIFI"
          },
          {
            "count": 1709,
            "value": "DINING"
          },
          {
            "count": 1656,
            "value": "BEV"
          },
          {
            "count": 1627,
            "value": "NR"
          },
          {
            "count": 1521,
            "value": "SHOREX"
          },
          {
            "count": 1176,
            "value": "NRD"
          },
          {
            "count": 389,
            "value": "OBC"
          },
          {
            "count": 387,
            "value": "BOGO"
          },
          {
            "count": 222,
            "value": "GRATSI"
          },
          {
            "count": 190,
            "value": "KIDSFREE"
          },
          {
            "count": 172,
            "value": "FIT"
          },
          {
            "count": 125,
            "value": "RETREAT"
          },
          {
            "count": 120,
            "value": "ALWAYS"
          },
          {
            "count": 116,
            "value": "ELEVATE"
          },
          {
            "count": 116,
            "value": "INDULGE"
          },
          {
            "count": 9,
            "value": "EBB"
          },
          {
            "count": 8,
            "value": "FREEUPG"
          },
          {
            "count": 1,
            "value": "ADDGSTDISC"
          }
        ]
      },
      {
        "key": "price",
        "isRangeFilter": true,
        "values": [
          {
            "count": 3952,
            "from": 0,
            "to": 1000
          },
          {
            "count": 1498,
            "from": 1001,
            "to": 2000
          },
          {
            "count": 1946,
            "from": 2001,
            "to": 3000
          },
          {
            "count": 2094,
            "from": 3001,
            "to": 4000
          },
          {
            "count": 1377,
            "from": 4001,
            "to": 5000
          },
          {
            "count": 976,
            "from": 5001,
            "to": 6000
          },
          {
            "count": 2918,
            "from": 6001
          }
        ]
      },
      {
        "key": "departureDateTime",
        "isRangeFilter": true,
        "values": [
          {
            "count": 644,
            "from": "01-May-2023",
            "to": "31-May-2023"
          },
          {
            "count": 2048,
            "from": "01-Jun-2023",
            "to": "30-Jun-2023"
          },
          {
            "count": 2270,
            "from": "01-Jul-2023",
            "to": "31-Jul-2023"
          },
          {
            "count": 2219,
            "from": "01-Aug-2023",
            "to": "31-Aug-2023"
          },
          {
            "count": 1943,
            "from": "01-Sep-2023",
            "to": "30-Sep-2023"
          },
          {
            "count": 1738,
            "from": "01-Oct-2023",
            "to": "31-Oct-2023"
          },
          {
            "count": 1035,
            "from": "01-Nov-2023",
            "to": "30-Nov-2023"
          },
          {
            "count": 938,
            "from": "01-Dec-2023",
            "to": "31-Dec-2023"
          },
          {
            "count": 595,
            "from": "01-Jan-2024",
            "to": "31-Jan-2024"
          },
          {
            "count": 543,
            "from": "01-Feb-2024",
            "to": "29-Feb-2024"
          },
          {
            "count": 618,
            "from": "01-Mar-2024",
            "to": "31-Mar-2024"
          },
          {
            "count": 362,
            "from": "01-Apr-2024",
            "to": "30-Apr-2024"
          },
          {
            "count": 139,
            "from": "01-May-2024",
            "to": "31-May-2024"
          },
          {
            "count": 117,
            "from": "01-Jun-2024",
            "to": "30-Jun-2024"
          },
          {
            "count": 102,
            "from": "01-Jul-2024",
            "to": "31-Jul-2024"
          },
          {
            "count": 117,
            "from": "01-Aug-2024",
            "to": "31-Aug-2024"
          },
          {
            "count": 115,
            "from": "01-Sep-2024",
            "to": "30-Sep-2024"
          },
          {
            "count": 88,
            "from": "01-Oct-2024",
            "to": "31-Oct-2024"
          },
          {
            "count": 39,
            "from": "01-Nov-2024",
            "to": "30-Nov-2024"
          },
          {
            "count": 25,
            "from": "01-Dec-2024",
            "to": "31-Dec-2024"
          },
          {
            "count": 2,
            "from": "01-Jan-2025",
            "to": "31-Jan-2025"
          }
        ]
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
