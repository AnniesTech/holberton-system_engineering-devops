# Installs puppet-lint in version 2.5.0

package { 'puppet-lint':
    ensure   => '2.5.0',
    provider => 'gem',
    source   => 'https://rubygems.org'
}
