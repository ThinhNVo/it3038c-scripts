function getIP {
    (Get-NetIPAddress).IPAddress | Select-String "1.17"
}

function getType {
    (Get-LocalUser).Name | Select-String "ad"
}

$ver = $host.version.major
$IP = getIP
$name = $env:USERNAME
$type = getType
$date =(Get-Date).DayofWeek
$day = (get-date).DayOfYear
$month = (get-date).Month
$year = (get-date).Year


$body = "This Machine's IP is $IP. User is $type. Hostname is $name. Powershell version $ver.
Today's Date is $date, <$month> <$day> <$year>"

 $body | out-file -FilePath Downloads\Body.txt
