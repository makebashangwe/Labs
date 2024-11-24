
#fix time (minutes)
computer_standard_time = 15
computer_bit_time = 39
server_standard_time = 19
server_bit_time = 57

#computers
total_computers = 0
bit_computers = 0
standard_computers = total_computers - bit_computers
standard_computer_fixtime = computer_standard_time* standard_computers
bit_computer_fixtime = computer_bit_time*bit_computers


#servers
total_servers = 0
bit_servers= 0
standard_servers = total_servers-bit_servers
standard_server_fixtime = server_standard_time*(standard_servers)
bit_server_fixtime = bit_servers*server_bit_time

#calculated total fixtime
total_fixtime = standard_computer_fixtime+bit_computer_fixtime+bit_server_fixtime+standard_server_fixtime

department = 0
information = [total_computers, total_servers, total_fixtime, standard_computer_fixtime, standard_server_fixtime, bit_computers, bit_servers, bit_server_fixtime, bit_computer_fixtime]

def query(department, information):
    print(f"Department: {department}")
    total_computers += int(input("How many computers need to be fixed?"))
    bit_computers += int(input("How many of those computers had Bitlocker enabled?"))
    total_servers += int(input("How many servers need to be fixed? "))
    bit_servers += int(input("How many of those servers had Bitlocker enabled? "))
    return information

def info_report(information):
    print(f"Across all departments, there are {total_computers} computers and {total_servers} servers. Of those, {bit_computers} computers and {bit_servers} servers had Bitlocker enabled.")
    print(f"The {standard_computers} computers without Bitlocker will take {standard_computer_fixtime} minutes to fix.")
    print(f"The {bit_computers} computers with Bitlocker will take {bit_computer_fixtime} minutes to fix.")
    print(f"The {standard_servers} servers with Bitlocker will take {standard_server_fixtime} minutes to fix.")
    print(f"The {bit_servers} servers without Bitlocker will take {bit_server_fixtime} to fix.")
    print(f"Assuming we fix one at a time, it will take {total_fixtime} minutes to repair all devices.")


while True:
    query(department,information)

    department_query = input("Is there another department?").toupper()
    if department_query == 'Y':
        department += 1
        query(department,information)
    if department_query == 'N':
        info_report
    else:
        print("Invalid Answer, please try again.")

