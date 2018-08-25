EESchema Schematic File Version 4
LIBS:sensorBoard-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Amplifier_Operational:LM358 U1
U 1 1 5B781B27
P 1650 900
F 0 "U1" H 1650 1267 50  0000 C CNN
F 1 "LM358" H 1650 1176 50  0000 C CNN
F 2 "" H 1650 900 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 1650 900 50  0001 C CNN
	1    1650 900 
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U1
U 3 1 5B781C5D
P 1650 900
F 0 "U1" H 1608 946 50  0000 L CNN
F 1 "LM358" H 1608 855 50  0000 L CNN
F 2 "" H 1650 900 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 1650 900 50  0001 C CNN
	3    1650 900 
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U1
U 2 1 5B781CF1
P 1650 1600
F 0 "U1" H 1650 1967 50  0000 C CNN
F 1 "LM358" H 1650 1876 50  0000 C CNN
F 2 "" H 1650 1600 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 1650 1600 50  0001 C CNN
	2    1650 1600
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U2
U 1 1 5B781DF1
P 1650 2250
F 0 "U2" H 1650 2617 50  0000 C CNN
F 1 "LM358" H 1650 2526 50  0000 C CNN
F 2 "" H 1650 2250 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 1650 2250 50  0001 C CNN
	1    1650 2250
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U2
U 3 1 5B781DF8
P 1650 2250
F 0 "U2" H 1608 2296 50  0000 L CNN
F 1 "LM358" H 1608 2205 50  0000 L CNN
F 2 "" H 1650 2250 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 1650 2250 50  0001 C CNN
	3    1650 2250
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U2
U 2 1 5B781DFF
P 1650 2950
F 0 "U2" H 1650 3317 50  0000 C CNN
F 1 "LM358" H 1650 3226 50  0000 C CNN
F 2 "" H 1650 2950 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 1650 2950 50  0001 C CNN
	2    1650 2950
	1    0    0    -1  
$EndComp
$Comp
L LED:IR204A D1
U 1 1 5B784770
P 1050 1000
F 0 "D1" H 1000 785 50  0000 C CNN
F 1 "IR204A" H 1000 876 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 1050 1175 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 1000 1000 50  0001 C CNN
	1    1050 1000
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D2
U 1 1 5B785837
P 1050 1700
F 0 "D2" H 1000 1485 50  0000 C CNN
F 1 "IR204A" H 1000 1576 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 1050 1875 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 1000 1700 50  0001 C CNN
	1    1050 1700
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D3
U 1 1 5B78588D
P 1050 2350
F 0 "D3" H 1000 2135 50  0000 C CNN
F 1 "IR204A" H 1000 2226 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 1050 2525 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 1000 2350 50  0001 C CNN
	1    1050 2350
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D4
U 1 1 5B785DFC
P 1050 3050
F 0 "D4" H 1000 2835 50  0000 C CNN
F 1 "IR204A" H 1000 2926 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 1050 3225 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 1000 3050 50  0001 C CNN
	1    1050 3050
	-1   0    0    1   
$EndComp
$Comp
L Analog_ADC:ADS1015IDGS U5
U 1 1 5B789BCA
P 3150 1250
F 0 "U5" H 3150 1928 50  0000 C CNN
F 1 "ADS1015IDGS" H 3150 1837 50  0000 C CNN
F 2 "Package_SO:TSSOP-10_3x3mm_P0.5mm" H 3150 750 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/ads1015.pdf" H 3100 350 50  0001 C CNN
	1    3150 1250
	1    0    0    -1  
$EndComp
Wire Wire Line
	1350 800  550  800 
Wire Wire Line
	550  800  550  1000
Wire Wire Line
	1350 1500 550  1500
Connection ~ 550  1500
Wire Wire Line
	550  1500 550  1700
Wire Wire Line
	950  1000 550  1000
Connection ~ 550  1000
Wire Wire Line
	550  1000 550  1200
