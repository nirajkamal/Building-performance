# Building-performance
Python Script written to process and output the results using sensor data from the buildings. The script also uses the datasets of ASHRAE and CBRI.

# parameters calculated
Sensors were deployed in various locations in Humanscapes habitat, and data on light intensity(lux), humidity(relative and absolute), ambient room temperature, surface wall temperature(inner and outer), roof surface temperature(inner and outer), clo values of clothing and black bulb temperature were continuously recorded.

The parameters calculated using the above data are as follows:
## thermal comfort 
Tropical summer index; \n
predicted mean vote;
predicteed percentage dissatisfied;
heat stress distribution;
fan wind velocity required

## thermal performance
damping percentage;
depreciation factor;
time lag;
thermal performance index;
instantaneous damping


other outputs include the maximum, minimum and average of all the readings on a daily basis. Using these parameters, the thermal performace of humanscapes habitat were calculated, and also strategies both active and passive were proposed to optimise the energy usage and thermal performance.
