import platform
import requests
import shutil
import traceback
from typing import Union
from nb_log import get_logger

logger = get_logger("updateHost", log_level_int=1)


def retrieve_host_file(system: str, host_type: Union["origin", "backup"]) -> str:
    logger.info(f"Current system: {system}, hosts file type: {host_type}")
    different_system_host = {
        "Linux": {
            "origin": "/etc/hosts",
            "backup": "/etc/hosts.bk"
        },
        "Darwin": {
            "origin": "/etc/hosts",
            "backup": "/etc/hosts.bk"
        },
        "Windows": {
            "origin": r"c:\Windows\System32\Drivers\etc\hosts",
            "backup": r"c:\Windows\System32\Drivers\etc\hosts.bk"
        }
    }
    return different_system_host.get(system).get(host_type)


class CopyError(Exception):
    """An Copy Error occurred."""


class UpdateHosts:
    platform_sytem = platform.system()
    hosts_online_link1 = 'https://raw.hellogithub.com/hosts'
    hosts_online_link2 = 'https://raw.githubusercontent.com/521xueweihan/GitHub520/main/hosts'
    hosts_file_origin = retrieve_host_file(platform_sytem, "origin")
    hosts_file_backup = retrieve_host_file(platform_sytem, "backup")
    new_hosts_content = ''
    origin_hosts = []
    headers = {
        'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }

    def read_hosts(self, host_url: str):
        logger.info(f'Current url:{host_url}')
        response = requests.get(host_url, headers=self.headers, timeout=300)
        if response.status_code == 200:
            self.new_hosts_content = response.text
            logger.info('Read the remote contents successfully.')
        else:
            logger.error('Get contents failed...Exit')
            exit(-1)

    def read_hosts_online(self):
        error_num = 0
        link_list = [self.hosts_online_link1, self.hosts_online_link2]
        for link in link_list:
            try:
                self.read_hosts(link)
                break
            except:
                logger.error(f'Read Hosts From Online Fail: {traceback.format_exc()}')
                error_num += 1
                continue
        if error_num == len(link_list):
            logger.error(' The two links are unreachable. '.center(60, '*'))
            for i in link_list:
                logger.info(i)
            exit(-1)

    def copy_hosts(self):
        logger.info('Start to make a backup of hosts file.')
        try:
            shutil.copy(self.hosts_file_origin, self.hosts_file_backup)
        except PermissionError:
            logger.error(f'Permission Error(See details bellow):\n{traceback.format_exc()}')
            exit(-1)
        except CopyError:
            logger.error(f'Copy Error(See details bellow):\n{traceback.format_exc()}')
            exit(-1)

        logger.info('Copy done.')

    def write_new_content_to_hosts(self):
        logger.info('Start to write the new contents to hosts file.')
        with open(self.hosts_file_origin, 'r') as f_r:
            self.origin_hosts = f_r.readlines()

        hosts_length = len(self.origin_hosts)
        for i in range(18, hosts_length)[::-1]:
            del self.origin_hosts[i]

        self.origin_hosts.append(self.new_hosts_content)
        with open(self.hosts_file_origin, 'w') as f_w:
            f_w.writelines(self.origin_hosts)

        logger.info('Write done.')


def main():
    uh = UpdateHosts()
    # Get host's contents from remote url.
    uh.read_hosts_online()
    # Make a backup of original hosts file.
    uh.copy_hosts()
    # Write the new contents to original hosts file.
    uh.write_new_content_to_hosts()


if __name__ == '__main__':
    main()
