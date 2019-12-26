import sys
import re

print("\nWelcome to the ISA simulator! - Designed by Simon, Thomas and Sara")

if len(sys.argv) < 4:
    print('Too few arguments.')
    sys.exit(-1)
elif (len(sys.argv) > 4):
    print('Too many arguments.')
    sys.exit(-1)

'''
This class models the register file of the processor. It contains 16 8-bit unsigned
registers named from R0 to R15 (the names are strings). R0 is read only and
reads always 0 (zero). When an object of the class RegisterFile is instantiated,
the registers are generated and initialized to 0.
'''
class RegisterFile:
    def __init__(self):
        self.registers = {}
        for i in range(0, 16):
            self.registers['R'+str(i)] = 0
        
        self.functions = [{"NOP":self.NOP, "END":self.END},{"JR":self.JR},{"NOT":self.NOT, "LI":self.LI, "LD":self.LD, "SD":self.SD},{"ADD":self.ADD, "SUB":self.SUB, "OR":self.OR, "AND":self.AND, "JEQ":self.JEQ, "JLT":self.JLT}] #element 0 are 0-ary functions, element 1 are the 1-ary functions and so on
        
    '''
    This method writes the content of the specified register.
    '''
    def write_register(self, register, register_value):
        if register in self.registers:
            if register == 'R0':
                print('WARNING: Cannot write R0. Register R0 is read only.')
            else:
                self.registers[register] = register_value % 256
        else:
            print('Register ' + str(register) + ' does not exist. Terminating execution.')
            sys.exit(-1)

    '''
    This method reads the content of the specified register.
    '''
    def read_register(self, register):
        if register in self.registers:
            return self.registers[register]
        else:
            print('Register ' + str(register) + ' does not exist. Terminating execution.')
            sys.exit(-1)

    '''
    This method prints the content of the specified register.
    '''
    def print_register(self, register):
        if register in self.registers:
            print(register + ' = ' + str(self.registers[register]))
        else:
            print('Register ' + str(register) + ' does not exist. Terminating execution.')
            sys.exit(-1)

    '''
    This method prints the content of the entire register file.
    '''
    def print_all(self):
        print('Register file content:')
        for i in range(0, 16):
            self.print_register('R' + str(i))
    """     
    Functions based on currying!
    0ary functions
    """
    def NOP(self,simulation):
        return 0
    
    def END(self,simulation):
        print("End command reached")
        simulation.end = True
    
    
    """
    1ary functions
    """
    def JR(self,simulation):
        def layer1(r1):
            simulation.jumpPC(self.read_register(r1))
        return layer1
      
        
    """
    2ary functions
    """
    def NOT(self,simulation):
        def layer1(r1):
            def layer2(r2):
                self.write_register(r1, ~self.read_register(r2))
            return layer2
        return layer1
    
    def LI(self,simulation):
        def layer1(r1):
            def layer2(x):
                self.write_register(r1,int(x))
            return layer2
        return layer1
    
    def LD(self,simulation):
        def layer1(r1):
            def layer2(r2):
                self.write_register(r1,simulation.dataMemory.read_data(self.read_register(r2)))
            return layer2
        return layer1
    
    def SD(self,simulation):
        def layer1(r1):
            def layer2(r2):
                simulation.dataMemory.write_data(self.read_register(r2),self.read_register(r1))
            return layer2
        return layer1
    
    """
    3ary functions
    """
    def ADD(self,simulation):
        def layer1(r1):
            def layer2(r2):
                def layer3(r3):
                    self.write_register(r1, self.read_register(r2) + self.read_register(r3))
                return layer3
            return layer2
        return layer1

    def SUB(self,simulation):
        def layer1(r1):
            def layer2(r2):
                def layer3(r3):
                    self.write_register(r1, self.read_register(r2) - self.read_register(r3))
                return layer3
            return layer2
        return layer1

    def OR(self,simulation):
        def layer1(r1):
            def layer2(r2):
                def layer3(r3):
                    self.write_register(r1, self.read_register(r2) | self.read_register(r3))
                return layer3
            return layer2
        return layer1

    def AND(self,simulation):
        def layer1(r1):
            def layer2(r2):
                def layer3(r3):
                    self.write_register(r1, self.read_register(r2) & self.read_register(r3))
                return layer3
            return layer2
        return layer1
    
    def JEQ(self,simulation):
        def layer1(r1):
            def layer2(r2):
                def layer3(r3):
                        if self.read_register(r2) == self.read_register(r3):
                            simulation.jumpPC(self.read_register(r1))
                return layer3
            return layer2
        return layer1
    
    def JLT(self,simulation):
        def layer1(r1):
            def layer2(r2):
                def layer3(r3):
                    if self.read_register(r2) < self.read_register(r3):
                        simulation.jumpPC(self.read_register(r1))
                return layer3
            return layer2
        return layer1

