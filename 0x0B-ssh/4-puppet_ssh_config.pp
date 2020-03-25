# SSH configuration file so that you can connect to a server without typing a password
file_line { 'holberton':
    ensure => present,
    path   => '~/.ssh',
    line   => '%sudonopw ALL=(ALL) NOPASSWD: ALL',
}
