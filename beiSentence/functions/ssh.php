<?php
/* copy file via scp, exec remote using ssh, then reture output */
function sshRemote($filename, $target, $cmd) {
	
	# ssh connection, 1. keys must have group accessiable (SECURITY RISK)
	$connection = ssh2_connect('132.236.79.195', 22, array('hostkey'=>'ssh-rsa'));
		
	if (ssh2_auth_pubkey_file($connection, 'oscar',
		'/home/ubuntu/sshKey/id_rsa.pub',
		'/home/ubuntu/sshKey/id_rsa')) {
		// echo "Public Key Authentication Successful\n";
	} else {
		die('Public Key Authentication Failed');
	}	
	// MUST SPECIFIED TO FILE (not enought if just specified to folder)
	// $target = "/home/oscar/Documents/AptanaStudio3Workspace/segmenterREMOTERUN/temp.txt";
	ssh2_scp_send($connection, $filename, $target, 0644);
		
	// $cmd = "bash /home/oscar/Documents/AptanaStudio3Workspace/segmenterREMOTERUN/segment.sh ctb ".$target." UTF-8 0";
	if ( !($stream = ssh2_exec($connection, $cmd) ) ) {
		echo "fail: unable to execulte command\n";
	} else {
		stream_set_blocking($stream, true);
        $data = "";
        while ($buf = fread($stream, 4096)) {
           $data .= $buf;
        }
           fclose($stream);
	}
	ssh2_exec($connection, 'exit');
	return $data;
}

/* receive file via scp */
function sshReceive($filename, $target) {
	
	# ssh connection, 1. keys must have group accessiable (SECURITY RISK)
	$connection = ssh2_connect('132.236.79.195', 22, array('hostkey'=>'ssh-rsa'));
		
	if (ssh2_auth_pubkey_file($connection, 'oscar',
		'/home/ubuntu/sshKey/id_rsa.pub',
		'/home/ubuntu/sshKey/id_rsa')) {
		// echo "Public Key Authentication Successful\n";
	} else {
		die('Public Key Authentication Failed');
	}	
	// MUST SPECIFIED TO FILE (not enought if just specified to folder)
	// $target = "/home/oscar/Documents/AptanaStudio3Workspace/segmenterREMOTERUN/temp.txt";
	$isOK = ssh2_scp_recv($connection, $filename, $target);
	
	ssh2_exec($connection, 'exit');
	return $isOK;
}


/* exec remote using ssh, then reture output */
function sshSimpleRemote($cmd) {
	
	# ssh connection, 1. keys must have group accessiable (SECURITY RISK)
	$connection = ssh2_connect('132.236.79.195', 22, array('hostkey'=>'ssh-rsa'));
		
	if (ssh2_auth_pubkey_file($connection, 'oscar',
		'/home/ubuntu/sshKey/id_rsa.pub',
		'/home/ubuntu/sshKey/id_rsa')) {
		// echo "Public Key Authentication Successful\n";
	} else {
		die('Public Key Authentication Failed');
	}	
		
	// $cmd = "bash /home/oscar/Documents/AptanaStudio3Workspace/segmenterREMOTERUN/segment.sh ctb ".$target." UTF-8 0";
	if ( !( $stream = ssh2_exec($connection, $cmd) ) ) {
		echo "fail: unable to execulte command\n";
	} else {
		stream_set_blocking($stream, true);
        $data = "";
        while ($buf = fread($stream, 4096)) {
           $data .= $buf;
        }
           fclose($stream);
	}
	ssh2_exec($connection, 'exit');
	return $data;
}

function sshPHPSecLib($cmd) {
	include('Net/SSH2.php');
	include('Crypt/RSA.php');

	$rsa = new Crypt_RSA();
	//$rsa->setPassword('password');
	$rsa->loadKey('/home/ubuntu/sshKey/id_rsa');

	$ssh = new Net_SSH2('132.236.79.195', 22, array('hostkey'=>'ssh-rsa'));
	$ssh->login('oscar', $rsa);

	$data = $ssh->exec('ls -la');
	return $data;
}	

 ?>