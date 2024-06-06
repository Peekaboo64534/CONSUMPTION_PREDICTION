# IDEAL Household Energy Data - Detailed description

This document describes the technical detail of the data contained in the IDEAL Household Energy Dataset. Please read the overview document to understand this data in context. 

There are three related data types:

* **Metadata** - data describing the homes and participants in the study;
* **Sensor Data** - time-series data from individual sensors in the home;
* **Survey Data** - Participant surveys including repeated measures of environmental attitudes.

In this document, each field in each file of each data type is described in turn.

# Metadata
The diagram below indicates how the metadata files relate to each other: each study participant belongs to a home and each home has rooms containing sensorboxes which in turn contain individual sensors that record data.

The diagram is simplified for clarity. It does not show the
```other_appliance```, 
```meterreading``` and 
```tariff``` metadata files, which each link to homeid in the home table.

![metadata relationships](https://i.ibb.co/3Fzb6F5/metadata.png)

## Metadata: home 

There are 255 homes in the dataset. To 30 June 2018, which is the cutoff date for data in this dataset, the sensor system was installed for durations between 55 and 673 days (mean 286 days). The ``home`` file contains the following fields:

| Field  | Description |
|------------|--------------------------------|
| homeid | Numeric home identifier (globally unique)
| install_type | Type of install: ```standard``` or ```enhanced``` 
| location | e.g. ```Edinburgh``` (links to location table)
| residents  | Number of residents at install time (or 0 for missing data\*)
| starttime  | Date / time of standard install
| starttime_enhanced | Date / time of enhanced install (or NULL)
| endtime  | End date of home's participation in the project, or 30 June 2018 (no data in this data release after this point)
| cohortid | Study group of the home. Format is ```[study_class]_[date]``` where ```[study_class]``` is as in the field below, and ```[date]``` is date of allocation to that study class.
| income_band  | Household gross income band (explanation below)
| study_class  | ```control```, ```treatment```, ```enhanced```: home was in the control or treatment group of the randomised controlled trial, or in the group that received an enhanced installation, which did not participate in the RCT.
| hometype | ```house_or_bungalow```, ```flat```
| equivalised_income | ```above_median```, ```below_median```, ```missing``` (explanation below)
| occupancy  | ```single```, ```multiple```, ```missing```
| urban_rural_class | 2016 Scottish Government Urban Rural Classification value, 8-fold. Values ```1``` to ```8```. See below
| urban_rural_name  | 2016 Scottish Government Urban Rural Classification name. See below.
| build_era | Banded period of building construction
| new_build_year | Year of construction for buildings constructed in 2002 or later
| smart_monitors | Whether household has existing smart monitors. ```Own and use```,```Own but don't use```,```Don't own```,```missing```
| smart_automation | Whether household has existing smart automation equipment. ```Own and use```,```Own but don't use```,```Don't own```,```missing```
| occupied_days | Number of days home is typically occupied during the day. ```0``` to ```7```
| occupied_nights | Number of days home is typically occupied during the night. ```0``` to ```7```
| entry_floor | Floor on which home's entry door is located, UK numbering system, e.g. ```Ground```,```1st```,```2nd``` 
| outdoor_space | Whether household has access to privately-owned outdoor space. ```Yes - private```,```Yes - shared with neighbours```,```No```
| outdoor_drying | Whether household has option to dry clothes outdoors. ```Yes```,```No```,```Don't know```,```missing```

\* Five homes had missing occupant data following the installation visit survey where this data is collected. Given the likely importance of this variable for analyses, the primary participants of these homes were subsequently individually contacted to request this information. Home 187 responded, so this data is included in the data release.

### Household income

#### Gross household income

Household gross (pre-tax) income bands were reported by the primary participant during the installation visit and mid-point surveys. Abridged values are provided in the home and survey_responses tables respectively. For ease of reading, these tables present only the annualised figures - participants were also shown monthly and (in the initial survey) weekly equivalents. In the data release, the lowest and highest income bands have been collapsed to improve anonymisation. See the Overview documentation for a full description of the income band variables.

#### Equivalised household income

The home's equivalised income was calculated approximately into above and below national median equivalised income, to enable quota monitoring during participant recruitment and allocation to control and treatment groups for standard participants. Equivalised incomes was calculated as being equal to their total gross income divided by an equivalence scale:
* Gross income: as we asked income bands, we assumed a homes' gross income is the mid-point between the annual upper and lower bounds of the band they self-report as being in during the installation visit survey.
* We calculate an approximation of the modified OECD equivalence scale developed by Hagenaars, de Vos and Zaidi (1994). 'Under this scale, household income is divided by an “equivalence factor”, which is the sum of the values from the following: the first adult in the household has a value of 1; subsequent adults (aged 14 or over) have a value of 0.5; children (13 and under) have a value of 0.3.'. We take occupant numbers and their ages from the installation visit survey. As our survey age bands for occupants are five-yearly, occupants aged 10-14 (and below) are counted as children, and 15-19 (and above) are counted as adults.
* Median income: household median income was then compared to a measure of UK median individual gross income to determine if they are above or below it. The measure was [from the gov.uk website, Feb 2017](https://www.gov.uk/government/statistics/percentile-points-from-1-to-99-for-total-income-before-and-after-tax), which gives percentile individual incomes for taxpayers; the most recent data was for 2013-14. The 50th percentile pre-tax income for 2013-14 was £21,900 according to this source.

There are ten homes in the release set for which there is no income band information and 4 homes for which there is no occupancy information. For these, the ```equivalised_income``` field could therefore not be calculated and is marked ```missing```.

Reference: Hagenaars, A. J. M., K. de Vos, and M. A. Zaidi. 1994. *Poverty statistics in the late 1980s: Research based on micro-data.* Luxembourg: Office for Official Publications of the European Communities.

### Scottish Government Urban Rural Classification, 8-fold

This is a geographic classification describing urban and rural areas based on settlement size and drive times, as described below.

These were looked up from postcodes of participating households from the publically available lookup table references below.

| Class | Class Name | Description
|---|-------|-------------------
| 1 | Large Urban Areas | Settlements of 125,000 people and over.
| 2 | Other Urban Areas | Settlements of 10,000 to 124,999 people.
| 3 | Accessible Small Towns | Settlements of 3,000 to 9,999 people, and within a 30 minute drive time of a Settlement of 10,000 or more.
| 4 | Remote Small Towns | Settlements of 3,000 to 9,999 people, and with a drive time of over 30 minutes but less than or equal to 60 minutes to a Settlement of 10,000 or more.
| 5 | Very Remote Small Towns | Settlements of 3,000 to 9,999 people, and with a drive time of over 60 minutes to a Settlement of 10,000 or more.
| 6 | Accessible Rural Areas | Areas with a population of less than 3,000 people, and within a drive time of 30 minutes to a Settlement of 10,000 or more.
| 7 | Remote Rural Areas | Areas with a population of less than 3,000 people, and with a drive time of over 30 minutes but less than or equal to 60 minutes to a Settlement of 10,000 or more.
| 8 | Very Remote Rural Areas | Areas with a population of less than 3,000 people, and with a drive time of over 60 minutes to a Settlement of 10,000 or more.

References:

* Scottish Government Geographic Information Science & Analysis Team, Rural and Environment Science and Analytical Services Division, 2018. *Scottish Government Urban Rural Classification 2016.* URL: https://www2.gov.scot/Resource/0054/00542959.pdf. Accessed 26 February 2020.

* Scottish Government, 10 Jan 2019. Scottish Government Urban Rural Classification 2016 - Postcode Lookup (https://www2.gov.scot/Resource/0054/00544931.csv). Available via: https://www2.gov.scot/Publications/2018/03/6040/downloads. Accessed 26 February 2020. 

## Metadata: person

A ``person`` is a study participant described by the following fields:

| Field | Description
|---------|-----------------------------|
| personid  | Numeric person identifier (globally unique)
| homeid  | Link to home table
| primaryparticipant  | Boolean field - True (```1```) if this is the primary study participant (the person who completed the initial survey during the system installation visit)
| relationtoprimary | Person's relation to the primary participant (or null, for primary participant or if not reported)
| gender  | ```male```, ```female``` or null if not reported
| ageband | Age at install. 5-year windows, e.g. ```35-39```. Null if not reported
| workingstatus | Working status, e.g. ```Paid work```, ```Retired```, etc.
| weeklyhoursofwork | Working hours, in 10-hour bands, e.g. ```31-40```. Null if not working or not reported
| education | Highest educational level, e.g. ```Degree level qualification```. Null if not reported
| ageleavingeducation | Age leaving full time education. Null if not reported
| signedup  | Boolean field - True (```1```) if this participant was the initial contact who signed up to join the project (usually, but not always, the primary participant)
| startdate | Date that the participant was reported to the project (usually during installation visit or the second primary participant survey, if new occupants joined participating homes partway through the project)
| highest_earner | Boolean - True (```1```) if this participant is reported to be the household's highest income earner

## Metadata: room

| Field | Description |
|---------|--------------------------|
| roomid  | Numeric room identifier (globally unique)
| homeid  | Link to home table
| type  | Room type: ```bathroom, kitchen, bedroom, study, hall, livingroom, diningroom, utility, cupboard, playroom, conservatory, outside, kitchenliving, other```
| secondarytype | Secondary room type (or empty string)
| storey  | Storey, where ```0``` is ground floor, etc.
| externalwindows | ```1``` (true) if room has external windows
| externaldoors | ```1``` (true) if room has external doors
| externalwalls | Number of external walls
| floorarea | Room floor area in tenths of meters squared
| height  | Room height in centimeters (approximate mean if height varies)
| radiators | ```1```  (true) if room has one or more radiators
| trvs  | Do radiators have thermostatic valves: ```All, None, Some``` (or null)
| clothesdrying | If room used for drying clothes: ```never, sometimes, often, unknown```
| windowsopen | ```1```  (true) if room has openable windows
| thermostat  | ```1```  (true) if room contains the main central heating thermostat
| othertype | Further details of room use (free string)
| stairup | ```1```  (true) if stairs lead up from this room
| stairupdoor | ```1```  (true) if stairs leading up have a door that can be closed
| stairdown | ```1```  (true) if stairs lead down from this room
| stairdowndoor | ```1```  (true) if stairs leading down have a door that can be closed
| mezzanine | ```1```  (true) if the room has a mezzanine level

## Metadata: sensorbox

Each ``sensorbox`` does not send data directly but instead may contain multiple sensors. The type of the sensorbox will determine which sensors occur.

| Field | Description
|-----------|----------------------|
| sensorboxid | Numeric sensorbox identifier (globally unique)
| local_id  | Identifier within the home
| roomid  | Link to room table
| status  | ```active, offline, faulty```
| sensorbox_type  | ```room, clamp, electric, gas, relay, plug_monitor, subcircuit_monitor```
| notes | Notes about this sensorbox
| heightfromfloor | Height in centimetres of the sensorbox
| name  | Detail about what type of appliance this sensorbox is detecting (for sensobox_type ```plug_monitor```)
| onMainThermostat  | ```1```  (true) if the sensorbox is next to the main home thermostat
| temperatureInaccuracy | ```1```  (true) if the sensorbox may report inaccurate temperature due to its positioning
| humidityInaccuracy  | ```1```  (true) if the sensorbox may report inaccurate humidity due to its positioning
| lightInaccuracy | ```1```  (true) if the sensorbox may report inaccurate light due to its positioning
| install_type  | Type of install: ```standard, enhanced```
| currentrange  | For electricity sensors (sensorbox_type ```electric```, the maximum calibrated accuracy of the clamp: ```30A, 100A, LED```)
| clamp1pipe  | For sensor-type ```clamp```, the type of pipe to which clamp 1 is attached. ```Hot, Cold, CH Flow, CH Return, RadiatorInput, RadiatorOutput, Sink, Bath, Shower, Oven```. The first four are boiler sensors from the standard install indicating hot water outflow to taps etc., cold water inflow for the hot water, and central heating pipes out to radiators and returning from radiators, respectively; the others are present in enhanced installs only
| clamp2pipe  | The type of pipe to which clamp 2 is attached. Values as for ```clamp1pipe```
| gasblock  | For sensor-type ```gas```, the type of connector used (which is determined by the meter model): ```White, IN-Z61, Direct, Rectangular, Square```
| installtime | time at which the sensorbox was installed in seconds since _January 1, 1970_ (midnight UTC/GMT) (or 0 for sensor_type `plug_monitor`)
| applianceid | For sensorboxes monitoring a single appliance, link to the appliance table (or ```0```)
| hasTRV  | For radiator sensors only - ```1``` (true) if the radiator has a TRV
| clamp1detail  | For enhanced clamp sensors - detail of placement of clamp 1. ```hot tap, under sink, under bath, other```
| clamp2detail  | For enhanced clamp sensors - detail of placement of clamp 2. Values as for clamp1detail
| oven  | For enhanced over sensors - detail of placement. ```door, side, other```
| function  | For enhanced sensorboxes - sensorbox function: ```Radiator, Heater, PipeClamp, HeatCook, Oven, Relay```

## Metadata: sensor

A ``sensor`` is a data source for a single type of data, and always belongs to a particular sensorbox.

| Field | Description
|--------|----------------------|
| sensorid  | Numeric sensor identifier (globally unique)
| sensorboxid | Link to sensorbox table
| type  | ```temperature, clamp_temperature, humidity, light, gas, electric, electric_socket, electric_pulse, power, battery```
| unit  | Unit of measurement of data in ```reading``` table (see sensor data release)
| status  | ```active, offline, faulty```
| roomid  | Link to room table
| subcircuit_type | Only for sensors in ```subcircuit_monitor``` sensorboxes, this describes the individual subcircuit monitored
| offset  | Offset used when converting raw data to reading data
| scalingfactor | Scaling factor used when converting raw data to reading data
| rawunit | Raw unit of measurement of sensor. Only used for electric sensors
| counter | Count to distinguish multiple sensors of the same type in the same sensor box

## Metadata: appliance

Large, high-power and generally fixed or rarely moved appliances within the home. Data collected by the IDEAL project technician during the installation visit. 

| Field  | Description
|--------|-------------------|
| applianceid  | Numeric appliance identifier (globally unique)
| homeid | Link to home table
| roomid | Link to room table
| applianceclass | Type of application of appliance: ```heating``` for space heating, ```water``` for water heating, ```food``` for food and drink storage and preparation, ```other```
| powertype  | ```gas, electric, other_fuel```
| appliancetype  | ```gasfire, electricheater, fridge, freezer, fridgefreezer, gashob, electrichob, gasoven, electricoven, grill, toaster, woodburningstove, microwave, shower, electricshower, bath, washingmachine, tumbledrier, washingmachinetumbledrier, dishwasher, sink, kettle, dehumidifier, vacuumcleaner, other```
| appliancesubtype | Free text field for extra information about appliance
| number | Quantity of this appliance type

## Metadata: other_appliance

Other potentially high-power or significant energy-using appliances and equipment that are not covered in the appliance table. These may be portable but potentially high-power appliances within the home, outdoor appliances, or motor vehicles. Normally low-power appliances are not recorded. Data provided by the primary participant during the installation visit.

| Field  | Description
|--------|-------------------|
| otherapplianceid  | Numeric 'other appliance' identifier (globally unique)
| homeid | Link to home table
| appliancename | ```air_conditioning, computer, dehumidifier, electric_blanket, electric_fan, electric_heater, gas_heater, humidifier, iron, laptop, media_entertainment, motor_vehicle, non_smart_phone, outdoor_elec_space_heater, outdoor_gas_space_heater, outdoor_hot_tub, outdoor_light, outdoor_water_feature, smartphone, sound_system, tablet, television, vacuum_cleaner, other_high_power_1, other_high_power_2, other_high_power_3, other_high_power_4```
| number | Quantity of this appliance type

## Metadata: meterreading

Meter readings for home electricity and gas meters.

| Field  | Description
|-------|------------------|
| homeid | Link to home table
| date | Date reading provided
| provenance | Person who provided the meter reading. Either ```technician``` (an IDEAL project technician) or ```[personid]``` - a participant (link to person table)
| provenancedetail | How the data were collected and provided. For readings by technicians, either ```installation_visit``` or ```repair_visit```. For readings by participants, the survey or data collection channel - ```all_inapp_meters_mid``` or ```all_web_end```
| energytype | ```electricity, gas```
| reading | The meter reading provided

## Metadata: tariff

Tariffs for home electricity and gas supply.

| Field  | Description
|-----------|------------------|
| homeid | Link to home table
| notification_date | Date tariff details provided by a participant
| provenancedetail | How the data were collected and provided. Either ```primary_facetoface_initial``` - via the installation visit survey, or ```in_app``` - via the dedicated interface in the IDEAL app. Note that after 9 March 2017,  collection of tariff details during the installation visit was moved from the survey to the IDEAL app.
| energytype | ```electricity, gas```
| daily_standing_charge_pence | Standing charge per day, in pence, inclusive of VAT
| unit_charge_pence_per_kwh | Charge per kWh, in pence, inclusive of VAT

## Metadata: weatherfeed

Metadata about weather feeds. Weather readings are in the sensor data release.

| Field  | Description
|-------|------------------|
| feedid | Numeric feed identifier (globally unique)
| weather_type | ```temperature, humidity, winddirection, windspeed, conditions```
| locationid | Same ID set as used in home (and location) table
| unit | Unit of data in the feed
| source | Source of feed
| url  | URL of feed

## Metadata: location

Location is used in the ```home``` and ```weatherreading``` tables. 

| Field  | Description
|-------|------------------|
| locationid | Link to ```location``` in the home, and ```locationid``` in the forecast and weatherreading tables
| weather_centre | The town / city from which weather readings are taken

# Sensor data: Introduction

Sensor data is divided into one compressed CSV file per sensor. All timestamps are in UTC (Coordinated Universal Time). The file-naming convention is designed to be human readable:
> *home*```homeid```\_*roomtype*```roomid```\_*sensor*```sensorid```\_*sensorbox-type*\_*sensor-type*.csv.gz

* *home* is the string "home"
* ```homeid``` is the numeric ID of the home
* *roomtype* is one of  *bathroom*, *bedroom*, *conservatory*, *cupboard*, *diningroom*, *hall*, *kitchen*, *kitchenliving*, *livingroom*, *other*, *outside*, *playroom*, *study*, *utility*
* ```roomid``` is the numeric ID of the room. There can be multiple rooms of the same type in each house
* *sensor* is the string "sensor"
* ```sensorid``` is the numeric ID of the sensor or sensors.
*  *sensorbox-type* describes the function of the sensorbox. This is one of *electric-appliance*, *electric-mains*, *electric-subcircuit*, *gas-pulse*, *heatcook*, *heater*, *room*, *tempprobe*
* *sensor-type* describes the function of the sensor (sometimes you need to interpret using the sensorbox-type). For standard homes tempprobe sensorboxes are divided into: *central-heating-flow*, *central-heating-return*, *hot-water-cold-pipe*, *hot-water-hot-pipe*; room sensorboxes have *humidity*, *light* and *temperature* sensors; electric-mains sensorboxes have *electric-combined* sensors (*combined* indicating the readings from the 30A and 100A current clamps are amalgamated); gas-pulse sensorboxes have *gas* sensors. Enhanced homes add: further tempprobe sensors for radiators etc.; electric-appliance sensorboxes with the appliance type as the sensor-type; electric-subcircuit sensorboxes with the name of the subcircuit as the sensor-type.


## Sensor data file naming examples  

* home251_hall2321_sensor15042_gas-pulse_gas.csv
* home99_outside1027_sensor4385c4390_electric-mains_electric-combined.csv.gz
* home287_hall2672_sensor18505_tempprobe_central-heating-flow.csv
* home287_hall2672_sensor18504_tempprobe_central-heating-return.csv
* home287_hall2672_sensor18512_tempprobe_hot-water-hot-pipe.csv
* home287_hall2672_sensor18511_tempprobe_hot-water-cold-pipe.csv
* home86_study932_sensor3502_room_light.csv
* home86_study932_sensor3503_room_humidity.csv
* home86_study932_sensor3504_room_temperature.csv
  

## Sensor data file naming examples (enhanced)

* home96_kitchen999_sensor9110_electric-appliance_kettle.csv
* home208_utility2644_sensor17997_electric-subcircuit_mains.csv
* home208_utility2644_sensor17998_electric-subcircuit_shower.csv
* home90_kitchen957_sensor4818_heatcook_temperature.csv
* home99_livingroom1029_sensor4394_heater_temperature.csv
* home231_hall2140_sensor18842_tempprobe_radiator-input.csv
* home231_hall2140_sensor18841_tempprobe_radiator-output.csv
* home140_kitchen1317_sensor10447_tempprobe_sink.csv
* home242_bathroom2258_sensor18814_tempprobe_bath.csv

## Sensor data: sensor reading file content

The metadata specifies units for each individual sensor but for reference:
 * all temperatures (clamp and ambient) are in tenths of degrees Celsius; 12-second data
 * humidity values are in tenths of percent relative humidity; 12-second data
* light values do not have calibrated units; 12-second data
* electric-mains and electric-combined readings are in Watts; 1-second data
* electric-subcircuit readings are in Watts; 5-second data
* gas values are in Watt hours; variable-rate, maximum one reading per gas pulse
* electric-appliance readings are in Watts; variable-rate, reading on change (or approx every hour)

The sensor reading files have this structure:

| Field  | Description |
|-------|----------------|
| timestamp| time of reading in UTC 'YYYY-MM-DD hh:mm:ss' |
| value  | Value of reading; for units see metadata |


## Sensor data: sensor content example

home126_hall1183_sensor5718c5722_electric-mains_electric-combined.csv.gz extracted content:

* 2017-06-15 09:21:45,267
* 2017-06-15 09:21:46,272
* 2017-06-15 09:21:47,2026
* 2017-06-15 09:21:48,1958
* 2017-06-15 09:21:49,1931
* ...
* 2017-06-15 09:21:58,1909
* 2017-06-15 09:21:59,1909
* 2017-06-15 09:22:00,272
* 2017-06-15 09:22:01,272

## Sensor data: weather reading

The metadata release specifies locations, units and description for weather feeds. For each of five locations we record 15 minute data for temperature (0.1C), humidity (0.1%), wind speed (0.1kph), wind direction (16 divisions of the compass using the standard strings *N*, *NNE*, *NE* etc.) and overall weather conditions in short strings like *Mostly Cloudy*.

Note that wind speed readings of '0' indicate speeds of <1kph.

| Field  | Description |
|----------|-------------------|
| feedid | Link to the weatherfeed table for full metadata |
| time | Time of reading in UTC 'YYYY-MM-DD hh:mm:ss' |
| value  | Value of weather reading |

## Auxiliary Sensor Data
There are several types of data that were collected but are not considered primary. Some of these are gathered together in the *auxiliary* data download:

 - **Anomalous readings** - IDEAL sensor readings that were marked as  anomalous, for example relative humidity sensor readings below 1% or above 110%, or ambient room temperatures greater than 60 degrees Celsius.
 -  **Battery readings** - each IDEAL sensorbox reports 2 battery readings for every 300 'normal' readings. This means that almost all sensors will report battery status every hour, but mains current clamp sensors report every 5 minutes. The battery readings (*battery1* and *battery2*) are taken immediately before and after a standard reading is taken by the the sensorbox. This provides a delta which may be instructive as to the state of the battery. Battery values are not calibrated against any standard measure, but a fresh lithium battery will report values around 1000 and a fresh alkaline battery will report around 910. Standard alkaline batteries are installed in IDEAL sensors that only measure ambient humidity, temperature and light; all other IDEAL sensors contain lithium batteries.
 - **Hourly summary readings** IDEAL sensor data at an hourly resolution. These are provided for convenience of analysis. Note that these are calculated based on the mean of the available readings, and as such, in cases where there are substantial data gaps, may not be the most accurate estimates of actual figures achievable. These summary figures are not provided for electric appliance data or electrical subcircuit readings.
 - **Hourly propagation data** For each IDEAL sensor, this indicates the number of readings received and stored in the database as a percentage of the number expected, at an hourly resolution. Note that for the gas sensor, which only provides readings when a pulse is produced by the meter, propagation is an estimate, based on the data being received by the ambient temperature sensor in the same sensorbox.
 - **Room-level light readings** Each room sensorbox that records temperature and humidity, also records an ambient light level. These are included as *auxiliary* data because the values are uncalibrated. 
 - **Weather forecast data** The main dataset contains measured weather data from 5 locations in the vicinity of the installed homes. Forecast data was also recorded to be presented on the user-facing GUI. It is included here for completeness.

Note that for anomalous data, hourly summary data, and associated battery data, readings are reported for two separate electric mains sensors in each home: one is a 30A current clamp and the other a 100A clamp. Within the main release, the readings from these two sensors have been combined into a single 1-second data stream.

## Sensor data: known issues

 - All sensor data in the hour between 08:50 and 09:50 on 17th April 2018 should be considered unreliable. Due to a server error, too many data points are recorded during this time.
 - Home 223 has no released electric mains data as both mains sensors reported very unreliably due to properties of the home.

## Sensor data: missing gas data

Gas sensors report a timestamped reading whenever a pulse is produced by the gas meter. Gas sensors report a cumulative pulse count from the date of installation; the base station then calculates the number of pulses since the last reading it received, and sends that value to the server to store in the database. This means that even if propagation from the sensor to the base station fails for a period of time, when the sensorbox re-connects the total number of pulses recorded during the gap is correctly calculated by the base station and sent to the database, retaining the accuracy of the cumulative total. Gas data are still lost however if the sensor box, whole home system or whole IDEAL system are not functioning for a period. Large gaps in the gas data can therefore be due to no or very low gas use, or missing gas data. The end user can distinguish periods of lost gas data from periods of low use by making use of the hourly sensor propagation data available in the auxiliary dataset. These figures indicate the amount of data received from a sensor for a given hour as a proportion of the amount of data points that would be expected. If a home's propagation from all sensors for an hour is zero, then gas data from that hour are very likely to have been lost - this is most likely due to the home's system or entire IDEAL system having a fault. If a gas sensor's propagation for an hour is zero, this could also indicate gas data were lost, due to a gas sensor fault. This is a more approximate indicator, as it could be due to poor propagation. Periods of many hours are increasingly likely to be due to a gas sensor fault, particularly if the next reading recorded is a single pulse rather than large value. 

# Survey data: participant responses

Survey data were collected from participants at several times during the study.  Survey responses relating to certain 'objective' data, such as properties of the home or appliances, or participants' ages, working statuses, etc. are presented in the metadata tables, described earlier, as most appropriate.  

All remaining survey responses are presented in the ```survey_responses``` and ```survey_responses_numeric``` tables. These are identical except in the latter, the Likert values have been converted to a purely numeric form for ease of use. These tables contain one row per personid in the data release, and fields as described below: 

| Field  | Description |
|--------------|---------------------|
| personid | Link to person table. |
| homeid  | Link to home table. |
| primary_facetoface_initial, all_inapp_initial, primary_web_mid, all_inapp_mid, all_web_end | Datetime columns showing when the last survey response was submitted by the participant for each of the five surveys included in this data release. null indicates no response, either because the participant was not asked to complete that survey, or becasuse they opted not to. See the Overview document for information about which participants were inviated to complete each survey. Note that all surveys could be completed by respondents over multiple sessions.
| [```uniquequestionid```] | The remaining fields/columns present participants' responses, with one field for each ```uniquequestionid``` in the data release. Data in any given field depend on the the survey question, and are either: one of the response options available for that question; a numeric value; or a Boolean (True or False). Fields for personids who did not respond to a given question are marked null. A small number of ```uniquequestionid```s are omitted from the data release where there were no responses, or, to protect anonymity, where there were only very few responses. 

Further details about the surveys themselves, including the survey timings, recipients, and where to find the wording of questions and response options for each ```uniquequestionid```, are described in the document "Overview of the IDEAL Home Energy Project and Dataset" accompanying this data release. 


