import wmi
w_temp = wmi.WMI(namespace="root\\wmi")
print((w_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0)-273.15)