<!DOCTYPE html>
<html>
<body>
	Welcome
	<?php
		function prime($n)
		{
			if ($n == 1) {
				return 0;
			}
			for ($i = 2; $i < $n; $i++) {
				if ($n % $i == 0) {
					return 0;
				}
			}
			return 1;
		}
		$a = $_POST["n1"];
		$b = $_POST["n2"];
		for ($i = $a; $i <= $b; $i++) {
			$p = prime($i);
			if ($p == 1) {
				echo $i." ";
			}
		}
	?>
</body>
</html>