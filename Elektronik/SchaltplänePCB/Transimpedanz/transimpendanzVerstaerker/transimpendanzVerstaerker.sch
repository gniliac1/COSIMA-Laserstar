EESchema Schematic File Version 4
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
U 1 1 5B755F9C
P 4750 2200
F 0 "U1" H 4750 2567 50  0000 C CNN
F 1 "LM358" H 4750 2476 50  0000 C CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 4750 2200 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 4750 2200 50  0001 C CNN
	1    4750 2200
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:LM358 U1
U 3 1 5B75602F
P 4750 2200
F 0 "U1" H 4708 2246 50  0000 L CNN
F 1 "LM358" H 4708 2155 50  0000 L CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 4750 2200 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 4750 2200 50  0001 C CNN
	3    4750 2200
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x03_Male J1
U 1 1 5B756334
P 6250 2200
F 0 "J1" H 6222 2130 50  0000 R CNN
F 1 "con1" H 6222 2221 50  0000 R CNN
F 2 "Connector:FanPinHeader_1x03_P2.54mm_Vertical" H 6250 2200 50  0001 C CNN
F 3 "~" H 6250 2200 50  0001 C CNN
	1    6250 2200
	-1   0    0    1   
$EndComp
$Comp
L LED:IR204A D1
U 1 1 5B7563EA
P 4250 3000
F 0 "D1" V 4154 3152 50  0000 L CNN
F 1 "IR204A" V 4245 3152 50  0000 L CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 4250 3175 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR204-A.pdf" H 4200 3000 50  0001 C CNN
	1    4250 3000
	0    1    1    0   
$EndComp
Wire Wire Line
	5050 2200 5350 2200
Wire Wire Line
	4450 2300 4250 2300
Wire Wire Line
	4450 2100 4000 2100
$Comp
L Device:R R1
U 1 1 5B75688D
P 5050 2750
F 0 "R1" V 4843 2750 50  0000 C CNN
F 1 "1MOhm" V 4934 2750 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 4980 2750 50  0001 C CNN
F 3 "~" H 5050 2750 50  0001 C CNN
	1    5050 2750
	0    1    1    0   
$EndComp
$Comp
L Device:C C1
U 1 1 5B756932
P 5050 3150
F 0 "C1" V 4798 3150 50  0000 C CNN
F 1 "1pF" V 4889 3150 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 5088 3000 50  0001 C CNN
F 3 "~" H 5050 3150 50  0001 C CNN
	1    5050 3150
	0    1    1    0   
$EndComp
Wire Wire Line
	5350 2750 5200 2750
Wire Wire Line
	5350 2200 5350 2750
Connection ~ 5350 2200
Wire Wire Line
	5350 2200 6050 2200
Wire Wire Line
	5350 2750 5350 3150
Wire Wire Line
	5350 3150 5200 3150
Connection ~ 5350 2750
Wire Wire Line
	4900 2750 4750 2750
Wire Wire Line
	4250 2750 4250 2800
Wire Wire Line
	4900 3150 4750 3150
Wire Wire Line
	4750 3150 4750 2750
Connection ~ 4750 2750
Wire Wire Line
	4750 2750 4250 2750
Wire Wire Line
	4250 2300 4250 2750
Connection ~ 4250 2750
Wire Wire Line
	4000 2100 4000 3350
Wire Wire Line
	4000 3350 4250 3350
Wire Wire Line
	4250 3100 4250 3350
Connection ~ 4250 3350
Wire Wire Line
	4250 3350 4650 3350
Text Notes 6500 2300 0    50   ~ 0
5V\nOut\nGND
Wire Wire Line
	6050 2300 6050 3350
Wire Wire Line
	4650 1900 6050 1900
Wire Wire Line
	6050 1900 6050 2100
Wire Wire Line
	4650 2500 4650 3350
Connection ~ 4650 3350
Wire Wire Line
	4650 3350 6050 3350
$EndSCHEMATC
