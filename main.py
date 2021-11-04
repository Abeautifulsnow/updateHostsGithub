import shutil
import requests
import traceback


class CopyError(Exception):
    """An Copy Error occurred."""


class UpdateHosts:
    hosts_online_link1 = 'https://raw.hellogithub.com/hosts'
    hosts_online_link2 = 'https://raw.githubusercontent.com/521xueweihan/GitHub520/main/hosts'
    hosts_file_origin = '/etc/hosts'
    hosts_file_backup = '/etc/hosts.bk'
    new_hosts_content = ''
    origin_hosts = []
    headers = {
        'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }

    def read_hosts(self, host_url: str):
        print('Current url:', host_url)
        response = requests.get(host_url, headers=self.headers, timeout=300)
        if response.status_code == 200:
            self.new_hosts_content = response.text
            print('Read the remote contents successfully.')
        else:
            print('Get contents failed...Exit')
            exit(-1)

    def read_hosts_online(self):
        error_num = 0
        link_list = [self.hosts_online_link1, self.hosts_online_link2]
        for link in link_list:
            try:
                self.read_hosts(link)
                break
            except:
                print('Read Hosts From Online Fail:', traceback.format_exc())
                error_num += 1
                continue
        if error_num == len(link_list):
            print(' The two links are unreachable. '.center(60, '*'))
            for i in link_list:
                print(i)
            exit(-1)

    def copy_hosts(self):
        print('Start to make a backup of hosts file.')
        try:
            shutil.copy(self.hosts_file_origin, self.hosts_file_backup)
        except PermissionError:
            print('Permission Error(See details bellow):\n',
                  traceback.format_exc())
            exit(-1)
        except CopyError:
            print('Copy Error(See details bellow):\n', traceback.format_exc())
            exit(-1)

        print('Copy done.')

    def write_new_content_to_hosts(self):
        print('Start to write the new contents to hosts file.')
        with open(self.hosts_file_origin, 'r') as f_r:
            self.origin_hosts = f_r.readlines()

        hosts_length = len(self.origin_hosts)
        for i in range(18, hosts_length)[::-1]:
            del self.origin_hosts[i]

        self.origin_hosts.append(self.new_hosts_content)
        with open(self.hosts_file_origin, 'w') as f_w:
            f_w.writelines(self.origin_hosts)

        print('Write done.')


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
