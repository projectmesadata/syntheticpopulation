# Synthetic Population 



This repository uses [Worldpop.org](https://www.worldpop.org/) to generate a synthetic population to seed a Agent Based Model. 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/projectmesadata/syntheticpopulation/HEAD)
*Due to size Binder only has files for Density Exploration and Conversion*

It consists of four files: 

1. **Population Data Download:** This file downloads Worlpop density data and demographic data for the desired country of interest using Worldpop's file transfer protocol (ftp) procedures. It does require a log in. 

2. **Density Exploration and Conversion:** This file takes the downloaded density (ppp) file, plots the density it on a heat map and allows users to select the whole country or narrow down to smaller location. The information is saved in Hierarchical Data Format 5 (.h5). Due to the size of the files this is the only file where the data is stored locally on github and can run completely through the binder badge using Albania as an example. However, larger countries will be significantly larger files. 
3. **Demographic Exploration and Conversion:** This files takes the downloaded demographic data and plots it in a vertical bar graph. The files then saves at the users desired level of accuracy an .h5 file. Due to the size and number of data these files can be very large as an example a country the size of Niger is **approximately 70 gigabytes.**

4. **syntheticpopulation_starter:** This file provides an example of taking the demographic.h5 file and converting it Mesa agent objects in a *RandomActivation* schedule.    