Wire Wire Line
	1350 1700 1250 1700
Wire Wire Line
	950  1700 550  1700
Wire Wire Line
	1250 1000 1350 1000
Wire Wire Line
	1950 900  2650 900 
Wire Wire Line
	2650 900  2650 1150
Wire Wire Line
	2650 1150 2750 1150
Wire Wire Line
	1950 1600 1950 1000
Wire Wire Line
	1950 1000 2500 1000
Wire Wire Line
	2500 1000 2500 1250
Wire Wire Line
	2500 1250 2750 1250
Wire Wire Line
	1550 600  3150 600 
Wire Wire Line
	3150 750  3150 600 
Connection ~ 3150 600 
Wire Wire Line
	3150 600  4250 600 
Wire Wire Line
	3150 1650 3150 1800
Wire Wire Line
	3150 1900 550  1900
Wire Wire Line
	550  1900 550  1700
Connection ~ 550  1700
Wire Wire Line
	1550 1200 550  1200
Connection ~ 550  1200
Wire Wire Line
	550  1200 550  1500
Wire Wire Line
	1550 1950 4250 1950
Wire Wire Line
	4250 600  4250 1950
Wire Wire Line
	550  1900 550  2150
Wire Wire Line
	550  2550 1550 2550
Connection ~ 550  1900
Wire Wire Line
	1350 2350 1250 2350
Wire Wire Line
	950  2350 550  2350
Connection ~ 550  2350
Wire Wire Line
	550  2350 550  2550
Wire Wire Line
	1950 2250 2100 2250
Wire Wire Line
	2100 2250 2100 1350
Wire Wire Line
	2100 1350 2750 1350
Wire Wire Line
	1350 2150 550  2150
Connection ~ 550  2150
Wire Wire Line
	550  2150 550  2350
Wire Wire Line
	2250 2950 2250 1450
Wire Wire Line
	2250 1450 2750 1450
Wire Wire Line
	1350 3050 1250 3050
Wire Wire Line
	1350 2850 550  2850
Wire Wire Line
	550  2850 550  2550
Connection ~ 550  2550
Wire Wire Line
	550  2850 550  3050
Wire Wire Line
	550  3050 950  3050
Connection ~ 550  2850
Wire Wire Line
	1950 2950 2250 2950
$Comp
L Amplifier_Operational:LM358 U3
U 1 1 5B79FB07
P 1700 3750
F 0 "U3" H 1700 4117 50  0000 C CNN
F 1 "LM358" H 1700 4026 50  0000 C CNN
F 2 "" H 1700 3750 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 1700 3750 50  0001 C CNN
	1    1700 3750
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U3
U 3 1 5B79FB0E
P 1700 3750
F 0 "U3" H 1658 3796 50  0000 L CNN
F 1 "LM358" H 1658 3705 50  0000 L CNN
F 2 "" H 1700 3750 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 1700 3750 50  0001 C CNN
	3    1700 3750
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U3
U 2 1 5B79FB15
P 1700 4450
F 0 "U3" H 1700 4817 50  0000 C CNN
F 1 "LM358" H 1700 4726 50  0000 C CNN
F 2 "" H 1700 4450 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 1700 4450 50  0001 C CNN
	2    1700 4450
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U4
U 1 1 5B79FB1C
P 1700 5100
F 0 "U4" H 1700 5467 50  0000 C CNN
F 1 "LM358" H 1700 5376 50  0000 C CNN
F 2 "" H 1700 5100 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 1700 5100 50  0001 C CNN
	1    1700 5100
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U4
U 3 1 5B79FB23
P 1700 5100
F 0 "U4" H 1658 5146 50  0000 L CNN
F 1 "LM358" H 1658 5055 50  0000 L CNN
F 2 "" H 1700 5100 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 1700 5100 50  0001 C CNN
	3    1700 5100
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U4
U 2 1 5B79FB2A
P 1700 5800
F 0 "U4" H 1700 6167 50  0000 C CNN
F 1 "LM358" H 1700 6076 50  0000 C CNN
F 2 "" H 1700 5800 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 1700 5800 50  0001 C CNN
	2    1700 5800
	1    0    0    -1  
