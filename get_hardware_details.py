import logging
import sys

import paramiko
import yaml

from optparse import OptionParser


def run_cmd(server, cmds, user="root"):
    """
    Runs the command on remote server

    Args:
        server (str): server on which command should execute
        cmds (list): list  of commands to execute

    Returns:
        tuple: tuple consisting of the command return code (list),
               stdout (list), and stderr(list)

    eg: >>> run_cmd("rhs-client11.lab.eng.blr.redhat.com", ["uname", "whoami", "arch"])
            ([0, 0, 0], ['Linux', 'root', 'x86_64'], ['', '', ''])

    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, username=user)
    retcode = []
    outputs = []
    errors = []
    for cmd in cmds:
        _, stdout, stderr = client.exec_command(cmd)
        retcode.append(stdout.channel.recv_exit_status())
        outputs.append(stdout.read().decode('ascii').strip("\n"))
        errors.append(stderr.read().decode('ascii').strip("\n"))
    client.close()
    return retcode, outputs, errors


def get_hw_details(servers, data):
    """
    Get Hardware Details for the servers

    Args:
        servers (list): List of servers
        data (dict): dictionary which contains key as header to display
                     and value as command
            eg: {'USER': "whoami", 'Arhitecture': "arch"}
    """
    remove_var = "test"
    hw_info = {}
    cmd_list = [cmd for cmd in data.values()]

    for server in servers:
        hw_info[server] = {}
        res = run_cmd(server, cmd_list)
        for index, key in enumerate(data):
            hw_info[server][key.upper()] = res[1][index]

    # print ALL INFO
    for server in hw_info:
        print("=================================================================================")
        print(server + ":")
        for y in hw_info[server]:
            print(y, ":", hw_info[server][y])
    print("=================================================================================")


if __name__ == '__main__':

    usage = r'''
    %prog -f <server_file> -c <commands_file>
    '''

    parser = OptionParser(usage=usage, version="1.0")
    parser.add_option("-f", "--file", dest="server_file", help="file which contains server names/ips")
    parser.add_option("-c", "--cmds_file", dest="cmds_file", help="file which contains commands in yaml format")

    (options, args) = parser.parse_args()

    if not options.server_file or not options.cmds_file:
        logging.error("Please specify the server file and commands file")
        parser.print_help()
        sys.exit(1)

    with open(options.server_file) as f:
        target_servers = [each_line.strip() for each_line in f]

    # read the cmd_list from cmds.yaml
    with open(options.cmds_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        # cmd_list = [cmd for cmd in data.values()]

    # print(f"cmd_list: {cmd_list}")
    print(f"Target Servers : {target_servers}")

    get_hw_details(target_servers, data)
