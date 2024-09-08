## Outlook
This is the codebase for the implementation of LocateMe. It uses the wifi RSSI data of different APs available in one of the floors. 

`iwlist` command is used to display some additional information from a wireless network interface. 

The output of this command was parsed using `grep` and `awk`.

Then, data cleaning was done, followed by applying the `K-Nearest Neighbors` algorithm for classification. 

A total of 6 distinct locations were chosen to be identified by the Raspberry Pi running this model.

## Issues
- [ ] Python library version incompatibility for scikit-learn in the RPI 