$EndComp
$Comp
L LED:IR204A D5
U 1 1 5B79FB31
P 1100 3850
F 0 "D5" H 1050 3635 50  0000 C CNN
F 1 "IR204A" H 1050 3726 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 1100 4025 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 1050 3850 50  0001 C CNN
	1    1100 3850
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D6
U 1 1 5B79FB38
P 1100 4550
F 0 "D6" H 1050 4335 50  0000 C CNN
F 1 "IR204A" H 1050 4426 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 1100 4725 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 1050 4550 50  0001 C CNN
	1    1100 4550
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D7
U 1 1 5B79FB3F
P 1100 5200
F 0 "D7" H 1050 4985 50  0000 C CNN
F 1 "IR204A" H 1050 5076 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 1100 5375 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 1050 5200 50  0001 C CNN
	1    1100 5200
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D8
U 1 1 5B79FB46
P 1100 5900
F 0 "D8" H 1050 5685 50  0000 C CNN
F 1 "IR204A" H 1050 5776 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 1100 6075 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 1050 5900 50  0001 C CNN
	1    1100 5900
	-1   0    0    1   
$EndComp
$Comp
L Analog_ADC:ADS1015IDGS U6
U 1 1 5B79FB4D
P 3200 4100
F 0 "U6" H 3200 4778 50  0000 C CNN
F 1 "ADS1015IDGS" H 3200 4687 50  0000 C CNN
F 2 "Package_SO:TSSOP-10_3x3mm_P0.5mm" H 3200 3600 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/ads1015.pdf" H 3150 3200 50  0001 C CNN
	1    3200 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	600  3650 600  3850
Wire Wire Line
	1400 4350 600  4350
Connection ~ 600  4350
Wire Wire Line
	600  4350 600  4550
Wire Wire Line
	1000 3850 600  3850
Connection ~ 600  3850
Wire Wire Line
	600  3850 600  4050
Wire Wire Line
	1400 4550 1300 4550
Wire Wire Line
	1000 4550 600  4550
Wire Wire Line
	1300 3850 1400 3850
Wire Wire Line
	2000 3750 2700 3750
Wire Wire Line
	2700 3750 2700 4000
Wire Wire Line
	2700 4000 2800 4000
Wire Wire Line
	2000 4450 2000 3850
Wire Wire Line
	2000 3850 2550 3850
Wire Wire Line
	2550 3850 2550 4100
Wire Wire Line
	2550 4100 2800 4100
Wire Wire Line
	1600 3450 3200 3450
Wire Wire Line
	3200 3600 3200 3450
Connection ~ 3200 3450
Wire Wire Line
	3200 3450 3950 3450
Wire Wire Line
	3200 4500 3200 4750
Wire Wire Line
	3200 4750 600  4750
Wire Wire Line
	600  4750 600  4550
Connection ~ 600  4550
Wire Wire Line
	1600 4050 600  4050
Connection ~ 600  4050
Wire Wire Line
	600  4050 600  4350
Wire Wire Line
	1600 4800 4300 4800
Wire Wire Line
	4300 3450 4300 4800
Wire Wire Line
	600  4750 600  5000
Wire Wire Line
	600  5400 1600 5400
Connection ~ 600  4750
Wire Wire Line
	1400 5200 1300 5200
Wire Wire Line
	1000 5200 600  5200
Connection ~ 600  5200
Wire Wire Line
	600  5200 600  5400
Wire Wire Line
	2000 5100 2150 5100
Wire Wire Line
	2150 5100 2150 4200
Wire Wire Line
	2150 4200 2800 4200
Wire Wire Line
	1400 5000 600  5000
Connection ~ 600  5000
Wire Wire Line
	600  5000 600  5200
