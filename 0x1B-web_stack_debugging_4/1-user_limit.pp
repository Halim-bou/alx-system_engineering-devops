# to login whit the holberton user and apen a file without error message.

exec {'change the OS config':
command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
