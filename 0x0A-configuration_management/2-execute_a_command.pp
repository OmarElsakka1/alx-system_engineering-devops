# Using Puppet, create a manifest for killing the process with name killmenow

exec { 'pkill -f killmenow':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}