Wire Wire Line
	2300 5800 2300 4300
Wire Wire Line
	2300 4300 2800 4300
Wire Wire Line
	1400 5900 1300 5900
Wire Wire Line
	1400 5700 600  5700
Wire Wire Line
	600  5700 600  5400
Connection ~ 600  5400
Wire Wire Line
	600  5700 600  5900
Wire Wire Line
	600  5900 1000 5900
Connection ~ 600  5700
Wire Wire Line
	2000 5800 2300 5800
$Comp
L Amplifier_Operational:LM358 U7
U 1 1 5B7A2321
P 6950 900
F 0 "U7" H 6950 1267 50  0000 C CNN
F 1 "LM358" H 6950 1176 50  0000 C CNN
F 2 "" H 6950 900 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 6950 900 50  0001 C CNN
	1    6950 900 
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U7
U 3 1 5B7A2328
P 6950 900
F 0 "U7" H 6908 946 50  0000 L CNN
F 1 "LM358" H 6908 855 50  0000 L CNN
F 2 "" H 6950 900 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 6950 900 50  0001 C CNN
	3    6950 900 
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U7
U 2 1 5B7A232F
P 6950 1600
F 0 "U7" H 6950 1967 50  0000 C CNN
F 1 "LM358" H 6950 1876 50  0000 C CNN
F 2 "" H 6950 1600 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 6950 1600 50  0001 C CNN
	2    6950 1600
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U8
U 1 1 5B7A2336
P 6950 2250
F 0 "U8" H 6950 2617 50  0000 C CNN
F 1 "LM358" H 6950 2526 50  0000 C CNN
F 2 "" H 6950 2250 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 6950 2250 50  0001 C CNN
	1    6950 2250
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U8
U 3 1 5B7A233D
P 6950 2250
F 0 "U8" H 6908 2296 50  0000 L CNN
F 1 "LM358" H 6908 2205 50  0000 L CNN
F 2 "" H 6950 2250 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 6950 2250 50  0001 C CNN
	3    6950 2250
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U8
U 2 1 5B7A2344
P 6950 2950
F 0 "U8" H 6950 3317 50  0000 C CNN
F 1 "LM358" H 6950 3226 50  0000 C CNN
F 2 "" H 6950 2950 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 6950 2950 50  0001 C CNN
	2    6950 2950
	1    0    0    -1  
$EndComp
$Comp
L LED:IR204A D9
U 1 1 5B7A234B
P 6350 1000
F 0 "D9" H 6300 785 50  0000 C CNN
F 1 "IR204A" H 6300 876 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 6350 1175 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 6300 1000 50  0001 C CNN
	1    6350 1000
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D10
U 1 1 5B7A2352
P 6350 1700
F 0 "D10" H 6300 1485 50  0000 C CNN
F 1 "IR204A" H 6300 1576 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 6350 1875 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 6300 1700 50  0001 C CNN
	1    6350 1700
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D11
U 1 1 5B7A2359
P 6350 2350
F 0 "D11" H 6300 2135 50  0000 C CNN
F 1 "IR204A" H 6300 2226 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 6350 2525 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 6300 2350 50  0001 C CNN
	1    6350 2350
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D12
U 1 1 5B7A2360
P 6350 3050
F 0 "D12" H 6300 2835 50  0000 C CNN
F 1 "IR204A" H 6300 2926 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 6350 3225 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 6300 3050 50  0001 C CNN
	1    6350 3050
	-1   0    0    1   
$EndComp
$Comp
L Analog_ADC:ADS1015IDGS U11
U 1 1 5B7A2367
P 8450 1250
F 0 "U11" H 8450 1928 50  0000 C CNN
F 1 "ADS1015IDGS" H 8450 1837 50  0000 C CNN
F 2 "Package_SO:TSSOP-10_3x3mm_P0.5mm" H 8450 750 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/ads1015.pdf" H 8400 350 50  0001 C CNN
	1    8450 1250
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 800  5850 800 
Wire Wire Line
	5850 800  5850 1000
