# Synthetic Population 

This repository uses [Worldpop.org](https://www.worldpop.org/) to generate a synthetic population to seed a Agent Based Model. 

It consists of four files: 

1. **Population Data Download:** This file downloads Worlpop density data and demographic data for the desired country of interest using Worldpop's file transfer protocol (ftp) procedures. It does require a log int. 

2. **Density Demographic Exploration and Conversion:** This file takes the downloaded density (ppp) file, plots the density it on a heat map and allows users to select the whole country or narrow down to smaller location. The files then saves at the users desired level of accuracy a json file where it latitude and longitude has a discrete number of agents. Due to the size of the files this is the only file where the data is stored locally on github and can run completely through the binder badge. 

3. **Demographic Exploration and Conversion:** This files takes the downloaded demographic data and plot it in a vertical bar graph. The files then saves at the users desired level of accuracy a json file where it latitude and longitude has a discrete number of agents for each demographic category.

4. **Density and Demographic Merge:** This file merges and deconflict the density and demographic json outputs. The user can then save the large dataframe in a .csv or .json and use it to build a synthetic population assigned each agent to a specific latitude and longitude based on the users desired level of accuracy.  