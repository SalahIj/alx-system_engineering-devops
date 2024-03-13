# Change the limit from 15 to 2000
exec { 'set limit to 2000':
  path    => '/bin',
  command => "sed -i 's/15/2000/' /etc/default/nginx"
}
exec { 'reboot nginx':
  command => '/usr/sbin/service nginx restart'
}