Wire Wire Line
	6650 1500 5850 1500
Connection ~ 5850 1500
Wire Wire Line
	5850 1500 5850 1700
Wire Wire Line
	6250 1000 5850 1000
Connection ~ 5850 1000
Wire Wire Line
	5850 1000 5850 1200
Wire Wire Line
	6650 1700 6550 1700
Wire Wire Line
	6250 1700 5850 1700
Wire Wire Line
	6550 1000 6650 1000
Wire Wire Line
	7250 900  7950 900 
Wire Wire Line
	7950 900  7950 1150
Wire Wire Line
	7950 1150 8050 1150
Wire Wire Line
	7250 1600 7250 1000
Wire Wire Line
	7250 1000 7800 1000
Wire Wire Line
	7800 1000 7800 1250
Wire Wire Line
	7800 1250 8050 1250
Wire Wire Line
	6850 600  8450 600 
Wire Wire Line
	8450 750  8450 600 
Connection ~ 8450 600 
Wire Wire Line
	8450 600  9550 600 
Wire Wire Line
	8450 1650 8450 1900
Wire Wire Line
	8450 1900 5850 1900
Wire Wire Line
	5850 1900 5850 1700
Connection ~ 5850 1700
Wire Wire Line
	6850 1200 5850 1200
Connection ~ 5850 1200
Wire Wire Line
	5850 1200 5850 1500
Wire Wire Line
	6850 1950 9550 1950
Wire Wire Line
	9550 600  9550 1950
Wire Wire Line
	5850 1900 5850 2150
Wire Wire Line
	5850 2550 6850 2550
Connection ~ 5850 1900
Wire Wire Line
	6650 2350 6550 2350
Wire Wire Line
	6250 2350 5850 2350
Connection ~ 5850 2350
Wire Wire Line
	5850 2350 5850 2550
Wire Wire Line
	7250 2250 7400 2250
Wire Wire Line
	7400 2250 7400 1350
Wire Wire Line
	7400 1350 8050 1350
Wire Wire Line
	6650 2150 5850 2150
Connection ~ 5850 2150
Wire Wire Line
	5850 2150 5850 2350
Wire Wire Line
	7550 2950 7550 1450
Wire Wire Line
	7550 1450 8050 1450
Wire Wire Line
	6650 3050 6550 3050
Wire Wire Line
	6650 2850 5850 2850
Wire Wire Line
	5850 2850 5850 2550
Connection ~ 5850 2550
Wire Wire Line
	5850 2850 5850 3050
Wire Wire Line
	5850 3050 6250 3050
Connection ~ 5850 2850
Wire Wire Line
	7250 2950 7550 2950
$Comp
L Amplifier_Operational:LM358 U9
U 1 1 5B7A7061
P 6950 3750
F 0 "U9" H 6950 4117 50  0000 C CNN
F 1 "LM358" H 6950 4026 50  0000 C CNN
F 2 "" H 6950 3750 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 6950 3750 50  0001 C CNN
	1    6950 3750
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U9
U 3 1 5B7A7068
P 6950 3750
F 0 "U9" H 6908 3796 50  0000 L CNN
F 1 "LM358" H 6908 3705 50  0000 L CNN
F 2 "" H 6950 3750 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 6950 3750 50  0001 C CNN
	3    6950 3750
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U9
U 2 1 5B7A706F
P 6950 4450
F 0 "U9" H 6950 4817 50  0000 C CNN
F 1 "LM358" H 6950 4726 50  0000 C CNN
F 2 "" H 6950 4450 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 6950 4450 50  0001 C CNN
	2    6950 4450
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U10
U 1 1 5B7A7076
P 6950 5100
F 0 "U10" H 6950 5467 50  0000 C CNN
F 1 "LM358" H 6950 5376 50  0000 C CNN
F 2 "" H 6950 5100 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 6950 5100 50  0001 C CNN
	1    6950 5100
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U10
U 3 1 5B7A707D
P 6950 5100
F 0 "U10" H 6908 5146 50  0000 L CNN
F 1 "LM358" H 6908 5055 50  0000 L CNN
F 2 "" H 6950 5100 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 6950 5100 50  0001 C CNN
	3    6950 5100
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U10
U 2 1 5B7A7084
P 6950 5800
F 0 "U10" H 6950 6167 50  0000 C CNN
F 1 "LM358" H 6950 6076 50  0000 C CNN
F 2 "" H 6950 5800 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 6950 5800 50  0001 C CNN
	2    6950 5800
	1    0    0    -1  
