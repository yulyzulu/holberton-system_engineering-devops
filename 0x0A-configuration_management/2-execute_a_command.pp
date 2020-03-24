# Create a manifest that kills a process named killmenow
exec {'/usr/bin',
    command => 'pkill -f killmenow',
}