'''
This class models the data memory of the processor. When an object of the
class DataMemory is instantiated, the data memory model is generated and au-
tomatically initialized with the memory content specified in the file passed as
second argument of the simulator. The memory has 256 location addressed form
0 to 255. Each memory location contains an unsigned 8-bit value. Uninitialized
data memory locations contain the value zero.
'''
class DataMemory:
    def __init__(self):
        self.data_memory = {}
        print('\nInitializing data memory content from file.')
        try:
            with open(sys.argv[3], 'r') as fd:
                file_content = fd.readlines()
        except:
             print('Failed to open data memory file. Terminating execution.')
             sys.exit(-1)
        file_content = ''.join(file_content)
        file_content = re.sub(r'#.*?\n', ' ', file_content)
        file_content = re.sub(r'#.*? ', ' ', file_content)
        file_content = file_content.replace('\n', '')
        file_content = file_content.replace('\t', '')
        file_content = file_content.replace(' ', '')
        file_content_list = file_content.split(';')
        file_content = None
        while '' in file_content_list:
            file_content_list.remove('')
        try:
            for entry in file_content_list:
                address, data = entry.split(':')
                self.write_data(int(address), int(data))
        except:
            print('Malformed data memory file. Terminating execution.')
            sys.exit(-1)
        print('Data memory initialized.')

    '''
    This method writes the content of the memory location at the specified address.
    '''
    def write_data(self, address, data):
        if address < 0 or address > 255:
            print("Out of range data memory write access. Terminating execution.")
            sys.exit(-1)
        self.data_memory[address] = data % 256

    '''
    This method writes the content of the memory location at the specified address.
    '''
    def read_data(self, address):
        if address < 0 or address > 255:
            print("Out of range data memory read access. Terminating execution.")
            sys.exit(-1)
        if address in self.data_memory:
            return self.data_memory[address]
        else:
            self.data_memory[address] = 0
            return 0

    '''
    This method prints the content of the memory location at the specified address.
    '''
    def print_data(self, address):
        if address < 0 or address > 255:
            print('Address ' + str(address) + ' does not exist. Terminating execution.')
            sys.exit(-1)
        if address in self.data_memory:
            print('Address ' + str(address) + ' = ' + str(self.data_memory[address]))
        else:
            print('Address ' + str(address) + ' = 0')

    '''
    This method prints the content of the entire data memory.
    '''
    def print_all(self):
        print('Data memory content:')
        for address in range(0, 256):
            self.print_data(address)

    '''
    This method prints the content only of the data memory that have been used
    (initialized, read or written at least once).
    '''
    def print_used(self):
        print('Data memory content (used locations only):')
        for address in range(0, 256):
            if address in self.data_memory:
                print('Address ' + str(address) + ' = ' + str(self.data_memory[address]))