$EndComp
$Comp
L LED:IR204A D13
U 1 1 5B7A708B
P 6350 3850
F 0 "D13" H 6300 3635 50  0000 C CNN
F 1 "IR204A" H 6300 3726 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 6350 4025 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 6300 3850 50  0001 C CNN
	1    6350 3850
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D14
U 1 1 5B7A7092
P 6350 4550
F 0 "D14" H 6300 4335 50  0000 C CNN
F 1 "IR204A" H 6300 4426 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 6350 4725 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 6300 4550 50  0001 C CNN
	1    6350 4550
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D15
U 1 1 5B7A7099
P 6350 5200
F 0 "D15" H 6300 4985 50  0000 C CNN
F 1 "IR204A" H 6300 5076 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 6350 5375 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 6300 5200 50  0001 C CNN
	1    6350 5200
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D16
U 1 1 5B7A70A0
P 6350 5900
F 0 "D16" H 6300 5685 50  0000 C CNN
F 1 "IR204A" H 6300 5776 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 6350 6075 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 6300 5900 50  0001 C CNN
	1    6350 5900
	-1   0    0    1   
$EndComp
$Comp
L Analog_ADC:ADS1015IDGS U12
U 1 1 5B7A70A7
P 8450 4100
F 0 "U12" H 8450 4778 50  0000 C CNN
F 1 "ADS1015IDGS" H 8450 4687 50  0000 C CNN
F 2 "Package_SO:TSSOP-10_3x3mm_P0.5mm" H 8450 3600 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/ads1015.pdf" H 8400 3200 50  0001 C CNN
	1    8450 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 3650 5850 3650
Wire Wire Line
	5850 3650 5850 3850
Wire Wire Line
	6650 4350 5850 4350
Connection ~ 5850 4350
Wire Wire Line
	5850 4350 5850 4550
Wire Wire Line
	6250 3850 5850 3850
Connection ~ 5850 3850
Wire Wire Line
	5850 3850 5850 4050
Wire Wire Line
	6650 4550 6550 4550
Wire Wire Line
	6250 4550 5850 4550
Wire Wire Line
	6550 3850 6650 3850
Wire Wire Line
	7250 3750 7950 3750
Wire Wire Line
	7950 3750 7950 4000
Wire Wire Line
	7950 4000 8050 4000
Wire Wire Line
	7250 4450 7250 3850
Wire Wire Line
	7250 3850 7800 3850
Wire Wire Line
	7800 3850 7800 4100
Wire Wire Line
	7800 4100 8050 4100
Wire Wire Line
	6850 3450 8450 3450
Wire Wire Line
	8450 3600 8450 3450
Connection ~ 8450 3450
Wire Wire Line
	8450 3450 9550 3450
Wire Wire Line
	8450 4500 8450 4750
Wire Wire Line
	8450 4750 5850 4750
Wire Wire Line
	5850 4750 5850 4550
Connection ~ 5850 4550
Wire Wire Line
	6850 4050 5850 4050
Connection ~ 5850 4050
Wire Wire Line
	5850 4050 5850 4350
Wire Wire Line
	6850 4800 9550 4800
Wire Wire Line
	9550 3450 9550 4800
Wire Wire Line
	5850 4750 5850 5000
Wire Wire Line
	5850 5400 6850 5400
