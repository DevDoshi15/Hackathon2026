URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000128849459/en

ID: 80395000128849459
# Knowledge Base: ReservationPreferences Used During Create or Modify Reservation

## Overview

`ReservationPreferences` are optional behavioral flags that modify how
the Nitro Booking API processes Create Reservation and Modify
Reservation requests for specific cruise lines.

These preferences do **not** change the request schema. Instead, they
instruct Odysseus or the supplier integration to alter specific
processing logic.

> **Important:** Most ReservationPreferences are cruise-line specific.
> Only include them when the corresponding supplier supports the
> behavior.

------------------------------------------------------------------------

# Scope

**Applicable APIs** - Create Reservation - Modify Reservation

**Purpose** - Override default booking behavior - Enable
supplier-specific functionality - Control retry, lookup, package
inclusion, and passenger validation logic

------------------------------------------------------------------------

# Supported ReservationPreferences

  --------------------------------------------------------------------------------------------
  Preference                            Description       Cruise Line Applicability
  ------------------------------------- ----------------- ------------------------------------
  `DisableSecondaryPhoneFailureRetry`   Disables retry    All cruise lines that support
                                        attempts when     secondary phone numbers
                                        failures occur    
                                        while sending the 
                                        secondary phone   
                                        number.           

  `DoNotAutoIncludePackages`            Prevents          Holland America (HAL), Seabourn,
                                        automatic         Princess, Cunard
                                        inclusion of      
                                        pre-cruise or     
                                        post-cruise       
                                        packages.         

  `SendPastPassengerNumber`             Forces the past   Disney
                                        passenger number  
                                        to be transmitted 
                                        to the cruise     
                                        line regardless   
                                        of default        
                                        behavior.         

  `MandatoryUpgradeOptions`             Controls whether  Holland America (HAL), Seabourn
                                        a complimentary   
                                        upgrade option is 
                                        explicitly sent   
                                        for pricing.      
                                        Enabled =         
                                        **Yes**, Disabled 
                                        = **No**.         

  `PastPaxLookupByNumber`               Performs past     Supplier-specific lookup behavior
                                        passenger lookup  
                                        using only the    
                                        past passenger    
                                        number and        
                                        ignores other     
                                        guest attributes. 

  `TrustPastPaxNumber`                  Treats the        Norwegian Cruise Line (NCL)
                                        supplied past     
                                        passenger number  
                                        as already        
                                        validated. Guest  
                                        information is    
                                        not transmitted   
                                        during booking    
                                        creation; only    
                                        the past          
                                        passenger number  
                                        is sent.          
  --------------------------------------------------------------------------------------------

------------------------------------------------------------------------

# Preference Details

## DisableSecondaryPhoneFailureRetry

### Purpose

Stops automatic retry logic when a supplier rejects or fails the
secondary phone number.

### Applies To

All suppliers supporting secondary phone numbers.

------------------------------------------------------------------------

## DoNotAutoIncludePackages

### Purpose

Prevents Odysseus from automatically adding eligible pre/post-cruise
packages.

### Supported Suppliers

-   Holland America
-   Seabourn
-   Princess
-   Cunard

------------------------------------------------------------------------

## SendPastPassengerNumber

### Purpose

Overrides default logic and always transmits the guest's past passenger
number.

### Supported Supplier

Disney Cruise Line

------------------------------------------------------------------------

## MandatoryUpgradeOptions

### Purpose

Some suppliers require an explicit complimentary upgrade preference for
successful pricing.

-   Enabled → sends **Yes**
-   Disabled → sends **No**

### Supported Suppliers

-   Holland America
-   Seabourn

------------------------------------------------------------------------

## PastPaxLookupByNumber

### Purpose

Lookup is performed exclusively using the past passenger number.

Guest name, DOB, and other attributes are ignored.

------------------------------------------------------------------------

## TrustPastPaxNumber

### Purpose

Indicates that the past passenger number has already been validated.

For supported suppliers, only the loyalty/past passenger number is
transmitted during Create Booking.

Guest demographic information is omitted.

### Supported Supplier

Norwegian Cruise Line (NCL)

------------------------------------------------------------------------

# Business Rules

1.  ReservationPreferences are optional.
2.  Each preference has supplier-specific applicability.
3.  Unsupported suppliers may ignore these preferences.
4.  These preferences alter processing logic---not API structure.
5.  Use only when the associated business requirement exists.

------------------------------------------------------------------------

# Troubleshooting

### Past passenger number not transmitted

Verify `SendPastPassengerNumber` is enabled for Disney integrations.

### NCL booking without guest details fails

Ensure `TrustPastPaxNumber` is used only when the past passenger number
is validated.

### Complimentary upgrade pricing fails

Check `MandatoryUpgradeOptions` for HAL or Seabourn.

### Unexpected pre/post packages included

Verify `DoNotAutoIncludePackages` is enabled.

------------------------------------------------------------------------

# AI Agent Knowledge

The AI agent should know:

-   ReservationPreferences customize supplier-specific booking behavior.
-   They apply to Create and Modify Reservation APIs.
-   `TrustPastPaxNumber` is unique to NCL.
-   `SendPastPassengerNumber` is used for Disney.
-   `MandatoryUpgradeOptions` affects HAL and Seabourn pricing.
-   `DoNotAutoIncludePackages` prevents automatic package inclusion.
-   `PastPaxLookupByNumber` ignores all guest attributes except the
    loyalty number.
-   `DisableSecondaryPhoneFailureRetry` suppresses retry logic for
    secondary phone failures.

------------------------------------------------------------------------

# Search Keywords

ReservationPreferences, Create Booking, Modify Booking,
TrustPastPaxNumber, PastPaxLookupByNumber, SendPastPassengerNumber,
MandatoryUpgradeOptions, DoNotAutoIncludePackages,
DisableSecondaryPhoneFailureRetry, NCL, Disney, HAL, Seabourn, Princess,
Cunard, Nitro Booking API
