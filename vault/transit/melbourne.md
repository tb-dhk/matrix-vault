---
title: how does melbourne's metro work?
date: 2026-08-22
tags:
  - transit
  - metro
number: 0
hide: true
description: a deep dive into victoria's passenger rail network
---
as you can probably guess from the title and description, the title is a slight misnomer. i have recently been studying melbourne's metro system, but i quickly realised most maps of the melbourne metro also tend to include victoria's regional rail lines as well. this is mainly because melbourne has 5.4 million people, which is about 77% of victoria's total population (7.1 million), which makes victoria australia's most centralised state. melbourne's passenger rail network is thus also victoria's passenger rail network.

melbourne is home to many places that are very important to me. not sentimentally, of course - i have lived in singapore for all but slightly less than two years of my life. however, the university of melbourne, where my parents met, and the many apartments (and one house) my parents lived in together during the late 1990s and early 2000s had a huge part to play in my conception and early childhood. while i do not remember much of my life there, i feel like some part of me wants to learn a bit more about the city where i spent some of my most foundational years in.

victoria's passenger rail network has three (or four) main components, as detailed in the following table:

| name                                        | company                | type                       | aim                                               | notes                                                                                                                                     |
| ------------------------------------------- | ---------------------- | -------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [melbourne metro](<#metro>)                   | metro trains melbourne | commuter rail / heavy rail | connecting melbourne's suburbs to the city centre | despite its name, this is not a metro for the most part (other than the city loop).                                                       |
| [v/line](<#v/line>)                           | v/line corporation     | regional commuter rail     | connecting melbourne to other parts of victoria   | v/line also runs coach services that include connections that do not involve melbourne, but we will not be covering them in this article. |
| [suburban rail loop](<#suburban rail loop>) | transitlinx            | automated rapid transit    | interconnectivity between melbourne's suburbs     | under construction; also not an actual loop                                                                                               |

all assets are owned by victrack, a state-owned corporation, and leased to transport victoria, a government department. transport victoria then sub-leases operational rights to the respective companies.

![full map of the current victorian train network](network.png)

in this article, i'll be going through each component and the history and infrastructure surrounding it.
# metro
the melbourne metro system is owned by transport victoria and metro trains melbourne, which is a private joint venture between three companies:
- MTR corporation (60%) - hong kong's government-owned transport operator and property developer that runs hong kong's MTR as well as several other countries, including australia
- john holland (20%) - an oceania-based infrastructure, building, and rail transport services companies, owned by the china communications transport company, a state-owned engineering and construction firm
- UGL rail (20%) - an australian rail company specialising in building, maintaining and refurbishing diesel locomotives
## lines
the melbourne metro is basically the pinnacle of the hub-and-spoke model. the main hub is the city centre, best represented by the [city loop](<#city loop>), which branches out into several trunks from the city centre. each individual line then branches out further from the trunk to reach various different parts of melbourne. due to how the network is centered around a central hub, trains are usually referred to as "inbound" (towards the city centre) or "outbound" (towards the suburbs)

there are a total of 15 main metro lines, which are usually grouped into 6 main groups based on the spoke they use. the groups going through the city loop are named after the last station all the lines share before they start branching out. each line is named after its terminus, with the exception of some lines that have been extended without any renaming, like the pakenham line that has since been extended to east pakenham.

here is some information about each group:

| group                                                                                 | eponym (station) | colour     | lines                                                                              | city loop direction                                      | entry point to city loop                                                                                              |
| ------------------------------------------------------------------------------------- | ---------------- | ---------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| <span class="box" style="background-color: #be1014; color: white">clifton hill</span> | <                | red        | mernda, hurstbridge                                                                | clockwise                                                | between parliament and flinders street                                                                                |
| <span class="box" style="background-color: #028430; color: white">caulfield</span>    | <                | green      | frankston                                                                          | anticlockwise                                            | ^                                                                                                                     |
| <span class="box" style="background-color: #152c6b; color: white">burnley</span>      | <                | dark blue  | lilydale, belgrave, alamein, glen waverley                                         | anticlockwise on weekday mornings, clockwise otherwise   | ^                                                                                                                     |
| <span class="box" style="background-color: #ffbe00; color: black">northern</span>     | north melbourne  | yellow     | craigieburn, upfield                                                               | anticlockwise on weekday afternoons, clockwise otherwise | between southern cross and flagstaff                                                                                  |
| <span class="box" style="background-color: #f178af; color: black">cross-city</span>   | n/a              | pink       | sandringham, werribee, williamstown                                                | n/a (flinders street and southern cross only)            | between parliament and flinders street (sandringham)<br>between southern cross and flagstaff (williamstown, werribee) |
| <span class="box" style="background-color: #279fd5; color: white">yarra</span>        | ^                | light blue | cranbourne, pakenham, sunbury, [airport rail (under construction)](<#airport rail\>) | n/a ([metro tunnel](<#metro tunnel>))                    | <                                                                                                                     |

there are two other special lines that are part of the metro network.

| line                  | colour | route                                                                                                                                                                                           | notes                                                                                                                                        |
| --------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| stony point           | green  | from frankston (end of frankston line) to stony point                                                                                                                                           | only non-electrified line (diesel), serves as a shuttle service                                                                              |
| flemington racecourse | grey   | runs clockwise from flinders street, parallel with the <span class="box" style="background-color: #ffbe00; color: black">northern</span> group until north melbourne | also called the special event line; only for special events happening at or near the racecourse, including races and university examinations |

## infrastructure
the melbourne metro is a mix of commuter and heavy rail, where it is fully underground in the middle (city loop and metro tunnel) and above ground otherwise with many at-grade crossings.

> [!info] what are commuter and heavy rail?
> **commuter rail** uses large trains to connect outer suburbs and city centers mostly during peak hours. these tracks are often shared with regional and intercity trains and have many at-grade crossings. this is the case for most of the melbourne metro.
> **heavy rail** uses fully separated and dedicated urban tracks with high frequency and all-day service to move large crowds within a city. this applies specifically to the city loop and metro tunnel, which are fully underground and reserved for melbourne metro trains.
### city loop
the city loop is a loop consisting of 5 stations in melbourne's city centre. in clockwise order starting from the west, they are:
- southern cross
- flagstaff
- melbourne central
- parliament
- flinders street

all metro and regional lines (other than the stony point metro line) have at least one station on the city loop, and the <span class="box" style="background-color: #be1014; color: white">clifton hill</span>, <span class="box" style="background-color: #028430; color: white">caulfield</span>, <span class="box" style="background-color: #152c6b; color: white">burnley</span> and <span class="box" style="background-color: #ffbe00; color: black">northern</span> groups actually go around the city loop before turning back to their respective termini. notably, they will pass through each station once before leaving the same way they came.

the city loop only consists of four tracks, each assigned to a group. this has led to a lot of congestion since up to four (previously [five](<#initial groupings>)) different lines could be running in one tunnel at the same time. additionally, when tracks switch directions slightly past noon, all trains on the track have to leave the loop before new trains can start running the other way, which can lead to a gap in some services from 1230 to 1300.
### metro tunnel
the metro tunnel is a relatively recent development in melbourne's rail system that essentially allows lines to go through the city, to prevent congestion in the city loop. it now accommodates the cranbourne, pakenham and sunbury lines (the <span class="box" style="background-color: #279fd5; color: white">yarra</span> group). the metro tunnel runs through two stations in the city centre with direct underground connections to the city loop:
- town hall (flinders street)
- state library (melbourne central)

the metro tunnel initially opened in november of 2025. to allow for a gradual transition, <span class="box" style="background-color: #279fd5; color: white">yarra</span> group services initially only used the metro tunnel at certain times of the day while reverting to their original city loop routes otherwise. in february of 2026, the <span class="box" style="background-color: #279fd5; color: white">yarra</span> group switched fully to the metro tunnel.
## regroupings
there have been two major events that have led to the regroupings of some lines. both of these are related to pulling lines out of the city loop due to congestion.
### initial groupings
when the city loop was fully commissioned in 1985, all metropolitan lines were funneled into the city loop through one of four groups, and they all went around the city loop before returning to their respective termini.

| group                                                                                                        | colour    | lines                                                                 |
| ------------------------------------------------------------------------------------------------------------ | --------- | --------------------------------------------------------------------- |
| <span class="box" style="background-color: #be1014; color: white">clifton hill</span>           | red       | mernda (then epping), hurstbridge                                     |
| <span class="box" style="background-color: #028430; color: white">caulfield</span>              | green     | frankston, pakenham, cranbourne, sandringham                          |
| <span class="box" style="background-color: #152c6b; color: white">burnley</span>                | dark blue | lilydale, belgrave, alamein, glen waverley                            |
| <span class="box" style="background-color: #ffbe00; color: black">northern</span> | yellow    | werribee, williamstown, sunbury (then sydenham), craigieburn, upfield |
### formation of the <span class="box" style="background-color: #f178af; color: black">cross-city</span> group
in 2011, the frankston line (<span class="box" style="background-color: #028430; color: white">caulfield</span>) as well as the werribee and williamstown lines (<span class="box" style="background-color: #ffbe00; color: black">northern</span>) were pulled out of their respective groups to form a new <span class="box" style="background-color: #f178af; color: black">cross-city</span> group where trains would simply run from one end to the other, through flinders street and southern cross stations.
### opening of metro tunnel and formation of the <span class="box" style="background-color: #279fd5; color: white">yarra</span> group
when the metro tunnel was fully opened in 2026, yet another reassignment occured. the sunbury line (<span class="box" style="background-color: #ffbe00; color: black">northern</span>) as well as the pakenham and cranbourne lines (<span class="box" style="background-color: #028430; color: white">caulfield</span>) were extracted from the city loop and routed through the metro tunnel, creating the new <span class="box" style="background-color: #279fd5; color: white">yarra</span> group. 

additionally, the frankston line (<span class="box" style="background-color: #f178af; color: black">cross-city</span>) and sandringham line (<span class="box" style="background-color: #028430; color: white">caulfield</span>) swapped groups, meaning the frankston line was returned to the city loop and the <span class="box" style="background-color: #028430; color: white">caulfield</span> group, while the sandringham line became part of the <span class="box" style="background-color: #f178af; color: black">cross-city</span> group, pairing with the werribee and williamstown lines.
### summary table of all changes
jesus fucking christ.

| line         | 1985                                                                               | 2011                                                                                | 2026                                                                                |
| ------------ | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| frankston    | <span class="box" style="background-color: #028430; color: white">caulfield</span> | <span class="box" style="background-color: #f178af; color: black">cross-city</span> | <span class="box" style="background-color: #028430; color: white">caulfield</span>  |
| sandringham  | <span class="box" style="background-color: #028430; color: white">caulfield</span> | <                                                                                   | <span class="box" style="background-color: #f178af; color: black">cross-city</span> |
| pakenham     | ^                                                                                  | <                                                                                   | <span class="box" style="background-color: #279fd5; color: white">yarra</span>      |
| cranbourne   | ^                                                                                  | <                                                                                   | ^                                                                                   |
| werribee     | <span class="box" style="background-color: #ffbe00; color: black">northern</span>  | <span class="box" style="background-color: #f178af; color: black">cross-city</span> | <                                                                                   |
| williamstown | ^                                                                                  | ^                                                                                   | <                                                                                   |
| sunbury      | <span class="box" style="background-color: #ffbe00; color: black">northern</span>  | <                                                                                   | <span class="box" style="background-color: #279fd5; color: white">yarra</span>      |
## airport rail
the airport rail is a new line to be integrated into the melbourne metro system. it will share tracks with the sunbury line starting from just west of sunshine station before heading towards the metro tunnel, making it effectively a part of the <span class="box" style="background-color: #279fd5; color: white">yarra</span> group.
# v/line
the v/line system is victoria's regional rail system, which extends beyond melbourne to other parts of victoria. it is operated by v/line corporation, a statutory authority.

regional lines are either commuter (formerly "interurban") or long-distance (formerly "intercity"), and are all named after their respective termini. they all run from southern cross in five different directions, sharing tracks with at least one metro line (usually acting as an express service along that line). each direction corresponds to one commuter line, and long-distance lines share all stops with the commuter line running in the same direction, but also extend past the commuter line's terminus. notably, the myki ticketing system that is used in the rest of melbourne's public transport is not usable for parts of the long-distance lines further away from melbourne.

here is some information about the regional train lines:

| direction | commuter line | long-distance line  | color  | corresponding metro line | last station shared with metro line |
| --------- | ------------- | ------------------- | ------ | ------------------------ | ----------------------------------- |
| southwest | geelong       | warrnambool         | purple | sunbury                  | sunshine                            |
| west      | ballarat      | ararat, maryborough | ^      | ^                        | ^                                   |
| north     | bendigo       | echuca, swan hill   | ^      | ^                        | sunbury                             |
| northeast | seymour       | albury, shepparton  | ^      | craigieburn              | <                                   |
| east      | traralgon     | bairnsdale          | ^      | pakenham                 | east pakenham                       |

while v/line trains do pass through some stations on the city loop, they do not use the underground city loop tracks that are reserved for metro trains. instead, they use their own overground tracks.
# suburban rail loop
the main problem with the hub-and-spoke model is that interconnectivity between spokes (the suburbs) is poor. the suburban rail loop (SRL) is an automated rapid transit line that aims to fix this by going in an arc around melbourne. while not an actual closed loop, it will serve as a bypass that allows commuters to go to other parts of melbourne without having to go through the city.

the suburban rail loop is run by transitlinx, a consortium of several companies:
- john holland (see [metro trains melbourne](<#metro>))
- RATP dev - a subsidiary of RATP group that provides operations and maintenance of passenger transport services. RATP group is a french state-owned enterprise that operates public transport systems primarily in paris, france
- alstom - a french multinational rail transport systems manufacturer
- KBR - a major american engineering company
- WSP - a canadian multinational engineering consultancy

![map of the suburban rail loop (and airport rail)](srl.png)

the suburban rail loop has three main sections:
- SRL east: runs from cheltenham to box hill
- SRL north: runs from box hill to melbourne airport
- SRL west: runs from weribee to sunshine

the [melbourne airport rail line](<#airport rail>) will serve as a link between SRL north and SRL west, since part of its route is from melbourne airport to sunshine.

while SRL east is due to finish by 2035, the SRL project is taking place over several decades. SRL north is still in the final stages of proposal and SRL west does not have any publicly available plans as of yet.
# conclusion
this concludes our brief venture into victoria's (although mostly melbourne's) metro system. despite how convoluted it is and how long their projects take, it's quite interesting to look at australia's biggest commuter rail system and its different layers in detail.