Connection ~ 5850 4750
Wire Wire Line
	6650 5200 6550 5200
Wire Wire Line
	6250 5200 5850 5200
Connection ~ 5850 5200
Wire Wire Line
	5850 5200 5850 5400
Wire Wire Line
	7250 5100 7400 5100
Wire Wire Line
	7400 5100 7400 4200
Wire Wire Line
	7400 4200 8050 4200
Wire Wire Line
	6650 5000 5850 5000
Connection ~ 5850 5000
Wire Wire Line
	5850 5000 5850 5200
Wire Wire Line
	7550 5800 7550 4300
Wire Wire Line
	7550 4300 8050 4300
Wire Wire Line
	6650 5900 6550 5900
Wire Wire Line
	6650 5700 5850 5700
Wire Wire Line
	5850 5700 5850 5400
Connection ~ 5850 5400
Wire Wire Line
	5850 5700 5850 5900
Wire Wire Line
	5850 5900 6250 5900
Connection ~ 5850 5700
Wire Wire Line
	7250 5800 7550 5800
Wire Wire Line
	3550 1250 4500 1250
Wire Wire Line
	4500 1250 4500 4100
Wire Wire Line
	3600 4100 4500 4100
Connection ~ 4500 4100
Wire Wire Line
	4500 4100 4500 6400
Wire Wire Line
	8850 1250 9050 1250
Wire Wire Line
	9800 1250 9800 4100
Wire Wire Line
	9800 6400 4500 6400
Connection ~ 4500 6400
Wire Wire Line
	8850 4100 9800 4100
Connection ~ 9800 4100
Wire Wire Line
	9800 4100 9800 6400
Wire Wire Line
	8850 1350 9450 1350
Wire Wire Line
	9450 1350 9450 4200
Wire Wire Line
	9450 6300 4800 6300
Wire Wire Line
	8850 4200 9000 4200
Connection ~ 9450 4200
Wire Wire Line
	9450 4200 9450 6300
Wire Wire Line
	4800 6300 4800 4200
Wire Wire Line
	4800 1350 3550 1350
Connection ~ 4800 6300
Wire Wire Line
	3600 4200 4800 4200
Connection ~ 4800 4200
Wire Wire Line
	4800 4200 4800 1350
$Comp
L Connector:Conn_01x02_Male J3
U 1 1 5B7F0F16
P 4600 6850
F 0 "J3" V 4753 6663 50  0000 R CNN
F 1 "Conn_01x02_Male" V 4662 6663 50  0000 R CNN
F 2 "" H 4600 6850 50  0001 C CNN
F 3 "~" H 4600 6850 50  0001 C CNN
	1    4600 6850
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4600 6650 4500 6650
Wire Wire Line
	4500 6400 4500 6650
Wire Wire Line
	4700 6650 4800 6650
Wire Wire Line
	4800 6300 4800 6650
Text Notes 4750 7050 1    50   ~ 0
SCL\nSDA
$Comp
L Connector:Conn_01x02_Male J2
U 1 1 5B803AFA
P 3850 6850
F 0 "J2" V 4003 6663 50  0000 R CNN
F 1 "Conn_01x02_Male" V 3912 6663 50  0000 R CNN
F 2 "" H 3850 6850 50  0001 C CNN
F 3 "~" H 3850 6850 50  0001 C CNN
	1    3850 6850
	0    -1   -1   0   
$EndComp
Text Notes 4000 7100 1    50   ~ 0
5V\nGND\n
Wire Wire Line
	4300 4800 4300 6200
Wire Wire Line
	4300 6400 3850 6400
Wire Wire Line
	3850 6400 3850 6650
Connection ~ 4300 4800
Wire Wire Line
	4250 1950 4250 3450
Connection ~ 4250 1950
Connection ~ 4250 3450
Wire Wire Line
	4250 3450 4300 3450
Wire Wire Line
	9550 1950 9550 3450
