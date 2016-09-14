**PS: Slider works best when being clicked on, rather than slid (haven't fixed this yet)**

This interactive tool visualizes the hotspots of the world's innovative activity in the past 40 years. The proxy for innovation which is used here is the number of new patent counts. More precisely, the origin of both the inventor and if applicable, the holding company is scraped from the raw data, aggregated by year, geocoded and projected onto a world map. 
The raw data originates from USPTO patent grant bibliographic data hosted by [Google](https://www.google.com/googlebooks/uspto-patents-grants-biblio.html).

The technical side draws from:
* [Force Chart](https://github.com/armollica/force-chart)
* [D3.js](https://d3js.org/)
* [D3 tip](https://github.com/Caged/d3-tip)
* [D3 slider](http://thematicmapping.org/playground/d3/d3.slider/)
* [Topojson](https://github.com/mbostock/topojson)

Only cities which have produced more than 100 patents in a given year are plotted. This explains the irruption of bubbles in recent years, as the increase of world population has gone hand in hand with greater innovative activity. Japan has unmistakably remained the world's most innovative country during the whole period in consideration. However, in recent years regional competition by South Korea, Taiwan has intensified.

In the US, we see the shifting of power from New York and it's surroundings to Silicon Valley, this has largely been contemporaneous with the microprocessor and Internet revolutions. Some other regional innovation clusters appear clearly, for example near Seattle, Boulder, Austin, Rochester, Atlanta, Chicago etc. As the origins of holding companies were included in the visualization, we observe some peculiarities such as Armonk NY with a population 4330 being more innovation than the whole of New York. However, the headquarters of IBM are situated there...

Finally, in Europe we see that Eastern European countries have not yet caught up with their neighbors. Innovation in Europe is mostly driven by densely populated capitals. In line with the stereotype, Germany seems to be the engine of innovation Europe. In the northern part of the continent Finland stands out, most likely due to the activities of Microsoft, Nokia etc. 

Surprisingly (at least for the author) there is very little innovative actitivity anywhere else, e.g Australia, South America, India, Arab States etc.