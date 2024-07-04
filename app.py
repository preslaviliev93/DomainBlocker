import platform


class DNSBlocker:
    def __init__(self):
        self.hosts_file_location = self.get_hosts_file_location()

    @staticmethod
    def get_hosts_file_location():
        hosts_file = platform.system()
        if hosts_file == 'Windows':
            hosts_file = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
        elif hosts_file == 'Linux':
            hosts_file = '/etc/hosts'
        elif hosts_file == 'Darwin':
            hosts_file = '/etc/hosts'
        elif "BSD" in hosts_file.upper():
            hosts_file = '/etc/hosts'

        return hosts_file

    def block_dns(self, domain):
        entry = f'127.0.0.1 {domain}\n'
        hosts_file = self.get_hosts_file_location()
        try:
            with open(hosts_file, 'r+') as f:
                content = f.read()
                if domain not in content:
                    f.write(entry)
                    return f'Domain {domain} has been blocked.'
                else:
                    return f'Domain {domain} already blocked!'

        except FileNotFoundError as error:
            return f'File {hosts_file} not found! {error}'
        except PermissionError as error:
            return f'Permission denied! {error}'
        except Exception as error:
            return f'Something went wrong! {error}'

    def main(self):
        while True:
            domain_to_block = input('Domain to block [Exit] to exit: ')
            if domain_to_block == 'Exit':
                break
            else:
                result = self.block_dns(domain_to_block)
                print(result)


if __name__ == '__main__':
    dns_blocker = DNSBlocker()
    dns_blocker.main()