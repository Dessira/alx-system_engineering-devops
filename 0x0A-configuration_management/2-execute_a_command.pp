# Kills a process called killmenow
exec { 'killmenow':
path    => ['/usr/bin', '/sbin', '/bin', '/usr/bin'],
command => 'pkill "killmenow"'
}
