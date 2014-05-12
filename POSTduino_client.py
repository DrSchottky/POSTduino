import serial 
import time
import getopt
import sys,os

postCodes={0x10: "Payload/1BL started",
            	0x11: "FSB_CONFIG_PHY_CONTROL",
                0x12: "FSB_CONFIG_RX_STATE",
                0x13: "FSB_CONFIG_TX_STATE",
                20: "FSB_CONFIG_TX_CREDITS",
                0x15: "FETCH_OFFSET",
                0x16: "FETCH_HEADER",
                0x17: "VERIFY_HEADER",
                0x18: "FETCH_CONTENTS",
                0x19: "HMACSHA_COMPUTE",
                0x1a: "RC4_INITIALIZE",
                0x1b: "RC4_DECRYPT",
                0x1c: "SHA_COMPUTE",
                0x1d: "SIG_VERIFY",
                30: "BRANCH",
                0x81: "Panic - MACHINE_CHECK",
                130: "Panic - DATA_STORAGE",
                0x83: "Panic - DATA_SEGMENT",
                0x84: "Panic - INSTRUCTION_STORAGE",
                0x85: "Panic - INSTRUCTION_SEGMENT",
                0x86: "Panic - EXTERNAL",
                0x87: "Panic - ALIGNMENT",
                0x88: "Panic - PROGRAM",
                0x89: "Panic - FPU_UNAVAILABLE",
                0x8a: "Panic - DECREMENTER",
                0x8b: "Panic - HYPERVISOR_DECREMENTER",
                140: "Panic - SYSTEM_CALL",
                0x8d: "Panic - TRACE",
                0x8e: "Panic - VPU_UNAVAILABLE",
                0x8f: "Panic - MAINTENANCE",
                0x90: "Panic - VMX_ASSIST",
                0x91: "Panic - THERMAL_MANAGEMENT",
                0x92: "Panic - 1BL is executed on wrong CPU thread panic)",
                0x93: "Panic - TOO_MANY_CORES",
                0x94: "Panic - VERIFY_OFFSET",
                0x95: "Panic - VERIFY_HEADER",
                150: "Panic - SIG_VERIFY",
                0x97: "Panic - NONHOST_RESUME_STATUS",
                0x98: "Panic - NEXT_STAGE_SIZE",
                0xd0: "CB_A entry point reached",
                0xd1: "READ_FUSES",
                210: "VERIFY_OFFSET_CB_B",
                0xd3: "FETCH_HEADER_CB_B",
                0xd4: "VERIFY_HEADER_CB_B",
                0xd5: "FETCH_CONTENTS_CB_B",
                0xd6: "HMACSHA_COMPUTE_CB_B",
                0xd7: "RC4_INITIALIZE_CB_B",
                0xd8: "RC4_DECRYPT_CB_B",
                0xd9: "SHA_COMPUTE_CB_B",
                0xda: "SHA_VERIFY_CB_B",
                0xdb: "BRANCH_CB_B",
                240: "Panic - VERIFY_OFFSET_CB_B",
                0xf1: "Panic - VERIFY_HEADER_CB_B",
                0xf2: "Panic - SHA_VERIFY_CB_B",
                0xf3: "Panic - ENTRY_SIZE_INVALID_CB_B",
                0x20: "CB entry point reached",
                0x21: "INIT_SECOTP",
                0x22: "INIT_SECENG",
                0x23: "INIT_SYSRAM",
                0x24: "VERIFY_OFFSET_3BL_CC",
                0x25: "LOCATE_3BL_CC",
                0x26: "FETCH_HEADER_3BL_CC",
                0x27: "VERIFY_HEADER_3BL_CC",
                40: "FETCH_CONTENTS_3BL_CC",
                0x29: "HMACSHA_COMPUTE_3BL_CC",
                0x2a: "RC4_INITIALIZE_3BL_CC",
                0x2b: "RC4_DECRYPT_3BL_CC",
                0x2c: "SHA_COMPUTE_3BL_CC",
                0x2d: "SIG_VERIFY_3BL_CC",
                0x2e: "HWINIT",
                0x2f: "RELOCATE",
                0x30: "VERIFY_OFFSET_4BL_CD",
                0x31: "FETCH_HEADER_4BL_CD",
                50: "VERIFY_HEADER_4BL_CD",
                0x33: "FETCH_CONTENTS_4BL_CD",
                0x34: "HMACSHA_COMPUTE_4BL_CD",
                0x35: "RC4_INITIALIZE_4BL_CD",
                0x36: "RC4_DECRYPT_4BL_CD",
                0x37: "SHA_COMPUTE_4BL_CD",
                0x38: "SIG_VERIFY_4BL_CD",
                0x39: "SHA_VERIFY_4BL_CD",
                0x3a: "BRANCH",
                0x3b: "PCI_INIT",
                0x9b: "Panic - VERIFY_SECOTP_1",
                0x9c: "Panic - VERIFY_SECOTP_2",
                0x9d: "Panic - VERIFY_SECOTP_3",
                0x9e: "Panic - Panic - VERIFY_SECOTP_4",
                0x9f: "Panic - VERIFY_SECOTP_5",
                160: "Panic - VERIFY_SECOTP_6",
                0xa1: "Panic - VERIFY_SECOTP_7",
                0xa2: "Panic - VERIFY_SECOTP_8",
                0xa3: "Panic - VERIFY_SECOTP_9",
                0xa4: "Panic - VERIFY_SECOTP_10",
                0xa5: "Panic - VERIFY_OFFSET_3BL_CC",
                0xa6: "Panic - LOCATE_3BL_CC",
                0xa7: "Panic - VERIFY_HEADER_3BL_CC",
                0xa8: "Panic - SIG_VERIFY_3BL_CC",
                0xa9: "Panic - HWINIT",
                170: "Panic - VERIFY_OFFSET_4BL_CD",
                0xab: "Panic - VERIFY_HEADER_4BL_CD",
                0xac: "Panic - SIG_VERIFY_4BL_CD",
                0xad: "Panic - SHA_VERIFY_4BL_CD",
                0xae: "Panic - UNEXPECTED_INTERRUPT",
                0xaf: "Panic - UNSUPPORTED_RAM_SIZE",
                0xb0: "Panic - VERIFY_CONSOLE_TYPE",
                0x40: "Entrypoint of CD reached",
                0x41: "VERIFY_OFFSET",
                0x42: "FETCH_HEADER",
                0x43: "VERIFY_HEADER",
                0x44: "FETCH_CONTENTS",
                0x45: "HMACSHA_COMPUTE",
                70: "RC4_INITIALIZE",
                0x47: "RC4_DECRYPT",
                0x48: "SHA_COMPUTE",
                0x49: "SHA_VERIFY",
                0x4a: "LOAD_6BL_CF",
                0x4b: "LZX_EXPAND",
                0x4c: "SWEEP_CACHES",
                0x4d: "DECODE_FUSES",
                0x4e: "FETCH_OFFSET_6BL_CF",
                0x4f: "VERIFY_OFFSET_6BL_CF",
                80: "LOAD_UPDATE_1",
                0x51: "LOAD_UPDATE_2",
                0x52: "BRANCH",
                0x53: "DECRYT_VERIFY_HV_CERT",
                0xb1: "Panic - VERIFY_OFFSET",
                0xb2: "Panic - VERIFY_HEADER",
                0xb3: "Panic - SHA_VERIFY",
                180: "Panic - LZX_EXPAND",
                0xb5: "Panic - VERIFY_OFFSET_6BL",
                0xb6: "Panic - DECODE_FUSES",
                0xb7: "Panic - UPDATE_MISSING",
                0xc1: "LZX_EXPAND_1",
                0xc2: "LZX_EXPAND_2",
                0xc3: "LZX_EXPAND_3",
                0xc4: "LZX_EXPAND_4",
                0xc5: "LZX_EXPAND_5",
                0xc6: "LZX_EXPAND_6",
                0xc7: "LZX_EXPAND_7",
                200: "SHA_VERIFY",
                0x58: "INIT_HYPERVISOR",
                0x59: "INIT_SOC_MMIO",
                90: "INIT_XEX_TRAINING",
                0x5b: "INIT_KEYRING",
                0x5c: "INIT_KEYS",
                0x5d: "INIT_SOC_INT",
                0x5e: "INIT_SOC_INT_COMPLETE",
                0xff: "FATAL",
                0x60: "INIT_KERNEL",
                0x61: "INIT_HAL_PHASE_0",
                0x62: "INIT_PROCESS_OBJECTS",
                0x63: "INIT_KERNEL_DEBUGGER",
                100: "INIT_MEMORY_MANAGER",
                0x65: "INIT_STACKS",
                0x66: "INIT_OBJECT_SYSTEM",
                0x67: "INIT_PHASE1_THREAD",
                0x68: "Started phase 1 Initialization + INIT_PROCESSORS",
                0x69: "INIT_KEY_VAULT",
                0x6a: "INIT_HAL_PHASE_1",
                0x6b: "INIT_SFC_DRIVER",
                0x6c: "INIT_SECURITY",
                0x6d: "INIT_KEY_EX_VAULT",
                110: "INIT_SETTINGS",
                0x6f: "INIT_POWER_MODE",
                0x70: "INIT_VIDEO_DRIVER",
                0x71: "INIT_AUDIO_DRIVER",
                0x72: "INIT_BOOT_ANIMATION + XMADecoder & XAudioRender Init",
                0x73: "INIT_SATA_DRIVER",
                0x74: "INIT_SHADOWBOOT",
                0x75: "INIT_DUMP_SYSTEM",
                0x76: "INIT_SYSTEM_ROOT",
                0x77: "INIT_OTHER_DRIVERS",
                120: "INIT_STFS_DRIVER",
                0x79: "LOAD_XAM",
                0xb8: "Panic - CF auth failed"}
