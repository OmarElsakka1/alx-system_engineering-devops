#configure ssh configuration

file_line{'Turning off password auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}

file_line{'Declaring the identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}