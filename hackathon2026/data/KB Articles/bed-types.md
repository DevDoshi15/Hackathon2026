URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000033205457/en

ID: 80395000033205457
# Domain Table: Bed Types

## Overview

This table defines the full set of cabin bed configuration types used across the booking platform. Each bed type has a fixed integer ID used as its identifier throughout the system (e.g. in cabin category/configuration mappings). Entries range from simple single/double/twin/queen/king configurations to convertible configurations, sofa-bed combinations, accessibility (wheelchair) configurations, and infant/child bedding (crib, cot).

## Reference Table

| ID | Name |
|---|---|
| 190 | 1 Lower Twin Bed |
| 191 | 1 Lower With 1 Upper |
| 192 | 1 Upper Berth |
| 193 | 1 Double 2 Lower Twin Beds |
| 194 | 2 Lower Beds |
| 195 | 2 Lower Beds Rollaway |
| 196 | 2 Lower Beds 1 Upper Bed |
| 197 | 2 Lower Beds 2 Upper Beds |
| 198 | 2 Lower Twin Conv To Double |
| 199 | 2 Lower Beds 1 Upper Berth |
| 200 | 2 Lower Twin Conv To Queen |
| 201 | 2 Lower L Shape Conv King |
| 202 | 2 Lower Twin Conv To King |
| 203 | 2 Sofa Beds |
| 204 | 2 Upper Berths |
| 205 | 3 Lower Twin Beds |
| 206 | 3 Lower L Shape No Convert |
| 207 | Bed Boards |
| 208 | Bed Extensions |
| 209 | Bed Rails |
| 210 | Convertible |
| 211 | Cot |
| 212 | Crib |
| 213 | Double Bed |
| 214 | Double Converts To Twin |
| 215 | Double Murphy Bed |
| 216 | Double Single Sofa 1 Upper |
| 217 | Double Sofa |
| 218 | Double With Crib |
| 219 | Double With Rollaway |
| 220 | Double With Sofa |
| 221 | Double With Upper Pullman |
| 222 | First Lower Twin Berth |
| 223 | First Upper Pullman |
| 224 | Four Convertible Twins |
| 225 | Interchangeable Berth Use Spare |
| 226 | King Bed |
| 227 | King With 1 Upper |
| 228 | King With Crib |
| 229 | King With Double Sofa |
| 230 | King With Rollaway |
| 231 | King With Single Sofa 1 Upper |
| 232 | King With Sofa |
| 233 | L Shape Converts To Twin/Double |
| 234 | Lower Single Conv Sofa |
| 235 | Multiple |
| 236 | Murphy Bed |
| 237 | No Selection |
| 238 | Non Converting Twins |
| 239 | Non Interchangeable Berth Use Spare |
| 240 | Pullman |
| 241 | Pullout Bed |
| 242 | Quad Twin Beds |
| 243 | Queen Bed |
| 244 | Queen Bed Single Sofa 1 Upper |
| 245 | Queen Bed With Sofa |
| 246 | Queen Bed With Upper Pullman |
| 247 | Queen Bedded Handicap Cabin |
| 248 | Queen Conv To Twin |
| 249 | Queen With Crib |
| 250 | Queen With Rollaway |
| 251 | Rollaway Bed |
| 252 | Second Lower Twin Berth |
| 253 | Second Upper Pullman |
| 254 | Single Sofa |
| 255 | Single With Crib |
| 256 | Sofa Bed |
| 257 | Sofa Made In Lower Berth |
| 258 | Stationary Lower Bed |
| 259 | Twin/King Conv Single Sofa 1 Upper |
| 260 | Twin/Double Reduces Floor Space |
| 261 | Twin Beds |
| 262 | Twin Beds With Sofa |
| 263 | Twin Double Sofa |
| 264 | Twin King Conv 1 Upper |
| 265 | Twin King Conv 2 Uppers |
| 266 | Twin King Conv Double Sofa |
| 267 | Twin King Conv Single Sofa |
| 268 | Twin King Converting |
| 269 | Twin King Single Sofa |
| 270 | Twin Murphy |
| 271 | Twin Single Sofa 1 Upper |
| 272 | Twin With 1 Upper |
| 273 | Twin With Child Bed |
| 274 | Twin With Crib |
| 275 | Twin With Foldout |
| 276 | Twin With Pullman |
| 277 | Wheelchair Ship And Tour |
| 278 | Wheelchair Ship And Tour Disability |
| 279 | Wheelchair Tour Use Only |
| 280 | 1 Lower Bed |
| 281 | Apart |
| 282 | Together |
| 283 | One Set Together |
| 284 | Couch Bed |
| 285 | 2 Lower Twin Bed - Not Convertible |
| 286 | Lower Pullman |
| 287 | Sofa Bed Double |
| 288 | 1 Single Sofa and 2 Lower Twin Beds in L Shape Configuration |
| 289 | 1 Single Sofa and 1 Double Murphy Bed |

## Notes on Naming Conventions

Several recurring patterns/abbreviations appear across entries:
- **Conv / Converts / Convertible** — indicates the configuration can be physically converted between two bed types (e.g. twin → king, twin → queen, double → twin).
- **Pullman** — a fold-down berth, typically an upper bunk.
- **Sofa / Sofa Bed / Murphy Bed** — indicates the sleeping surface folds out of or converts from furniture (sofa or wall-mounted Murphy bed) rather than being a standing bed.
- **Lower / Upper / Berth** — refers to bunked sleeping positions, common in multi-occupancy or triple/quad cabins.
- **Wchr (Wheelchair)** — accessibility-designated bed/cabin configurations (IDs 277–279).
- **Crib / Cot** — infant bedding add-ons, generally paired with a primary bed type (e.g. "Double With Crib," "Queen With Crib," "Twin With Crib").
- **Rollaway** — a temporary, wheeled extra bed added to a primary configuration.
- **Interchangeable / Non Interchangeable Berth** — indicates whether berth positions can be swapped using spare components (IDs 225, 239).
- **No Selection (237)** — placeholder/default value indicating no specific bed type has been chosen.
- **Multiple (235)** — placeholder indicating more than one bed configuration applies and isn't broken out individually.

## Category Groupings (for quick reference)

- **Single/Twin-based:** 190, 192, 205, 222, 238, 242, 252, 261, 262, 268, 272–276, 285
- **Double-based:** 213–221
- **Queen-based:** 243–250
- **King-based:** 226–232
- **Convertible configurations:** 198, 200–202, 210, 214, 233, 248, 259, 264–269
- **Sofa/Murphy-bed based:** 203, 215–217, 231, 234, 236, 254, 256–257, 263, 270–271, 284, 287–289
- **Berth/Pullman (bunk-style):** 191, 192, 199, 204, 222–223, 240, 252–253, 258, 264–265, 271, 276, 286
- **Accessibility (wheelchair):** 277–279
- **Infant/child bedding:** 211, 212, 218, 228, 249, 255, 273–274
- **Miscellaneous/utility entries:** 207–209 (bed hardware/accessories), 235, 237, 281–283 (occupancy arrangement descriptors, not bed types per se)
