# Norwegian Cruiseline

**Path:** List Cruise Line Airports > Norwegian Cruiseline

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/ListAirGateways`

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
// for norwegian we will only receive departure city codes
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1310202
        }
    },
    "trackingInfo": {
        "token": "EQTEMPKEN"
    }
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Fri, 26 May 2023 12:03:49 GMT
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
    "airGateways": [
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "NPT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "OKK"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SPF"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YMX"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ABE"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ABI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ABQ"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ACT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ACY"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "AGS"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "AHN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ALB"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "AMA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ANC"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "APF"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ATL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ATW"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "AUS"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "AVL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "AVP"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "AZO"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BDL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BFL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BGM"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BGR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BHM"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BIL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BIS"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BLI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BMI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BNA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BOI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BOS"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BPT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BTR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BTV"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BUF"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BUR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BWI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BZN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CAE"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CAK"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CDV"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CHA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CHO"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CHS"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CID"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CLE"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CLT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CMH"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CMI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "COS"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "COU"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CPR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CRP"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CRW"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CSG"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CVG"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CWA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "DAY"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "DCA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "DEN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "DFW"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "DLH"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "DSM"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "DTW"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ELM"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ELP"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ERI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "EUG"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "EVV"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "EWN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "EWR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "EYW"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "FAR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "FAT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "FAY"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "FCA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "FLL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "FLO"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "FNT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "FSD"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "FWA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "GEG"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "GFK"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "GNV"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "GPT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "GRB"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "GRR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "GSO"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "GSP"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "GTF"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "HGR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "HLN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "HNL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "HOU"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "HPN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "HRL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "HSV"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "HTS"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "IAD"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "IAH"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ICT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ILM"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "IND"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "IPL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "IPT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ISO"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ISP"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ITH"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "JAN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "JAX"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "JFK"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "JLN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "JNU"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "KOA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LAN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LAS"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LAX"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LBB"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LEX"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LFT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LGA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LGB"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LIH"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LIT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LNK"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LRD"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LSE"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LYH"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MAF"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MBS"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MCI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MCO"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MDT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MDW"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MEM"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MFE"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MFR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MGM"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MHT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MIA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MKE"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MLI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MLU"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MOB"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MOD"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MOT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MSN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MSO"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MSP"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MSY"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MYR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "OAK"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "OGG"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "OKC"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "OMA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ONT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ORD"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ORF"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "OXR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PBI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PDX"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PFN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PHF"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PHL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PHX"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PIA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PIT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PNS"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PSC"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PSP"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PVD"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PWM"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "RAP"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "RDD"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "RDG"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "RDU"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "RFD"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "RHI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "RIC"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "RNO"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ROA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ROC"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "RST"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "RSW"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SAN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SAT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SAV"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SBA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SBN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SBP"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SBY"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SDF"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SEA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SFO"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SGF"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SHV"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SJC"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SLC"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SMF"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SNA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SPI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SRQ"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "STL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SUX"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SWF"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SYR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TLH"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TOL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TPA"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TRI"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TTN"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TUL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TUS"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TVC"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TVR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TYR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TYS"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YEG"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YHZ"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YOW"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YQB"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YQM"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YQR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YQT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YSJ"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YUL"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YVR"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YWG"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YXE"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YYC"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YYG"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YYJ"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YYT"
          }
        }
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YYZ"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
