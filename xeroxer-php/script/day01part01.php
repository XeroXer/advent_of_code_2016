<?php
chdir(dirname(__DIR__));
if (!is_file('input/day01')) {
    throw new Exception('Input file for day not found');
}
$input = array_map('trim', explode(',', file_get_contents('input/day01')));
$x = $y = $direction = 0;
foreach ($input as $command) {
    $turn = substr($command, 0, 1);
    $blocks = (int) substr($command, 1);
    if ($turn == 'L') {
        --$direction;
    } elseif ($turn == 'R') {
        ++$direction;
    }
    $direction = ($direction < 0 ? 3 : ($direction > 3 ? 0 : $direction));
    for ($i = 0; $i < $blocks; ++$i) {
        switch ($direction) {
            case 0:
                ++$y;
                break;
            case 1:
                ++$x;
                break;
            case 2:
                --$y;
                break;
            case 3:
                --$x;
                break;
        }
    }
}
echo 'Easter Bunny HQ is ' . (abs($x) + abs($y)) . ' blocks away' . PHP_EOL;