'''
This class models the data memory of the processor. When an object of the class
InstructionMemory is instantiated, the instruction memory model is generated
and automatically initialized with the program specified in the file passed as first
argument of the simulator. The memory has 256 location addressed form 0 to
255. Each memory location contains one instruction. Uninitialized instruction
memory locations contain the instruction NOP.
'''
class InstructionMemory:
    def __init__(self):
        self.instruction_memory = {}
        self.operands = [self.read_operand_1, self.read_operand_2, self.read_operand_3]
        print('\nInitializing instruction memory content from file.')
        try:
            with open(sys.argv[2], 'r') as fd:
                file_content = fd.readlines()
        except:
             print('Failed to open program file. Terminating execution.')
             sys.exit(-1)
        file_content = ''.join(file_content)
        file_content = re.sub(r'#.*?\n', '', file_content)
        file_content = re.sub(r'#.*? ', '', file_content)
        file_content = re.sub(r'\s*[\n\t]+\s*', '', file_content)
        file_content = re.sub('\s\s+', ' ',  file_content)
        file_content = file_content.replace(': ', ':')
        file_content = file_content.replace(' :', ':')
        file_content = file_content.replace(', ', ',')
        file_content = file_content.replace(' ,', ',')
        file_content = file_content.replace('; ', ';')
        file_content = file_content.replace(' ;', ';')
        file_content = file_content.strip()
        file_content = file_content.replace(' ', ',')
        file_content_list = file_content.split(';')
        file_content = None
        while '' in file_content_list:
            file_content_list.remove('')
        try:
            for entry in file_content_list:
                address, instruction_string = entry.split(':')
                instruction = instruction_string.split(',')
                if len(instruction)<1 or len(instruction)>4:
                    raise Exception('Malformed program.')
                self.instruction_memory[int(address)] = {'opcode': str(instruction[0]), 'op_1':'-','op_2':'-','op_3':'-' }
                if len(instruction)>1:
                    self.instruction_memory[int(address)]['op_1'] = str(instruction[1])
                if len(instruction)>2:
                    self.instruction_memory[int(address)]['op_2'] = str(instruction[2])
                if len(instruction)>3:
                    self.instruction_memory[int(address)]['op_3'] = str(instruction[3])
        except:
            print('Malformed program memory file. Terminating execution.')
            sys.exit(-1)
        print('Instruction memory initialized.')

    '''
    This method returns the OPCODE of the instruction located in the instruction
    memory location in the specified address. For example, if the instruction is ADD
    R1, R2, R3;, this method returns ADD.
    '''
    def read_opcode(self, address):
        if address < 0 or address > 255:
            print("Out of range instruction memory access. Terminating execution.")
            sys.exit(-1)
        if address in self.instruction_memory:
            return self.instruction_memory[address]['opcode']
        else:
            return 'NOP'

    '''
    This method returns the first operand of the instruction located in the instruc-
    tion memory location in the specified address. For example, if the instruction
    is ADD R1, R2, R3;, this method returns R1.
    '''
    def read_operand_1(self, address):
        if address < 0 or address > 255:
            print("Out of range instruction memory access. Terminating execution.")
            sys.exit(-1)
        if address in self.instruction_memory:
            return self.instruction_memory[address]['op_1']
        else:
            return '-'

    '''
    This method returns the second operand of the instruction located in the instruc-
    tion memory location in the specified address. For example, if the instruction
    is ADD R1, R2, R3;, this method returns R2.
    '''
    def read_operand_2(self, address):
        if address < 0 or address > 255:
            print("Out of range instruction memory access. Terminating execution.")
            sys.exit(-1)
        if address in self.instruction_memory:
            return self.instruction_memory[address]['op_2']
        else:
            return '-'

    '''
    This method returns the third operand of the instruction located in the instruc-
    tion memory location in the specified address. For example, if the instruction
    is ADD R1, R2, R3;, this method returns R3.
    '''
    def read_operand_3(self, address):
        if address < 0 or address > 255:
            print("Out of range instruction memory access. Terminating execution.")
            sys.exit(-1)
        if address in self.instruction_memory:
            return self.instruction_memory[address]['op_3']
        else:
            return '-'

    '''
    This method prints the instruction located at the specified address.
    '''
    def print_instruction(self, address):
        if address < 0 or address > 255:
            print("Out of range instruction memory access. Terminating execution.")
            sys.exit(-1)
        if address in self.instruction_memory:
            print(self.read_opcode(address), end='')
            if self.read_operand_1(address)!='-':
                print(' ' + self.read_operand_1(address), end='')
            if self.read_operand_2(address)!='-':
                print(', ' + self.read_operand_2(address), end='')
            if self.read_operand_3(address)!='-':
                print(', ' + self.read_operand_3(address), end='')
            print(';')
        else:
            print('NOP;')

    '''
    This method prints the content of the entire instruction memory (i.e., the pro-
    gram).
    '''
    def print_program(self):
        print('Instruction memory content (program only, the rest are NOP):')
        for address in range(0, 256):
            if address in self.instruction_memory:
                print('Address ' + str(address) + ' = ', end='')
                self.print_instruction(address)


"""
This class contains all methods for running the simulation, and objects edited during simulation
"""
class simulation:
    def __init__(self):
        #initiate variables
        self.PC = 0
        self.cycle = 0
        self.end = False
        self.max_cycles = int(sys.argv[1])
        
        #initiate object of other classes
        self.registerFile = RegisterFile()
        self.dataMemory = DataMemory()
        self.instructionMemory = InstructionMemory()
    
    
    """
    Three methods for incrementing and editing pc and cycle
    """
    def incrementPC(self):
        self.PC = (self.PC + 1) % 256

    def incrementCycle(self):
        self.cycle += 1
    
    #jump to instruction at gotoValue
    def jumpPC(self,gotoValue):
        print("jumped to " + str(gotoValue))
        self.PC = (gotoValue - 1) % 256

    """
    Method for executing operation at address: PC
    """
    def executeOperation(self):
        #find operation to be executed
        operation = self.instructionMemory.read_opcode(self.PC)
        
        for i in range(4):#find number of parameters taken by the operation
            if operation in self.registerFile.functions[i]:
                
                #give operation method simulation as argument
                function = self.registerFile.functions[i][operation](self)
                
                #Add registers as argument one by one, via currying
                r = 0
                while r < i:
                    function = function(self.instructionMemory.operands[r](self.PC))
                    r += 1
                
                break
    
    """
    Method that runs one cycle of the simulation
    """
    def executeCycle(self):
        #Display
        print("----------------------------------")
        print("Cycle: " + str(self.cycle))
        print("PC: " + str(self.PC))
        print("Instruction executed:")
        self.instructionMemory.print_instruction(self.PC)
        print("----------------------------------")
        
        #Updating simulation
        self.executeOperation()
        self.incrementPC()
        self.incrementCycle()
        if self.cycle == self.max_cycles:
            self.end = True
    
    """
    Method for printing conclussion at end of sim
    """
    def endprint(self):
        print("END OF SIMULATION\n")
        self.registerFile.print_all()
        print()
        self.dataMemory.print_all()

#Run simulation
sim = simulation()

print('\n---Start of simulation---')

while not sim.end:
    sim.executeCycle()

sim.endprint()