def stop():
	print ("Post seems stuck on " + hex(int(new_post[:8],2)))
	print "Exiting..."
	ser.close()
	os._exit(0)


debugLog=None
timeout=0;
running=False

print "POSTduino by DrSchottky/cirowner"
print "version 0.1 beta"
ser=serial.Serial("/dev/ttyACM0",1000000)
time.sleep(2)
post=ser.readline()

Opts,Args=getopt.getopt(sys.argv[1:],"o:")
for Option,Argument in Opts:
	if Option == "-o":
		debugLog=open(Argument,'w')
		
while 1:
	new_post=ser.readline()
	if new_post!=post and new_post!="00000000\n" and len(new_post)==9:
		if int(hex(int(new_post[:8],2)),16)==0x10 or (int(hex(int(new_post[:8],2)),16)==0x11 and int(hex(int(post[:8],2)),16)!=0x10 ):
			print "\nStart\n"
		print (hex(int(new_post,2)),postCodes.get(int(hex(int(new_post[:8],2)),16),"Unknown PC"),new_post[:8])
		if debugLog is not None:
			debugLog.write(hex(int(new_post,2))+", ")
			debugLog.write(postCodes.get(int(hex(int(new_post[:8],2)),16),"Unknown PostCode")+'\n')
		post=new_post
		timeout=0;
		running=True
	else:
		timeout+=1
	if timeout==3000 and running==True:
		stop()
