<?php
chdir(dirname(__DIR__));
if (!is_file('input/day02')) {
    throw new Exception('Input file for day not found');
}
$input = new SplFileObject('input/day02');
$input->setFlags(SplFileObject::READ_AHEAD | SplFileObject::SKIP_EMPTY);

$code = '';
$x = $y = 1;
$numpad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];

while (!$input->eof()) {
    $line = trim($input->current());
    $input->next();

    $length = strlen($line);
    for ($i = 0; $i < $length; ++$i) {
        switch ($line[$i]) {
            case 'U':
                $y = (isset($numpad[($y - 1)][$x]) ? ($y - 1) : $y);
                break;
            case 'D':
                $y = (isset($numpad[($y + 1)][$x]) ? ($y + 1) : $y);
                break;
            case 'L':
                $x = (isset($numpad[$y][($x - 1)]) ? ($x - 1) : $x);
                break;
            case 'R':
                $x = (isset($numpad[$y][($x + 1)]) ? ($x + 1) : $x);
                break;
        }
    }

    $code .= $numpad[$y][$x];
}

echo 'The bathroom code is ' . $code . PHP_EOL;
