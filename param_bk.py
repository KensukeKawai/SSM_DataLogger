
from dataclasses import dataclass

# Header
HEADER_T2C = [0x80,0x10,0xF0]
HEADER_C2T = [0x80,0xF0,0x10]

# Command
@dataclass
class command:
    READ_MEMORY: int
    READ_SINGLE_ADDRESS: int
    WRITE_MEMORY: int
    WRITE_SINGLE_ADDRESS: int
    ECU_INIT: int
    
# Instantiate
command_t2c = command(0xA0,0xA8,0xB0,0xB8,0xBF)
command_c2t = command(0xE0,0xE8,0xF0,0xF8,0xFF)

# Element param_list
NAME = 0
ADDRESS = 1
SYM1 = 2
NUM1 = 3
SYM2 = 4
NUM2 = 5
SYM3 = 6
NUM3 = 7
SYM4 = 8
NUM4 = 9
UNIT = 10

param_list = [  # param_list[Column][Row]
    # Name[0]                                   Address[1]                          sym1[2] num1[3] sym2[4] num2[5] sym3[6] num3[7]         sym4[8]     num4[9]         unit[10]
    ['Engine Load',	                            [0x00,0x00,0x07],	                'mul',	100,	'div',	255,	'-',	'-',	        '-',	    '-',	        '%'],
    ['Coolant Temperature',	                    [0x00,0x00,0x08],	                'sub',	40,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        '°C'],
    ['AirFuel Correction No1',	                [0x00,0x00,0x09],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['AirFuel Learning No1',	                [0x00,0x00,0x0A],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['AirFuel Correction No2',	                [0x00,0x00,0x0B],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['AirFuel Learning No2',	                [0x00,0x00,0x0C],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['Manifold Absolute Pressure',	            [0x00,0x00,0x0D],	                'mul',	37,	    'div',	255,	'mul',	0.070307246672,	'-',	    '-',	        'kgf/cm2'],
    ['Engine Speed',	                        [0x00,0x00,0x0F,0x00,0x00,0x0E],	'div',	4,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'rpm'],
    ['Vehicle Speed',	                        [0x00,0x01,0x00],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'km/h'],
    ['Ignition Timing',	                        [0x00,0x01,0x01],	                'sub',	128,	'div',	2,	    '-',	'-',	        '-',	    '-',	        'deg'],
    ['Intake Air Temperature',	                [0x00,0x01,0x02],	                'sub',	40,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        '°C'],
    ['Mass Air Flow',	                        [0x00,0x01,0x04,0x00,0x01,0x03],	'div',	100,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'grams/s'],
    ['Throttle Opening Angle',	                [0x00,0x01,0x05],	                'mul',	100,	'div',	255,	'-',	'-',	        '-',	    '-',	        '%'],
    ['Front O2 Sensor No1',	                    [0x00,0x01,0x07,0x00,0x01,0x06],	'mul',	0.005,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Rear O2 Sensor',	                        [0x00,0x01,0x09,0x00,0x01,0x08],	'mul',	0.005,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Front O2 Sensor No2',	                    [0x00,0x01,0x0B,0x00,0x01,0x0A],	'mul',	0.005,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Battery Voltage',	                        [0x00,0x01,0x0C],	                'mul',	0.08,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Air Flow Sensor Voltage',	                [0x00,0x01,0x0D],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Throttle Sensor Voltage',	                [0x00,0x01,0x0E],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Differential Pressure Sensor Voltage',	[0x00,0x01,0x0F],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Fuel Injection No1 Pulse Width',	        [0x00,0x02,0x00],	                'mul',	0.256,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'ms'],
    ['Fuel Injection No2 Pulse Width',	        [0x00,0x02,0x01],	                'mul',	0.256,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'ms'],
    ['Knock Correction',	                    [0x00,0x02,0x02],	                'sub',	128,	'div',	2,	    '-',	'-',	        '-',	    '-',	        'deg'],
    ['Atmospheric Pressure',	                [0x00,0x02,0x03],	                'mul',	37,	    'div',	255,	'mul',	0.070307246672,	'-',	    '-',	        'kgf/cm2'],
    ['Manifold Relative Pressure',	            [0x00,0x02,0x04],	                'sub',	128,	'mul',	37,	    'div',	255,	        'mul',	    0.070307246672,	'kgf/cm2'],
    ['Pressure Differential Sensor',	        [0x00,0x02,0x05],	                'sub',	128,	'mul',	37,	    'div',	255,	        'mul',	    6.89476,	    'kPa'],
    ['Fuel Tank Pressure',	                    [0x00,0x20,0x06],	                'sub',	128,	'mul',	0.0035,	'mul',	6.89476,	    '-',	    '-',	        'kPa'],
    ['CO Adjustment',	                        [0x00,0x02,0x07],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Learned Ignition Timing',	                [0x00,0x02,0x08],	                'sub',	128,	'div',	2,	    '-',	'-',	        '-',	    '-',	        'deg'],
    ['Accelerator Opening Angle',	            [0x00,0x02,0x09],	                'div',	2.56,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Fuel Temperature',	                    [0x00,0x02,0x0A],	                'sub',	40,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        '°C'],
    ['Front O2 Heater No1',	                    [0x00,0x02,0x0B],	                'mul',	10.04,	'div',	256,	'-',	'-',	        '-',	    '-',	        'A'],
    ['Rear O2 Heater Current',	                [0x00,0x02,0x0C],	                'mul',	10.04,	'div',	256,	'-',	'-',	        '-',	    '-',	        'A'],
    ['Front O2 Heater No2',	                    [0x00,0x02,0x0D],	                'mul',	10.04,	'div',	256,	'-',	'-',	        '-',	    '-',	        'A'],
    ['Fuel Level',	                            [0x00,0x02,0x0E],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Primary Wastegate Duty Cycle',	        [0x00,0x03,0x00],	                'mul',	100,	'div',	255,	'-',	'-',	        '-',	    '-',	        '%'],
    ['Secondary Wastegate Duty Cycle',	        [0x00,0x03,0x01],	                'mul',	100,	'div',	255,	'-',	'-',	        '-',	    '-',	        '%'],
    ['CPC Valve Duty Ratio',	                [0x00,0x03,0x02],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Tumble Valve Position Sensor Right',	    [0x00,0x03,0x03],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Tumble Valve Position Sensor Left',	    [0x00,0x03,0x04],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Idle Speed Control Valve Duty Ratio',	    [0x00,0x03,0x05],	                'div',	2,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['AirFuel Lean Correction',	                [0x00,0x03,0x06],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['AirFuel Heater Duty',	                    [0x00,0x03,0x07],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Idle Speed Control Valve Step',	        [0x00,0x03,0x08],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'Step'],
    ['Number of ExGas Recirc Steps',	        [0x00,0x03,0x09],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'Step'],
    ['Alternator Duty',	                        [0x00,0x03,0x0A],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Fuel Pump Duty',	                        [0x00,0x03,0x0B],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Intake VVT Advance Angle Right',	        [0x00,0x03,0x0C],	                'sub',	50,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'deg'],
    ['Intake VVT Advance Angle Left',	        [0x00,0x03,0x0D],	                'sub',	50,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'deg'],
    ['Intake OCV Duty Right',	                [0x00,0x03,0x0E],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Intake OCV Duty Left',	                [0x00,0x03,0x0F],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Intake OCV Current Right',	            [0x00,0x04,0x00],	                'mul',	32,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'mA'],
    ['Intake OCV Current Left',	                [0x00,0x04,0x01],	                'mul',	32,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'mA'],
    ['AirFuel Sensor No1 Current',	            [0x00,0x04,0x02],	                'sub',	128,	'mul',	0.125,	'-',	'-',	        '-',	    '-',	        'mA'],
    ['AirFuel Sensor No2 Current',	            [0x00,0x04,0x03],	                'sub',	128,	'mul',	0.125,	'-',	'-',	        '-',	    '-',	        'mA'],
    ['AirFuel Sensor No1 Resistance',	        [0x00,0x04,0x04],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'Ω'],
    ['AirFuel Sensor No2 Resistance',	        [0x00,0x04,0x05],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'Ω'],
    ['AirFuel Sensor No1',	                    [0x00,0x04,0x06],	                'div',	128,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'λ'],
    ['AirFuel Sensor No2',	                    [0x00,0x04,0x07],	                'div',	128,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'λ'],
    ['Gear Position',	                        [0x00,0x04,0x0A],	                'add',	1,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        '-'],
    ['AbyF Sensor No1 Heater Current',	        [0x00,0x05,0x03],	                'div',	10,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'A'],
    ['AbyF Sensor No2 Heater Current',	        [0x00,0x05,0x04],	                'div',	10,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'A'],
    ['Roughness Monitor Cylinder No1',	        [0x00,0x0C,0x0E],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        '-'],
    ['Roughness Monitor Cylinder No2',	        [0x00,0x0C,0x0F],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        '-'],
    ['AirFuel Correction No3',	                [0x00,0x0D,0x00],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['AirFuel Learning No3',	                [0x00,0x0D,0x01],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['Rear O2 Heater Voltage',	                [0x00,0x0D,0x02],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['AirFuel Adjustment Voltage',	            [0x00,0x0D,0x03],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Roughness Monitor Cylinder No3',	        [0x00,0x0D,0x08],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        '-'],
    ['Roughness Monitor Cylinder No4',	        [0x00,0x0D,0x09],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        '-'],
    ['Throttle Motor Duty',	                    [0x00,0x0F,0x0A],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['Throttle Motor Voltage',	                [0x00,0x0F,0x0B],	                'mul',	0.08,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Sub Throttle Sensor',	                    [0x01,0x00,0x00],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Main Throttle Sensor',	                [0x01,0x00,0x01],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Sub Accelerator Sensor',	                [0x01,0x00,0x02],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Main Accelerator Sensor',	                [0x01,0x00,0x03],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Brake Booster Pressure',	                [0x01,0x00,0x04],	                'mul',	37,	    'div',	255,	'mul',	6.89476,	    '-',	    '-',	        'kPa'],
    ['Fuel Pressure High',	                    [0x01,0x00,0x05],	                'mul',	0.04,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'Mpa'],
    ['Exhaust Gas Temperature',	                [0x01,0x00,0x06],	                'add',	40,	    'mul',	5,	    '-',	'-',	        '-',	    '-',	        '°C'],
    ['Cold Start Injector',	                    [0x01,0x00,0x08],	                'mul',	0.256,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'ms'],
    ['SCV Step',	                            [0x01,0x00,0x09],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'Step'],
    ['Memorised Cruise Speed',	                [0x01,0x00,0x0A],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'km/h'],
    ['Exhaust VVT Advance Angle Right',	        [0x01,0x01,0x08],	                'sub',	50,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'deg'],
    ['Exhaust VVT Advance Angle Left',	        [0x01,0x01,0x09],	                'sub',	50,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'deg'],
    ['Exhasut OCV Duty Right',	                [0x01,0x01,0x0A],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Exhasut OCV Duty Left',	                [0x01,0x01,0x0B],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Exhasut OCV Current Right',	            [0x01,0x01,0x0C],	                'mul',	32,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'mA'],
    ['Exhasut OCV Current Left',	            [0x01,0x01,0x0D],	                'mul',	32,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'mA']
]

# 取得したいパラメータを配列にextendで結合する
Engine_Load =                           [0x00,0x00,0x07]
Coolant_Temperature =                   [0x00,0x00,0x08]
AirFuel_Correction_No1 =                [0x00,0x00,0x09]
AirFuel_Learning_No1 =                  [0x00,0x00,0x0A]
AirFuel_Correction_No2 =                [0x00,0x00,0x0B]
AirFuel_Learning_No2 =                  [0x00,0x00,0x0C]
Manifold_Absolute_Pressure =            [0x00,0x00,0x0D]
Engine_Speed =                          [0x00,0x00,0x0F,0x00,0x00,0x0E]
Vehicle_Speed =                         [0x00,0x01,0x00]
Ignition_Timing =                       [0x00,0x01,0x01]
Intake_Air_Temperature =                [0x00,0x01,0x02]
Mass_Air_Flow =                         [0x00,0x01,0x04,0x00,0x01,0x03]
Throttle_Opening_Angle =                [0x00,0x01,0x05]
Front_O2_Sensor_No1 =                   [0x00,0x01,0x07,0x00,0x01,0x06]
Rear_O2_Sensor =                        [0x00,0x01,0x09,0x00,0x01,0x08]
Front_O2_Sensor_No2 =                   [0x00,0x01,0x0B,0x00,0x01,0x0A]
Battery_Voltage =                       [0x00,0x01,0x0C]
Air_Flow_Sensor_Voltage =               [0x00,0x01,0x0D]
Throttle_Sensor_Voltage =               [0x00,0x01,0x0E]
Differential_Pressure_Sensor_Voltage =  [0x00,0x01,0x0F]
Fuel_Injection_No1_Pulse_Width =        [0x00,0x02,0x00]
Fuel_Injection_No2_Pulse_Width =        [0x00,0x02,0x01]
Knock_Correction =                      [0x00,0x02,0x02]
Atmospheric_Pressure =                  [0x00,0x02,0x03]
Manifold_Relative_Pressure =            [0x00,0x02,0x04]
Pressure_Differential_Sensor =          [0x00,0x02,0x05]
Fuel_Tank_Pressure =                    [0x00,0x20,0x06]
CO_Adjustment =                         [0x00,0x02,0x07]
Learned_Ignition_Timing =               [0x00,0x02,0x08]
Accelerator_Opening_Angle =             [0x00,0x02,0x09]
Fuel_Temperature =                      [0x00,0x02,0x0A]
Front_O2_Heater_No1 =                   [0x00,0x02,0x0B]
Rear_O2_Heater_Current =                [0x00,0x02,0x0C]
Front_O2_Heater_No2 =                   [0x00,0x02,0x0D]
Fuel_Level =                            [0x00,0x02,0x0E]
Primary_Wastegate_Duty_Cycle =          [0x00,0x03,0x00]
Secondary_Wastegate_Duty_Cycle =        [0x00,0x03,0x01]
CPC_Valve_Duty_Ratio =                  [0x00,0x03,0x02]
Tumble_Valve_Position_Sensor_Right =    [0x00,0x03,0x03]
Tumble_Valve_Position_Sensor_Left =     [0x00,0x03,0x04]
Idle_Speed_Control_Valve_Duty_Ratio =   [0x00,0x03,0x05]
AirFuel_Lean_Correction =               [0x00,0x03,0x06]
AirFuel_Heater_Duty =                   [0x00,0x03,0x07]
Idle_Speed_Control_Valve_Step =         [0x00,0x03,0x08]
Number_of_ExGas_Recirc_Steps =          [0x00,0x03,0x09]
Alternator_Duty =                       [0x00,0x03,0x0A]
Fuel_Pump_Duty =                        [0x00,0x03,0x0B]
Intake_VVT_Advance_Angle_Right =        [0x00,0x03,0x0C]
Intake_VVT_Advance_Angle_Left =         [0x00,0x03,0x0D]
Intake_OCV_Duty_Right =                 [0x00,0x03,0x0E]
Intake_OCV_Duty_Left =                  [0x00,0x03,0x0F]
Intake_OCV_Current_Right =              [0x00,0x04,0x00]
Intake_OCV_Current_Left =               [0x00,0x04,0x01]
AirFuel_Sensor_No1_Current =            [0x00,0x04,0x02]
AirFuel_Sensor_No2_Current =            [0x00,0x04,0x03]
AirFuel_Sensor_No1_Resistance =         [0x00,0x04,0x04]
AirFuel_Sensor_No2_Resistance =         [0x00,0x04,0x05]
AirFuel_Sensor_No1 =                    [0x00,0x04,0x06]
AirFuel_Sensor_No2 =                    [0x00,0x04,0x07]
Gear_Position =                         [0x00,0x04,0x0A]
AbyF_Sensor_No1_Heater_Current =        [0x00,0x05,0x03]
AbyF_Sensor_No2_Heater_Current =        [0x00,0x05,0x04]
Roughness_Monitor_Cylinder_No1 =        [0x00,0x0C,0x0E]
Roughness_Monitor_Cylinder_No2 =        [0x00,0x0C,0x0F]
AirFuel_Correction_No3 =                [0x00,0x0D,0x00]
AirFuel_Learning_No3 =                  [0x00,0x0D,0x01]
Rear_O2_Heater_Voltage =                [0x00,0x0D,0x02]
AirFuel_Adjustment_Voltage =            [0x00,0x0D,0x03]
Roughness_Monitor_Cylinder_No3 =        [0x00,0x0D,0x08]
Roughness_Monitor_Cylinder_No4 =        [0x00,0x0D,0x09]
Throttle_Motor_Duty =                   [0x00,0x0F,0x0A]
Throttle_Motor_Voltage =                [0x00,0x0F,0x0B]
Sub_Throttle_Sensor =                   [0x01,0x00,0x00]
Main_Throttle_Sensor =                  [0x01,0x00,0x01]
Sub_Accelerator_Sensor =                [0x01,0x00,0x02]
Main_Accelerator_Sensor =               [0x01,0x00,0x03]
Brake_Booster_Pressure =                [0x01,0x00,0x04]
Fuel_Pressure_High =                    [0x01,0x00,0x05]
Exhaust_Gas_Temperature =               [0x01,0x00,0x06]
Cold_Start_Injector =                   [0x01,0x00,0x08]
SCV_Step =                              [0x01,0x00,0x09]
Memorised_Cruise_Speed =                [0x01,0x00,0x0A]
Exhaust_VVT_Advance_Angle_Right =       [0x01,0x01,0x08]
Exhaust_VVT_Advance_Angle_Left =        [0x01,0x01,0x09]
Exhasut_OCV_Duty_Right =                [0x01,0x01,0x0A]
Exhasut_OCV_Duty_Left =                 [0x01,0x01,0x0B]
Exhasut_OCV_Current_Right =             [0x01,0x01,0x0C]
Exhasut_OCV_Current_Left =              [0x01,0x01,0x0D]