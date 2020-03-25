# SSH configuration file so that you can connect to a server without typing a password
file_line { 'holberton':
  path => 'etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'password':
  path => 'etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