Connection ~ 9550 1950
Connection ~ 9550 3450
Wire Wire Line
	9550 4800 9550 6200
Wire Wire Line
	9550 6200 4300 6200
Connection ~ 9550 4800
Connection ~ 4300 6200
Wire Wire Line
	4300 6200 4300 6400
Wire Wire Line
	5850 3050 5850 3650
Connection ~ 5850 3050
Connection ~ 5850 3650
Wire Wire Line
	5850 5900 5850 6100
Wire Wire Line
	5850 6100 3950 6100
Wire Wire Line
	3950 6100 3950 6650
Connection ~ 5850 5900
Wire Wire Line
	600  5900 600  6100
Wire Wire Line
	600  6100 3950 6100
Connection ~ 600  5900
Connection ~ 3950 6100
Wire Wire Line
	550  3050 550  3650
Wire Wire Line
	550  3650 600  3650
Connection ~ 550  3050
Connection ~ 600  3650
Wire Wire Line
	600  3650 1400 3650
Wire Wire Line
	3550 1800 3150 1800
Connection ~ 3150 1800
Wire Wire Line
	3150 1800 3150 1900
Text Notes 3600 1500 0    50   ~ 0
0x48
Wire Wire Line
	3600 4300 3950 4300
Wire Wire Line
	3950 4300 3950 3450
Connection ~ 3950 3450
Wire Wire Line
	3950 3450 4250 3450
Text Notes 3650 4400 0    50   ~ 0
0x49
Wire Wire Line
	8850 1450 9050 1450
Wire Wire Line
	9050 1450 9050 1250
Connection ~ 9050 1250
Wire Wire Line
	9050 1250 9800 1250
Text Notes 8850 1550 0    50   ~ 0
0x4A
Wire Wire Line
	8850 4300 9000 4300
Wire Wire Line
	9000 4300 9000 4200
Connection ~ 9000 4200
Wire Wire Line
	9000 4200 9450 4200
Text Notes 8850 4400 0    50   ~ 0
0x4B
$Comp
L Connector:Conn_01x04_Male J1
U 1 1 5B7EC636
P 3150 6850
F 0 "J1" V 3303 6563 50  0000 R CNN
F 1 "Conn_01x04_Male" V 3212 6563 50  0000 R CNN
F 2 "" H 3150 6850 50  0001 C CNN
F 3 "~" H 3150 6850 50  0001 C CNN
	1    3150 6850
	0    -1   -1   0   
$EndComp
Text Notes 3050 7000 0    50   ~ 0
Interrupt 1- 4
Wire Wire Line
	3550 6000 3050 6000
Wire Wire Line
	3050 6000 3050 6650
Wire Wire Line
	3550 1050 3550 1250
Connection ~ 3550 1250
Wire Wire Line
	3550 1250 3550 1350
Connection ~ 3550 1350
Wire Wire Line
	3550 1350 3550 1450
Connection ~ 3550 1450
Wire Wire Line
	3550 1450 3550 1800
Connection ~ 3550 1800
Wire Wire Line
	3550 1800 3550 6000
Wire Wire Line
	3600 3900 3600 4100
Wire Wire Line
	3600 6050 3150 6050
Wire Wire Line
	3150 6050 3150 6650
Connection ~ 3600 4100
Wire Wire Line
	3600 4100 3600 4200
Connection ~ 3600 4200
Wire Wire Line
	3600 4200 3600 4300
Connection ~ 3600 4300
Wire Wire Line
	3600 4300 3600 6050
Wire Wire Line
	8850 1050 10000 1050
Wire Wire Line
	10000 1050 10000 6450
Wire Wire Line
	10000 6450 3250 6450
Wire Wire Line
	3250 6450 3250 6650
Wire Wire Line
	8850 3900 10200 3900
Wire Wire Line
	10200 3900 10200 6550
Wire Wire Line
	10200 6550 3350 6550
Wire Wire Line
	3350 6550 3350 6650
$EndSCHEMATC
