# Practice using Puppet to make changes to our configuration file
include stdlib

file_line { 'IdentityFile':
    ensure => 'present',
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school'
}

file_line { 'PasswordAuthentication':
    ensure => 'present',
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no'
}
