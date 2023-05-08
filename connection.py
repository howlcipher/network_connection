
import paramiko
import datetime



# Network connection class needs host, username, password, and port
class Network_Connection():
    def __init__(self, host, username, password, port):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.data = 'No Output'
        self.data_cmd = 'No Command'
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connection credentials
    def connection_vars(self):
         self.ssh.connect(self.host, self.port, self.username, self.password)
    
    # Executes a command and stores the result in self.data
    def command_with_output(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        self.data = stdout.read().decode('utf-8') 

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
        try:    
            self.function_title(command)
            self.connection_vars()
            self.command_with_output(command)
            self.data_cmd = command
            self.ssh.close() 
        except:
            print("Couldn't exec command")

    # Executes the command given as a string
    def custom_command(self, command):
        try:
            self.data_cmd = command
            self.function_title(command)
            self.connection_vars()
            self.command_with_output(command)          
            self.ssh.close() 
        except:
            print("Couldn't exec command")
    
    # Writes self.data to file output
    def write_to_file(self):
        date = datetime.datetime.now()
        file_name = '{0}-{1}-{2} - {3}.txt'.format(date.year, date.month, date.day, self.data_cmd)
        f = open(file_name, "a")
        f.write(self.data)
        f.close()

# Testing

# Network connection class
# connection_test = Network_Connection('sandbox-iosxe-recomm-1.cisco.com',
#                                       'developer', 'lastorangerestoreball8876',
#                                       22)

# Executing a command
# connection_test.custom_command('sh ip route')

# Writing a command output to a file
# connection_test.write_to_file()