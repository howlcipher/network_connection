
import paramiko
import datetime



# Network connection class needs host, username, password, and port
class Network_Connection():
    def __init__(self, host, username, password, port):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.data = ['No Output']
        self.data_cmd = ['No Command']
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connection credentials
    def connection_vars(self):
         self.ssh.connect(self.host, self.port, self.username, self.password)
    
    # Executes a command and stores the result in self.data
    def command_with_output(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        data = stdout.read().decode('utf-8')
        return data 

    # Executes a command with no output
    def command_no_output(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        self.data = "No Output"
    
    # Prints a command formatted
    def function_title(self, title):
        print('\n------\n{}\n------'.format(title))
    
    # Connects to a remote device
    def connect(self):
        try:
            self.function_title('Connecting')
            self.connection_vars()
            print("Yeah, we're connected")
            self.ssh.close()       
        except:
            print("We're not connected, idiot!")

    # Executes the show ip route command
    def show_ip_route(self):
        command = 'sh ip route'
        # self.data_cmd = []
        self.data_cmd = [command]
        self.data = []
        try:    
            self.function_title(command)
            self.connection_vars()
            self.data.append(self.command_with_output(command))
            self.ssh.close() 
        except:
            print("Couldn't exec command")

    # Executes the command given as a string
    def custom_command(self, command):
        self.data_cmd = []
        self.data = []
        try:
            self.data_cmd.append(command)
            self.function_title(command)
            self.connection_vars()
            self.data.append(self.command_with_output(command))         
            self.ssh.close() 
        except:
            print("Couldn't exec command")
    
    # Executes a list of commands given as a strings
    def custom_multi_command(self, commands):        
        self.data = []
        self.data_cmd = []
        try:
            for command in commands:
                self.data_cmd.append(command)
                self.function_title(command)
                self.connection_vars()
                self.data.append(self.command_with_output(command))        
                self.ssh.close() 
        except:
            print("Couldn't exec command")
    
    # Writes self.data to file output
    def write_to_file(self):
        date = datetime.datetime.now()
        i = 0
        try:
            for output in self.data:
                file_name = '{0}-{1}-{2} - {3}.txt'.format(date.year, date.month, date.day, self.data_cmd)
                f = open(file_name, "a")
                f.write('\n-----\n{2} ENTRY: {0}\n{1}'.format(i+1, output, self.data_cmd[i]))
                f.close()
                i += 1
        except:
            print('Error, unable to write to file.')

# Testing

# Network connection class
# connection_test = Network_Connection('sandbox-iosxe-recomm-1.cisco.com',
#                                        'developer', 'lastorangerestoreball8876',
#                                        22)

# Executing a custom command
# connection_test.custom_command('sh ip route')

# Executing a predefined command
# connection_test.show_ip_route()

# Executing a list of commands
# commands = ['sh ip route', 'sh version']
# connection_test.custom_multi_command(commands)

# Writing a command output to a file
# connection_test.write_to_file()