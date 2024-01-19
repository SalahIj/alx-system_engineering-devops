# 1-install_a_package.pp

# Install python3 and pip3
package { 'python3':
  ensure => installed,
}

package { 'python3-pip':
  ensure => installed,
}

# Ensure the package is present and at the specified version
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => [Package['python3'], Package['python3-pip']],  # Ensure python3 and pip3 are installed first
}
