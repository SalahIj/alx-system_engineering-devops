# Installing flask

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require => Exec['python-installed'],
  command => '/usr/bin/pip3 install flask==2.1.0'
}
