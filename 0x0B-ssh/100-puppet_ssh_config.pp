# Script to creat ssh connection using puppet

exec { 'ssh_config':
command	 => 'echo "Host *\nPasswordAuthentication no\nUser ubuntu\nHostname 35.153.18.176\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
provider => 'shell'
}
