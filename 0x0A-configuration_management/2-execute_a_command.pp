# Create a manifest that kills a process named killmenow
exec {
    path    => '/usr/bin',
    command => 'pkill -f killmenow',
}
