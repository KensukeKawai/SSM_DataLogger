
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

# Test
TEST_RESPONSE = [0x05,0xA8,0x00,0x00,0x00,0x61]

param_list = [  # param_list[Column][Row]
    # Param[0]                                  Address[1]                          sym1[2] num1[3] sym2[4] num2[5] sym3[6] num3[7]         sym4[8]     num4[9]         unit[10]
    ['Engine_Load',	                            [0x00,0x00,0x07],	                'mul',	100,	'div',	255,	'-',	'-',	        '-',	    '-',	        '%'],
    ['Coolant_Temperature',	                    [0x00,0x00,0x08],	                'sub',	40,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        '℃'],
    ['AirFuel_Correction_No1',	                [0x00,0x00,0x09],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['AirFuel_Learning_No1',	                [0x00,0x00,0x0A],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['AirFuel_Correction_No2',	                [0x00,0x00,0x0B],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['AirFuel_Learning_No2',	                [0x00,0x00,0x0C],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['Manifold_Absolute_Pressure',	            [0x00,0x00,0x0D],	                'mul',	37,	    'div',	255,	'mul',	0.070307246672,	'-',	    '-',	        'kgf/cm2'],
    ['Engine_Speed',	                        [0x00,0x00,0x0F,0x00,0x00,0x0E],	'div',	4,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'rpm'],
    ['Vehicle_Speed',	                        [0x00,0x01,0x00],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'km/h'],
    ['Ignition_Timing',	                        [0x00,0x01,0x01],	                'sub',	128,	'div',	2,	    '-',	'-',	        '-',	    '-',	        'deg'],
    ['Intake_Air_Temperature',	                [0x00,0x01,0x02],	                'sub',	40,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        '℃'],
    ['Mass_Air_Flow',	                        [0x00,0x01,0x04,0x00,0x01,0x03],	'div',	100,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'grams/s'],
    ['Throttle_Opening_Angle',	                [0x00,0x01,0x05],	                'mul',	100,	'div',	255,	'-',	'-',	        '-',	    '-',	        '%'],
    ['Front_O2_Sensor_No1',	                    [0x00,0x01,0x07,0x00,0x01,0x06],	'mul',	0.005,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Rear_O2_Sensor',	                        [0x00,0x01,0x09,0x00,0x01,0x08],	'mul',	0.005,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Front_O2_Sensor_No2',	                    [0x00,0x01,0x0B,0x00,0x01,0x0A],	'mul',	0.005,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Battery_Voltage',	                        [0x00,0x01,0x0C],	                'mul',	0.08,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Air_Flow_Sensor_Voltage',	                [0x00,0x01,0x0D],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Throttle_Sensor_Voltage',	                [0x00,0x01,0x0E],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Differential_Pressure_Sensor_Voltage',	[0x00,0x01,0x0F],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Fuel_Injection_No1_Pulse_Width',	        [0x00,0x02,0x00],	                'mul',	0.256,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'ms'],
    ['Fuel_Injection_No2_Pulse_Width',	        [0x00,0x02,0x01],	                'mul',	0.256,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'ms'],
    ['Knock_Correction',	                    [0x00,0x02,0x02],	                'sub',	128,	'div',	2,	    '-',	'-',	        '-',	    '-',	        'deg'],
    ['Atmospheric_Pressure',	                [0x00,0x02,0x03],	                'mul',	37,	    'div',	255,	'mul',	0.070307246672,	'-',	    '-',	        'kgf/cm2'],
    ['Manifold_Relative_Pressure',	            [0x00,0x02,0x04],	                'sub',	128,	'mul',	37,	    'div',	255,	        'mul',	    0.070307246672,	'kgf/cm2'],
    ['Pressure_Differential_Sensor',	        [0x00,0x02,0x05],	                'sub',	128,	'mul',	37,	    'div',	255,	        'mul',	    6.89476,	    'kPa'],
    ['Fuel_Tank_Pressure',	                    [0x00,0x20,0x06],	                'sub',	128,	'mul',	0.0035,	'mul',	6.89476,	    '-',	    '-',	        'kPa'],
    ['CO_Adjustment',	                        [0x00,0x02,0x07],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Learned_Ignition_Timing',	                [0x00,0x02,0x08],	                'sub',	128,	'div',	2,	    '-',	'-',	        '-',	    '-',	        'deg'],
    ['Accelerator_Opening_Angle',	            [0x00,0x02,0x09],	                'div',	2.56,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Fuel_Temperature',	                    [0x00,0x02,0x0A],	                'sub',	40,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        '℃'],
    ['Front_O2_Heater_No1',	                    [0x00,0x02,0x0B],	                'mul',	10.04,	'div',	256,	'-',	'-',	        '-',	    '-',	        'A'],
    ['Rear_O2_Heater_Current',	                [0x00,0x02,0x0C],	                'mul',	10.04,	'div',	256,	'-',	'-',	        '-',	    '-',	        'A'],
    ['Front_O2_Heater_No2',	                    [0x00,0x02,0x0D],	                'mul',	10.04,	'div',	256,	'-',	'-',	        '-',	    '-',	        'A'],
    ['Fuel_Level',	                            [0x00,0x02,0x0E],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Primary_Wastegate_Duty_Cycle',	        [0x00,0x03,0x00],	                'mul',	100,	'div',	255,	'-',	'-',	        '-',	    '-',	        '%'],
    ['Secondary_Wastegate_Duty_Cycle',	        [0x00,0x03,0x01],	                'mul',	100,	'div',	255,	'-',	'-',	        '-',	    '-',	        '%'],
    ['CPC_Valve_Duty_Ratio',	                [0x00,0x03,0x02],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Tumble_Valve_Position_Sensor_Right',	    [0x00,0x03,0x03],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Tumble_Valve_Position_Sensor_Left',	    [0x00,0x03,0x04],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Idle_Speed_Control_Valve_Duty_Ratio',	    [0x00,0x03,0x05],	                'div',	2,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['AirFuel_Lean_Correction',	                [0x00,0x03,0x06],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['AirFuel_Heater_Duty',	                    [0x00,0x03,0x07],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Idle_Speed_Control_Valve_Step',	        [0x00,0x03,0x08],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'Step'],
    ['Number_of_ExGas_Recirc_Steps',	        [0x00,0x03,0x09],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'Step'],
    ['Alternator_Duty',	                        [0x00,0x03,0x0A],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Fuel_Pump_Duty',	                        [0x00,0x03,0x0B],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Intake_VVT_Advance_Angle_Right',	        [0x00,0x03,0x0C],	                'sub',	50,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'deg'],
    ['Intake_VVT_Advance_Angle_Left',	        [0x00,0x03,0x0D],	                'sub',	50,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'deg'],
    ['Intake_OCV_Duty_Right',	                [0x00,0x03,0x0E],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Intake_OCV_Duty_Left',	                [0x00,0x03,0x0F],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Intake_OCV_Current_Right',	            [0x00,0x04,0x00],	                'mul',	32,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'mA'],
    ['Intake_OCV_Current_Left',	                [0x00,0x04,0x01],	                'mul',	32,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'mA'],
    ['AirFuel_Sensor_No1_Current',	            [0x00,0x04,0x02],	                'sub',	128,	'mul',	0.125,	'-',	'-',	        '-',	    '-',	        'mA'],
    ['AirFuel_Sensor_No2_Current',	            [0x00,0x04,0x03],	                'sub',	128,	'mul',	0.125,	'-',	'-',	        '-',	    '-',	        'mA'],
    ['AirFuel_Sensor_No1_Resistance',	        [0x00,0x04,0x04],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'Ω'],
    ['AirFuel_Sensor_No2_Resistance',	        [0x00,0x04,0x05],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'Ω'],
    ['AirFuel_Sensor_No1',	                    [0x00,0x04,0x06],	                'div',	128,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'λ'],
    ['AirFuel_Sensor_No2',	                    [0x00,0x04,0x07],	                'div',	128,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'λ'],
    ['Gear_Position',	                        [0x00,0x04,0x0A],	                'add',	1,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        '-'],
    ['AbyF_Sensor_No1_Heater_Current',	        [0x00,0x05,0x03],	                'div',	10,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'A'],
    ['AbyF_Sensor_No2_Heater_Current',	        [0x00,0x05,0x04],	                'div',	10,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'A'],
    ['Roughness_Monitor_Cylinder_No1',	        [0x00,0x0C,0x0E],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        '-'],
    ['Roughness_Monitor_Cylinder_No2',	        [0x00,0x0C,0x0F],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        '-'],
    ['AirFuel_Correction_No3',	                [0x00,0x0D,0x00],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['AirFuel_Learning_No3',	                [0x00,0x0D,0x01],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['Rear_O2_Heater_Voltage',	                [0x00,0x0D,0x02],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['AirFuel_Adjustment_Voltage',	            [0x00,0x0D,0x03],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Roughness_Monitor_Cylinder_No3',	        [0x00,0x0D,0x08],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        '-'],
    ['Roughness_Monitor_Cylinder_No4',	        [0x00,0x0D,0x09],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        '-'],
    ['Throttle_Motor_Duty',	                    [0x00,0x0F,0x0A],	                'sub',	128,	'div',	1.28,	'-',	'-',	        '-',	    '-',	        '%'],
    ['Throttle_Motor_Voltage',	                [0x00,0x0F,0x0B],	                'mul',	0.08,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Sub_Throttle_Sensor',	                    [0x01,0x00,0x00],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Main_Throttle_Sensor',	                [0x01,0x00,0x01],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Sub_Accelerator_Sensor',	                [0x01,0x00,0x02],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Main_Accelerator_Sensor',	                [0x01,0x00,0x03],	                'mul',	0.02,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'V'],
    ['Brake_Booster_Pressure',	                [0x01,0x00,0x04],	                'mul',	37,	    'div',	255,	'mul',	6.89476,	    '-',	    '-',	        'kPa'],
    ['Fuel_Pressure_High',	                    [0x01,0x00,0x05],	                'mul',	0.04,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'Mpa'],
    ['Exhaust_Gas_Temperature',	                [0x01,0x00,0x06],	                'add',	40,	    'mul',	5,	    '-',	'-',	        '-',	    '-',	        '℃'],
    ['Cold_Start_Injector',	                    [0x01,0x00,0x08],	                'mul',	0.256,	'-',	'-',	'-',	'-',	        '-',	    '-',	        'ms'],
    ['SCV_Step',	                            [0x01,0x00,0x09],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'Step'],
    ['Memorised_Cruise_Speed',	                [0x01,0x00,0x0A],	                '-',	'-',	'-',	'-',	'-',	'-',	        '-',	    '-',	        'km/h'],
    ['Exhaust_VVT_Advance_Angle_Right',	        [0x01,0x01,0x08],	                'sub',	50,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'deg'],
    ['Exhaust_VVT_Advance_Angle_Left',	        [0x01,0x01,0x09],	                'sub',	50,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'deg'],
    ['Exhasut_OCV_Duty_Right',	                [0x01,0x01,0x0A],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Exhasut_OCV_Duty_Left',	                [0x01,0x01,0x0B],	                'div',	2.55,	'-',	'-',	'-',	'-',	        '-',	    '-',	        '%'],
    ['Exhasut_OCV_Current_Right',	            [0x01,0x01,0x0C],	                'mul',	32,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'mA'],
    ['Exhasut_OCV_Current_Left',	            [0x01,0x01,0x0D],	                'mul',	32,	    '-',	'-',	'-',	'-',	        '-',	    '-',	        'mA']
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