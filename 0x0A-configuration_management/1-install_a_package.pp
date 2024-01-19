# A Manifest that's installs Flask v2.1.0 on Puppet-agent.
package {'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
